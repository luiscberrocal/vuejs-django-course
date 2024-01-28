const app = Vue.createApp({
    data() {
        return {
            courseGoal: "Finish course",
            vueLink: "https://google.com/"
        };
    },
    methods: {
        outputGoal(){
            const  n = Math.random()
            if (n > 0.5){
                return 'Learn Vue'
            } else {
                return 'Master Vueu'
            }
        }
    }
});

app.mount('#user-goal');

