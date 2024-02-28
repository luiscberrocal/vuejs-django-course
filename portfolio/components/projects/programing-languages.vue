<script lang="ts" setup>
const props = defineProps(['languageUrl'])
const {error, pending, data} = await useFetch(props.languageUrl);
const languages = computed(() => {
    const my_list = []
    if (data.value.Python) {
        my_list.push('Python')
    }
    if (data.value.Java) {
        my_list.push('Java')
    }
    return my_list
});
</script>1

<template>
<div>
    {{ languageUrl}}
    <section v-if="pending">Loading...</section>
    <section v-else-if="error">Error: {{ error.message }}</section>
    <section v-else>
        {{ data}}
    </section>
</div>
</template>

<style scoped>

</style>
