<script>
import StoredResources from "./StoredResources.vue";
import AddResource from "./AddResource.vue";

export default {
  components: {StoredResources, AddResource},
  props: [],
  data() {
    return {
      selectedTab: 'stored-resources'
    };
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
