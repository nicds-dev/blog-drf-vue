<template>
  <section class="container vh-70">
    <h1 class="text-center fw-bold mt-5">Search Results for "{{ query }}"</h1>
    <Post v-if="!loading" :posts="posts" />
    <PostLoading v-else />
  </section>
</template>

<script setup>
  import { ref, watch, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import axiosInstance from '@/interceptors/axios'

  const route = useRoute()
  const loading = ref(true)
  const posts = ref([])
  const query = ref('')

  onMounted(() => {
    updateQueryFromRoute()
    fetchData()
  })

  watch(() => route.query.search, (newSearch) => {
    query.value = newSearch || ''
    fetchData()
  })

  const updateQueryFromRoute = () => {
    query.value = route.query.search || ''
  }

  const fetchData = () => {
    console.log('Fetching data for query:', query.value)
    axiosInstance.get(`search/?search=${query.value}`)
      .then((res) => {
        posts.value = res.data
        loading.value = false
        console.log('Posts: ', res.data)
      })
      .catch((error) => {
        console.error('Error during fetching posts:', error)
      })
  }
</script>