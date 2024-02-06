<script>
export default {
  data() {
    return {
      detailsVisible: false,
    }
  },
  props: [
    'name',
    'phone',
    'email',
    'isFavorite'
  ]
  ,
  methods: {
    toggleDetails() {
      this.detailsVisible = !this.detailsVisible;
    }
  }
}
</script>

<template>
  <li>
    <h2>{{ name }} <span v-if="isFavorite">(Favorite)</span></h2>
    <button @click="toggleDetails">{{ detailsVisible ? 'Hide' : 'Show' }} details</button>
    <ul v-if="detailsVisible">
      <li><strong>Phone:</strong>{{ phone }}</li>
      <li><strong>Email:</strong>{{ email }}</li>
    </ul>
  </li>
</template>

<style scoped>

</style>
