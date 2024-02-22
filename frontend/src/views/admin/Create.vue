<template>
  <section class="container vh-70">
    <h1 class="fs-2 text-center fw-bold mt-5">Create New Post</h1>
    <div class="row justify-content-center my-5 px-4">
      <div class="mw-700 card">
        <div class="card-body">
          <form @submit.prevent="submitPost">
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
              Create Post
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
  import { ref } from 'vue'
  import axiosInstance from '@/axios'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  
  const formData = ref({
    title: '',
    slug: '',
    excerpt: '',
    content: '',
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

  const submitPost = () => {
    axiosInstance
      .post('admin/create', {
        title: formData.value.title.trim(),
        slug: formData.value.slug.trim(),
        author: 1,
        excerpt: formData.value.excerpt.trim(),
        content: formData.value.content.trim(),
      })
      .then((res) => {
        console.log('Post created:', res)
        router.push('/admin/')
      })
      .catch((error) => {
        console.error("Error during post creation:", error)
      })
  }
</script>