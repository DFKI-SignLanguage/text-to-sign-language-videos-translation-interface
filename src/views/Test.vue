<template>
  
 
  <div class="Alpha">
     <textarea v-model="text" placeholder="Enter text to translate"></textarea><br>
     <h3 class="languageDirection">
       Choose the language direction:
     </h3>
     <select class="selectLanguage" v-model="sourceLanguage">
       <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
     </select>
     <button @click="translateAndGenerateVideo">Translate and Generate Video</button>
  </div>
  <div class="Beta">
    <h3>Translation result as sign language:</h3>
    <p>{{ translation }}</p>
    <!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/-81RIxbkE24?si=TGvuksokQRqPe4Jp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> -->
    <!-- <video id="player" src="https://www.sign-lang.uni-hamburg.de/korpusdict/clips/4439167_1.mp4" width="520" height="380" muted="muted" autoplay="autoplay" onclick="if (this.paused) { this.play(); } else { this.pause(); }; return true;"></video>  -->
    <video ref="video" controls width="680" height="380">
    <source :src="videoUrl" type="video/mp4">
    </video>
    <div class="C">
      <select class="selectSpeed" @change="changeSpeed" v-model="selectedSpeed">
        <option value="0.25">0.25x</option>
        <option value="0.5">0.5x</option>
        <option value="1.0">1x</option>
        <option value="1.5">1.5x</option>
        <option value="2.0">2x</option>
      </select>
    </div> 
    <div class="D">
      <button @click="changeLastLetter('1')">front</button>
      <button @click="changeLastLetter('2')">oblique front</button>
      <button @click="changeLastLetter('3')">side</button>
      <button @click="changeLastLetter('4')">from above</button>
    </div>
  </div>
  <div class="E">
      <h3 class="feedback">
        Please give us your feedback on the quality of the translation you just did:
      </h3>
      <table class="feedbackTable">
        <thead class="columnTitle">
          <tr>
            <th>Criteria</th>
            <th>Rating</th>
            <th>Comment</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(feedback, index) in feedbackList" :key="index">
            <td>
              <div class="criteria">
                {{ feedback.translation }}
              </div>  
            </td>
            <td>
              <div class="rating">
                <button v-for="i in 5" :key="i" :class="{ active: i <= feedback.rating, 
                  'btn-red': i === 1,
                  'btn-orange': i === 2,
                  'btn-yellow': i === 3,
                  'btn-light-green': i === 4,
                  'btn-green': i === 5 }" 
                  @click="updateRating(index, i)">
                  {{ i }}
                </button>
              </div>
            </td>
            <td>
              <input type="text" style="width: 250px;" v-model="feedback.comment" />
            </td>
          </tr>
        </tbody>
      </table>
  </div>

  

</template>

<script>
export default {
data() {
  return {
    videoUrl: 'src/assets/video_1.mp4', // Initial video URL
    text: '',
    sourceLanguage: 'de',
    languages: {
      de: 'German > DGS',
      en: 'English > ASL',
      fr: 'French > LSF',
      es: 'Spanish > LSE',
      cn: 'Chinese > CSL',
      // Add more language codes and names as needed
    },
    translation: '',
    selectedSpeed: '1.0', // Initial selected speed
    feedbackList: [
        { translation: 'General Quality', rating: 0, comment: '' },
        { translation: 'Grammar', rating: 0, comment: '' },
        // Add more translations as needed
      ],
  };
},
methods: {
  changeSpeed() {
    const videoElement = this.$refs.video;
    videoElement.playbackRate = parseFloat(this.selectedSpeed);
  },
  changeLastLetter(lastLetter) {
    const oldUrl = this.videoUrl
    this.videoUrl = oldUrl.slice(0, -5) + lastLetter + ".mp4"; // Update the URL with the last letter changed
    const videoElement = this.$refs.video;
    videoElement.load(); // Reload the video with the new URL
  },
  updateRating(index, value) {
      this.feedbackList[index].rating = value;
    },
    updateComment(index, text) {
      this.feedbackList[index].comment = text;
    },
  async translateAndGenerateVideo() {
    const apiKey = 'YOUR_API_KEY';
    const endpoint = `https://api.signlanguage.com`;
    
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          text: this.text,
          source_lang: this.sourceLanguage,
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
  width: 220px;
  height: 25px;
  border: 1px solid #999;
  font-size: 18px;
  color: hsla(160, 100%, 37%, 1);
  background-color: #eee;
  border-radius: 5px;
  box-shadow: 4px 4px #ccc;
  appearance: none;
  background: url("@/assets/down-arrow-5.png") 96% / 10% no-repeat #eee;
}

.selectSpeed {
  width: 85px;
  height: 25px;
  margin-left: 595px;
  margin-top: -20px;
  border: 1px solid #999;
  font-size: 15px;
  color: hsla(160, 100%, 37%, 1);
  background-color: #eee;
  border-radius: 5px;
  /* box-shadow: 4px 4px #ccc; */
  appearance: none;
  background: url("@/assets/down-arrow-5.png") 96% / 10% no-repeat #eee;
  background: url("@/assets/speed.png") 96% / 40% no-repeat #eee;
  
}

.videoSpeed {
font-size: 10px;
}

.languageDirection {
margin-top: 20px;
}

.Alpha{
float: left;
margin-top: 65px;
}
.Beta{
float: left;
margin-left: -550px;
}

.C{
margin-top: 0px;
}

.D{
margin-top: -20px;
}

.E{
  margin-top: 50px;
}

/* .F{
  margin-top: 80px;
  margin-right: 400px;
} */

.feedback{
  font-style: oblique;
  font-weight: 500;
}

.feedbackTable{
  margin-top: 20px;
}

.columnTitle{
  font-size: 20px;
}

.criteria{
  width: 150px;
}

button {
width: 250px;
height: 25px;
margin-left: 30px;
border: 1px solid #999;
font-size: 16px;
color: hsla(160, 100%, 37%, 1);
background-color: #eee;
border-radius: 5px;
box-shadow: 4px 4px #ccc;
}

.rating {
  display: flex;
  margin-right: 50px;
}

.rating button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  width: 100px;
}

.btn-red {
  color: red;
}

.btn-orange {
  color: orange;
}

.btn-yellow {
  color: #FFD700;
}

.btn-light-green {
  color: lightgreen;
}

.btn-green {
  color: green;
}

</style>
