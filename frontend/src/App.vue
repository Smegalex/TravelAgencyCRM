<script setup>
import { ref, computed } from "vue";
import { defineAsyncComponent } from "vue";
import "@/styles/vue.scss";

const Clients = defineAsyncComponent(() =>
	import("@/pages/tables/Clients.vue")
);
const Home = defineAsyncComponent(() => import("@/pages/Home.vue"));

const routes = {
	"/": Home,
	"/clients-panel": Clients,
};

const currentPath = ref(window.location.pathname);

window.addEventListener("popstate", () => {
	currentPath.value = window.location.pathname;
});

const navigate = (path) => {
	window.history.pushState({}, "", path);
	currentPath.value = path; // Update current path manually
};

const currentView = computed(() => {
	return routes[currentPath.value || Home];
});
// app.component("CustomHeader", CustomHeader);
</script>
<template>
	<component :is="currentView" />
</template>
