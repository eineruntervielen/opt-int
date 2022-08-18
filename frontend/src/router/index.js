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
    component: () => import('../views/LinearProgramming/LP.vue')
  },
  {
    path: '/staffscheduling',
    name: 'StaffScheduling',
    component: () => import('../views/StaffScheduling/StaffScheduling.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../views/Contact.vue')
  },
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router