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
      resources: this.storedResources,
      addResource: this.addResource
    }
  },
  methods: {
    addResource(title, description, link) {
      const res = {
        id: new Date().toISOString(),
        title: title,
        // date: new Date().toISOString(),
        description: description,
        link: link
      };
      console.log('Add Resource', res)
      this.storedResources.unshift(res);
      this.setSelectTab('stored-resources');
    },
    setSelectTab(tab) {
      this.selectedTab = tab;
    }
  },
  computed: {
    setButtonMode1() {
      return this.selectedTab === 'stored-resources' ? null : 'flat';
    },
    setButtonMode2() {
      return this.selectedTab === 'add-resource' ? null : 'flat';
    },
  }
}
</script>

<template>
  <base-card>
    <base-button @click="setSelectTab('stored-resources')"
                 :mode="setButtonMode1"
    >Stored Resources
    </base-button>
    <base-button @click="setSelectTab('add-resource')"
                 :mode="setButtonMode2"
    >Add Resource
    </base-button>
  </base-card>
  <keep-alive>
    <component :is="selectedTab"></component>
  </keep-alive>
</template>

<style scoped>

</style>
