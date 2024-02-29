<template>
  <div class="flex items-center">
    <img src="/images/Hagar.jpg" alt="Profile picture" class="picture">
    <NuxtLink to="/" class="link"> Luis C. Berrocal</NuxtLink>
  </div>
</template>


<style scoped>

.link {
  @apply hidden md:block text-2xl font-semibold ml-2;
  /* Prevents the image container from shrinking */
}

.picture {
  @apply rounded-full border-2 border-gray-200 dark:border-gray-700 w-8 h-8 md:w-16 md:h-16;
}

</style>

