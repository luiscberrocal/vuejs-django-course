<script lang="ts" setup>
const lock = '🔒';
const forkIcon = '🔱';
let projectUrl = 'https://api.github.com/users/luiscberrocal/repos?per_page=100';
const {error, pending, data} = await useFetch(projectUrl, {
  onResponse(context) {
    console.log(context.response.headers);
  },
});
const repos = computed(() => data.value.filter(repo => repo.description)
    .sort((a, b) => b.stargazers_count - a.stargazers_count));
</script>

<template>
  <div>
    <section v-if="pending">Loading...</section>
    <section v-else-if="error">Error: {{ error.message }}</section>
    <section v-else>
      <ul class="grid grid-cols-1 gap-4">
        <li v-for="repo in repos" class="border border-gray-200 rounded-sm p-4 hover:bg-gray-100 mono-font"
            :key="repo.id">
          <a :href="repo.html_url" target="_blank">
            <div class="flex justify-between items-center">
              <h2 class="text-xl font-bold"><span v-if="repo.fork">{{ forkIcon }}</span>{{ repo.name }} <span
                  v-if="repo.fork">(Forked)</span></h2>
              <div>{{ repo.stargazers_count }} *</div>
            </div>
            <p>{{ repo.description }}</p>
            <p>Last push: {{ repo.pushed_at }}</p>
          </a>
        </li>
      </ul>

    </section>

  </div>

</template>

<style scoped>

</style>
