<script>
export default {
  data() {
    return {
      detailsVisible: false,
      friend2: {
        name: "Luis",
        phone: "889-0000",
        email: "pop@hoca.com"
      }
    }
  },
    props:[
        'name',
        'phone',
        'email'
    ]
    ,
  methods: {
    toggleDetails() {
      this.detailsVisible = !this.detailsVisible;
      // this.friend = this.frnd;
    }
  }
}
</script>

<template>
  <li>
    <h2>{{ name }}</h2>
    <button @click="toggleDetails">{{ detailsVisible ? 'Hide' : 'Show'}} details</button>
    <ul v-if="detailsVisible">
      <li><strong>Phone:</strong>{{ phone }}</li>
      <li><strong>Email:</strong>{{ email }}</li>
    </ul>
  </li>
</template>

<style scoped>

</style>
