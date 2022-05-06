import { createApp } from 'vue'
import router from './router';
import App from './App.vue'
import LPGenForm from './components/lp_generator_form.vue'
import LPForm from './components/lp_form.vue'
import Sidebar from './components/sidebar.vue'
import SBBtn from './components/sidebar_btn.vue'
import Card from './components/card.vue'
import Deck from './components/deck.vue'
import './index.css'



const app = createApp(App)
app.use(router)
app.component('Card', Card)
app.component('Deck', Deck)
app.component('LPForm', LPForm)
app.component('LPGenForm', LPGenForm)
app.component('SBBtn', SBBtn)
app.component('Sidebar', Sidebar)
app.mount('#app')