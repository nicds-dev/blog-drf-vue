<template>
    <div v-if="postsStore.posts.length === 0" class="text-center my-5" role="alert">
        <h1 class="fs-5 alert alert-warning m-3">No posts yet</h1>
    </div>
    <div v-else class="row row-cols-1 row-cols-md-3 g-4 my-5 mx-auto">
        <div v-for="post in postsStore.posts" :key="post.id" class="col">
            <div class="card h-100">
                <a :href="`/post/${post.slug}`" class="ratio ratio-16x9">
                    <img :src="post.image" alt="" class="card-img-top object-fit-cover">
                </a>
                <div class="card-body pb-0">
                    <h5 class="card-title multi-line">{{ post.title }}</h5>
                </div>
                <div v-if="router.currentRoute.value.name !== 'userProfile'" class="card-footer bg-white border-0">
                    <h6 class="text-primary">{{ post.category_name }}</h6>
                    <span class="text-secondary mt-auto">{{ formatDate(post.created_at) }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { usePostsStore } from '@/stores/posts'
    import { useRouter } from 'vue-router'

    const router = useRouter()
    const postsStore = usePostsStore()

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
    .multi-line {
        display: -webkit-box;
        -webkit-line-clamp: 2; /* number of lines to show */
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
</style>