<template>
  <div>
    <h2>Comentarios</h2>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        {{ comment.content }}
      </li>
    </ul>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import axiosInstance from '@/interceptors/axios'

  const props = defineProps({
    slug: String
  })

  const comments = ref([])

  onMounted(() => {
    axiosInstance.get(`post/${props.slug}/comments`)
      .then((res) => {
        comments.value = res.data;
      })
      .catch((error) => {
        console.error("Error during fetching post comments:", error);
      });
  });
</script>
