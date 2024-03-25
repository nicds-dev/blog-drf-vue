<template>
  <section class="container vh-70">
    <h1 class="text-center fw-bold mt-5">Latest Posts</h1>
    <Post v-if="!loading" />
    <PostLoading v-else />
  </section>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { usePostsStore } from '@/stores/posts'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import axiosInstance from '@/interceptors/axios'

  const postsStore = usePostsStore()
  const loading = ref(true)

  onMounted(() => {
    axiosInstance.get('')
      .then((res) => {
        postsStore.posts = res.data
        loading.value = false
      })
      .catch((error) => {
        console.error("Error during fetching posts:", error)
      })
  })

</script>