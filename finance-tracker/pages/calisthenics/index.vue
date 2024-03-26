<script lang="ts" setup>
const exercisesSummaries = [
  {
    name: 'Pushups',
    average: 35,
    todaysCount: 50
  },
  {
    name: 'Pullups',
    average: 50,
    todaysCount: 25
  },
  {
    name: 'Squats',
    average: 200,
    todaysCount: 100
  }
]
</script>

<template>
  <div>
    <h1>Calisthenics</h1>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 sm:gap-16">
      <CalisthenicsExerciseSummary
          v-for="exercise in exercisesSummaries" :key="exercise.name"
          :name="exercise.name"
          :average="exercise.average"
          :todaysCount="exercise.todaysCount"
      />
    </div>
  </div>
</template>

<style scoped>

</style>
