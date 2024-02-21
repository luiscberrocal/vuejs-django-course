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
