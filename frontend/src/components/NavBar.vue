<template>
  <nav
    data-bs-theme="dark" 
    id="navbar" 
    class="navbar navbar-expand-lg bg-dark border-bottom p-2"
  >
    <div class="container" style="max-width: 1200px">
      <!-- Name/Logo -->
      <router-link to="/" class="navbar-brand nb-principal fw-bold fs-4 ps-3">Blog.<span class="text-primary">Dev</span></router-link>
      <!-- Toggle Button -->
      <button 
        class="navbar-toggler shadow-none border-0"
        @click="toggleOffcanvas"
        type="button" 
        data-bs-toggle="offcanvas" 
        data-bs-target="#offcanvasNavbar" 
        aria-controls="offcanvasNavbar" 
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <!-- SideBar -->
      <div 
        class="sidebar offcanvas offcanvas-start px-3" 
        tabindex="-1" 
        id="offcanvasNavbar" 
        aria-labelledby="offcanvasNavbarLabel"
      >
        <div class="container offcanvas-header">
          <h5 class="offcanvas-title fs-4 fw-bold" id="offcanvasNavbarLabel">
            Blog.
            <span class="text-primary">Dev</span>
          </h5>
          <button 
            type="button" 
            class="btn-close shadow-none" 
            data-bs-dismiss="offcanvas" aria-label="Close"
          ></button>
        </div>
        <div class="d-flex justify-content-between align-items-center my-3 order-2">
          <div class="text-end">
            <template v-if="!authStore.user">
              <router-link to="/log-in" class="btn btn-outline-light me-2">Login</router-link>
              <router-link to="/sign-up" class="btn btn-primary">Sign Up</router-link>
            </template>
            <template v-else>
              <router-link to="/admin" class="btn btn-outline-light me-2">Admin</router-link>
              <router-link to="/log-out" class="btn btn-primary ms-2">Logout</router-link>
            </template>
          </div>
          <router-link to="/" class="navbar-brand nb-secondary fw-bold fs-1 m-0">Blog.<span class="text-primary">Dev</span></router-link>
          <form class="d-flex">
            <input
              v-model="searchText" type="text" class="form-control me-2" placeholder="Search..." aria-label="Search"
            />
            <button @click.prevent="goSearch" class="btn btn-outline-light">
              <i class="bi bi-search"></i>
            </button>
          </form>
        </div>
        <CategoriesNavBar v-if="router.currentRoute.value.name === 'home'" />
      </div>
    </div>
  </nav>
</template>

<script setup>
  import CategoriesNavBar from '@/components/CategoriesNavBar.vue'
  import { useRouter } from 'vue-router'
  import { useAuthStore } from '@/stores/auth'
  import { ref } from 'vue'

  const router = useRouter()
  const authStore = useAuthStore()
  const searchText = ref('')

  const goSearch = () => {
    if(searchText.value.trim() !== '') {
      router.push({ 
        path: '/search/',
        name: 'search',
        params: { query: searchText.value }
      })
      searchText.value = '';
    }
  }
</script>
  
<style scoped>
  .form-control {
    width: 107px;
  }
  @media (min-width: 992px) {
    .nb-principal {
      display: none;
    }
  }
  @media (max-width: 992px) {
    .nb-secondary {
      display: none;
    }
  }
</style>
  