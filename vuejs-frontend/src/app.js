function getAttackValue(min, max) {
    return Math.floor(Math.random() * (max - min) + min)
}

const app = Vue.createApp(
    {
        data() {
            return {
                playerHealth: 100,
                monsterHealth: 100,
                currentRound: 0
            };
        },
        watch: {},
        computed: {
            monsterHealthBar() {
                return {width: this.monsterHealth + '%'}
            },
            playerHealthBar() {
                return {width: this.playerHealth + '%'}
            },
            allowSpecialAttack(){
                return this.currentRound % 3 !== 0;
            }
        },
        methods: {
            attackMonster() {
                this.currentRound++;
                const attackValue = getAttackValue(5, 12);
                this.monsterHealth -= attackValue;
                this.attackPlayer();
            },
            attackPlayer() {
                const attackValue = getAttackValue(8, 15);
                this.playerHealth -= attackValue;
            },
            specialAttackMonster() {
                this.currentRound++;
                const attackValue = getAttackValue(10, 25);
                this.monsterHealth -= attackValue;
                this.attackPlayer();
            },
        }
    }
)

app.mount("#game")
