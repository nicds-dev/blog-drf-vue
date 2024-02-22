<template>
  <div class="container">
    <div v-if="posts.length === 0" class="alert alert-warning fs-5 text-center my-5" role="alert">
      No posts yet
    </div>
    <div class="card p-4 my-5">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Category</th>
            <th scope="col">Title</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="post in posts" :key="post.id">
            <td scope="row">{{ post.id }}</td>
            <td>{{ post.category }}</td>
            <td>
              <router-link :to="`/post/${post.slug}`" class="custom-link">
                {{ post.title }}
              </router-link>
            </td>
            <td class="d-flex">
              <div class="col">
                <router-link :to="`/admin/update/${post.id}`" class="">
                  <i class="bi bi-pencil-square fs-5"></i>
                </router-link>
              </div>
              <div class="col">
                <router-link :to="`/admin/delete/${post.id}`" class="">
                  <i class="bi bi-trash-fill fs-5"></i>
                </router-link>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="ms-auto mt-3">
        <router-link to="/admin/create" class="btn btn-primary">New Post</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps(['posts'])
</script>