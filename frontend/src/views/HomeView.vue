<template>
  <section class="container min-vh-100-wfooter">
    <h1 class="text-center fw-bold py-5">Latest Posts</h1>
    <Post v-if="!loading" :posts="posts" />
    <PostLoading v-else />
  </section>
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
      console.error('Error fetching data:', error)
    } finally {
      loading.value = false
    }
  }

  onMounted(() => {
    fetchData(apiUrl.value);
  })

</script>
