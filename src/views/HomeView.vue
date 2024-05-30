<template>
  
  <div class="A">
    <textarea v-model="text" @keydown.enter.prevent="handleEnter" placeholder="Enter text to translate"></textarea><br>
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
    <p>{{ translation }}</p>

    <div class="video-container">
      <!-- <div class="main-video"> -->
      <div class="prevPreview-video" v-show="currentVideoIndex !== 0">
        <video :src="videos[currentVideoIndex - 1]" controls muted style="max-width: 150px;"></video>
      </div>
      <button class="prevVideo" @click="prevVideo" v-show="currentVideoIndex !== 0">&lt;</button>
      <div class="current-video">
        <div v-if="currentVideoSource">
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

        <div v-else>
          <div class="main-video-placeholder" v-show="!currentVideoSource">
          <!-- This div will show when there is no current video -->
            <div class="video-overlay">
              <font-awesome-icon icon="play" />
            </div>
          </div>
        </div>
      </div>
      <div class="nextPreview-video" v-if="currentVideoSource" v-show="currentVideoIndex !== videos.length - 1">
        <video :src="videos[currentVideoIndex + 1]" controls muted style="max-width: 150px;"></video>
      </div>
      <button class="nextVideo" v-if="currentVideoSource" @click="nextVideo" v-show="currentVideoIndex !== videos.length - 1">&gt;</button>
    </div>

    <!-- Thumbnails row -->
    <div class="thumbnail-row">
      <div v-for="(video, index) in videos" :key="index" class="thumbnail-container">
        <video
          :src="video"
          @click="switchMainVideo(index)"
          :class="{ 'playing': index === currentVideoIndex }"
          poster=""
          alt="Video Thumbnail"
          muted
          style="width: 150px;"
        ></video>
        <!-- Display the word underneath the thumbnail -->
        <div class="word-overlay">{{ translatedWords[index] }}</div>
      </div>
    </div>
    <div class="controls">
      <button @click="playAllVideos">Play All Videos</button>
      <button @click="stopPlaying">Stop</button>
    </div>
  </div>

  <div>
    <h3 class="prototype-note">This is a prototype as part of a scientific thesis. The translation logic is not implemented yet, which is why it is only possible to translate example sentences. These sentences can be found here:
      <a href="https://forms.gle/D2TWbPP9goM3MuR18" target="_blank">Google Forms Survey</a>
      The videos are from the DGS corpus project, click here to go to their website:
      <a href="https://www.sign-lang.uni-hamburg.de/korpusdict/overview/intro.html" target="_blank">DGS-Korpus</a>
    </h3>
  </div>
</template>

<script>
import video1 from "@/assets/videos/video_1.mp4";
import video2 from "@/assets/videos/4427585_1.mp4";
import video3 from "@/assets/videos/4363934_1.mp4";
import axios from 'axios';
import { faPlay } from '@fortawesome/free-solid-svg-icons';


