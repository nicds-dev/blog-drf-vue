<template>
  <div class="container">
    <h1 class="text-center fw-bold my-4">Latest Posts</h1>
    <Post v-if="!loading" :posts="posts" />
    <PostLoading v-else />
  </div>
</template>

<script setup>
  import axios from 'axios'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import { ref, onMounted } from 'vue'

  const apiUrl = ref('http://localhost:8000/api/')
  const posts = ref([])
  const loading = ref(true)

  const fetchData = async (apiUrl) => {
    try {
      const response = await axios.get(apiUrl)
      posts.value = response.data
    } catch (error) {
      console.error(error)
    } finally {
      loading.value = false
    }
  }

  onMounted(() => {
    fetchData(apiUrl.value);
  })

</script>
