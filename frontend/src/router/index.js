import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import LogOut from '../views/LogOut.vue'
import PostDetail from '../views/PostDetail.vue'
import SearchView from '../views/SearchView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'logIn',
    component: LogIn
  },
  {
    path: '/log-out',
    name: 'logOut',
    component: LogOut
  },
  {
    path: '/post/:slug',
    name: 'postDetail',
    component: PostDetail
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router