export default {
data() {
  return {
    videos: [],
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
/*       en: 'English > ASL',
      fr: 'French > LSF',
      es: 'Spanish > LSE',
      cn: 'Chinese > CSL', */
      // Add more language codes and names as needed
    },
    translation: '',
    selectedSpeed: '1.0', // Initial selected speed
    // New data properties to store selected perspective and speed
    selectedPerspective: '1',
    translatedWords: [], // Define translatedWords as an empty array initially
  };
},
computed: {
  currentVideoSource() {
    return this.videos[this.currentVideoIndex];
  }, 
},
methods: {
  handleEnter(event) {
      if (event.keyCode === 13) {
        this.translateAndGenerateVideo();
      }
    },
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

    // Set the playback speed for the current video in the array
    this.$set(this.playbackSpeeds, this.currentVideoIndex, this.selectedSpeed);
  },
  changeLastLetter(lastLetter) {
    //const oldUrl = this.videoUrl
    //this.videoUrl = oldUrl.slice(0, -5) + lastLetter + ".mp4"; // Update the URL with the last letter changed
    const currentVideo = this.videos[this.currentVideoIndex];
    const newVideoUrl = currentVideo.replace(/_[1-4]\.mp4$/, `_${lastLetter}.mp4`);
    
    this.$refs.video.src = newVideoUrl;

    // Update the selected perspective
    this.selectedPerspective = lastLetter;
  },
  setPlaybackSpeed(speed) {
    const videoElement = this.$refs.video;
    videoElement.playbackRate = speed;
  },
  prevVideo() {
    if (this.currentVideoIndex > 0) {
      this.currentVideoIndex--;

      const currentSpeed = parseFloat(this.selectedSpeed);
      
      // Update the src attribute and selected perspective for the new video
      const currentVideo = this.videos[this.currentVideoIndex];
      this.$refs.video.src = currentVideo.replace(/_[1-4]\.mp4$/, `_${this.selectedPerspective}.mp4`);
      
      // Use $nextTick to ensure that the DOM has been updated
      this.$nextTick(() => {
        this.setPlaybackSpeed(currentSpeed);
        //this.$refs.video.play();
      });
    }
  },
  nextVideo() {
    if (this.currentVideoIndex < this.videos.length - 1) {
      this.currentVideoIndex++;
      const currentSpeed = parseFloat(this.selectedSpeed);
      
      // Update the src attribute and selected perspective for the new video
      const currentVideo = this.videos[this.currentVideoIndex];
      this.$refs.video.src = currentVideo.replace(/_[1-4]\.mp4$/, `_${this.selectedPerspective}.mp4`);
      
      // Use $nextTick to ensure that the DOM has been updated
      this.$nextTick(() => {
        this.setPlaybackSpeed(currentSpeed);
        //this.$refs.video.play();
      });
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
  async translateAndGenerateVideo() {
    try {
      // Retrieve CSRF token from cookie if necessary
      const csrftoken = this.getCookie('csrftoken');
      console.log('CSRF Token:', csrftoken);
  
      console.log('Text:', this.text);
  
      // Make a POST request to your Django backend
      const response = await axios.post(
        'http://janis.9kmzimzwnemgjob5.myfritz.net:5174/api/translate/',
        {
          text: this.text,
          source_language: this.sourceLanguage,
        },
        {
          headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );
  
      // Log the response from the backend
      console.log('Backend Response:', response.data);
  
      // Handle the response from the backend
      const { translated_words } = response.data;
      console.log('Translated words:', translated_words);
      this.translatedWords = translated_words.map(tuple => tuple[0]); // Set translatedWords with the received data

      // Update the videos array in your component state
      this.videos = await Promise.all(translated_words.map(async (tuple, index) => {
        const [word, videoUrl] = tuple; // Destructure the tuple to get the second element (video URL)
              
        // Log the video URL to check its structure
        console.log('Video URL:', videoUrl);
        const videoPath = `../assets/videos/${videoUrl}`;
        console.log('Importing video for path:', videoPath);
          
        try {
          const { default: video } = await import(videoPath);
          return video;
        } catch (importError) {
            console.error('Error importing video:', importError);
            return null;
          }
      }));
  
  
    } catch (error) {
        console.error('Error translating text:', error);
      }
  },
  // Utility function to retrieve a cookie value by name
  getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  },
  async playAllVideos() {
    // Get the main video element
    const mainVideo = this.$refs.video;

    // Add an event listener to handle the "ended" event
    mainVideo.addEventListener('ended', this.playNextVideo);

    // Function to set playback rate for all videos
    const setPlaybackRateForAllVideos = () => {
        const videos = document.querySelectorAll('.video-container video');
        videos.forEach(video => {
            video.playbackRate = parseFloat(this.selectedSpeed);
        });
    };
    // Iterate through each video in the 'videos' array
    for (let i = 0; i < this.videos.length; i++) {
      // Update the 'currentVideoIndex' to play the next video
      this.currentVideoIndex = i;

      // Update the 'src' attribute for the new main video
      mainVideo.src = this.videos[i];

      // Set the selected perspective
      this.changeLastLetter(this.selectedPerspective);

      // Set playback rate for all videos
      setPlaybackRateForAllVideos();

      // Play the main video
      mainVideo.play();

      // Wait for the current video to finish playing
      await new Promise(resolve => {
        // Resolve the promise when the "ended" event is triggered
        mainVideo.addEventListener('ended', function onEnded() {
          mainVideo.removeEventListener('ended', onEnded);
          resolve();
        });
      });

      // Scroll the thumbnail row to the right
      const thumbnailRow = document.querySelector('.thumbnail-row');
      thumbnailRow.scrollLeft += 160; // Adjust the value based on your thumbnail width

      // You can add a delay here if needed
      // await new Promise(resolve => setTimeout(resolve, 2000));
    }
    // Remove the event listener after all videos have been played
    mainVideo.removeEventListener('ended', this.playNextVideo);
  },
  // Method to play the next video
  playNextVideo() {
    // Increment the 'currentVideoIndex' if there is a next video
    if (this.currentVideoIndex < this.videos.length - 1) {
      this.currentVideoIndex++;
      this.$refs.video.src = this.videos[this.currentVideoIndex];
      this.$refs.video.play();
    }
  },
  stopPlaying() {
    // Get the main video element
    const mainVideo = this.$refs.video;

    // Pause and reset the video
    mainVideo.pause();
    mainVideo.currentTime = 0;

    // Reload the video by setting the src attribute again
    mainVideo.src = this.videos[this.currentVideoIndex];

    // Remove the event listener
    mainVideo.removeEventListener('ended', this.playNextVideo);
  },
},
};
</script>

