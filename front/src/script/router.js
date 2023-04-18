import {createRouter, createWebHistory} from 'vue-router';
import Home from '@/view/Home';
import Order from '@/view/Order';
import TopGC from '@/view/TopGC';
import Roots from '@/view/Roots';

export default createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{path: '/', name: 'home', component: Home},
		{path: '/order', name: 'order', component: Order},
		{path: '/topgc', name: 'topgc', component: TopGC},
		{path: '/roots', name: 'roots', component: Roots}
	]
});