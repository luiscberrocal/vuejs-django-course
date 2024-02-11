<script>
export default {
  props: [],
  data() {
    return {
      inputIsInvalid: false
    };
  },
  inject: ['addResource'],
  methods: {
    submitData() {
      console.log('Append Resource.....');
      const title = this.$refs.titleInput.value;
      const description = this.$refs.descriptionInput.value;
      const link = this.$refs.linkInput.value;
      this.inputIsInvalid = title.trim() === '' || description.trim() === '' || link.trim() === ''
      if (this.inputIsInvalid) {
        return;
      }
      this.addResource(title, description, link);

    },
    confirmError() {
      this.inputIsInvalid = false;
    }
  }
}
</script>

<template>
  <base-dialog v-if="inputIsInvalid" title="Invalid Data">

    <template #default>
      <p>Please enter all data required.</p>
    </template>
    <template #actions>
      <base-button @click="confirmError">Ok</base-button>
    </template>
  </base-dialog>
  <base-card>
    <form @submit.prevent="submitData">
      <div class="form-control">
        <label for="title">Title</label>
        <input type="text" id="title" ref="titleInput">
      </div>
      <div class="form-control">
        <label for="description">Description</label>
        <textarea id="description" rows="3" ref="descriptionInput"></textarea>
      </div>
      <div class="form-control">
        <label for="link">Link</label>
        <input type="url" id="link" ref="linkInput">
      </div>
      <div class="form-control">
        <base-button
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
