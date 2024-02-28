<script lang="ts" setup>

const posts = await queryContent('/blog').only(['_path', 'title', 'description']).find();
console.log(posts);
</script>

<template>
  <div>
    <section>
      <ul>
        <li v-for="post in posts" :key="post._path">
          <NuxtLink :to="post._path">{{ post.title }}</NuxtLink>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>

</style>
