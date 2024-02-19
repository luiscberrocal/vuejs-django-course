import {createApp} from 'vue';
import {createRouter, createWebHistory} from 'vue-router';
import App from './App.vue';
import UsersList from "./components/users/UsersList.vue";
import TeamMembers from "./components/teams/TeamMembers.vue";
import TeamFooter from "./components/teams/TeamFooter.vue";
import UserFooter from "./components/users/UserFooter.vue";
import TeamsList from "./components/teams/TeamsList.vue";
import PaymentList from "./components/payments/PaymentList.vue";

const app = createApp(App)
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', redirect: '/teams'},
        {
            path: '/teams',
            components: {default: TeamsList, footer: TeamFooter},
            children: [
                {name: 'team-members', path: ':teamId', component: TeamMembers, props: true},
            ]
        },
        {path: '/users', components: {default: UsersList, footer: UserFooter}},
        {path: '/payments', components: {default: PaymentList}},
        {path: '/:notFound(.*)', redirect: '/teams'}
    ],
    linkActiveClass: 'active'
})

app.use(router);

app.mount('#app');
