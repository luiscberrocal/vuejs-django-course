<script>
import BaseCard from "../UI/BaseCard.vue";

export default {
    components: {BaseCard},
  props: [
    'title',
    'description',
    'link'
  ],
  data() {
    return {};
  },
  methods: {}
}
</script>

<template>
  <li>
    <base-card>
      <header>
        <h3>{{ title }}</h3>
        <div>
          <button>Delete</button>
          <button>Share</button>
        </div>
      </header>
      <p>{{ description }}</p>
      <nav>
        <a :href="link" target="_blank">View resource</a>
      </nav>
    </base-card>
  </li>
</template>

<style scoped>
li {
  margin: auto;
  max-width: 40rem;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h3 {
  font-size: 1.25rem;
  margin: 0.5rem 0;
}

p {
  margin: 0.5rem 0;
}

a {
  text-decoration: none;
  color: #ce5c00;
}

a:hover,
a:active {
  color: #c89300;
}

</style>
