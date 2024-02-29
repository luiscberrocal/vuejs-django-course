<template>
  <div class="container">
    <div class="image-container">
      <img src="/images/Hagar.jpg" alt="" class="picture">
    </div>
    <NuxtLink to="/" class="name-link">
      John Wick
    </NuxtLink>
  </div>
</template>

<style scoped>
.container {
  @apply flex items-center md:gap-8; /* This ensures the elements are in a flex row and aligned at the center */
}

.image-container {
  @apply flex-shrink-0; /* Prevents the image container from shrinking */
}

.picture {
  @apply rounded-full border-2 border-gray-200 dark:border-gray-700; /* Adjusts the size and border of the picture */
  width: 5rem; /* Adjusts the width of the picture */
  height: 5rem; /* Adjusts the height of the picture */
}

.name-link {
  @apply text-xl font-semibold p-2 hover:bg-gray-200 dark:hover:bg-gray-800; /* Styles the link */
}
</style>

