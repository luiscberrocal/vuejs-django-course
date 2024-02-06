<script setup>
export default {
    data(){
        return {
            newFriendName: '',
            newFriendPhone: '',
            newFriendEmail: '',
        }
    }
}
</script>

<template>
    <form action="">
        <div>
            <label for="inputName" v-model="newFriendName">Name:</label>
            <input type="text" id="inputName">
        </div>
        <div>
            <label for="inputPhone">Phone:</label>
            <input type="text" id="inputPhone">
        </div>
        <div>
            <label for="inputEmail">Email:</label>
            <input type="text" id="inputEmail">
        </div>
        <button>Save</button>
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
</style>
