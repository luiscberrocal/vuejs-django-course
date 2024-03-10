<script setup>
const props = defineProps({
  level: {
    type: String,
    default: null
  }
})
const isError = computed(() => props.level === 'error');
const isInfo = computed(() => props.level === 'info');
</script>

<template>
  <div class="border-4 border-red-600 p-1 m-1">
    <div class="grid grid-cols-1 gap-2">
      <header class="bs-header" :class="{'error': isError, 'info': isInfo}">
        <slot name="title">DEBUG Window</slot>
      </header>
      <div>
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bs-header {
  @apply bg-green-800 text-white p-4 rounded-lg
}

.error {
  @apply bg-red-800
}

.info {
  @apply bg-blue-800
}
</style>
