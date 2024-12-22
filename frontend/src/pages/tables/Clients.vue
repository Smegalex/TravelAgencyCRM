<script setup>
// Vue
import { ref, onMounted } from "vue";

// Components
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";

// Yup
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

// Requests
import {
	fetchClient,
	fetchClients,
	addClient,
	updateClient,
	deleteClient,
} from "@/requests/clientsRequests";

const clients = ref([]);

const getClients = async () => {
	clients.value = await fetchClients();
};

const clientFormResolver = ref(
	yupResolver(
		yup.object().shape({
			name: yup
				.string()
				.required("Name is required.")
				.max(255, "Name too long."),
			surname: yup.string().notRequired(),
			email: yup
				.string()
				.email("Invalid email format")
				.required("Email is required.")
				.max(50, "Email too long. Contact IT."),
		})
	)
);

// create new client
const showCreateClientForm = ref(false);
const newClient = ref({ name: "", surname: null, email: "" });
const createClientFormFields = [
	{
		name: "name",
		placeholder: "Client's name*",
		props: "",
		type: "",
	},
	{
		name: "surname",
		placeholder: "Client's surname",
		props: "",
		type: "",
	},
	{
		name: "email",
		placeholder: "Client's email*",
		props: "",
		type: "",
	},
];

const createClient = async ({ valid }) => {
	if (valid) {
		const addedClient = await addClient(newClient.value);
		clients.value.push(addedClient); // Add new student to local list
		newClient.value = { name: "", surname: null, email: "" }; // Reset form fields
		showCreateClientForm.value = false;
	}
};

const changeCreateFormVisibility = () => {
	showCreateClientForm.value = !showCreateClientForm.value;
};

// edit client
const currentClient = ref([]);
const showEditClientForm = ref(false);

const editClientFormFields = [
	{
		name: "name",
		placeholder: "Client's name*",
		props: "",
		type: "",
	},
	{
		name: "surname",
		placeholder: "Client's surname",
		props: "",
		type: "",
	},
	{
		name: "email",
		placeholder: "Client's email*",
		props: "",
		type: "",
	},
];

const changeEditFormVisibility = () => {
	showEditClientForm.value = !showEditClientForm.value;
};

const editClientTrigger = async (id) => {
	currentClient.value = clients.value.find((client) => client.id === id);
	showEditClientForm.value = true;
	// console.log(currentClient.value);
};

const editClient = async ({ valid }) => {
	if (valid) {
		const editedClient = await updateClient(currentClient.value);
		clients.value = clients.value.map((client) =>
			client.id == editedClient.id ? editedClient : client
		);
		showEditClientForm.value = false;
	}
};

const removeClient = async (id) => {
	await deleteClient(id);
	clients.value = clients.value.filter((client) => client.id !== id); // Update local list
};

onMounted(() => {
	getClients();
});
</script>
<template>
	<div id="page-wrapper" class="h-screen overflow-y-scroll flex flex-column">
		<!-- Header -->
		<header>
			<CustomHeader active-page="clients" />
		</header>
		<main>
			<div class="clients-table">
				<div class="button-container">
					<Button
						pButton
						label="Add New Client"
						icon="pi pi-plus"
						class="p-mb-3"
						@click="showCreateClientForm = true"
					></Button>
				</div>
				<DataTable
					:value="clients"
					:rows="5"
					paginator
					paginatorPosition="bottom"
					class="p-datatable-gridlines"
					striped-rows
					:rowsPerPageOptions="[5, 10, 20]"
				>
					<Column
						field="id"
						header="ID"
						:sortable="true"
						style="width: 10%"
					></Column>
					<Column
						field="name"
						header="Name"
						:sortable="true"
						style="width: 15%"
					></Column>
					<Column
						field="surname"
						header="Surname"
						:sortable="true"
						style="width: 20%"
					></Column>
					<Column
						field="email"
						header="Email"
						:sortable="true"
						style="width: 40%"
					></Column>

					<Column header="Actions" style="width: 15%">
						<template #body="{ data }">
							<Button
								pButton
								icon="pi pi-external-link"
								rounded
								variant="text"
								title="Detailed view"
								as="router-link"
								:to="'/clients/' + data.id"
							></Button>
							<Button
								pButton
								icon="pi pi-pencil"
								rounded
								variant="text"
								title="Edit"
								@click="editClientTrigger(data.id)"
							></Button>
							<Button
								pButton
								icon="pi pi-trash"
								severity="danger"
								rounded
								variant="text"
								title="Delete"
								@click="removeClient(data.id)"
							></Button>
						</template>
					</Column>
				</DataTable>
			</div>
		</main>
		<UniversalModal
			header="Create new client"
			:show-form="showCreateClientForm"
			@change-visibility="changeCreateFormVisibility"
			:fields="createClientFormFields"
			:form-resolver="clientFormResolver"
			:data="newClient"
			:call-back="createClient"
			submit-label="Create"
		/>
		<UniversalModal
			header="Edit client"
			:show-form="showEditClientForm"
			@change-visibility="changeEditFormVisibility"
			:fields="editClientFormFields"
			:form-resolver="clientFormResolver"
			:data="currentClient"
			:call-back="editClient"
			submit-label="Save"
		/>
		<CustomFooter />
	</div>

	<!-- Модальне вікно Авторизації -->
	<div
		class="modal fade"
		id="loginModal"
		tabindex="-1"
		role="dialog"
		aria-labelledby="loginModalTitle"
		aria-hidden="true"
	>
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="loginModalTitle">
						Форма Авторизації
					</h5>
					<button
						type="button"
						class="close"
						data-dismiss="modal"
						aria-label="Close"
					>
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<form>
						<div class="form-group">
							<label for="emailLogin">Email</label>
							<input
								type="email"
								class="form-control"
								id="emailLogin"
								placeholder="Enter email"
							/>
						</div>
						<div class="form-group">
							<label for="passwordLogin">Password</label>
							<input
								type="password"
								class="form-control"
								id="passwordLogin"
								placeholder="Password"
							/>
						</div>
						<button type="submit" class="btn btn-primary">
							Login
						</button>
					</form>
				</div>
			</div>
		</div>
	</div>

	<!-- Модальне вікно FAQ -->
	<div
		class="modal fade"
		id="faqModal"
		tabindex="-1"
		role="dialog"
		aria-labelledby="faqModalTitle"
		aria-hidden="true"
	>
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="faqModalTitle">FAQ</h5>
					<button
						type="button"
						class="close"
						data-dismiss="modal"
						aria-label="Close"
					>
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<p><strong>1. Як користуватися CRM?</strong></p>
					<p>
						Наша CRM розроблена для зручності управління клієнтами,
						бронюванням та аналітикою в реальному часі.
					</p>
					<p><strong>2. Чи є підтримка клієнтів?</strong></p>
					<p>
						Так, наша підтримка клієнтів доступна 24/7 через телефон
						або електронну пошту.
					</p>
				</div>
			</div>
		</div>
	</div>
</template>
<style scoped>
html,
body {
	overflow: hidden;
}

.clients-table {
	display: flex;
	flex-direction: column;
	padding: 1rem;
	gap: 0.5rem;
}

main {
	flex: 1;
}

@media (max-width: 768px) {
	.clients-table {
		padding: 0.5rem;
	}
	.p-datatable {
		font-size: 0.875rem;
	}
}

.button-container {
	display: flex;
	justify-content: flex-end;
}

.button-container .p-button {
	width: auto;
}

label {
	margin: 0;
}
</style>
