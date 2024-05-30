<template>
  
  <div class="Alpha">
     <textarea v-model="text" @keydown.enter.prevent="handleEnter" placeholder="Enter text to translate"></textarea><br>
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
   <!--  <video ref="video" controls width="680" height="380">
    <source :src="videoUrl" type="video/mp4">
    </video> -->
    <!-- <div v-for="(videoSource, index) in videoSources" :key="index">
      <video controls width="400">
        <source :src="videoSource" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div> -->
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
   <!-- </div> -->

  </div>

  <div class="E">
    <h3 class="feedback">
      Please give us your feedback on the quality of the translation you just did:
    </h3>
<!--     <table class="feedbackTable">
      <thead class="columnTitle">
        <tr>
          <th style="width: 250px;">Words:</th>
          <th>Rating</th>
          <th>Comment</th>
        </tr>
      </thead>
      <tbody> -->
        <!-- Loop through each word in the translatedWords array -->
<!--         <tr v-for="(word, index) in uniqueTranslatedWords" :key="index">
          <td>
            <div class="criteria" style="font-size:25px;">
                {{ word }}
            </div>  
          </td>
          <td>
            <div class="rating">
              <button v-for="i in 5" :key="i" :class="{ active: i <= getRatingForWord(word),
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
            <input type="text" style="width: 250px;" v-model="overallComment" />
          </td>
        </tr> -->
        <!-- <tr>
      <td>
        <label for="sentence-rating">Overall Sentence Rating:</label>
      </td>
      <td>
        <div class="rating">
          <button v-for="i in 5" :key="i" :class="{ active: i <= overallRating, 
            'btn-red': i === 1,
            'btn-orange': i === 2,
            'btn-yellow': i === 3,
            'btn-light-green': i === 4,
            'btn-green': i === 5 }" 
            @click="updateOverallRating(i)">
            {{ i }}
          </button>
        </div>
      </td>
      <td>
        <input type="text" style="width: 250px;" v-model="overallComment" />
      </td>
    </tr> -->
<!--       </tbody>
    </table> -->

    <div class="feedback">
  <table class="feedbackTable">
    <thead class="columnTitle">
      <tr>
        <th></th>
        <th style="width: 4600px;">Criteria:</th>
        <th>Rating</th>
        <th>Comment</th>
      </tr>
    </thead>
    <tbody>
  <tr>
    <td></td> <!-- Empty first column -->
    <td style="font-size: 25px;">Fluency</td>
    <td>
      <div class="rating">
        <!-- For loop to generate rating buttons for Fluency -->
        <button v-for="i in 5" :key="'fluency-' + i" :class="getButtonClasses(i, 'fluency')" @click="updateRating(i, 'fluency')">
          {{ i }}
        </button>
      </div>
    </td>
    <td>
      <input type="text" style="width: 250px;" v-model="fluencyComment" />
    </td>
  </tr>
  
  <!-- Add similar rows for Adequacy and Overall Scores -->
  
  <tr>
    <td></td> <!-- Empty first column -->
    <td style="font-size: 25px;">Adequacy</td>
    <td>
      <div class="rating">
        <!-- For loop to generate rating buttons for Adequacy -->
        <button v-for="i in 5" :key="'adequacy-' + i" :class="getButtonClasses(i, 'adequacy')" @click="updateRating(i, 'adequacy')">
          {{ i }}
        </button>
      </div>
    </td>
    <td>
      <input type="text" style="width: 250px;" v-model="adequacyComment" />
    </td>
  </tr>
  
  <tr>
    <td></td> <!-- Empty first column -->
    <td style="font-size: 25px;">Overall Scores</td>
    <td>
      <div class="rating">
        <!-- For loop to generate rating buttons for Overall Scores -->
        <button v-for="i in 5" :key="'overall-' + i" :class="getButtonClasses(i, 'overall')" @click="updateRating(i, 'overall')">
          {{ i }}
        </button>
      </div>
    </td>
    <td>
      <input type="text" style="width: 250px;" v-model="overallComment" />
    </td>
  </tr>
</tbody>

  </table>
