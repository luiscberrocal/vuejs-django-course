const app = Vue.createApp(
    {
        data() {
            return {
                paraIsVisible: true,
                newGoal: "",
                goals: []
            };
        },
        watch: {},
        computed: {
            paraClasses() {
                return {
                    visible: this.paraIsVisible,
                    hidden: !this.paraIsVisible,
                }
            }
        },
        methods: {
            addGoal() {
                this.goals.push(this.newGoal);
                this.newGoal = "";
            },
            toggleVisibility() {
                console.log('Vis', this.paraIsVisible)
                this.paraIsVisible = !this.paraIsVisible;
            }
        }
    }
)

app.mount("#assignment")
