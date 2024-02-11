<script>
import LearningResource from "./LearningResource.vue";

export default {
    components: {LearningResource},
    inject: ['resources'],
    data() {
        return {};
    },
    methods: {},
    computed: {}
}
</script>

<template>
    <ul>
        <learning-resource v-for="resource in resources"
                           :key="resource.id"
                           :title="resource.title"
                           :description="resource.description"
                           :link="resource.link"
        ></learning-resource>
    </ul>
</template>

<style scoped>
ul {
    list-style: none;
    margin: 0;
    padding: 0;
    margin: auto;
    max-width: 40rem;
}
</style>
