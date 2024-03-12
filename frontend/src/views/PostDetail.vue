<template>
    <section class="container vh-70">
        <h1 class="text-center fw-semibold mt-5">{{ post.title }}</h1>
        <p class="text-start my-5">{{ post.excerpt }}</p>
        <p class="text-end fw-medium">Published at: <span class="fw-normal">{{ post.published }}</span></p>
    </section>
</template>

<script setup>
    import { useRoute } from 'vue-router'
    import { ref, onMounted } from 'vue'
    import axiosInstance from '@/interceptors/axios'

    const post = ref({})

    onMounted(() => {
        const { slug } = useRoute().params
        axiosInstance.get(`post/${slug}`)
            .then((res) => {
                post.value = res.data
                console.log("Post: ", res.data)
            })
            .catch((error) => {
                console.error("Error during fetching post:", error)
            })
    })
</script>