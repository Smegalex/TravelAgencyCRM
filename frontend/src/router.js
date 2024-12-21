import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

// Define the components to load
const Clients = () => import("@/pages/tables/Clients.vue");
const Home = () => import("@/pages/Home.vue");
const ClientDetail = () => import("@/pages/detailed/ClientView.vue");
const routes = [
	{ path: "/", component: Home },
	{ path: "/clients", component: Clients },
	{ path: "/clients/:id", component: ClientDetail, props: true }, // Dynamic route for client detail
];
const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
