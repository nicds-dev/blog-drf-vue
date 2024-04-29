<template>
  <div class="container py-3 border-top order-lg-2 order-1" style="max-width: 1200px">
    <div class="offcanvas-body navbar-nav justify-content-center gap-4">
      <button
        class="nav-link fs-6"
        v-for="category in categories"
        :key="category.id"
        @click="filterByCategory(category.id)"
      >
        {{ category.name }}
      </button>
      <button
        class="nav-link fs-6"
        @click="filterByCategory('')"
      >
        All
      </button>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import axiosInstance from '@/interceptors/axios'
  import { usePostsStore } from '@/stores/posts'

  const postsStore = usePostsStore()
  const categories = ref([])

  onMounted(() => {
    axiosInstance.get('categories/')
      .then((res) => {
        categories.value = res.data
      })
  })

  const filterByCategory = (categoryId) => {
    axiosInstance.get(`?category=${categoryId}`)
      .then((res) => {
        postsStore.posts = res.data
      })
      .catch((error) => {
        console.error('Error during fetching posts:', error)
      })
  }
</script>