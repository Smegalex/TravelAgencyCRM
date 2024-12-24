<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";
import { ref, onMounted } from "vue";
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

const trips = ref([]);

const fetchtrips = async () => {
	try {
		const response = await fetch("http://127.0.0.1:5000/trips");
		trips.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		// console.log(trips.value);
	} catch (error) {
		console.error("Error fetching trips:", error);
	}
};

const tripFormResolver = ref(
	yupResolver(
		yup.object().shape({
			name: yup
				  .string()
				  .required("Name is required.")
				  .max(255, "Name too long."),
			idplace: yup
          .number()
				  .integer("Place ID must be an integer.")
          .positive("Place ID must be a positive number.")
          .required("Place ID is required."),
			season: yup
          .number()
          .integer("Season must be an integer.")
          .min(1, "Season must be between 1 and 4.")
				  .max(4, "Season must be between 1 and 4.")
				  .required("Season is required."),
		})
	)
);

// create new trip
const showCreateTripForm = ref(false);
const newTrip = ref({ name: "", idplace: "", season: "" });
const createTripFormFields = [
	{
		name: "name",
		placeholder: "Trip's name*",
		props: "",
		type: "",
	},
	{
		name: "idplace",
		placeholder: "Trip's idplace",
		props: "",
		type: "",
	},
	{
		name: "season",
		placeholder: "Trip's season*",
		props: "",
		type: "",
	},
];

const addTrip = async ({ valid }) => {
	if (valid) {
		try {
			const response = await fetch("http://localhost:5000/trips", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(newTrip.value), // Directly use validated form values
			});
			const addedTrip = await response.json();
			trips.value.push(addedTrip); // Add new student to local list
			newTrip.value = { name: "", idplace: "", season: "" }; // Reset form fields
			showCreateTripForm.value = false;
		} catch (error) {
			console.error("Error adding trip:", error);
		}
	}
};

const changeCreateFormVisibility = () => {
	showCreateTripForm.value = !showCreateTripForm.value;
};

// edit trip
const currentTrip = ref([]);
const showEditTripForm = ref(false);

const editTripFormFields = [
	{
		name: "name",
		placeholder: "Trip's name*",
		props: "",
		type: "",
	},
	{
		name: "idplace",
		placeholder: "Trip's idplace",
		props: "",
		type: "",
	},
	{
		name: "season",
		placeholder: "Trip's season*",
		props: "",
		type: "",
	},
];

const changeEditFormVisibility = () => {
	showEditTripForm.value = !showEditTripForm.value;
};

const fetchTrip = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/trips/${id}`);
		currentTrip.value = await response.json(); // Зберігаємо відповідь у реактивну змінну
		currentTrip.value = currentTrip.value[0];
		console.log(currentTrip.value);
	} catch (error) {
		console.error(`Error fetching trip (id: ${id}):`, error);
	}
};

const editTripTrigger = async (id) => {
	await fetchTrip(id);
	showEditTripForm.value = true;
	console.log(currentTrip.value);
};

const editTrip = async ({ valid }) => {
	if (valid) {
		try {
			const id = currentTrip.value["id"];
			const response = await fetch(
				`http://127.0.0.1:5000/trips/${id}`,
				{
					method: "PUT",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify(currentTrip.value), // Directly use validated form values
				}
			);
			const editedTrip = (await response.json())[0];

			trips.value = trips.value.map((trip) =>
				trip.id == editedTrip.id ? editedTrip : trip
			);
			showEditTripForm.value = false;
		} catch (error) {
			console.error("Error adding trip:", error);
		}
	}
};

const deleteTrip = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/trips/${id}`, {
			method: "DELETE",
		});
		trips.value = trips.value.filter((trip) => trip.id !== id); // Update local list
	} catch (error) {
		console.error("Error deleting trip:", error);
	}
};

onMounted(() => {
	fetchtrips();
});
</script>
<template>
	<div id="page-wrapper" class="h-screen overflow-y-scroll flex flex-column">
		<!-- Header -->
		<header>
			<CustomHeader active-page="trips" />
		</header>
		<main>
			<div class="trips-table">
				<div class="button-container">
					<Button
						pButton
						label="Add New Trip"
						icon="pi pi-plus"
						class="p-mb-3"
						@click="showCreateTripForm = true"
					></Button>
				</div>
				<DataTable
					:value="trips"
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
						field="idplace"
						header="Place ID"
						:sortable="true"
						style="width: 20%"
					></Column>
					<Column
						field="season"
						header="Season"
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
								@click="editTripTrigger(data.id)"
							></Button>
							<Button
								pButton
								icon="pi pi-calendar-plus"
								rounded
								variant="text"
								title="Add Booking"
								@click="addBooking(data)"
							></Button>
							<Button
								pButton
								icon="pi pi-trash"
								severity="danger"
								rounded
								variant="text"
								title="Delete"
								@click="deleteTrip(data.id)"
							></Button>
						</template>
					</Column>
				</DataTable>
			</div>
		</main>
		<UniversalModal
			header="Create new trip"
			:show-form="showCreateTripForm"
			@change-visibility="changeCreateFormVisibility"
			:fields="createTripFormFields"
			:form-resolver="tripFormResolver"
			:data="newTrip"
			:call-back="addTrip"
			submit-label="Create"
		/>
		<UniversalModal
			header="Edit trip"
			:show-form="showEditTripForm"
			@change-visibility="changeEditFormVisibility"
			:fields="editTripFormFields"
			:form-resolver="tripFormResolver"
			:data="currentTrip"
			:call-back="editTrip"
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

.trips-table {
	display: flex;
	flex-direction: column;
	padding: 1rem;
	gap: 0.5rem;
}

main {
	flex: 1;
}

footer {
	margin-top: auto;
}

@media (max-width: 768px) {
	.trips-table {
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
