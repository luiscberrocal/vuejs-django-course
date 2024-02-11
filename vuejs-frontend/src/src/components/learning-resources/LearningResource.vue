<script>
export default {
    props: [
        'title',
        'description',
        'link'
    ],
    data() {
        return {};
    },
    methods: {}
}
</script>

<template>
<li>
    <h3>{{ title }}</h3>
    <p>{{ description }}</p>
    <nav>
        <a :href="link" target="_blank">Link</a>
    </nav>
    <button>Delete</button>
</li>
</template>

<style scoped>

</style>
