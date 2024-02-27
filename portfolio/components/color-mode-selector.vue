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
const nextModeIcons = {
  system: '🌓',
  light: '🌕',
  dark: '🌑'
}
const nextModeIcon = computed(() => nextModeIcons[nextMode.value])
const toggleColorMode = () => {
  colorMode.preference = nextMode.value;
}
</script>

<template>
  <button @click="toggleColorMode"
          class="hover:bg-gray-200 dark:hover:bg-gray-600 px-2 py-1 text-gray-500">{{ nextModeIcon }}
  </button>
</template>

<style scoped>

</style>
