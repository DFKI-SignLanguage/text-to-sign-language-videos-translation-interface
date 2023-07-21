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
    <main>
        <head>
    <title>Übersetzungswebseite</title>
  </head>
  <body>
    <h1>Willkommen auf unserer Übersetzungswebseite!</h1>
    
    <nav>
      <label for="text">Gib den zu übersetzenden Text ein:</label><br>
      <textarea id="text" name="text" rows="4" cols="50"></textarea><br><br>
      

      <label for="language">Wähle die Zielsprache aus: </label>

      <select id="language" name="language">
        <option value="de">Deutsch</option>
        <option value="en">Englisch</option>
        <option value="fr">Französisch</option>
        
      </select><br><br>
      
      <input type="submit" value="Übersetzen">
    </nav>
    
    <div id="translation">
      <!-- Hier wird die übersetzte Version des Textes angezeigt -->
    </div>
    
    
  </body>
    </main>
</template>

<script>
// import { ref } from "vue";

import languages from '@/languages.json'
// import Dropdown from 'primevue/dropdown';

export default {
    
    
}

</script>

<!-- 
<script>
    // export default {
    //     props: ['language']
    // }
      // Hier kannst du JavaScript-Code einfügen, um den Text zu übersetzen
</script> -->

<style>
/* nav {
    display: flex;
    align-items: center;
    justify-content: center;
} */


</style>
  