<!-- <template>
    <div class="card flex justify-content-center">
        <Dropdown v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a Language" class="w-full md:w-14rem" /><br>
        <input type="submit" value="Übersetzen">
    </div>
</template>

<script setup>
import { ref } from "vue";
import Dropdown from 'primevue/dropdown';

const selectedCity = ref();
const cities = ref([
  { "id": 1, "name": "Deutsch" },
  { "id": 2, "name": "Englisch" },
  { "id": 3, "name": "Spanisch" },
  { "id": 4, "name": "Französisch" },
  { "id": 5, "name": "Italienisch" },
  { "id": 6, "name": "Portugiesisch" },
  { "id": 7, "name": "Niederländisch" },
  { "id": 8, "name": "Russisch" },
  { "id": 9, "name": "Chinesisch" },
  { "id": 10, "name": "Japanisch" },
  { "id": 11, "name": "Koreanisch" },
  { "id": 12, "name": "Arabisch" },
  { "id": 13, "name": "Türkisch" },
  { "id": 14, "name": "Polnisch" },
  { "id": 15, "name": "Schwedisch" },
  { "id": 16, "name": "Dänisch" },
  { "id": 17, "name": "Norwegisch" },
  { "id": 18, "name": "Finnisch" },
  { "id": 19, "name": "Griechisch" },
  { "id": 20, "name": "Ungarisch" }
]);
</script> -->

<!-- <template>
    <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Translation Website</title>
</head>
<body>
  <div id="app">
    <h1>Translation Website</h1>
    <div>
      <label for="text">Enter text:</label>
      <textarea id="text" v-model="inputText"></textarea>
    </div>
    <div>
      <button @click="translate">Translate</button>
    </div>
    <div v-if="translatedText">
      <h2>Translation:</h2>
      <p>{{ translatedText }}</p>
    </div>
  </div>

  
</body>
</template> -->

<!-- <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="app.js"></script> -->

<!-- <script>
  data ()  {
    return {
    inputText: '',
    translatedText: ''
    }
  },
  methods: {
    translate() {
      // Make an API request to a translation service
      axios.get('https://api.translation-service.com/translate', {
        params: {
          text: this.inputText,
          from: 'en',
          to: 'fr' // Translate from English to French (change to the desired language)
        }
      })
      .then(response => {
        this.translatedText = response.data.translation;
      })
      .catch(error => {
        console.error(error);
      });
    }
  }
</script> -->
<!-- 
<template>
    <div>
      <textarea v-model="text" placeholder="Enter text to translate"></textarea>
      <select v-model="sourceLanguage">
        <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
      </select>
      <select v-model="targetLanguage">
        <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
      </select>
      <button @click="translate">Translate</button>
      <div>
        <h3>Translation Result:</h3>
        <p>{{ translation }}</p>
      </div>
    </div>
  </template> -->
<!--   
  <script>
  export default {
    data() {
      return {
        text: '',
        sourceLanguage: 'en',
        targetLanguage: 'fr',
        languages: {
          en: 'English',
          fr: 'French',
          de: 'German',
          es: 'Spanish',
        },
        translation: '',
      };
    },
    methods: {
      async translate() {
        const apiKey = 'YOUR_DEEPL_API_KEY';
        const endpoint = `https://api-free.deepl.com/v2/translate?auth_key=${apiKey}`;
        
        try {
          const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
              text: this.text,
              source_lang: this.sourceLanguage,
              target_lang: this.targetLanguage,
            }),
          });
          
          const data = await response.json();
          if (response.ok) {
            this.translation = data.translations[0].text;
          } else {
            this.translation = 'Translation failed';
            console.error(data);
          }
        } catch (error) {
          this.translation = 'Translation failed';
          console.error(error);
        }
      },
    },
  };
  </script> -->
<!--   
  <style>

  </style> -->

  <template>
    <div>
      <textarea v-model="text" placeholder="Enter text to translate"></textarea><br>
      <select class="selectLanguage" v-model="sourceLanguage">
        <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
      </select>
      <select class="selectLanguage" v-model="targetLanguage">
        <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
      </select>
      <button @click="translateAndGenerateVideo">Translate and Generate Video</button>
      <div>
        <h3>Translation result as sign language :</h3>
        <p>{{ translation }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        text: '',
        sourceLanguage: 'en',
        targetLanguage: 'fr',
        languages: {
          en: 'English',
          fr: 'French',
          de: 'German',
          es: 'Spanish',
          // Add more language codes and names as needed
        },
        translation: '',
      };
    },
    methods: {
      async translateAndGenerateVideo() {
        const apiKey = 'YOUR_DEEPL_API_KEY';
        const endpoint = `https://api.deepl.com`;
        
        try {
          const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
              text: this.text,
              source_lang: this.sourceLanguage,
              target_lang: this.targetLanguage,
            }),
          });
          
          const data = await response.json();
          if (response.ok) {
            this.translation = data.translations[0].text;
            this.generateVideo();
          } else {
            this.translation = 'Translation failed';
            console.error(data);
          }
        } catch (error) {
          this.translation = 'Translation failed';
          console.error(error);
        }
      },
      generateVideo() {
        const utterance = new SpeechSynthesisUtterance(this.translation);
        utterance.lang = this.targetLanguage;
        
        const audioChunks = [];
        utterance.addEventListener('end', () => {
          const audioBlob = new Blob(audioChunks);
          const audioUrl = URL.createObjectURL(audioBlob);
          this.createVideoFromAudio(audioUrl);
        });
        
        utterance.addEventListener('error', (error) => {
          console.error('Text-to-speech error:', error);
        });
        
        utterance.addEventListener('audioprocess', (event) => {
          const { inputBuffer } = event;
          const channelData = inputBuffer.getChannelData(0);
          const clonedData = Float32Array.from(channelData);
          audioChunks.push(clonedData);
        });
        
        speechSynthesis.speak(utterance);
      },
      createVideoFromAudio(audioUrl) {
        // Here, you can use additional libraries or services to create a video from the audio URL
        // The implementation of this step depends on your chosen video generation method
        console.log('Video creation placeholder');
      },
    },
  };
  </script>
  
  <style>
  textarea {
  resize: none;
  width: 500px;
  height: 300px;
  font-size: 18px;
  }

  .selectLanguage {
      width: 150px;
      height: 25px;
      border: 1px solid #999;
      font-size: 18px;
      color: hsla(160, 100%, 37%, 1);
      background-color: #eee;
      border-radius: 5px;
      box-shadow: 4px 4px #ccc;
      appearance: none;
      background: url("@/assets/down-arrow-5.png") 96% / 15% no-repeat #eee;
  }

  button {
    width: 250px;
    height: 25px;
    border: 1px solid #999;
    font-size: 16px;
    color: hsla(160, 100%, 37%, 1);
    background-color: #eee;
    border-radius: 5px;
    box-shadow: 4px 4px #ccc;
  }
  </style>
  
  