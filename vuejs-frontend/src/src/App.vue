<script>
export default {
  data() {
    return {
      storedResources: [
        {
          id: 'official-guide',
          title: 'Vue.js  Official Guide',
          date: '2021-07-17',
          description: 'The Official Guide to Vue.js',
          link: 'https://vuejs.org',
        },
        {
          id: 'google',
          title: 'Google',
          date: '2021-07-17',
          description: 'Google Search Engine',
          link: 'https://www.google.com',
        },
        {
          id: 'yahoo',
          title: 'Yahoo',
          date: '2021-07-17',
          description: 'Yahoo Search Engine',
          link: 'https://www.yahoo.com',
        },
      ],
    };
  },
  methods: {}
}
</script>

<template>
  <ul>
    <li v-for="resource in storedResources" :key="resource.id">
      <h2>{{ resource.title }}</h2>
      <p>{{ resource.date }}</p>
      <p>{{ resource.description }}</p>
      <a :href="resource.link" target="_blank">Link</a>
    </li>
  </ul>
</template>

<style scoped>

</style>
