import { defineStore } from 'pinia'

export const usePostsStore = defineStore('posts', {
    state: () => {
        return {
            posts: [],
        }
    },
    actions: {
        updatePosts(newPosts) {
            this.posts = newPosts
        }
    }
})