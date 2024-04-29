<template>
    <section class="container vh-70">
        <div class="container text-center">
            <h1 class="fw-semibold mt-5 mb-2">{{ post.title }}</h1>
            <ul class="header-detail">
                <li class="text-secondary">{{ formatDate(post.created_at) }}</li>
                <li class="text-secondary">In <span class="text-dark">{{ post.category_name }}</span></li>
            </ul>
        </div>
        <div class="ratio ratio-21x9 my-5">
            <img :src="post.image" alt="" class="card-img-top object-fit-cover">
        </div>
        <p class="fs-6 px-md-5 mb-5">{{ post.content }}</p>
        <div class="container px-md-5 py-5 border-top">
            <h2 class="fs-4 text-secondary">
                Post by: <a :href="`/${post.author_name}`" class="text-dark fw-medium">{{ post.author_name }}</a>
            </h2>
            <p class="my-3 px-md-5 fst-italic text-secondary">"{{ post.author_bio }}"</p>
        </div>
        <div class="px-md-5 py-5 text-center border-top">
            <button @click="showComments" class="btn btn-primary fs-5">
                Charge comments
            </button>
        </div>
        <CommentList v-if="showingComments" :slug="post.slug" />
    </section>
</template>

<script setup>
    import { useRoute, useRouter } from 'vue-router'
    import { ref, onMounted } from 'vue'
    import { useAuthStore } from '@/stores/auth';
    import axiosInstance from '@/interceptors/axios'
    import CommentList from '@/components/CommentList.vue'

    const router = useRouter()
    const { slug } = useRoute().params
    const authStore = useAuthStore()
    const post = ref({})
    const showingComments = ref(false)

    onMounted(() => {
        axiosInstance.get(`post/${slug}`)
            .then((res) => {
                post.value = res.data
                console.log("Post: ", res.data)
            })
            .catch((error) => {
                console.error("Error during fetching post:", error)
            })
    })

    const showComments = () => {
        if (!authStore.user) {
            router.push('/log-in')
        } else {
            showingComments.value = true
        }
    }

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