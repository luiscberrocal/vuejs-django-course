<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "debugBlock"
})
</script>

<template>
  <div class="border-4 border-red-600">
    <div class="grid grid-cols-1 gap-2">
      <header class="bs-header">
        DEBUG WINDOW
      </header>
      <div>
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
