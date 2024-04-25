import { defineStore } from 'pinia'
import axiosInstance from '@/interceptors/axios'
import { jwtDecode } from 'jwt-decode'
import dayjs from 'dayjs'

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            authTokens: localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null,
            user: localStorage.getItem('authTokens') ? jwtDecode(localStorage.getItem('authTokens')) : null,
            errorMessage: null,
        }
    },
    getters: {},
    actions: {
        async login(email, password) {
            try {
                const response = await axiosInstance.post('user/account/login/', {
                    email,
                    password
                })
                if (response.status === 200) {
                    this.authTokens = response.data
                    this.user = jwtDecode(response.data.access)
                    localStorage.setItem('authTokens', JSON.stringify(response.data))
                }
            } catch (error) {
                if (error.response && error.response.status === 401) {
                    this.errorMessage = 'Invalid email or password. Please try again.'
                } else {
                    this.errorMessage = 'An error occurred while logging in. Please try again.'
                }
            }
        },
        async logout() {
            const isAboutExpired = dayjs.unix(this.user.exp).diff(dayjs(), 'seconds') < 12 // 12 seconds before expiration
            // If the token is not about to expire, then logout
            if (!isAboutExpired) {
                try {
                    await axiosInstance.post('user/account/logout-blacklist/', {
                        refresh: this.authTokens.refresh
                    })
                } catch (error) {
                    console.log('Error during logout', error)
                } finally {
                    this.authTokens = null
                    this.user = null
                    localStorage.removeItem('authTokens')
                }
            } else {
                this.authTokens = null
                this.user = null
                localStorage.removeItem('authTokens')
            }
        },
    }
})