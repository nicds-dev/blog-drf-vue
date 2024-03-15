import { defineStore } from 'pinia'
import axiosInstance from '@/interceptors/axios'

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            isAuthenticated: !!localStorage.getItem('access_token'),
            errorMessage: null,
        }
    },
    getters: {
    },
    actions: {
        async login(email, password) {
            try {
                const response = await axiosInstance.post('/token/', {
                    email,
                    password
                })
                localStorage.setItem('access_token', response.data.access)
                localStorage.setItem('refresh_token', response.data.refresh)
                axiosInstance.defaults.headers['Authorization'] =
                    'JWT ' + response.data.access
                    
                this.isAuthenticated = true
                this.errorMessage = null
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    this.errorMessage = 'Invalid email or password. Please try again.'
                } else {
                    this.errorMessage = 'An error occurred while logging in. Please try again.'
                }
            }
        },
        async logout() {
            try {
                await axiosInstance.post('user/logout/blacklist/', {
                    refresh_token: localStorage.getItem('refresh_token')
                })
            } catch (error) {
                console.error('Error during logout', error)
            } finally {
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
                axiosInstance.defaults.headers['Authorization'] = null
                
                this.isAuthenticated = false
                this.errorMessage = null
            }

        }
    }
})