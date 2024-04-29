<template>
  <section class="container vh-70">
    <header class="row my-5">
      <div class="col d-flex align-items-center justify-content-center">
        <img v-if="userData.image" :src="userData.image" alt="profile-image" class="rounded-circle img-fluid">
        <img
          v-else src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
          alt="profile-image" class="rounded-circle img-fluid"
          width="150px"
        >
      </div>
      <div class="col-12 col-md-8 d-flex flex-column justify-content-center">
        <h1 class="fs-4 fw-bold my-0">{{ userData.user_name }}</h1>
        <div class="d-flex flex-row my-3">
          <span class="text-gray"><strong class="text-dark fw-bold">{{ userData.num_posts }}</strong> posts</span>
          <a @click="showFollows('followers')" class="text-decoration-none text-gray ms-3" href="#followers">
            <span class="text-dark fw-bold">{{ userData.num_followers }}</span> followers
          </a>
          <a @click="showFollows('following')" class="text-decoration-none text-gray ms-3" href="#following">
            <span class="text-dark fw-bold">{{ userData.num_following }}</span> following
          </a>
        </div>
        <div>
          <h2 class="fs-6 fw-semibold my-2">{{ userData.first_name }} {{ userData.last_name }}</h2>
          <p class="mb-0">{{ userData.about }}</p>
        </div>
      </div>
    </header>
    <div class="row">
      <div class="text-center pt-4 border-top" style="margin-bottom: -3rem;">
        <h2 class="fs-5 fw-semibold">POSTS</h2>
      </div>
      <Post v-if="!loading" />
      <PostLoading v-else />
    </div>
  </section>
</template>

<script setup>
  import { useRoute } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { usePostsStore } from '@/stores/posts'
  import Post from '@/components/Post.vue'
  import PostLoading from '@/components/PostLoading.vue'
  import axiosInstance from '@/interceptors/axios'
  
  const { user } = useRoute().params
  const postsStore = usePostsStore()
  const loading = ref(true)

  const userData = ref({})
  // const followers = ref({})
  // const following = ref({})

  onMounted(() => {
    axiosInstance.get(`user/${user}/`)
      .then((res) => {
        userData.value = res.data
      })
      .catch((error) => {
        console.error("Error during fetching user info:", error)
      })

    axiosInstance.get(`?author__user_name=${user}`)
      .then((res) => {
        postsStore.posts = res.data
        loading.value = false
      })
  })

  const showFollows = (follows) => {
    axiosInstance.get(`user/${user}/${follows}/`)
      .then((res) => {
        console.log(res.data)
      })
      .catch((error) => {
        console.error("Error during fetching user follows:", error)
      })
  }
</script>