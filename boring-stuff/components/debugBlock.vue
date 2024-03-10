<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "debugBlock"
})
</script>

<template>
  <div class="border-4 border-red-600 p-6 m-4">
    <div class="grid grid-cols-1 gap-2">
      <header class="bs-header">
        DEBUG WINDOW2
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
