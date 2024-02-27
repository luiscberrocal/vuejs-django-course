This application is using Django 4.2.x and Django Rest Framework 3.12.x. For the front end, it is using
Nuxt 3.0.x and Tailwind CSS 3.0.x. We prefer using composable API for the front end.
To keep track of stores we are using Pinia.

With the following code template. Rewrite the Nuxt page to do the following.
1 - Call the aut-token endpoint to obtain a token. If the user is not authenticated then display an error message.
2 - Save the token to the local storage using Pinia
3 - Create a composable to handle the login form


<script lang="ts" setup>
const url = 'http://127.0.0.1:8000/auth-token/'
</script>

<template>
  <div class="container place-content-center">
    <div class="grid grid-cols-1">
      <h2>Login</h2>
      <form>
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" class="form-control">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" class="form-control">
        </div>
        <button type="submit" class="btn">Login</button>
      </form>
    </div>
  </div>
</template>

<style scoped>

</style>
