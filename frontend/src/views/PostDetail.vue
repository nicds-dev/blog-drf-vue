<template>
    <section class="container vh-70">
        <div class="container text-center">
            <h1 class="fw-semibold mt-5 mb-2">{{ post.title }}</h1>
            <ul class="header-detail">
                <li class="text-secondary">{{ formatDate(post.published) }}</li>
                <li class="text-secondary">In <span class="text-dark">{{ post.category_name }}</span></li>
            </ul>
        </div>
        <div class="ratio ratio-21x9 my-5">
            <img :src="post.image" alt="" class="card-img-top object-fit-cover">
        </div>
        <p class="fs-6 px-md-5 mb-5">{{ post.content }}</p>
        <div class="container px-md-5 py-5 border-top">
            <h2 class="fs-4 text-secondary">Post by: <span class="text-dark fw-medium">{{ post.author_name }}</span></h2>
            <p class="my-3 px-md-5 fst-italic text-secondary">"{{ post.author_about }}"</p>
        </div>
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

    const formatDate = (dateString) => {
        const date = new Date(dateString)
        const formattedDate = date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
        })
        return formattedDate
    }
</script>

<style scoped>
    .header-detail {
        padding-left: 0 !important;
    }
    .header-detail li {
        display: inline;
        padding-left: 0;
        margin: 0 1rem;
    }
    p {
        line-height: 1.8;
    }
</style>