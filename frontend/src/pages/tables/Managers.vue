<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";
import { ref, onMounted } from "vue";
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

const managers = ref([]);

const fetchmanagers = async () => {
	try {
		const response = await fetch("http://127.0.0.1:5000/managers");
		managers.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		// console.log(managers.value);
	} catch (error) {
		console.error("Error fetching managers:", error);
	}
};

const managerFormResolver = ref(
	yupResolver(
		yup.object().shape({
			name: yup
				.string()
				.required("Name is required.")
				.max(255, "Name too long."),
			surname: yup.string().max(255, "Surname too long."),
			email: yup
				.string()
				.email("Invalid email format")
				.required("Email is required.")
				.max(50, "Email too long. Contact IT."),
			adminRights: yup.bool(),
			password: yup
				.string()
				.required("Password is required.")
				.max(255, "Password too long."),
		})
	)
);

// create new manager
const showCreateManagerForm = ref(false);
const newManager = ref({
	name: "",
	surname: "",
	email: "",
	adminRights: false,
	password: "",
});
const managerFormFields = [
	{
		name: "name",
		placeholder: "Manager's name*",
		props: "",
		type: "",
	},
	{
		name: "surname",
		placeholder: "Manager's surname",
		props: "",
		type: "",
	},
	{
		name: "email",
		placeholder: "Manager's email*",
		props: "",
		type: "",
	},
	{
		name: "adminRights",
		placeholder: "Admin rights",
		props: "",
		type: "checkbox", // змінили тип на checkbox
	},
	{
		name: "password",
		placeholder: "Manager's password*",
		props: "",
		type: "",
	},
];

const addManager = async ({ valid }) => {
	if (valid) {
		try {
			const response = await fetch("http://localhost:5000/managers", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(newManager.value), // Directly use validated form values
			});
			const addedManager = await response.json();
			managers.value.push(addedManager); // Add new student to local list
			newManager.value = {
				name: "",
				surname: "",
				email: "",
				adminRights: false,
				password: "",
			}; // Reset form fields
			showCreateManagerForm.value = false;
		} catch (error) {
			console.error("Error adding manager:", error);
		}
	}
};

const changeCreateFormVisibility = () => {
	showCreateManagerForm.value = !showCreateManagerForm.value;
};

// edit manager
const currentManager = ref([]);
const showEditManagerForm = ref(false);


const changeEditFormVisibility = () => {
	showEditManagerForm.value = !showEditManagerForm.value;
};

const fetchManager = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/managers/${id}`);
		currentManager.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		currentManager.value = currentManager.value[0];
		console.log(currentManager.value);
	} catch (error) {
		console.error(`Error fetching manager (id: ${id}):`, error);
	}
};

const editManagerTrigger = async (id) => {
	await fetchManager(id);
	showEditManagerForm.value = true;
	console.log(currentManager.value);
};

const editManager = async ({ valid }) => {
	if (valid) {
		try {
			const id = currentManager.value["id"];
			const response = await fetch(
				`http://127.0.0.1:5000/managers/${id}`,
				{
					method: "PUT",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(currentManager.value), // Directly use validated form values
				}
			);
			const editedManager = (await response.json())[0];

			managers.value = managers.value.map((manager) =>
				manager.id == editedManager.id ? editedManager : manager
			);
			showEditManagerForm.value = false;
		} catch (error) {
			console.error("Error adding manager:", error);
		}
	}
};

const deleteManager = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/managers/${id}`, {
			method: "DELETE",
		});
		managers.value = managers.value.filter((manager) => manager.id !== id); // Update local list
	} catch (error) {
		console.error("Error deleting manager:", error);
	}
};

onMounted(() => {
	fetchmanagers();
});
</script>
<
<template>
	<div id="page-wrapper" style="overflow-y: scroll; height: 100vh">
		<!-- Header -->
		<header>
			<CustomHeader active-page="managers" />
		</header>
		<main>
			<div class="managers-table">
				<div class="button-container"></div>
				<DataTable
					:value="managers"
					:rows="5"
					paginator
					paginatorPosition="bottom"
					class="p-datatable-gridlines"
					:rowsPerPageOptions="[5, 10, 20]"
					><template #header>
						<div
							class="flex flex-wrap items-center justify-content-between gap-2"
						>
							<span class="text-3xl font-bold">
								Managers table
							</span>
							<Button
								pButton
								label="Add New Manager"
								icon="pi pi-plus"
								class="p-button-primary p-mb-3"
								@click="showCreateManagerForm = true"
							/>
						</div>
					</template>
					<Column
						field="id"
						header="ID"
						:sortable="true"
						style="width: 5%"
					></Column>
					<Column
						field="name"
						header="Name"
						:sortable="true"
						style="width: 15%"
					></Column>
					<Column
						field="surname"
						header="Place ID"
						:sortable="true"
						style="width: 15%"
					></Column>
					<Column
						field="email"
						header="Email"
						:sortable="true"
						style="width: 28%"
					></Column>
					<!-- Замінили текстове поле на чекбокс -->
					<Column
						class="text-center"
						field="adminRights"
						header="Admin rights"
						:sortable="true"
						style="width: 5%"
					>
						<template #body="{ data }">
							<span
								:class="
									data.adminRights
										? 'pi pi-check text-success'
										: 'pi pi-times text-danger'
								"
								class="p-mr-2 text-3xl font-bold"
							></span>
						</template>
					</Column>
					<Column
						field="password"
						header="Password"
						:sortable="true"
						style="width: 15%"
					></Column>

					<Column header="Actions" style="width: 17%" class="text-center">
						<template #body="{ data }">
							<Button
								pButton
								icon="pi pi-pencil"
								class="p-button-text p-button-rounded"
								title="Edit"
								@click="editManagerTrigger(data.id)"
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
								severity="danger"
								@click="deleteManager(data.id)"
							></Button>
						</template>
					</Column>
				</DataTable>
			</div>
		</main>
		<UniversalModal
			header="Create new manager"
			:show-form="showCreateManagerForm"
			@change-visibility="changeCreateFormVisibility"
			:fields="managerFormFields"
			:form-resolver="managerFormResolver"
			:data="newManager"
			:call-back="addManager"
			submit-label="Create"
		/>
		<UniversalModal
			header="Edit manager"
			:show-form="showEditManagerForm"
			@change-visibility="changeEditFormVisibility"
			:fields="managerFormFields"
			:form-resolver="managerFormResolver"
			:data="currentManager"
			:call-back="editManager"
			submit-label="Save"
		/>
		<CustomFooter />
	</div>
	<!-- TODO: login -->
</template>
<style scoped>
html,
body {
	overflow: hidden;
}

.managers-table {
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
	.managers-table {
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
