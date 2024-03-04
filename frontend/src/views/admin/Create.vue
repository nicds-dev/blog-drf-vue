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
                @change="handleChange"
                v-model="initFormData.title"
                @input="updateSlug"
                type="text"
                class="form-control"
                id="title"
                required
              />
            </div>
            <div class="form-group mt-3">
              <label for="image" class="fw-medium">Post Image *</label>
              <input
                @change="handleChange"
                class="form-control"
                type="file"
                id="image"
                required
              />
            </div>
            <div class="form-group mt-3">
              <label for="excerpt">Post Excerpt *</label>
              <textarea
                @change="handleChange"
                v-model="initFormData.excerpt"
                class="form-control"
                id="excerpt"
                rows="4"
                required
              ></textarea>
            </div>
            <div class="form-group mt-3">
              <label for="slug">Slug *</label>
              <input
                @change="handleChange"
                v-model="initFormData.slug"
                type="text"
                class="form-control"
                id="slug"
                required
              />
            </div>
            <div class="form-group mt-3">
              <label for="content">Content *</label>
              <textarea
                @change="handleChange"
                v-model="initFormData.content"
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
  
  const initFormData = ref({
    title: '',
    slug: '',
    excerpt: '',
    content: '',
  })
  const postImage = ref(null)

  const updateSlug = () => {
    initFormData.value.slug = initFormData.value.title
      .toLowerCase()
      .normalize("NFD")
      .replace(/&+/g, 'and')
      .replace(/[^a-z0-9\s]+/g, '')
      .replace(/\s+/g, '-')
      .replace(/^-+|-+$/g, '')
  }

  const handleChange = (e) => {
    if (e.target.id === 'image') {
      postImage.value = e.target.files[0]
    } else {
      initFormData.value[e.target.id] = e.target.value.trim()
    }
  }

  const submitPost = () => {
    const formData = new FormData()
    formData.append('title', initFormData.value.title)
    formData.append('image', postImage.value)
    formData.append('slug', initFormData.value.slug)
    formData.append('excerpt', initFormData.value.excerpt)
    formData.append('content', initFormData.value.content)
    axiosInstance.post('admin/create', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
      .then((res) => {
        console.log('Post created:', res)
        router.push('/admin/')
      })
      .catch((error) => {
        console.error("Error during post creation:", error)
        if (error.response) {
          console.error("Error response:", error.response.data)
        }
      })
  }
</script>