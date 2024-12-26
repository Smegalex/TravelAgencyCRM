<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
import UniversalModal from "../modals/UniversalModal.vue";
import { ref, onMounted } from "vue";
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";
import { fetchPlace, fetchPlaces } from "@/requests/placesRequests";
import {
	fetchTrips,
	fetchTrip,
	addTrip,
	updateTrip,
} from "@/requests/tripsRequests";
import { icon } from "@fortawesome/fontawesome-svg-core";

const trips = ref([]);
const places = ref([]);
const seasonsSelect = [
	{ name: "Winter", number: 1 },
	{ name: "Spring", number: 2 },
	{ name: "Summer", number: 3 },
	{ name: "Autumn", number: 4 },
];

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

const getTrips = async () => {
	const tripsRaw = await fetchTrips();
	for (let i = 0; i < tripsRaw.length; i++) {
		let trip = tripsRaw[i];
		const place = await fetchPlace(trip["idplace"]);
		trip["place"] = place;
		trips.value.push(trip);
	}
};

// create new trip
const showCreateTripForm = ref(false);
const newTrip = ref({ name: "", idplace: "", season: "" });
const tripFormFields = [
	{
		name: "name",
		placeholder: "Trip's name*",
		props: "",
		type: "",
	},
	{
		name: "idplace",
		placeholder: "Place of trip*",
		props: {
			optionLabel: (place) => {
				return place.name;
			},
			optionValue: "id",
		},
		type: "select",
	},
	{
		name: "season",
		placeholder: "Season of trip*",
		props: {
			optionLabel: (season) => {
				return season.name;
			},
			optionValue: "number",
		},
		type: "select",
		optionValue: "id",
	},
];

const tripFormSelectOptions = ref({});

const createTrip = async ({ valid }) => {
	if (valid) {
		let addedTrip = await addTrip(newTrip.value);
		const place = await fetchPlace(addedTrip["idplace"]);
		addedTrip["place"] = place;
		trips.value.push(addedTrip); // Add new student to local list
		newTrip.value = { name: "", idplace: "", place: null, season: "" }; // Reset form fields
		showCreateTripForm.value = false;
	}
};

const changeCreateFormVisibility = () => {
	showCreateTripForm.value = !showCreateTripForm.value;
};

// edit trip
const currentTrip = ref([]);
const showEditTripForm = ref(false);

const changeEditFormVisibility = () => {
	showEditTripForm.value = !showEditTripForm.value;
};

const editTripTrigger = async (id) => {
	currentTrip.value = await fetchTrip(id);
	showEditTripForm.value = true;
	// console.log(currentTrip.value);
};

const editTrip = async ({ valid }) => {
	if (valid) {
		let editedTrip = updateTrip(currentTrip);

		const place = await fetchPlace(editedTrip["idplace"]);
		editedTrip["place"] = place;

		trips.value = trips.value.map((trip) =>
			trip.id == editedTrip.id ? editedTrip : trip
		);
		showEditTripForm.value = false;
	}
};

const deleteTrip = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/trips/${id}`, {
			method: "DELETE",
		});
		trips.value = trips.value.filter((trip) => trip.id !== id); // Update local list
	} catch (error) {
		console.error(`Error deleting trip (id: ${id}):`, error);
	}
};

const seasonIconSelector = (season) => {
	switch (season) {
		case 1:
			return "fa-regular fa-snowflake";
		case 2:
			return "fa-solid fa-seedling";
		case 3:
			return "fa-regular fa-sun";
		case 4:
			return "fa-brands fa-canadian-maple-leaf";
	}
};

const seasonClassSelector = (season) => {
	switch (season) {
		case 1:
			return "text-blue-400";
		case 2:
			return "text-green-500";
		case 3:
			return "text-yellow-500";
		case 4:
			return "text-orange-600";
	}
};

const initialise = async () => {
	await getTrips();
	places.value = await fetchPlaces();
	tripFormSelectOptions.value = {
		idplace: places.value,
		season: seasonsSelect,
	};
};

onMounted(() => {
	initialise();
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
				<DataTable
					:value="trips"
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
						<span class="text-3xl font-bold">Trips table</span>
							<Button
								pButton
								label="Add New Trip"
								icon="pi pi-plus"
								class="p-mb-3"
								@click="showCreateTripForm = true"
							/>
						</div>
					</template>
					<Column
						field="id"
						header="ID"
						:sortable="true"
						style="width: 11%"
					></Column>
					<Column
						field="name"
						header="Name"
						:sortable="true"
						style="width: 31%"
					></Column>
					<Column
						field="place"
						header="Place"
						:sortable="true"
						style="width: 31%"
						><template #body="{ data }">
							<span>{{ data.place.name }}</span>
						</template></Column
					>
					<Column
						field="season"
						header="Season"
						:sortable="true"
						style="width: 11%"
						class="text-center"
					>
						<template #body="{ data }">
							<font-awesome-icon
								:icon="seasonIconSelector(data.season)"
								icon="fa-regular fa-snowflake"
								class="text-2xl"
								:class="seasonClassSelector(data.season)"
							/>
						</template>
					</Column>

					<Column header="Actions" style="width: 16%">
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
								icon="pi pi-external-link"
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
			:fields="tripFormFields"
			:form-resolver="tripFormResolver"
			:data="newTrip"
			:call-back="createTrip"
			:options="tripFormSelectOptions"
			submit-label="Create"
		/>
		<UniversalModal
			header="Edit trip"
			:show-form="showEditTripForm"
			@change-visibility="changeEditFormVisibility"
			:fields="tripFormFields"
			:form-resolver="tripFormResolver"
			:data="currentTrip"
			:call-back="editTrip"
			:options="tripFormSelectOptions"
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
