<script >
export default {
  props: [
    'name',
    'age'
  ]
}
</script>
<template>
  <section>
    <h2>{{ name }}</h2>
      <h3>{{ age }}</h3>
  </section>
</template>

<style scoped>

</style>
