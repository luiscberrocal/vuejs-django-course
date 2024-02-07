<script>
export default {
  data() {
    return {
      newFriendName: '',
      newFriendPhone: '',
      newFriendEmail: '',
    }
  },
  emits: [
    'add-friend'
  ],
  methods: {
    saveData() {
      this.$emit('add-friend', this.newFriendName, this.newFriendPhone, this.newFriendEmail)
    }
  }
}
</script>

<template>
  <form @submit.prevent="">
    <div>
      <label for="inputName">Name:</label>
      <input type="text" id="inputName" v-model="newFriendName">
    </div>
    <div>
      <label for="inputPhone">Phone:</label>
      <input type="tel" id="inputPhone" v-model="newFriendPhone">
    </div>
    <div>
      <label for="inputEmail">Email:</label>
      <input type="email" id="inputEmail" v-model="newFriendEmail">
    </div>
    <button @click="saveData">Save</button>
  </form>
</template>

<style scoped>
#app input {
  font: inherit;
  padding: 0.15rem;
}

#app label {
  font-weight: bold;
  margin-right: 1rem;
  width: 7rem;
  display: inline-block;
}

#app form div {
  margin: 1rem 0;
}

#app form {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin: 1rem auto;
  border-radius: 10px;
  padding: 1rem;
  text-align: center;
  width: 90%;
  max-width: 40rem;
}
</style>
