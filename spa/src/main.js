import { createApp } from 'vue'
import App from './App.vue'
import store from "./util/store"
import "./index.css"

createApp(App).use(store).mount('#app')
