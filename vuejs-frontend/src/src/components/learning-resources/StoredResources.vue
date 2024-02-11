<script>
import LearningResource from "./LearningResource.vue";

export default {
    components: {LearningResource},
    props: ['resources'],
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

</style>
