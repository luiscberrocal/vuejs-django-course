<script lang="ts" setup>

const colorMode = useColorMode();
const modes = [
  'system',
  'dark',
  'light'
]
const nextMode = computed(() => {
  const i = modes.indexOf(colorMode.preference);
  const nextModeValue = modes[(i + 1) % modes.length];
  return nextModeValue;
});

const toggleColorMode = () => {
  colorMode.preference = nextMode.value;
}
</script>

<template>
  <button @click="toggleColorMode">{{ nextMode }}</button>
</template>

<style scoped>

</style>
