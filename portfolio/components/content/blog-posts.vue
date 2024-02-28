<script setup>

const {data: posts} = await useAsyncData(
    'post-list',
    () => queryContent('/blog')
        .only(['_path', 'title', 'description'])
        .where({_path: {$ne: '/blog'}})
        .find()
);
console.log(posts);
</script>

<template>
  <div>
    <section class="not-prose">
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
