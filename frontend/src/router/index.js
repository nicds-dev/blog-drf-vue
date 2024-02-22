import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUp from '@/views/auth/SignUp.vue'
import LogIn from '@/views/auth/LogIn.vue'
import LogOut from '@/views/auth/LogOut.vue'
import PostDetail from '@/views/PostDetail.vue'
import SearchView from '@/views/SearchView.vue'
import Admin from '@/views/Admin.vue'
import Create from '@/views/admin/Create.vue'
import Update from '@/views/admin/Update.vue'
import Delete from '@/views/admin/Delete.vue'


const routes = [
  {
    path: '/', name: 'home', component: HomeView
  },
  {
    path: '/admin', name: 'admin', component: Admin
  },
  {
    path: '/admin/create', name: 'create', component: Create
  },
  {
    path: '/admin/update/:id', name: 'update', component: Update
  },
  {
    path: '/admin/delete/:id', name: 'delete', component: Delete
  },
  {
    path: '/sign-up', name: 'signUp', component: SignUp
  },
  {
    path: '/log-in', name: 'logIn', component: LogIn
  },
  {
    path: '/log-out', name: 'logOut', component: LogOut
  },
  {
    path: '/post/:slug', name: 'postDetail', component: PostDetail
  },
  {
    path: '/search', name: 'search', component: SearchView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
