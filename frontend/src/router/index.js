import {createRouter, createWebHistory} from 'vue-router'
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
        path: '/knapsack',
        name: 'Knapsack',
        component: () => import('../views/Knapsack/Knapsack.vue')
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue')
    },
]
const router = createRouter({
    history: createWebHistory(),
    routes
})
export default router