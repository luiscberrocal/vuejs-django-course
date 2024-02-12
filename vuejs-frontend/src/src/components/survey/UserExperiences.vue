<template>
  <section>
    <base-card>
      <h2>Submitted Experiences</h2>
      <div>
        <base-button @click="loadExperiences">Load Submitted Experiences</base-button>
      </div>
      <p v-if="isLoading" Loading...></p>
      <ul v-if="!isLoading">
        <survey-result
            v-for="result in results"
            :key="result.id"
            :name="result.name"
            :rating="result.rating"
        ></survey-result>
      </ul>
    </base-card>
  </section>
</template>

<script>
import SurveyResult from './SurveyResult.vue';

export default {
  data() {
    return {
      results: [],
      isLoading: false,

    };
  },
  components: {
    SurveyResult,
  },
  methods: {
    loadExperiences() {
      this.isLoading = true;
      const url = "https://vuejs-course-640bf-default-rtdb.firebaseio.com/surveys.json";
      console.log('Calling ', url)
      fetch(url).then(
          (response) => {
            console.log('Processing response', response)
            if (response.ok) {
              return response.json();
            }
          }
      ).then((data) => {
        this.isLoading = false;
        console.log('Processing data', data)
        const results = [];
        for (let key in data) {
          const result = data[key];
          results.push({
            id: key,
            name: result.name,
            rating: result.rating,
          });
          this.results = results;
        }
        console.log(results);
      })
    },
  },
  mounted() {
    this.loadExperiences();
  }
};
</script>

<style scoped>
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
</style>
