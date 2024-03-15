<template>
    <section class="container vh-70">
        <h1 class="fs-2 text-center fw-bold mt-5">Sign In</h1>
        <div class="row justify-content-center my-5 px-4">
            <div class="mw-400 card">
                <div class="card-body">
                    <form @submit.prevent="login">
                        <div class="form-group mt-3">
                            <label for="email" class="fw-medium">Email Address</label>
                            <input
                                type="email"
                                class="form-control"
                                v-model.trim="formData.email"
                                @input="loginChange('email')"
                            />
                        </div>
                        <div class="form-group mt-3">
                            <label for="password" class="fw-medium">Password</label>
                            <input
                                type="password"
                                class="form-control"
                                v-model.trim="formData.password"
                                @input="loginChange('password')"
                                required
                            />
                        </div>
                        <button type="submit" class="btn btn-primary mt-4 w-100">Sign In</button>
                        <div class="mt-3">
                            Don't have an account?
                            <router-link to="/sign-up" class="text-decoration-none">Sign up</router-link>
                        </div>
                        <div v-if="authStore.errorMessage" class="alert alert-danger mt-3" role="alert">
                            {{ authStore.errorMessage }}
                        </div>
                    </form> 
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    import { useAuthStore } from '@/stores/auth'

    const formData = ref({
        email: '',
        password: '',
    })

    const router = useRouter()
    const authStore = useAuthStore()

    const loginChange = (field) => (e) => {
        formData.value = {
            ...formData.value,
            [field]: e.target.value.trim(),
        }
    }

    const login = async () => {
        if (!formData.value.email || !formData.value.password) {
            authStore.errorMessage = 'Please fill in all fields.'
            return
        }
        
        try {
            await authStore.login(formData.value.email, formData.value.password)
            
            if (authStore.isAuthenticated) {
                router.push('/')
            }
        } catch (error) {
           authStore.errorMessage = 'An error occurred while sending the request. Please try again.'
        }
    }
</script>