<script>
export default {
  data() {
    return {
      name: 'ts',
      age: 33
    }
  },
  methods: {
    save(name, age) {
      this.name = name;
      this.age = age;
    }
  }
}
</script>

<template>
  <h2>User Application</h2>
  <active-user :name="name" :age="age"></active-user>
  <user-data @save-data="save"></user-data>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jost&display=swap');
@import "main.css";

section {
  margin: 2rem auto;
  max-width: 40rem;
  border-radius: 12px;
  border: #ccc solid 1px;
  padding: 1rem;
}
</style>
