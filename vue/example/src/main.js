import { createApp } from 'vue'
// import App from './App.vue'
import App from './ExampleApp.vue'
import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/views/HomeView.vue'
import AboutPage from './components/views/AboutView.vue'


// createApp(App).mount('#app')

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/home', component: HomePage },
        { path: '/about', component: AboutPage },
    ]
});

const app = createApp(App)

app.use(router)

app.mount('#app')
