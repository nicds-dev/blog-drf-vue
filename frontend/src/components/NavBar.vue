<template>
    <nav 
      id="navbar" 
      class="navbar navbar-expand-lg navbar-light border-bottom "
    >
      <div class="container-fluid py-1">
        <!-- Name/Logo -->
        <router-link to="/" class="navbar-brand fw-bold fs-4 ps-3">Blog.<span class="text-primary">Dev</span></router-link>
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
          class="sidebar offcanvas offcanvas-start py-1 px-3" 
          tabindex="-1" 
          id="offcanvasNavbar" 
          aria-labelledby="offcanvasNavbarLabel"
        >
          <div 
            class="container-fluid offcanvas-header">
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
          <form class="container-fluid d-flex justify-content-end">
            <router-link to="/log-in" class="btn btn-outline-primary me-2">Login</router-link>
            <router-link to="/sign-up" class="btn btn-outline-primary">Sign Up</router-link>
            <router-link to="/log-out" class="btn btn-outline-primary ms-2">Logout</router-link>
          </form>
        </div>
      </div>
    </nav>
</template>
  
<script>

</script>
  
<style scoped>
    .container-fluid {
        width: 95%;
    }
</style>
  