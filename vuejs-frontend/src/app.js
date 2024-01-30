const app = Vue.createApp(
    {
        data() {
            return {
                counter: 0,
                message: ""
            };
        },
        watch: {
            counter() {
                if (this.counter < 37) {
                    this.message = "Not there yet";
                }
                if (this.counter > 37){
                    this.message = "Too much";
                }
            }
        },
        methods: {
            add(value) {
                this.counter = this.counter + value;
            },
        }
    }
)

app.mount("#assignment")

