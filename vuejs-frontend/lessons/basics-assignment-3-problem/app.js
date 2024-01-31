const app = Vue.createApp(
    {
        data() {
            return {
                counter: 0,
            };
        },
        watch: {
            message() {
                const that = this;
                setTimeout(function(){
                    that.counter = 0;
                }, 5000);
            }
        },
        computed: {
            message(){
                 if (this.counter < 37) {
                    return "Not there yet";
                }
                if (this.counter > 37){
                    return "Too much";
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

