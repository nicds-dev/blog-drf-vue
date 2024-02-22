<template>
    <section class="container vh-70">
        <h1 class="fs-2 text-center fw-bold mt-5">Sign Up</h1>
        <div class="row justify-content-center my-5 px-4">
            <div class="mw-400 card">
                <div class="card-body">
                    <form @submit.prevent="signUp">
                        <div class="form-group mt-3">
                            <label for="email" class="fw-medium">Email Address</label>
                            <input
                                type="email"
                                class="form-control"
                                v-model="formData.email"
                                @input="signUpChange('email')"
                                required
                            />
                        </div>
                        <div class="form-group mt-3">
                            <label for="username" class="fw-medium">Username</label>
                            <input
                                type="text"
                                class="form-control"
                                v-model="formData.username"
                                @input="signUpChange('username')"
                                required
                            />
                        </div>
                        <div class="form-group mt-3">
                            <label for="password" class="fw-medium">Password</label>
                            <input
                                type="password"
                                class="form-control"
                                v-model="formData.password"
                                @input="signUpChange('password')"
                                required
                            />
                        </div>
                        <button type="submit" class="btn btn-primary mt-4 w-100">
                            <span>Sign Up</span>
                        </button>
                        <div class="mt-3">
                            Already have an account?
                            <router-link to="/log-in" class="text-decoration-none">Sign in</router-link>
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
    import axiosInstance from '@/axios.js'

    const router = useRouter()

    const formData = ref({
        email: '',
        username: '',
        password: '',
    })

    const signUpChange = (field) => (e) => {
        formData.value = {
            ...formData.value,
            [field]: e.target.value.trim(),
        }
    }

    const signUp = () => {
        console.log("Sign up form data:", formData.value)

        axiosInstance
            .post('user/register/', {
                email: formData.value.email,
                user_name: formData.value.username,
                password: formData.value.password,
            })
            .then((res) => {
                console.log('User created:', res)
                router.push('/log-in')
            })
            .catch((error) => {
                console.error("Error during user creation:", error)
            })
    }
</script>
  