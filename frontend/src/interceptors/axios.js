import axios from 'axios'
import { jwtDecode } from 'jwt-decode'
import dayjs from 'dayjs'

const baseUrl = 'http://127.0.0.1:8000/api/'

const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('authTokens')
            ? `Bearer ${JSON.parse(localStorage.getItem('authTokens')).access}`
            : null,
        'Content-Type': 'application/json',
        accept: 'application/json',
    },
})

let isRefreshing = false

axiosInstance.interceptors.request.use(async config => {
    const authTokens = JSON.parse(localStorage.getItem('authTokens'))

    if (authTokens) {
        const user = jwtDecode(authTokens.access)
        const isAboutExpired = dayjs.unix(user.exp).diff(dayjs(), 'seconds') < 10 // 10 seconds before expiration

        if (isAboutExpired && !isRefreshing) {
            isRefreshing = true
            try {
                const response = await axiosInstance.post('token/refresh/', {
                    refresh: authTokens.refresh
                })
                localStorage.setItem('authTokens', JSON.stringify(response.data))
                config.headers['Authorization'] = `Bearer ${response.data.access}`
            } catch (error) {
                console.log('Error during token refresh', error)
            } finally {
                isRefreshing = false
            }
        } else {
            config.headers['Authorization'] = `Bearer ${authTokens.access}`
        }
    } else {
        // If there is no authTokens in localStorage, then do not add any header
    }
    return config
})

export default axiosInstance