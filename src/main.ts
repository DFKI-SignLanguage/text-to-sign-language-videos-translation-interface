import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Primevue from 'primevue/config';

const app = createApp(App)

app.use(router)
app.use(Primevue)

app.mount('#app')
