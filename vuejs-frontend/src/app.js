const app = Vue.createApp(
    {
        data() {
            return {
                output: "",
                finalOutput: ""
            }
        },
        methods: {
            showAlert() {
                alert('Danger');
            },
            showOutput(event, onEnter) {
                console.log('onEnter', onEnter)
                console.log('value', event.target.value)
                if (onEnter){
                    this.finalOutput = event.target.value
                } else {
                    this.output = event.target.value;
                }
            },
        }
    }
)
app.mount("#assignment")
