function getAttackValue(min, max) {
    return Math.floor(Math.random() * (max - min) + min)
}

const app = Vue.createApp(
    {
        data() {
            return {
                playerHealth: 100,
                monsterHealth: 100
            };
        },
        watch: {},
        computed: {
            monsterHealthBar(){
                return {width: this.monsterHealth + '%'}
            },
            playerHealthBar(){
                return {width: this.playerHealth + '%'}
            }
        },
        methods: {
            attackMonster() {
                const attackValue = getAttackValue(8, 12);
                this.monsterHealth -= attackValue;
                this.attackPlayer();
            },
            attackPlayer() {
                const attackValue = getAttackValue(10, 18);
                this.playerHealth -= attackValue;
            },
        }
    }
)

app.mount("#game")
