import {createApp} from 'vue'
import router from './router';
import App from './App.vue'
import LPGenForm from './components/lp_generator_form.vue'
import LPForm from './components/lp_form.vue'
import Navbar from './components/Navbar.vue'
import NavbarLink from './components/NavbarLink.vue'
import Footer from './components/Footer.vue'
import FooterLogo from './components/FooterLogo.vue'
import Card from './components/card.vue'
import Deck from './components/deck.vue'
import TInput from './components/tinput.vue'
import './index.css'
// primevue
import PrimeVue from 'primevue/config';
import 'primeicons/primeicons.css'
import Chart from 'primevue/chart';
import InputNumber from 'primevue/inputnumber';
import Menubar from 'primevue/menubar';




const app = createApp(App)
app.use(router)
app.use(PrimeVue)
app.component('InputNumber', InputNumber)
app.component('Menubar', Menubar)
app.component('Chart', Chart);
// componetns from ejk
app.component('Card', Card)
app.component('Deck', Deck)
app.component('LPForm', LPForm)
app.component('Footer', Footer)
app.component('FooterLogo', FooterLogo)
app.component('LPGenForm', LPGenForm)
app.component('Navbar', Navbar)
app.component('NavbarLink', NavbarLink)
app.component('TInput', TInput)
app.mount('#app')