<style>
#app {
  max-width: 900px;
  max-height: 500px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}

body {
  overflow-y: scroll;
}

textarea {
  width: 100%; /* Use 100% width to fill the container */
  max-width: 500px; /* Set maximum width to prevent textarea from becoming too wide */
  height: 200px; /* Adjust height as needed */
  font-size: 18px;
}

select:hover{
  cursor: pointer;
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
  margin-top: -30px;
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

.selectLanguage, .selectSpeed {
  width: 100%; /* Use 100% width to fill the container */
  max-width: 220px; /* Set maximum width to prevent dropdown from becoming too wide */
  height: 25px;
  font-size: 18px;
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

.current-video video {
  width: 100%; /* Use 100% width to fill the container */
  max-width: 600px; /* Set maximum width for the video */
  height: auto; /* Automatically adjust height */
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

button:hover {
  cursor:pointer; /* Change cursor style on hover */
  background-color:gray;
  transition: 0.7s;
}

/* Add styling for the thumbnail row and individual thumbnails */
.thumbnail-row {
    display: flex;
    width: 600px;
    justify-content: flex-start;
    overflow-x: auto; /* Add horizontal scrollbar if content overflows */
    white-space: nowrap; /* Prevents videos from wrapping to the next line */
    margin-top: 20px;
    flex-wrap: nowrap; /* Prevent thumbnails from wrapping to the next line */
  }

  .thumbnail-row video {
  max-width: 150px;
  width: auto;
  height: auto;
  margin-right: 10px;
}

.thumbnail-row video.playing {
  border: 2px solid red; /* Adjust border style for the playing video */
}

.thumbnail-container {
  position: relative;
}

.word-overlay {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(255, 255, 255, 0.8);
  padding: 2px 5px;
  font-size: 14px;
  white-space: nowrap;
  border-radius: 5px;
}

.main-video {
  /* Adjust styling for the main video container as needed */
  display: flex;
}

.controls {
  margin-top: 20px;
}

.main-video-placeholder {
  width: 100%;
  height: 380px; /* Adjust the height as needed */
  background-color: #f5f5f5; /* Grey background color */
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-overlay {
  font-size: 50px; /* Adjust the size of the icon */
  color: #555; /* Icon color */
}

.prototype-note {
  margin-top: 50px;
  margin-left: -200px;
  width: 200%;
  text-align: justify;
}
</style>
