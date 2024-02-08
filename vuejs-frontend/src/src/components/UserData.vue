<script>
export default {
  data() {
    return {
      name: '',
      age: null
    }
  },
  emits: [
    'save-data'
  ],
  methods: {
    save() {
      this.$emit('save-data', this.name, this.age)
    }
  }
}
</script>

<template>

  <section>
    <h2>User Data</h2>
    <form @submit.prevent>
      <label for="name">Name:</label>
      <input id="name" type="text" v-model="name">
      <label for="age">Age:</label>
      <input id="age" type="number" v-model="age">
      <button @click="save">Save</button>
    </form>
  </section>
</template>

<style scoped>

</style>
