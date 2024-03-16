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
                                :class="{ 'is-invalid': errorField === 'email' }"
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
                                :class="{ 'is-invalid': errorField === 'username' }"
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
                                :class="{ 'is-invalid': errorField === 'password' }"
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

    const router = useRouter()
    const errorField = ref(null)
    const errorMessage = ref(null)

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

    const signUp = async () => {
        if (!formData.value.email || !formData.value.username || !formData.value.password) {
            showError('Please fill in all fields.')
            return
        }

        try {
            const response = await axiosInstance.post('user/register/', {
                email: formData.value.email,
                user_name: formData.value.username,
                password: formData.value.password,
            })
            router.push('/log-in')
        } catch (error) {
            if (error.response) {
                if (error.response.status === 400 && error.response.data) {
                    console.log(error.response.data.email)
                    console.log(error.response.data.user_name)
                    
                    if (error.response.data.email && error.response.data.email.length > 0) {
                        showError('email', 
                            error.response.data.email[0] === 'new user with this email address already exists.'
                            ? 'An account with this email already exists.'
                            : error.response.data.email[0]
                        )
                        
                    } else if (error.response.data.user_name && error.response.data.user_name.length > 0) {
                        showError('username', 'An account with this username already exists.')
                    } else if (error.response.data.password && error.response.data.password.length > 0) {
                       error.response.data.password.forEach((errorMessage) => {
                           showError('password', errorMessage)
                       })
                    } else {
                        showError(null, 'An error occurred while signing up. Please try again.')
                    }
                } else {
                    showError(null, 'An error occurred while signing up. Please try again.')
                }
            } else {
                showError(null, 'An error occurred. Please try again.')
            }
        }
    }

    const showError = (field, message) => {
        errorField.value = field
        
        if (field === 'password' && Array.isArray(message)) {
            errorMessage.value = message
        } else {
            errorMessage.value = message
            
        }
    }
</script>