<script>
import StoredResources from "./StoredResources.vue";
import AddResource from "./AddResource.vue";

export default {
  components: {StoredResources, AddResource},
  props: [],
  data() {
    return {
      selectedTab: 'stored-resources',
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
  provide() {
    return {
      resources: this.storedResources
    }
  },
  methods: {
    setSelectTab(tab) {
      this.selectedTab = tab;
    }
  },
  computed: {}
}
</script>

<template>
  <base-card>
    <base-button @click="setSelectTab('stored-resources')">Stored Resources</base-button>
    <base-button @click="setSelectTab('add-resource')">Add Resource</base-button>
  </base-card>
  <component :is="selectedTab"></component>
</template>

<style scoped>

</style>
