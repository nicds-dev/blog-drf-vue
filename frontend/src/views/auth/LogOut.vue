<template>
</template>

<script setup>
    import { useRouter } from 'vue-router'
    import axiosInstance from '@/interceptors/axios'
    import { onMounted } from 'vue'

    const router = useRouter()

    onMounted(() => {
        axiosInstance
            .post('user/logout/blacklist/', {
                refresh_token: localStorage.getItem('refresh_token')
            })
            .catch((error) => {
                console.error("Error during logout:", error)
            })

        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        axiosInstance.defaults.headers['Authorization'] = null

        router.push('/log-in')
    })
</script>