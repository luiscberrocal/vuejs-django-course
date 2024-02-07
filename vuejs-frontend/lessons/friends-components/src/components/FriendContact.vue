<script>
export default {
  data() {
    return {
      detailsVisible: false,
    }
  },
  props: [
    'id',
    'name',
    'phone',
    'email',
    'isFavorite'
  ],
  emits: [
    'delete'
  ],
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
    <button @click="$emit('delete', id)">Delete</button>
  </li>
</template>

<style scoped>

</style>
