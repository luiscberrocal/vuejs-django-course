const app = Vue.createApp(
    {
        data() {
            return {
                name: "Luis C. Berrocal",
                age: 57,
                imageLink: "https://cdn.pixabay.com/photo/2016/02/10/16/37/cat-1192026_640.jpg"
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
