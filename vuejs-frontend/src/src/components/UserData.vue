<script>
export default {
  data() {
    return {
      name: '',
      age: null
    }
  }
}
</script>

<template>

  <div>
    <h2>User Data</h2>
    <form @submit.prevent>
      <input type="text" v-model="name">
      <input type="number" v-model="age">
      <button>Save</button>
    </form>
  </div>
</template>

<style scoped>

</style>
