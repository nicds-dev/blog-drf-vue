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
                type="text"
                class="form-control"
                id="title"
                required
              />
            </div>
            <div class="form-group mt-3">
              <label for="category" class="fw-medium">Post Category *</label>
              <select
                @change="handleChange"
                v-model="initFormData.category"
                class="form-select"
                id="category"
                required
              >
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
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
              <label for="content">Content *</label>
              <textarea
                @change="handleChange"
                v-model="initFormData.content"
                class="form-control"
                id="content"
                rows="4"
              ></textarea>
            </div>
            <button type="submit" class="btn btn-primary mt-4 mb-2 w-100">
              Create Post
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import axiosInstance from '@/interceptors/axios'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const categories = ref([])

  onMounted(() => {
    axiosInstance.get('categories/')
      .then((res) => {
        categories.value = res.data
      })
  })
  
  const initFormData = ref({
    title: '',
    category: '',
    content: '',
  })
  const postImage = ref(null)

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
    formData.append('category', initFormData.value.category)
    formData.append('image', postImage.value)
    formData.append('content', initFormData.value.content)
    axiosInstance.post('admin/create/', formData, {
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