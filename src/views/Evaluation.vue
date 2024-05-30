<template>
  
  <div class="A">
    <textarea v-model="text" placeholder="Enter text to translate"></textarea><br>
    <h3 class="languageDirection">
      Choose the language direction:
    </h3>
    <select class="selectLanguage" v-model="sourceLanguage">
      <option v-for="(language, code) in languages" :value="code" :key="code">{{ language }}</option>
    </select>
    <button @click="translateAndGenerateVideo">Translate and Generate Video</button>
  </div>
  <div class="B">
    <h3>Translation result as sign language:</h3>
    <div class="video-container">
	    <div class="prevPreview-video" v-show="currentVideoIndex !== 0">
        <video :src="videos[currentVideoIndex - 1]" controls muted style="max-width: 150px;"></video>
      </div>
      <button class="prevVideo" @click="prevVideo" v-show="currentVideoIndex !== 0">&lt;</button>
      <div class="current-video">
        <video ref="video" :src="currentVideoSource" controls></video>
        <div class="perspective">
         <button @click="changeLastLetter('1')">front</button>
         <button @click="changeLastLetter('2')">oblique front</button>
         <button @click="changeLastLetter('3')">side</button>
         <button @click="changeLastLetter('4')">from above</button>
        </div>
        <div class="playbackspeedButton"></div>
        <select class="selectSpeed" @change="changeSpeed" v-model="selectedSpeed">
          <option value="0.1">0.1x</option>
          <option value="0.25">0.25x</option>
          <option value="0.5">0.5x</option>
          <option value="1.0">1x</option>
          <option value="1.5">1.5x</option>
        </select>
      </div>
      <div class="nextPreview-video" v-show="currentVideoIndex !== videos.length - 1">
        <video :src="videos[currentVideoIndex + 1]" controls muted style="max-width: 150px;"></video>
      </div>
      <button class="nextVideo" @click="nextVideo" v-show="currentVideoIndex !== videos.length - 1">&gt;</button>
    </div>

    <!-- Thumbnails row -->
    <div class="thumbnail-row">
      <video
        v-for="(video, index) in videos"
        :src="video"
        @click="switchMainVideo(index)"
        :key="index"
        poster=""
        alt="Video Thumbnail"
        muted
      ></video>
    </div>
  </div>

  <div>
    <h3 class="prototype-note">This is a prototype as part of a scientific thesis. The translation logic is not implemented yet, which is why it is only possible to translate example sentences. These sentences can be found here:
      <a href="https://forms.gle/D2TWbPP9goM3MuR18" target="_blank">Google Forms Survey</a>
    </h3>
  </div>
  <div>
    <h3>
      The videos are from the DGS corpus project, click here to go to their website:
      <a href="https://www.sign-lang.uni-hamburg.de/korpusdict/overview/intro.html" target="_blank">DGS-Korpus</a>
    </h3>
  </div>
  
</template>

<script>
import video1 from "@/assets/video_1.mp4";
import video2 from "@/assets/4427585_1.mp4";
import video3 from "@/assets/4363934_1.mp4";
import video4 from "@/assets/4440583_1.mp4";
import axios from 'axios';


