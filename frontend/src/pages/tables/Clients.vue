<script setup>
// Vue
import { ref, onMounted } from "vue";
import { useConfirm, useToast } from "primevue";

// Components
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";

// Yup
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

// Requests
import {
	fetchClients,
	addClient,
	updateClient,
	deleteClient,
} from "@/requests/clientsRequests";

const clients = ref([]);
const confirm = useConfirm();
const toast = useToast();

const getClients = async () => {
	try {
		clients.value = await fetchClients();
	} catch (error) {
		toast.add({
			severity: "error",
			summary: "Error",
			detail: error,
			life: 2000,
		});
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

const createClient = async ({ valid }) => {
	if (valid) {
		try {
			const addedClient = await addClient(newClient.value);
			clients.value.push(addedClient); // Add new student to local list
			newClient.value = { name: "", surname: null, email: "" }; // Reset form fields
			showCreateClientForm.value = false;
			toast.add({
				severity: "success",
				summary: "Successful",
				detail: "Record created.",
				life: 2000,
			});
		} catch (error) {
			toast.add({
				severity: "error",
				summary: "Error",
				detail: error,
				life: 2000,
			});
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

const editClientTrigger = async (id) => {
	try {
		currentClient.value = clients.value.find((client) => client.id === id);
		showEditClientForm.value = true;
		// console.log(currentClient.value);
	} catch (error) {
		toast.add({
			severity: "error",
			summary: "Error",
			detail: error,
			life: 2000,
		});
	}
};

const editClient = async ({ valid }) => {
	if (valid) {
		try {
			const editedClient = await updateClient(currentClient.value);
			clients.value = clients.value.map((client) =>
				client.id == editedClient.id ? editedClient : client
			);
			showEditClientForm.value = false;
			toast.add({
				severity: "success",
				summary: "Successful",
				detail: "Record edited.",
				life: 2000,
			});
		} catch (error){
			toast.add({
				severity: "error",
				summary: "Error",
				detail: error,
				life: 2000,
			});
		}
	}
};

const removeClient = async (id) => {
	confirm.require({
		message: "Are you sure you want to delete this record?",
		header: "Delete",
		icon: "pi pi-exclamation-circle",
		rejectLabel: "Cancel",
		rejectProps: {
			label: "Cancel",
			severity: "secondary",
			outlined: true,
		},
		acceptProps: {
			label: "Delete",
			severity: "danger",
		},
		accept: async () => {
			try {
				await deleteClient(id);
				clients.value = clients.value.filter(
					(client) => client.id !== id
				); // Update local list
				toast.add({
					severity: "info",
					summary: "Successful",
					detail: "Record deleted",
					life: 2000,
				});
			} catch (error) {
				toast.add({
					severity: "error",
					summary: "Error",
					detail: error,
					life: 2000,
				});
				}
		},
	});
};

onMounted(() => {
	getClients();
});
</script>
<template>
	<div id="page-wrapper" class="h-screen overflow-y-scroll flex flex-column">
		<ConfirmDialog></ConfirmDialog>
		<Toast />
		<!-- Header -->
		<header>
			<CustomHeader active-page="clients" />
		</header>
		<main>
			<div class="clients-table">
				<DataTable
					:value="clients"
					:rows="5"
					paginator
					paginatorPosition="bottom"
					class="p-datatable-gridlines"
					striped-rows
					:rowsPerPageOptions="[5, 10, 20]"
				>
					<template #header>
						<div
							class="flex flex-wrap items-center justify-content-between gap-2"
						>
							<span class="text-3xl font-bold">
								Clients table
							</span>
							<Button
								pButton
								label="Add New Client"
								icon="pi pi-plus"
								class="p-mb-3"
								@click="showCreateClientForm = true"
							/>
						</div>
					</template>
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
								rounded
								variant="text"
								title="Edit"
								@click="editClientTrigger(data.id)"
							></Button>
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

	<!--TODO - login-->
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
