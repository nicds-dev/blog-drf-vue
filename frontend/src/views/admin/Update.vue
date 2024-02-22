<template>
  <section class="container vh-70">
    <h1 class="fs-2 text-center fw-bold mt-5">Update Post</h1>
    <div class="row justify-content-center my-5 px-4">
      <div class="mw-700 card">
        <div class="card-body">
          <form @submit.prevent="updatePost">
            <div class="form-group mt-3">
              <label for="title" class="fw-medium">Post Title *</label>
              <input
                v-model="formData.title"
                @input="updateSlug"
                type="text"
                class="form-control"
                id="title"
              />
            </div>
            <div class="form-group mt-3">
              <label for="excerpt">Post Excerpt *</label>
              <textarea
                v-model="formData.excerpt"
                class="form-control"
                id="excerpt"
                rows="4"
              ></textarea>
            </div>
            <div class="form-group mt-3">
              <label for="slug">Slug *</label>
              <input
                v-model="formData.slug"
                type="text"
                class="form-control"
                id="slug"
              />
            </div>
            <div class="form-group mt-3">
              <label for="content">Content *</label>
              <textarea
                v-model="formData.content"
                class="form-control"
                id="content"
                rows="4"
              ></textarea>
            </div>
            <button type="submit" class="btn btn-primary mt-4 w-100">
              Update Post
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
  import { ref, onBeforeMount } from 'vue'
  import axiosInstance from '@/axios'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const id = router.currentRoute.value.params.id
  
  const formData = ref({
    id: '',
    title: '',
    slug: '',
    excerpt: '',
    content: '',
  })

  onBeforeMount(() => {
    axiosInstance.get(`admin/update/detail/${id}`)
      .then((res) => {
        formData.value.id = res.data.id
        formData.value.title = res.data.title
        formData.value.slug = res.data.slug
        formData.value.excerpt = res.data.excerpt
        formData.value.content = res.data.content
      })
      .catch((error) => {
        console.error("Error during fetching post:", error)
      })
  })
  
  const updateSlug = () => {
    formData.value.slug = formData.value.title
      .toLowerCase()
      .normalize("NFD")
      .replace(/&+/g, 'and')
      .replace(/[^a-z0-9\s]+/g, '')
      .replace(/\s+/g, '-')
      .replace(/^-+|-+$/g, '')
  }

  const updatePost = () => {
    axiosInstance
      .put(`admin/update/${id}`, {
        title: formData.value.title.trim(),
        slug: formData.value.slug.trim(),
        author: 1,
        excerpt: formData.value.excerpt.trim(),
        content: formData.value.content.trim(),
      })
      .then((res) => {
        console.log('Post updated:', res)
        router.push('/admin/')
      })
      .catch((error) => {
        console.error("Error during post update:", error)
      })
  }
</script>