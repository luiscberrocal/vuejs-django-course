const app = Vue.createApp(
    {
        data() {
            return {
                styleName: "",
                paraIsVisible: true,
                backGroundColor: ""
            };
        },
        watch: {},
        computed: {
            paraClasses() {
                return {
                    user1: this.styleName === "user1",
                    user2: this.styleName === "user2",
                    visible: this.paraIsVisible,
                    hidden: !this.paraIsVisible,
                }
            }
        },
        methods: {
            toggleVisibility(){
                this.paraIsVisible = !this.paraIsVisible
            }
        }
    }
)

app.mount("#assignment")
