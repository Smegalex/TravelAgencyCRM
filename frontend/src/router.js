import { createRouter, createWebHistory } from "vue-router";
import { useMainStore } from "./stores/mainStore";

// Define the components to load
const Clients = () => import("@/pages/tables/Clients.vue");
const Home = () => import("@/pages/Home.vue");
const Trips = () => import("@/pages/tables/Trips.vue");
const Managers = () => import("@/pages/tables/Managers.vue");
const ClientDetail = () => import("@/pages/detailed/ClientView.vue");
const LoginModal = () => import("@/pages/service/Login.vue");
const AccessError = () => import("@/pages/service/AccessError.vue");

const routes = [
	{
		path: "/",
		component: Home,
	},
	{ path: "/clients", component: Clients, meta: { requiresAuth: true } },
	{
		path: "/trips",
		component: Trips,
		meta: { requiresAuth: true },
	},
	{
		path: "/managers",
		component: Managers,
		meta: { requiresAuth: true, requiresAdmin: true },
	},
	{ path: "/clients/:id", component: ClientDetail, props: true },
	{ path: "/login", component: LoginModal },
	{ path: "/accessError", component: AccessError },
];
const router = createRouter({
	history: createWebHistory(),
	routes,
});
router.beforeEach((to, from) => {
	const store = useMainStore();

	if (to.meta.requiresAdmin && !store.getRights) return "/accessError";
	if (to.meta.requiresAuth && !store.getUsername) return "/login";
});
export default router;
