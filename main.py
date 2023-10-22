from flask import Flask, request, jsonify, send_file, Response, send_from_directory
from flask_cors import CORS
import azure.cognitiveservices.speech as speechsdk
import openai
from OpenSSL import SSL
#import librosa
#import soundfile as sf
#import wave
#import io
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import configparser
import json

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 MB
MAX_TEXT_SIZE = 400

app = Flask(__name__, static_folder='public_html')
limiter = Limiter(app=app, key_func=get_remote_address, default_limits=["100 per day", "40 per hour"], storage_uri="memory://",)


# Create a configuration parser instance
config = configparser.ConfigParser()

# Read the configuration file
config.read('config/config.ini')

api_key = config.get('azure', 'API_KEY')
api_region = config.get('azure', 'API_REGION')
api_language = config.get('azure', 'API_LANGUAGE')

openai.api_key = config.get('openai', 'API_KEY')
    
app.config['UPLOAD_EXTENSIONS'] = ['.wav']
app.config["LIMITER_HEADERS_ENABLED"] = True
CORS(app)


@app.route('/static/<path:filename>')
@limiter.exempt
def serve_files(filename):
    return send_from_directory('public_html/static', filename)


@app.route('/')
@limiter.exempt
def hello():
    return app.send_static_file('index.html')

@app.route('/response', methods=['POST'])
def response():
    print("arrived")
        # Retrieve the JSON data from the form data
    json_data = request.form['json']
    
    # Parse the JSON data to a Python dictionary
    data = json.loads(json_data)
    
    
    input_file = request.files['audio'] # Get the input data from the request
    
    
    file_size = int(request.headers.get('Content-Length', 0))
    if file_size > MAX_FILE_SIZE:
        error_msg = f"File size exceeds the maximum limit of 1MB."
        return jsonify({'error': error_msg}), 413  # Return HTTP 413 Payload Too Large error
    input_data = input_file.read()
    
    # DEPRECIATED Resample the audio to the target sample rate (16 kHz)
    #y, s = librosa.load('voice.wav', sr=16000) # Downsample 44.1kHz to 16kHz
    # # Load the original WAV file
    # audio, sr = librosa.load('voice.wav')
    # target_sr = 16000
    # resampled_audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
    # sf.write('resampled.wav', resampled_audio, target_sr)
    
    # Measure the execution time of function1
    #start_time = time.perf_counter()
    input = recognize_from_input(input_data, data["lang"])
    #end_time = time.perf_counter()
    #time1 = end_time - start_time
    #print("Function 1 execution time:", time1)
    
    return jsonify({"user": input})
    
@app.route('/gpt', methods=['POST'])
def gpt_response(): 
    json_data = request.form['json']
    data = json.loads(json_data)
    
    input = data["input"]  
    
    if len(input) > MAX_TEXT_SIZE:
        error_msg = f"Text size exceeds the maximum limit of 400 characters."
        return jsonify({'error': error_msg}), 413  # Return HTTP 413 Payload Too Large error
    output = talk_to_gpt(input, data["lang"])
    
    return jsonify({"server" :  output})
    
    
        
@app.route('/speech', methods=['POST'])
def speech():
    json_data = request.form['json']
    data = json.loads(json_data)
    
    output = data["output"]  
    if len(output) > MAX_TEXT_SIZE:
        error_msg = f"Text size exceeds the maximum limit of 400 characters."
        return jsonify({'error': error_msg}), 413  # Return HTTP 413 Payload Too Large error
    stream = None
    try:
        stream = talk_back(output,data["voice"])
        return Response(stream, mimetype='audio/wav')
    except:
        print("")
  

def recognize_from_input(audio_in, lang):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=api_region)
    speech_config.speech_recognition_language=lang
    audio_stream = speechsdk.audio.PushAudioInputStream()
    audio_config = speechsdk.audio.AudioConfig(stream=audio_stream)
    

    audio_stream.write(audio_in)
    audio_stream.close()
    # speech_config.set_property(Initial)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""



def talk_to_gpt(input, lang):



    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Only respond in " + lang + "."},
            {"role": "user", "content": input}
        ]
    )

    return completion.choices[0].message["content"]



def talk_back(output, voice):


    # Creates an instance of a speech config with specified subscription key and service region.


    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=api_region)
    # Note: the voice setting will not overwrite the voice element in input SSML.
    speech_config.speech_synthesis_voice_name = voice

    text = output 

    # use the default speaker as audio output.
    # audio_stream = speechsdk.audio.AudioOutputStream()
    # audio_config = speechsdk.audio.AudioOutputConfig()
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    result = speech_synthesizer.speak_text_async(text).get()
    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
        # return speechsdk.AudioDataStream(result)
        return result.audio_data
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
        raise Exception("Speech synthesis canceled")



            
if __name__ == '__main__':

    context = ('config/cert.pem', 'config/key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)
    
    