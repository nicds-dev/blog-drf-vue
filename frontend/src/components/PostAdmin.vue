<template>
  <div class="container">
    <div v-if="posts.length === 0" class="alert alert-warning fs-5 text-center my-5" role="alert">
      No posts yet
    </div>
    <div class="card p-4 my-5">
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th scope="col" class="col-1">Id</th>
              <th scope="col" class="col-2">Category</th>
              <th scope="col" class="col-8">Title</th>
              <th scope="col" class="col-1">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in visiblePosts" :key="post.id">
              <td scope="row">{{ post.id }}</td>
              <td class="single-line">{{ post.category_name }}</td>
              <td>
                <router-link :to="`/post/${post.slug}`" class="custom-link title-column">
                  {{ post.title }}
                </router-link>
              </td>
              <td class="d-flex">
                <div class="col">
                  <router-link :to="`/admin/update/${post.id}`" class="">
                    <i class="bi bi-pencil-square fs-5"></i>
                  </router-link>
                </div>
                <div class="col">
                  <router-link :to="`/admin/delete/${post.id}`" class="">
                    <i class="bi bi-trash-fill text-danger fs-5"></i>
                  </router-link>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <div>
          <button @click="previousPage" :disabled="currentPage === 1" class="btn btn-outline-primary">Previous</button>
          <button @click="nextPage" :disabled="currentPage === totalPages" class="btn btn-outline-primary ms-2">Next</button>
        </div>
        <div class="me-2me-1 me-md-2">
          <span>{{ startIndex + 1 }} - {{ endIndex }} of {{ props.posts.length }}</span>
        </div>
      </div>
      <div class="ms-auto mt-3">
        <router-link to="/admin/create" class="btn btn-primary">New Post</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'

  const props = defineProps(['posts'])

  const currentPage = ref(1)
  const pageSize = 4

  const startIndex = computed(() => (currentPage.value - 1) * pageSize)
  const endIndex = computed(() => Math.min(startIndex.value + pageSize, props.posts.length))

  const visiblePosts = computed(() => props.posts.slice(startIndex.value, endIndex.value))

  const previousPage = () => {
    if (currentPage.value > 1) {
      currentPage.value--
    }
  }

  const nextPage = () => {
    if (currentPage.value < totalPages.value) {
      currentPage.value++
    }
  }

  const totalPages = computed(() => Math.ceil(props.posts.length / pageSize))
</script>

<style scoped>
  .single-line {
    white-space: nowrap;
  }
</style>