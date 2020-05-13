import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: () => import('./views/Home.vue'),
        },
        {
            path: '/library',
            component: () => import('./views/Library.vue'),
        },
        {
            path: '/users',
            component: () => import('./views/Users.vue')
        },
        {
            path: '/about',
            component: () => import('./views/About.vue')
        },
        {
            path: '/login',
            component: () => import('./views/Login.vue')
        },
        {
            path: '/register',
            component: () => import('./views/Register.vue')
        },
        {
            path: '/book/:id',
            component: () => import('./views/OriginPage.vue')
        },
        {
            path: '/reading',
            component: () => import('./views/BookReading.vue')
        },
        {
            path: '/translation',
            component: () => import('./views/BookTranslation.vue')
        },
        {
            path: '/user',
            component: () => import('./views/User.vue')
        },
        {
            path: '/user-settings',
            component: () => import('./views/UserSettings.vue')
        },
        {
            path: '/user-onhold',
            component: () => import('./views/UserOnHold.vue')
        },
    ]
})