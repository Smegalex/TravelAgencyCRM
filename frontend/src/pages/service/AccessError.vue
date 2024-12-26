<template>
	<div class="page-container flex flex-column bg-red-50 h-screen">
		<header>
			<CustomHeader />
		</header>
		<main class="flex-1 flex flex-column justify-content-center">
			<div class="surface-card p-4 text-center">
				<div class="mb-4">
					<i class="pi pi-lock text-red-500 text-5xl"></i>
				</div>
				<h1 class="text-4xl font-bold text-gray-900 mb-2">
					Access Denied
				</h1>
				<p class="text-gray-600 mb-4">
					You don’t have permission to access this page. If you
					believe this is a mistake, please contact the administrator.
				</p>
			</div>
		</main>
		<CustomFooter />
	</div>
</template>
<style scoped>
footer {
	margin-top: auto;
}
</style>
