<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "debugBlock"
})
</script>

<template>
  <div class="border-4 border-red-600 p-1 m-1">
    <div class="grid grid-cols-1 gap-2">
      <header class="bs-header">
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
</style>
