<script lang="ts" setup>
</script>

<template>
<BlogPosts v-slot="{posts}">
  <div v-for="post in posts" :key="post.id">
      <NuxtLink :to="posts._path">{{ post.title}}</NuxtLink>
  </div>
</BlogPosts>
</template>

<style scoped>

</style>
