import {createApp} from 'vue'
import router from './router';
import App from './App.vue'
import LPGenForm from './components/lp_generator_form.vue'
import LPForm from './components/lp_form.vue'
import Navbar from './components/Navbar.vue'
import NavbarLink from './components/NavbarLink.vue'
import Footer from './components/Footer.vue'
import FooterLogo from './components/FooterLogo.vue'
import Deck from './components/deck.vue'
import TInput from './components/tinput.vue'
import './index.css'
// primevue
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

import Chart from 'primevue/chart';
import InputNumber from 'primevue/inputnumber';
import Menubar from 'primevue/menubar';
import InputText from 'primevue/inputtext';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button';



const app = createApp(App)
app.use(router)
app.use(PrimeVue)
app.component('Button', Button)
app.component('Menubar', Menubar)
app.component('Column', Column)
app.component('DataTable', DataTable)
app.component('InputText', InputText)
app.component('InputNumber', InputNumber)
app.component('Chart', Chart)
// componetns from ejk
app.component('Navbar', Navbar)
// ---
app.component('Deck', Deck)
app.component('LPForm', LPForm)
app.component('Footer', Footer)
app.component('FooterLogo', FooterLogo)
app.component('LPGenForm', LPGenForm)
app.component('NavbarLink', NavbarLink)
app.component('TInput', TInput)
app.mount('#app')