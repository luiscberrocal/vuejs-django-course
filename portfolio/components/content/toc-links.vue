<script lang="ts" setup>
const route = useRoute();

defineProps({
  links: {
    type: Array,
    required: true
  },
  level: {
    type: Number,
    default: 0
  }
});
</script>

<template>
  <ul>
    <li v-for="link in links" :key="link.id">
      <NuxtLink :to="{path: route.path, hash: `#${link.id}`}" class="hover:text-blue-500 dark:hover:text-blue-300">
        {{ link.text }}
      </NuxtLink>
    </li>
  </ul>
</template>

<style scoped>

</style>
