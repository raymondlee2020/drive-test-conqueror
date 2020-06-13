import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'
import Sign from '../views/Sign'
import Quiz from '../views/Quiz'
import Practice from '../views/Practice'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign',
    name: 'Sign',
    component: Sign
  },
  {
    path: '/quiz',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/practice',
    name: 'Practice',
    component: Practice
  }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
