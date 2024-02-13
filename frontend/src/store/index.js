import { createStore } from 'vuex'

export default createStore({
  state: {
    access_token: null,
    refresh_token: null,
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('access_token')) {
        state.access_token = localStorage.getItem('access_token')
        state.refresh_token = localStorage.getItem('refresh_token')
      } else {
        state.access_token = null
      }
    },
    setaccess_tokenToken(state, access_token) {
      state.access_token = access_token
    },
  },
  actions: {
  },
  modules: {
  }
})
