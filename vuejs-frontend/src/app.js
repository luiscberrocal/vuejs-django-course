const app = Vue.createApp(
    {
        data() {
            return {
                output: ""
            }
        },
        methods: {
            showAlert() {
                alert('Danger');
            },
            showOutput(event, onEnter) {
                if (onEnter){

                } else {
                    this.output = event.target.value;
                }
            }
        }
    }
)
app.mount("#assignment")
