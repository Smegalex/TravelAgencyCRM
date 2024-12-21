<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

const route = useRoute();

const client = ref({
	id: undefined,
	name: "",
	surname: null,
	email: "",
});

const { id } = defineProps({
	id: {
		type: String,
		required: true,
	},
});

const fetchClient = async () => {
	try {
		const response = await fetch(
			`http://127.0.0.1:5000/clients/${id}`
		);
		client.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		client.value = client.value[0];
		console.log(client.value);
	} catch (error) {
		console.error(`Error fetching client (id: ${id}):`, error);
	}
};

onMounted(fetchClient);
</script>

<template>
	<div id="page-wrapper" style="overflow-y: scroll; height: 100vh">
		<!-- Header -->
		<header>
			<CustomHeader active-page="clients" />
		</header>
		<main>
			<Splitter style="height: 300px">
    <SplitterPanel class="flex items-center justify-center" :size="25" :minSize="25"> 
		Panel 1 

	</SplitterPanel>
    <SplitterPanel class="flex items-center justify-center" :size="75">
		 <DataTable
		 :value="bookings"
		 >

		 </DataTable>
	</SplitterPanel>
</Splitter>
		</main>
		<CustomFooter />
	</div>
</template>

<style scoped>
html,
body {
	overflow: hidden;
}

.p-card {
	max-width: 600px;
	margin: 0 auto;
}

.p-card-header h2 {
	font-size: 1.5rem;
	color: var(--primary-color);
}

.p-card-footer {
	padding-top: 0;
}

.p-text-center {
	text-align: center;
}
</style>
