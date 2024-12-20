<script>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import Button from "primevue/button";
import { Form } from "@primevue/forms";
import { ref, onMounted } from "vue";
import * as Yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

export default {
	name: "ClientsTable",
	setup() {
		const clients = ref([]);
		const showCreateClientForm = ref(false);
		const newClient = ref({ name: "", surname: null, email: "" });
		// const createCustomerFormRules = {
		// 	name: required(),
		// 	email: [required(), email()],
		// };
		const createClientFormErrors = ref({
			name: null,
			email: null,
		});

		const createClientFormSchema = Yup.object().shape({
			name: Yup.string().required("Name is required."),
			surname: Yup.string(),
			email: Yup.string()
				.email("Invalid email format")
				.required("Email is required."),
		});

		const fetchClients = async () => {
			try {
				const response = await fetch("http://127.0.0.1:5000/clients");
				clients.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
				console.log(clients.value);
			} catch (error) {
				console.error("Error fetching clients:", error);
			}
		};
		const deleteClient = async (id) => {
			try {
				await fetch(`http://127.0.0.1:5000/clients/${id}`, {
					method: "DELETE",
				});
				clients.value = clients.value.filter(
					(client) => client.id !== id
				); // Update local list
			} catch (error) {
				console.error("Error deleting client:", error);
			}
		};

		const addClient = async () => {
			try {
				const response = await fetch("http://127.0.0.1:5000/clients", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(newClient.value),
				});
				const addedClient = await response.json();
				clients.value.push(addedClient); // Add new student to local list
				newClient.value = { name: "", surname: null, email: "" }; // Reset form fields
				showCreateClientForm.value = false;
			} catch (error) {
				console.error("Error adding trip:", error);
			}
		};
		onMounted(() => {
			fetchClients();
		});

		return {
			clients,
			deleteClient,
			showCreateClientForm,
			newClient,
			addClient,
			createClientFormErrors,
			createClientFormRules,
		};
	},
};
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
								@click="editClient(data)"
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
		<Dialog
			v-model:visible="showCreateClientForm"
			header="Create New Client"
			:closable="true"
			:modal="true"
			:style="{ width: '450px' }"
		>
			<Form
				v-slot="$form"
				class="form-container flex flex-column gap-3"
				:model="newClient"
				:resolver="createClientFormRules"
				@submit="addClient"
			>
				<!-- Form to Create Client -->
				<div
					class="p-field flex justify-content-between align-items-center"
				>
					<InputText
						id="name"
						v-model="newClient.name"
						placeholder="Client's name"
					/>
					<Message
						v-if="$form.name?.invalid"
						severity="error"
						size="small"
						>{{ $form.name.error.message }}
					</Message>
				</div>

				<div
					class="p-field flex justify-content-between align-items-center"
				>
					<InputText
						id="surname"
						v-model="newClient.surname"
						placeholder="Client's surname"
					/>
				</div>

				<div
					class="p-field flex justify-content-between align-items-center"
				>
					<InputText
						id="email"
						v-model="newClient.email"
						placeholder="Client's email"
						:class="{ 'p-invalid': createClientFormErrors.name }"
					/>
					<Message
						v-if="$form.email?.invalid"
						severity="error"
						size="small"
					>
						{{ $form.email.error.message }}
					</Message>
				</div>

				<Button label="Create" class="p-button-primary" type="submit" />
			</Form>
		</Dialog>
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
