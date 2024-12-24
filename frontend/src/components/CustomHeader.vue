<script setup>


const { activePage = null } = defineProps({
	activePage: {
		type: String,
		required: false,
	},
});

</script>

<template>
	<nav class="navbar navbar-expand-lg navbar-dark bg-dark px-5">
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
					<a
						class="nav-link"
						:href="activePage === 'home' ? '#' : '/'"
						>Home</a
					>
				</li>
				
				<li class="nav-item">
				<a class="nav-link" :href="activePage === 'login' ? '#' : '/login'">
					Login
				</a>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'register' ? 'active' : ''"
				>
					<a
						class="nav-link"
						:href="activePage === 'register' ? '#' : '#'"
					>
						Register
					</a>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'clients' ? 'active' : ''"
				>
					<a
						class="nav-link"
						:href="activePage === 'clients' ? '#' : '/clients'"
						>Clients panel</a
					>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'trips' ? 'active' : ''"
				>
					<a
						class="nav-link"
						:href="activePage === 'trips' ? '#' : '/trips'"
						>Trips panel</a
					>
				</li>
				<li
					class="nav-item"
					:class="activePage === 'managers' ? 'active' : ''"
				>
					<a
						class="nav-link"
						:href="activePage === 'managers' ? '#' : '/managers'"
						>Managers panel</a
					>
				</li>
				<li class="nav-item">
					<a
						class="nav-link"
						href="#"
						data-toggle="modal"
						data-target="#faqModal"
						>FAQ</a
					>
				</li>
			</ul>
		</div>
	</nav>
</template>


