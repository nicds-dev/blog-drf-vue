<template>
</template>

<script setup>
    import { useRouter } from 'vue-router'
    import { useAuthStore } from '@/stores/auth'
    import { onMounted } from 'vue'

    const router = useRouter()
    const authStore = useAuthStore()

    onMounted(() => {
        authStore.logout()
        router.push('/')
    })
</script>