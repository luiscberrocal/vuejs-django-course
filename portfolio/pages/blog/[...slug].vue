<script lang="ts" setup>
const route = useRoute();

console.log(route)

</script>


<template>
  <article
      class="prose dark:prose-invert prose-pre:bg-white dark:prose-pre:bg-gray-800 prose-pre:text-gray-700 dark:prose-pre:text-gray-300 max-w-none">
    <ContentDoc v-slot="{doc}">
      <div class="grid grid-cols-6 gap-16">
        <div :class="{'col-span-4': doc.toc, 'col-span-6': !doc.toc}">
          <ContentRenderer :value="doc"/>
        </div>
        <div class="col-span-2" v-if="doc.toc">
          {{ doc.body.toc.links }}
          <aside class="sticky top-8">
            <div class="font-semibold mb-2">Table of Contents</div>
            <nav>
              Links
            </nav>
          </aside>
        </div>
      </div>
    </ContentDoc>
  </article>
</template>

<style scoped>

</style>
