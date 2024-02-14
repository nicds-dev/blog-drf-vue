<template>
  <section class="container min-vh-100-wfooter">
    <h1 class="text-center fw-bold py-5">Latest Posts</h1>
    <Post v-if="!loading" :posts="posts" />
    <PostLoading v-else />
  </section>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import axiosInstance from '../axios.js';

  const posts = ref([])
  const loading = ref(true)

  onMounted(() => {
    axiosInstance.get('')
      .then((res) => {
        posts.value = res.data
        loading.value = false
        console.log("Posts: ", res.data)
      })
      .catch((error) => {
        console.error("Error during fetching posts:", error)
      })
  })

</script>
