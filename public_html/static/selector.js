const languageSelect = document.getElementById('language-select');
const voiceSelect = document.getElementById('voice-select');
let languageOptions;
let voiceOptions;

// Get URL parameters
const urlParams = new URLSearchParams(window.location.search);
const langParam = urlParams.get('lang');
const voiceParam = urlParams.get('voice');

// Update voice options based on selected language
function updateVoiceOptions() {
    const selectedLanguage = languageSelect.value
    // Remove previous voice options
    while (voiceSelect.firstChild) {
        voiceSelect.removeChild(voiceSelect.firstChild);
    }
    // Get voice options for selected language
    const selectedVoiceOptions = voiceOptions[selectedLanguage]
    // Add new voice options
    selectedVoiceOptions.forEach(option => {
        const { value, label } = option;
        voiceSelect.options.add(new Option(label, value));
    });
};
// Fetch language and voice options from JSON file
fetch('static/languages.json')
    .then(response => response.json())
    .then(data => {
        languageOptions = data.languages;
        voiceOptions = data.voices;

        // Populate language options
        languageOptions.forEach(option => {
            const { value, label } = option;
            languageSelect.options.add(new Option(label, value));
        });

        if (langParam) {
            languageSelect.value = langParam;
        }
        
        updateVoiceOptions();

        if (voiceParam) {
            voiceSelect.value = voiceParam;
        }
    })
    .catch(error => console.log(error));