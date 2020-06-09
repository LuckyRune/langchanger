import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: () => import('./views/Home.vue'),
            name: 'Home'
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
            path: '/logout',
            component: () => import('./views/Logout.vue')
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
            path: '/reading/:id',
            component: () => import('./views/BookReading.vue')
        },
        {
            path: '/translation/:id',
            component: () => import('./views/BookTranslation.vue')
        },
        {
            path: '/editing/:id',
            component: () => import('./views/AddVersion.vue')
        },
        {
            path: '/translating/:id',
            component: () => import('./views/BookTranslating.vue')
        },
        {
            path: '/user/:id',
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
        {
            path: '/changes/:id',
            component: () => import('./views/Changes.vue')
        },
        {
            path: '/version/:id',
            component: () => import('./views/VersionRead.vue')
        }
    ]
})