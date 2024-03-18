import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
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
    path: '/', name: 'home', component: HomeView,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/search', name: 'search', component: SearchView,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/post/:slug', name: 'postDetail', component: PostDetail,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/sign-up', name: 'signUp', component: SignUp,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/log-in', name: 'logIn', component: LogIn,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: '/admin', name: 'admin', component: Admin,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/admin/create', name: 'create', component: Create,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/admin/update/:id', name: 'update', component: Update,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/admin/delete/:id', name: 'delete', component: Delete,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/log-out', name: 'logOut', component: LogOut,
    meta: {
      requiresAuth: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  const isAuthenticated = authStore.isAuthenticated
  const needsAuth = to.meta.requiresAuth

  if (needsAuth && !isAuthenticated) {
    next({ name: 'logIn' })
  } else if (isAuthenticated && (to.name === 'logIn' || to.name === 'signUp')) {
    next({ name: 'home' })
  } else {
    next()
  }
})

export default router
