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
    <div v-for="exercise in exercisesSummaries" :key="exercise.name">
      <CalisthenicsExerciseSummary
          :name="exercise.name"
          :average="exercise.average"
          :todaysCount="exercise.todaysCount"
      />
    </div>
  </div>
</template>

<style scoped>

</style>
