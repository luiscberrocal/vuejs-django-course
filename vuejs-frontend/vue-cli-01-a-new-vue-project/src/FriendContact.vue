<script setup>
export default {
    data(){
        return {
            detailsVisible: false,
            friend: {
                name: "Luis",
                phone: "889-0000",
                email: "pop@hoca.com"
            }
        }
    }
}
</script>

<template>
<li>
    <h2>{{friend.name}}</h2>
    <button>Show details</button>
    <ul>
        <li><strong>Phone:</strong>{{friend.phone}}</li>
        <li><strong>Email:</strong>{{ friend.email}}</li>
    </ul>
</li>
</template>

<style scoped>

</style>
