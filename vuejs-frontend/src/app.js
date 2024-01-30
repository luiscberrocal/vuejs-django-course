const app = Vue.createApp(
    {
        data() {
            return {
                styleNum: 0
            };
        },
        watch: {},
        computed: {
            currentStyle() {
                console.log("Setting current style",  this.styleNum);
                if (this.styleNum === 0) {
                    return "";
                } else if (this.styleNum === 1 || this.styleNum === 2) {
                    return "user" + this.styleNum;
                } else {
                    return "";
                }
            }
        },
        methods: {
        }
    }
)

app.mount("#assignment")
