<template>
  <div>
    <h1>Home</h1>
    <p>Bla bla</p>
  </div>
</template>
<script setup lang="ts">
useSeoMeta({
  title: 'Portfolio Page',
  description: 'This is the main page of my portfolio',
  ogTitle: '[og:title]',
  ogDescription: '[og:description]',
  ogImage: '[og:image]',
  ogUrl: '[og:url]',
  twitterTitle: '[twitter:title]',
  twitterDescription: '[twitter:description]',
  twitterImage: '[twitter:image]',
  twitterCard: 'summary'
})

useHead({
  htmlAttrs: {
    lang: 'en'
  },
  link: [
    {
      rel: 'icon',
      type: 'image/png',
      href: '/favicon.png'
    }
  ]
})
</script>
