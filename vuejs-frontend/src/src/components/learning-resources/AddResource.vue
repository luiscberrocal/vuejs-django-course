<script>
export default {
  props: [],
  data() {
    return {
      newResource: {
        title: '',
        description: '',
        link: ''
      }
    };
  },
  emits: ['add-resource'],
  methods: {
    addResource(event) {
      // event.preventDefault();
      console.log(this.newResource);
      this.$emit('add-resource', this.newResource);
    }
  },
  computed: {}
}
</script>

<template>
  <base-card>
    <form>
      <div class="form-control" @submit.prevent>
        <label for="title">Title</label>
        <input type="text" id="title" v-model="newResource.title">
      </div>
      <div class="form-control">
        <label for="description">Description</label>
        <textarea id="description" rows="3" v-model="newResource.description"></textarea>
      </div>
      <div class="form-control">
        <label for="link">Link</label>
        <input type="url" id="link" v-model="newResource.link">
      </div>
      <div class="form-control">
        <base-button @click="addResource"
                     type="submit"
        >Add Resource
        </base-button>
      </div>
    </form>
  </base-card>
</template>

<style scoped>

label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  font: inherit;
  padding: 0.15rem;
  border: 1px solid #ccc;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #3a0061;
  background-color: #f7ebff;
}

.form-control {
  margin: 1rem 0;
}
</style>