export default {
data() {
  return {
    videos: [video1, video2, video3, video4],
    currentVideoIndex: 0,
    selectedVideoIndex: null,
    baseVideoWidth: 300, // Adjust the base width as needed
    videoMarginTopValue: 90, // Adjust the margin-top value as needed
    playingVideoZIndex: 2, // Set a higher zIndex for the playing video
    videoMarginLeftValue: 10, // Adjust the margin-left value as needed
    videoUrl: video1, // Initial video URL
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
    // New data properties to store selected perspective and speed
    selectedPerspective: '1',
  };
},
computed: {
  currentVideoSource() {
    return this.videos[this.currentVideoIndex];
  },
  
},
methods: {
  selectVideo(index) {
    this.selectedVideoIndex = index;
  },
  videoWidth(index) {
    if (this.selectedVideoIndex === null) {
      return this.baseVideoWidth;
    } else {
      return index === this.selectedVideoIndex ? this.baseVideoWidth * 2 : this.baseVideoWidth;
    }
  },
  videoMarginTop(index) {
    return index === this.selectedVideoIndex ? 0 : this.videoMarginTopValue;
  },
  videoZIndex(index) {
    return index === this.selectedVideoIndex ? 2 : 1;
  },
  videoMarginLeft(index) {
    return index === this.selectedVideoIndex ? 0 : this.videoMarginLeftValue;
  },
  changeSpeed() {
    const videoElement = this.$refs.video;
    videoElement.playbackRate = parseFloat(this.selectedSpeed);
  },
  changeLastLetter(lastLetter) {
	const currentVideo = this.videos[this.currentVideoIndex];
    const newVideoUrl = currentVideo.replace(/_[1-4]\.mp4$/, `_${lastLetter}.mp4`);
    
    this.$refs.video.src = newVideoUrl;

    // Update the selected perspective
    this.selectedPerspective = lastLetter;
  },
  prevVideo() {
    if (this.currentVideoIndex > 0) {
      this.currentVideoIndex--;
      // Use $nextTick to ensure that the DOM has been updated
      this.$nextTick(() => {
          // Update the src attribute and selected perspective for the new video
          const currentVideo = this.videos[this.currentVideoIndex];
          this.$refs.video.src = currentVideo.replace(/_[1-4]\.mp4$/, `_${this.selectedPerspective}.mp4`);
        });
    }
  },
  nextVideo() {
    if (this.currentVideoIndex < this.videos.length - 1) {
      this.currentVideoIndex++;
      // Log the current state before updating
      console.log('Before Update - currentVideoIndex:', this.currentVideoIndex);
        console.log('Before Update - selectedPerspective:', this.selectedPerspective);
       // Use $nextTick to ensure that the DOM has been updated
       this.$nextTick(() => {
          // Update the src attribute and selected perspective for the new video
          const currentVideo = this.videos[this.currentVideoIndex];
          this.$refs.video.src = currentVideo.replace(/_[1-4]\.mp4$/, `_${this.selectedPerspective}.mp4`);
        });
      // Log the current state after updating
      console.log('After Update - currentVideoIndex:', this.currentVideoIndex);
        console.log('After Update - selectedPerspective:', this.selectedPerspective);
     
   }
   
  },
  switchMainVideo(index) {
      // Switch the main video when a thumbnail is clicked
      this.currentVideoIndex = index;

      // Use $nextTick to ensure that the DOM has been updated
      this.$nextTick(() => {
        // Update the src attribute for the new main video
        const currentVideo = this.videos[this.currentVideoIndex];
        this.$refs.video.src = currentVideo;
        this.$refs.video.load(); // Reload the video to apply the changes
      });
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
  float: left;
  width: 85px;
  height: 25px;
  margin-left: 595px;
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


.video-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 600px;
  margin: 0 auto;
}

.current-video {
  flex-grow: 1;
}

.prevVideo {
  margin-left: -200px;
  margin-right: 200px;
}

.nextPreview-video {
  margin-left: -20px;
}

.nextVideo {
  margin-left: 20px;
}

.languageDirection {
margin-top: 20px;
}

.perspective {
  float: left;
}

.playbackspeedButton {
  float: left;
  margin-top: 10px;
}

.A{
float: left;
margin-top: 65px;
margin-left: -200px;
}

.B{
float: left;
margin-right: 20px;
margin-left: 200px;
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

/* Add styling for the thumbnail row and individual thumbnails */
.thumbnail-row {
  display: flex;
  justify-content: flex-start;
}

.thumbnail-row video {
  max-width: 150px; /* Set the maximum width for the thumbnail videos */
  width: 100%; /* Make sure the width is responsive within the maximum limit */
  height: auto; /* Automatically adjust the height while maintaining aspect ratio */
  margin-right: 10px; /* Adjust the margin as needed */
  cursor: pointer;
}

.main-video {
  /* Adjust styling for the main video container as needed */
  display: flex;
}
</style>
