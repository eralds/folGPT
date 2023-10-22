# FolGPT

A web-based voice assistant leveraging Flask, Azure's Cognitive Services, and OpenAI's GPT-4.

![Screenshot (18)](https://github.com/eralds/folGPT/assets/94328315/2be6293c-7bbd-4e01-8b97-581e8febfb68)


## Features

- Audio input via browser.
- Speech to text conversion with Azure's Cognitive Services.
- GPT-4 powered conversational responses.
- Text to speech response for server messages.
- SSL encryption support.


## Prerequisites

- Python 3.x
- A valid Azure API subscription for Cognitive Services.
- OpenAI API key for GPT-4.
  
Also run "pip install -r requirements.txt" in order to install the prerequisites

## Supported languages

| Locale (BCP-47) | Language |
|-----------------|----------|
| af-ZA|Afrikaans (South Africa)|
| am-ET|Amharic (Ethiopia)|
| ar-AE|Arabic (United Arab Emirates)|
| ar-BH|Arabic (Bahrain)|
| ar-DZ|Arabic (Algeria)|
| ar-EG|Arabic (Egypt)|
| ar-IL|Arabic (Israel)|
| ar-IQ|Arabic (Iraq)|
| ar-JO|Arabic (Jordan)|
| ar-KW|Arabic (Kuwait)|
| ar-LB|Arabic (Lebanon)|
| ar-LY|Arabic (Libya)|
| ar-MA|Arabic (Morocco)|
| ar-OM|Arabic (Oman)|
| ar-PS|Arabic (Palestinian Territories)|
| ar-QA|Arabic (Qatar)|
| ar-SA|Arabic (Saudi Arabia)|
| ar-SY|Arabic (Syria)|
| ar-TN|Arabic (Tunisia)|
| ar-YE|Arabic (Yemen)|
| az-AZ|Azerbaijani (Latin, Azerbaijan)|
| bg-BG|Bulgarian (Bulgaria)|
| bn-IN|Bengali (India)|
| bs-BA|Bosnian (Bosnia and Herzegovina)|
| ca-ES|Catalan (Spain)|
| cs-CZ|Czech (Czechia)|
| cy-GB|Welsh (United Kingdom)|
| da-DK|Danish (Denmark)|
| de-AT|German (Austria)|
| de-CH|German (Switzerland)|
| de-DE|German (Germany)|
| el-GR|Greek (Greece)|
| en-AU|English (Australia)|
| en-CA|English (Canada)|
| en-GB|English (United Kingdom)|
| en-GH|English (Ghana)|
| en-HK|English (Hong Kong SAR)|
| en-IE|English (Ireland)|
| en-IN|English (India)|
| en-KE|English (Kenya)|
| en-NG|English (Nigeria)|
| en-NZ|English (New Zealand)|
| en-PH|English (Philippines)|
| en-SG|English (Singapore)|
| en-TZ|English (Tanzania)|
| en-US|English (United States)|
| en-ZA|English (South Africa)|
| es-AR|Spanish (Argentina)|
| es-BO|Spanish (Bolivia)|
| es-CL|Spanish (Chile)|
| es-CO|Spanish (Colombia)|
| es-CR|Spanish (Costa Rica)|
| es-CU|Spanish (Cuba)|
| es-DO|Spanish (Dominican Republic)|
| es-EC|Spanish (Ecuador)|
| es-ES|Spanish (Spain)|
| es-GQ|Spanish (Equatorial Guinea)|
| es-GT|Spanish (Guatemala)|
| es-HN|Spanish (Honduras)|
| es-MX|Spanish (Mexico)|
| es-NI|Spanish (Nicaragua)|
| es-PA|Spanish (Panama)|
| es-PE|Spanish (Peru)|
| es-PR|Spanish (Puerto Rico)|
| es-PY|Spanish (Paraguay)|
| es-SV|Spanish (El Salvador)|
| es-US|Spanish (United States)|
| es-UY|Spanish (Uruguay)|
| es-VE|Spanish (Venezuela)|
| et-EE|Estonian (Estonia)|
| eu-ES|Basque|
| fa-IR|Persian (Iran)|
| fi-FI|Finnish (Finland)|
| fil-PH|Filipino (Philippines)|
| fr-BE|French (Belgium)|
| fr-CA|French (Canada)|
| fr-CH|French (Switzerland)|
| fr-FR|French (France)|
| ga-IE|Irish (Ireland)|
| gl-ES|Galician|
| gu-IN|Gujarati (India)|
| he-IL|Hebrew (Israel)|
| hi-IN|Hindi (India)|
| hr-HR|Croatian (Croatia)|
| hu-HU|Hungarian (Hungary)|
| hy-AM|Armenian (Armenia)|
| id-ID|Indonesian (Indonesia)|
| is-IS|Icelandic (Iceland)|
| it-CH|Italian (Switzerland)|
| it-IT|Italian (Italy)|
| ja-JP|Japanese (Japan)|
| jv-ID|Javanese (Latin, Indonesia)|
| ka-GE|Georgian (Georgia)|
| kk-KZ|Kazakh (Kazakhstan)|
| km-KH|Khmer (Cambodia)|
| kn-IN|Kannada (India)|
| ko-KR|Korean (Korea)|
| lo-LA|Lao (Laos)|
| lt-LT|Lithuanian (Lithuania)|
| lv-LV|Latvian (Latvia)|
| mk-MK|Macedonian (North Macedonia)|
| ml-IN|Malayalam (India)|
| mn-MN|Mongolian (Mongolia)|
| mr-IN|Marathi (India)|
| ms-MY|Malay (Malaysia)|
| mt-MT|Maltese (Malta)|
| my-MM|Burmese (Myanmar)|
| nb-NO|Norwegian Bokmål (Norway)|
| ne-NP|Nepali (Nepal)|
| nl-BE|Dutch (Belgium)|
| nl-NL|Dutch (Netherlands)|
| pl-PL|Polish (Poland)|
| ps-AF|Pashto (Afghanistan)|
| pt-BR|Portuguese (Brazil)|0
| pt-PT|Portuguese (Portugal)|
| ro-RO|Romanian (Romania)|
| ru-RU|Russian (Russia)|
| si-LK|Sinhala (Sri Lanka)|
| sk-SK|Slovak (Slovakia)|
| sl-SI|Slovenian (Slovenia)|
| so-SO|Somali (Somalia)|
| sq-AL|Albanian (Albania)|
| sr-RS|Serbian (Cyrillic, Serbia)|
| sv-SE|Swedish (Sweden)|
| sw-KE|Swahili (Kenya)|
| sw-TZ|Swahili (Tanzania)|
| ta-IN|Tamil (India)|
| te-IN|Telugu (India)|
| th-TH|Thai (Thailand)|
| tr-TR|Turkish (Turkey)|
| uk-UA|Ukrainian (Ukraine)|
| uz-UZ|Uzbek (Latin, Uzbekistan)|
| vi-VN|Vietnamese (Vietnam)|
| wuu-CN|Chinese (Wu, Simplified)|
| yue-CN|Chinese (Cantonese, Simplified)|
| zh-CN|Chinese (Mandarin, Simplified)|
| zh-CN-shandong|Chinese (Jilu Mandarin, Simplified)|
| zh-CN-sichuan|Chinese (Southwestern Mandarin, Simplified)|
| zh-HK|Chinese (Cantonese, Traditional)|
| zh-TW|Chinese (Taiwanese Mandarin, Traditional)|
| zu-ZA|Zulu (South Africa)|

![Screenshot (17)](https://github.com/eralds/folGPT/assets/94328315/2915c02f-c57f-4611-9101-34b25751b9c5)

## License
This project is licensed under the MIT License.

## Acknowledgements
The [Flask web framework](https://flask.palletsprojects.com/en/2.3.x/)

The [Azure SDK](https://azure.microsoft.com/en-us/products/cognitive-services/speech-services/)

The [OpenAI API](https://openai.com/blog/openai-api)

This [GMass blog page](https://www.gmass.co/blog/record-audio-mobile-web-page-ios-android/) written by Ajay Goel.


Feel free to contribute to this project by opening issues or submitting pull requests. Enjoy using the web speech recognizer!
