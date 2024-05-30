import './assets/main.css'

import { createApp } from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core';
import { faPlay } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import App from './App.vue'
import router from './router'
import Primevue from 'primevue/config';

library.add(faPlay);

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon);

app.use(router)
app.use(Primevue)
app.mount('#app')




