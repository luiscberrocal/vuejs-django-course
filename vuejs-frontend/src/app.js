const app = Vue.createApp(
    {
        data() {
            return {
                name: "Luis C. Berrocal",
                age: 57
            }
        },
        methods: {
            ageIn5Years() {
                return this.age + 5;
            },
            getRandom() {
                return Math.random();
            }
        }
    }
)

app.mount("#assignment")
