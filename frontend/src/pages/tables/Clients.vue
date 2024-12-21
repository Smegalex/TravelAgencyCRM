<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";
import { ref, onMounted } from "vue";
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

const clients = ref([]);

const fetchClients = async () => {
	try {
		const response = await fetch("http://127.0.0.1:5000/clients");
		clients.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		// console.log(clients.value);
	} catch (error) {
		console.error("Error fetching clients:", error);
	}
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

const addClient = async ({ valid }) => {
	if (valid) {
		try {
			const response = await fetch("http://127.0.0.1:5000/clients", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(newClient.value), // Directly use validated form values
			});
			const addedClient = await response.json();
			clients.value.push(addedClient); // Add new student to local list
			newClient.value = { name: "", surname: null, email: "" }; // Reset form fields
			showCreateClientForm.value = false;
		} catch (error) {
			console.error("Error adding trip:", error);
		}
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

const fetchClient = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/clients/${id}`);
		currentClient.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		currentClient.value = currentClient.value[0];
		console.log(currentClient.value);
	} catch (error) {
		console.error(`Error fetching client (id: ${id}):`, error);
	}
};

const editClientTrigger = async (id) => {
	await fetchClient(id);
	showEditClientForm.value = true;
	console.log(currentClient.value);
};

const editClient = async ({ valid }) => {
	if (valid) {
		try {
			const id = currentClient.value["id"];
			const response = await fetch(
				`http://127.0.0.1:5000/clients/${id}`,
				{
					method: "PUT",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(currentClient.value), // Directly use validated form values
				}
			);
			const editedClient = (await response.json())[0];

			clients.value = clients.value.map((client) =>
				client.id == editedClient.id ? editedClient : client
			);
			showEditClientForm.value = false;
		} catch (error) {
			console.error("Error adding trip:", error);
		}
	}
};

const deleteClient = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/clients/${id}`, {
			method: "DELETE",
		});
		clients.value = clients.value.filter((client) => client.id !== id); // Update local list
	} catch (error) {
		console.error("Error deleting client:", error);
	}
};

onMounted(() => {
	fetchClients();
});
</script>
<template>
	<div id="page-wrapper" style="overflow-y: scroll; height: 100vh">
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
						class="p-button-primary p-mb-3"
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
								icon="pi pi-pencil"
								class="p-button-text p-button-rounded"
								title="Edit"
								@click="editClientTrigger(data.id)"
							></Button>
							<Button
								pButton
								icon="pi pi-calendar-plus"
								class="p-button-text p-button-rounded"
								title="Add Booking"
								@click="addBooking(data)"
							></Button>
							<Button
								pButton
								icon="pi pi-trash"
								class="p-button-text p-button-rounded"
								title="Delete"
								@click="deleteClient(data.id)"
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
			:call-back="addClient"
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
#page-wrapper {
	display: flex;
	flex-direction: column;
	min-height: 100vh;
}

main {
	flex: 1;
}

footer {
	margin-top: auto;
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
