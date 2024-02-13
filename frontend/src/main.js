import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css'

import './assets/styles/main.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'


createApp(App)
    .use(store)
    .use(router)
    .use(axios)
    .mount('#app')
