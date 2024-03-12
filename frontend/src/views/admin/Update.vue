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
                @change="handleImageChange"
                class="form-control"
                type="file"
                id="image"
              />
            </div>
            <div class="form-group mt-3">
              <label for="excerpt">Post Excerpt *</label>
              <textarea
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
                v-model="initFormData.content"
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
  import axiosInstance from '@/interceptors/axios'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const id = router.currentRoute.value.params.id
  
  const initFormData = ref({
    id: '',
    title: '',
    slug: '',
    excerpt: '',
    content: '',
  })
  const postImage = ref(null)

  onBeforeMount(() => {
    axiosInstance.get(`admin/update/detail/${id}`)
      .then((res) => {
        initFormData.value.id = res.data.id
        initFormData.value.title = res.data.title
        initFormData.value.slug = res.data.slug
        initFormData.value.excerpt = res.data.excerpt
        initFormData.value.content = res.data.content
      })
      .catch((error) => {
        console.error("Error during fetching post:", error)
        if (error.response) {
          console.error("Error response:", error.response.data)
        }
      })
  })
  
  const updateSlug = () => {
    initFormData.value.slug = initFormData.value.title
      .toLowerCase()
      .normalize("NFD")
      .replace(/&+/g, 'and')
      .replace(/[^a-z0-9\s]+/g, '')
      .replace(/\s+/g, '-')
      .replace(/^-+|-+$/g, '')
  }

  const handleImageChange = (e) => {
    postImage.value = e.target.files[0]
  }

  const updatePost = () => {
    const formData = new FormData()
    formData.append('title', initFormData.value.title)
    formData.append('slug', initFormData.value.slug)
    formData.append('excerpt', initFormData.value.excerpt)
    formData.append('content', initFormData.value.content)
    if (postImage.value) {
      formData.append('image', postImage.value)
    }

    axiosInstance.put(`admin/update/${id}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
      .then((res) => {
        console.log('Post updated:', res)
        router.push('/admin/')
      })
      .catch((error) => {
        console.error("Error during post update:", error)
        if (error.response) {
          console.error("Error response:", error.response.data)
        }
      })
  }
</script>