</div>

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
    translatedWords: [], // Define translatedWords as an empty array initially
    feedbackList: [],
    fluencyRating: 0,
    adequacyRating: 0,
    overallRating: 0,
    fluencyComment: '',
    adequacyComment: '',
    overallComment: ''
  };
},
computed: {
  currentVideoSource() {
    return this.videos[this.currentVideoIndex];
  },
  uniqueTranslatedWords() {
    return [...new Set(this.translatedWords)];
  }  
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
  
          // Extract video URLs from the translated words
          // const translatedWordsArray = Object.values(translated_words);
  
          // Update the videos array in your component state
          /* this.videos = await Promise.all(Object.values(translated_words).map(async (word, index) => {
              // Log the word to check its structure
              console.log('Word:', word);
  
              // Assuming each word is a string representing the file name without extension
              const videoPath = `../assets/${word}`;
              console.log('Importing video for path:', videoPath);
  
              try {
                  const { default: video } = await import(videoPath);
                  return video;
              } catch (importError) {
                  console.error('Error importing video:', importError);
                  return null;
              }
          })); */

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
  updateRating(index, value) {
    this.feedbackList[index].rating = value;
  },
  updateComment(index, text) {
    this.feedbackList[index].comment = text;
  },
  updateOverallRating(value) {
      this.overallRating = value;
    },
  getRatingForWord(word) {
    // Find the entry in feedbackList corresponding to the given word
    const entry = this.feedbackList.find(item => item.translation === word);
    // If entry is found, return its rating, otherwise return 0 (default)
    return entry ? entry.rating : 0;
  },
  getCommentForWord(word) {
    // Find the entry in feedbackList corresponding to the given word
    const entry = this.feedbackList.find(item => item.translation === word);
    // If entry is found, return its comment, otherwise return an empty string
    return entry ? entry.comment : '';
  },
  updateRating(rating, type) {
    // Update the rating based on the type (fluency, adequacy, overall)
    if (type === 'fluency') {
      this.fluencyRating = rating;
    } else if (type === 'adequacy') {
      this.adequacyRating = rating;
    } else if (type === 'overall') {
      this.overallRating = rating;
    }
  },
  getButtonClasses(rating, type) {
    // Dynamically set button classes based on rating and type
    return {
      active: rating <= this.getRating(type),
      'btn-red': rating === 1,
      'btn-orange': rating === 2,
      'btn-yellow': rating === 3,
      'btn-light-green': rating === 4,
      'btn-green': rating === 5
    };
  },
  getRating(type) {
    // Get the current rating based on the type (fluency, adequacy, overall)
    if (type === 'fluency') {
      return this.fluencyRating;
    } else if (type === 'adequacy') {
      return this.adequacyRating;
    } else if (type === 'overall') {
      return this.overallRating;
    }
    return 0;
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
  /* display: flex;
  white-space: nowrap; */ /* Prevents videos from wrapping to the next line */
  /* overflow-x: auto; */ /* Add horizontal scrollbar if content overflows */
  /* height: 400px; */
  /* width: 1800px;  */
  /* padding-right: 20px; */ /* Add padding to ensure the scrollbar doesn't overlap content */
  /* margin-right: -800px; */
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

.Alpha{
float: left;
margin-top: 65px;
margin-left: -200px;
}

.Beta{
float: left;
margin-right: 220px;
margin-left: -550px;
}



.E{
  margin-top: 50px;
  margin-left: -50px;
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
    width: 600px;
    justify-content: flex-start;
    overflow-x: auto; /* Add horizontal scrollbar if content overflows */
    white-space: nowrap; /* Prevents videos from wrapping to the next line */
  }

.thumbnail-row video {
  max-width:150px; /* Set the maximum width for the thumbnail videos */
  width: 100%; /* Make sure the width is responsive within the maximum limit */
  height: auto; /* Automatically adjust the height while maintaining aspect ratio */
  margin-right: 10px; /* Adjust the margin as needed */
  cursor: pointer;
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

.feedback{
  font-style: oblique;
  font-weight: 500;
}

.feedbackTable{
  margin-top: 20px;
}

.feedback .feedbackTable th:first-child {
  width: 250px; /* Set width for the first column */
}

.columnTitle{
  font-size: 20px;
}

.criteria{
  width: 250px;
  margin-left: 0px;
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



