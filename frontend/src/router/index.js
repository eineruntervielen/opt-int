import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/lp',
    name: 'LP',
    component: () => import(/* webpackChunkName: "about" */ '../views/LP.vue')
  },
  {
    path: '/info',
    name: 'Info',
    component: () => import(/* webpackChunkName: "about" */ '../views/Info.vue')
  },
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router