<template>
  <section class="container vh-70">
    <h1 class="fs-2 text-center fw-bold mt-5">Search Results for "{{ query }}"</h1>
    <Post v-if="!loading" />
    <PostLoading v-else />
  </section>
</template>

<script setup>
  import { ref, watch, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { usePostsStore } from '@/stores/posts'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import axiosInstance from '@/interceptors/axios'

  const route = useRoute()
  const postsStore = usePostsStore()
  const loading = ref(true)
  const query = ref('')

  onMounted(() => {
    updateQueryFromRoute()
    fetchData()
  })

  watch(() => route.params.query, (newSearch) => {
    query.value = newSearch || ''
    fetchData()
  })

  const updateQueryFromRoute = () => {
    query.value = route.params.query || ''
  }

  const fetchData = () => {
    axiosInstance.get(`?slug__icontains=${query.value}`)
      .then((res) => {
        postsStore.posts = res.data
        loading.value = false
      })
      .catch((error) => {
        console.error('Error during fetching posts:', error)
      })
  }
</script>