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
                        <div v-if="errorMessage" class="alert alert-danger mt-3" role="alert">
                            {{ errorMessage }}
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
    import axiosInstance from '@/interceptors/axios'

    const formData = ref({
        email: '',
        password: '',
    })

    const router = useRouter()
    const errorMessage = ref(null)

    const loginChange = (field) => (e) => {
        formData.value = {
            ...formData.value,
            [field]: e.target.value.trim(),
        }
    }

    const login = async () => {
        if (!formData.value.email || !formData.value.password) {
            errorMessage.value = 'Please fill in all fields.'
            return
        }

        try {
            const response = await axiosInstance.post('token/', {
                email: formData.value.email,
                password: formData.value.password,
            })
            localStorage.setItem('access_token', response.data.access)
            localStorage.setItem('refresh_token', response.data.refresh)
            axiosInstance.defaults.headers['Authorization'] =
                'JWT ' + localStorage.getItem('access_token')

            router.push('/')
        } catch (error) {
            if (error.response && error.response.status === 401) {
                errorMessage.value = 'Invalid email or password. Please try again.'
            } else {
                errorMessage.value = 'An error occurred while logging in. Please try again.'
            }
        }
    }
</script>