<template>
    <section class="container min-vh-100-wfooter">
        <h1 class="text-center fw-semibold py-5">{{ post.title }}</h1>
        <p class="text-start">{{ post.excerpt }}</p>
        <p class="text-end fw-medium">Published at: <span class="fw-normal">{{ post.published }}</span></p>
    </section>
</template>

<script setup>
    import { useRoute } from 'vue-router'
    import { ref, onMounted } from 'vue'
    import axiosInstance from '../axios.js'

    const post = ref({})

    onMounted(() => {
        const { slug } = useRoute().params
        axiosInstance.get(slug)
            .then((res) => {
                post.value = res.data
                console.log("Post: ", res.data)
            })
            .catch((error) => {
                console.error("Error during fetching post:", error)
            })
    })
</script>