<script>
import LearningResource from "./components/learning-resources/LearningResource.vue";

export default {
  components: {
    LearningResource
  },
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
    <learning-resource v-for="resource in storedResources"
                       :key="resource.id"
                       :title="resource.title"
                       :description="resource.description"
                       :link="resource.link"
    ></learning-resource>
  </ul>
</template>

<style scoped>

</style>
