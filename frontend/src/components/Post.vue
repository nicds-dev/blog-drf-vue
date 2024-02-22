<template>
    <div class="container">
        <div v-if="posts.length === 0" class="alert alert-warning fs-5 text-center my-5" role="alert">
            No posts yet
        </div>
        <div v-else class="row row-cols-1 row-cols-md-4 g-4 my-5">
            <div v-for="post in posts" :key="post.id" class="col">
                <div class="card h-100">
                    <a :href="`/post/${post.slug}`">
                        <img src="https://source.unsplash.com/300x200" alt="" class="card-img-top">
                    </a>
                    <div class="card-body">
                        <h5 class="card-title">{{ post.title }}</h5>
                        <p class="card-text text-truncate">{{ post.content }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    const props = defineProps(['posts'])

</script>