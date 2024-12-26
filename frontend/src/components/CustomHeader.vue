<script setup>
import { useMainStore } from '@/stores/mainStore';
import { RouterLink } from 'vue-router';

const store = useMainStore();

const { activePage = null } = defineProps({
	activePage: {
		type: String,
		required: false,
	},
});
console.log(store)

</script>

<template>
	<Menubar :model="items"/>
	<nav class="navbar navbar-expand-lg navbar-dark surface-900 px-5">
		<a class="navbar-brand" href="#">
			<img src="../img/Logo2.png" alt="travel logo" class="brand-logo" />
		</a>
		<button
			class="navbar-toggler"
			type="button"
			data-toggle="collapse"
			data-target="#navbarNav"
			aria-controls="navbarNav"
			aria-expanded="false"
			aria-label="Toggle navigation"
		>
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarNav">
			<ul class="navbar-nav ml-auto">
				<li
					class="nav-item"
					:class="activePage === 'home' ? 'active' : ''"
				>
					<RouterLink
						class="nav-link"
						:to="activePage === 'home' ? '#' : '/'"
						>Home</RouterLink
					>
				</li>

				<li class="nav-item" v-if="!store.getUsername">
					<RouterLink
						class="nav-link"
						:to="activePage === 'login' ? '#' : '/login'"
					>
						Login
					</RouterLink>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'clients' ? 'active' : ''"
					v-if="store.getUsername"
				>
					<RouterLink
						class="nav-link"
						:to="activePage === 'clients' ? '#' : '/clients'"
						>Clients</RouterLink
					>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'trips' ? 'active' : ''"
					v-if="store.getUsername"
				>
					<RouterLink
						class="nav-link"
						:to="activePage === 'trips' ? '#' : '/trips'"
						>Trips</RouterLink>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'managers' ? 'active' : ''"
					v-if="store.getRights"
				>
					<RouterLink
						class="nav-link"
						:to="activePage === 'managers' ? '#' : '/managers'"
						>Managers</RouterLink
					>
				</li>
			</ul>
		</div>
	</nav>
</template>
