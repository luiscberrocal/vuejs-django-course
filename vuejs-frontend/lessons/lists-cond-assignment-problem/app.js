const app = Vue.createApp(
    {
        data() {
            return {
                paraIsVisible: true,
                inputVisible: true,
                newGoal: "",
                goals: []
            };
        },
        watch: {},
        computed: {},
        methods: {
            addGoal() {
                this.goals.push(this.newGoal);
                this.newGoal = "";
            },
            toggleVisibility() {
                // console.log('Vis', this.paraIsVisible);
                this.paraIsVisible = !this.paraIsVisible;
                this.inputVisible = this.paraIsVisible;
            }
        }
    }
)

app.mount("#assignment")
