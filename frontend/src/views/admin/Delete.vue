<template>
    <section class="container vh-70">
        <h1 class="fs-2 text-center fw-bold mt-5">Delete Post</h1>
        <p class="fs-5 text-center my-5">Are you sure you want to delete this post?</p>
        <div class="d-flex justify-content-center">
          <button class="btn btn-danger me-3" @click="deletePost">Delete</button>
          <router-link to="/admin/" class="btn btn-secondary ms-3">Cancel</router-link>
        </div>
    </section>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axiosInstance from '@/axios'

  const router = useRouter()
  const id = router.currentRoute.value.params.id

  const deletePost = () => {
    axiosInstance
      .delete(`admin/delete/${id}`)
      .then((res) => {
        console.log('Post deleted:', res)
        router.push('/admin/')
      })
      .catch((error) => {
        console.error("Error during post deletion:", error)
      })
  }
</script>