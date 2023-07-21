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