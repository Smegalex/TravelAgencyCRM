<script setup>
// Vue
import { ref, onMounted } from "vue";

// Primeflex
import { useToast, useConfirm } from "primevue";

// Yup
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

// Requests
import { fetchManagers, fetchManager } from "@/requests/managersRequests";
import { fetchTrips, fetchTrip } from "@/requests/tripsRequests";
import {
	addBooking,
	updateBooking,
	deleteBooking,
} from "@/requests/bookingsRequests";

import { useMainStore } from "@/stores/mainStore";

const store = useMainStore();
const confirm = useConfirm();
const toast = useToast();
const currentManagerId = store.getId;

const { bookings, changeBookings, idclient } = defineProps({
	bookings: {
		type: Array,
		required: true,
	},
	changeBookings: {
		type: Function,
		required: true,
	},
	idclient: {
		type: String,
		required: true,
	},
});

const bookingFormResolver = ref(
	yupResolver(
		yup.object().shape({
			idmanager: yup.number().max(9999).required("Choose manager."),
			idtrip: yup.number().max(9999).required("Choose trip."),
			people_amount: yup
				.number()
				.typeError("Please, enter numerical amount.")
				.max(
					999,
					"Too many peple, special arrangements have to be made."
				)
				.required("Enter how many people will go on this trip."),
		})
	)
);

const managers = ref([]);
const trips = ref([]);

const seasons = ["Winter", "Spring", "Summer", "Autumn"];

// create new client
const showCreateBookingForm = ref(false);
const newBooking = ref({
	idclient: idclient,
	idmanager: currentManagerId || null,
	idtrip: null,
	people_amount: 1,
});
const bookingFormFields = [
	{
		name: "idmanager",
		placeholder: "Manager who made the booking*",
		props: {
			optionLabel: (manager) => {
				let result = manager.name;
				manager.surname != null
					? (result += " " + manager.surname)
					: "";
				return result;
			},
			optionValue: "id",
		},
		type: "select",
	},
	{
		name: "idtrip",
		placeholder: "Trip the booking is for*",
		props: {
			optionLabel: (trip) => {
				let result = trip.name;
				seasons[trip.season] != undefined
					? (result += " " + seasons[trip.season])
					: "";
				return result;
			},
			optionValue: "id",
		},
		type: "select",
	},
	{
		name: "people_amount",
		placeholder: "Amount of people in a booking*",
		props: "",
		type: "",
	},
];

const bookingFormSelectOptions = ref({});

const createBooking = async ({ valid }) => {
	if (valid) {
		try {
			let addedBooking = await addBooking(newBooking.value);
			const manager = await fetchManager(addedBooking["idmanager"]);
			const trip = await fetchTrip(addedBooking["idtrip"]);
			addedBooking = {
				id: addedBooking["id"],
				idclient: idclient,
				idmanager: addedBooking["idmanager"],
				manager: manager,
				idtrip: addedBooking["idtrip"],
				trip: trip,
				people_amount: addedBooking["people_amount"],
			};
			bookings.push(addedBooking); // Add new student to local list
			newBooking.value = {
				idclient: idclient,
				idmanager: currentManagerId.value || null,
				idtrip: null,
				people_amount: 1,
			}; // Reset form fields
			showCreateBookingForm.value = false;
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
	showCreateBookingForm.value = !showCreateBookingForm.value;
};

// edit client
const currentBooking = ref([]);
const showEditBookingForm = ref(false);

const changeEditFormVisibility = () => {
	showEditBookingForm.value = !showEditBookingForm.value;
};

const editBookingTrigger = async (id) => {
	currentBooking.value = bookings.find((booking) => booking.id === id);

	showEditBookingForm.value = true;
	// console.log(currentClient.value);
};

const editBooking = async ({ valid }) => {
	if (valid) {
		try {
			let editedBooking = await updateBooking(currentBooking.value);
			const manager = await fetchManager(editedBooking["idmanager"]);
			const trip = await fetchTrip(editedBooking["idtrip"]);
			editedBooking = {
				id: editedBooking["id"],
				idclient: idclient,
				idmanager: editedBooking["idmanager"],
				manager: manager,
				idtrip: editedBooking["idtrip"],
				trip: trip,
				people_amount: editedBooking["people_amount"],
			};
			changeBookings(
				bookings.map((booking) =>
					booking.id == editedBooking.id ? editedBooking : booking
				)
			);
			showEditBookingForm.value = false;
			toast.add({
				severity: "success",
				summary: "Successful",
				detail: "Record edited.",
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

const removeBooking = async (id) => {
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
				await deleteBooking(id);
				changeBookings(bookings.filter((booking) => booking.id !== id)); // Update local list
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

const initialize = async () => {
	try {
		managers.value = await fetchManagers();
		trips.value = await fetchTrips();
		bookingFormSelectOptions.value = {
			idmanager: managers.value,
			idtrip: trips.value,
		};
		// console.log(bookingFormSelectOptions);
	} catch (error) {
		toast.add({
			severity: "error",
			summary: "Error",
			detail: error,
			life: 2000,
		});
	}
};

onMounted(initialize);
</script>

<template>
	<DataTable
		:value="bookings"
		:rows="5"
		paginator
		paginatorPosition="bottom"
		class="p-datatable-gridlines w-full h-full"
		striped-rows
		:rowsPerPageOptions="[5, 10, 20]"
	>
		<template #header>
			<div
				class="flex flex-wrap items-center justify-content-between gap-2"
			>
				<span class="text-xl font-bold">Client's bookings</span>
				<Button
					pButton
					label="Add New Booking"
					icon="pi pi-plus"
					class="p-mb-3"
					@click="showCreateBookingForm = true"
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
			field="manager"
			header="Manager"
			:sortable="true"
			style="width: 25%"
		>
			<template #body="{ data }">
				<Button
					:label="
						data.manager.name + ' ' + (data.manager.surname || '')
					"
					variant="link"
					as="router-link"
					:to="'/managers/' + data.manager.id"
				/>
			</template>
		</Column>
		<Column field="trip" header="Trip" :sortable="true" style="width: 40%">
			<template #body="{ data }">
				<Button
					:label="data.trip.name"
					variant="link"
					as="router-link"
					:to="'/trips/' + data.trip.id"
				/>
			</template>
		</Column>
		<Column
			field="people_amount"
			header="People"
			:sortable="true"
			style="width: 10%"
		>
		</Column>

		<Column header="Actions" style="width: 15%">
			<template #body="{ data }">
				<Button
					pButton
					icon="pi pi-pencil"
					class="p-button-text p-button-rounded"
					title="Edit"
					@click="editBookingTrigger(data.id)"
				></Button>
				<Button
					pButton
					icon="pi pi-trash"
					severity="danger"
					rounded
					variant="text"
					title="Delete"
					@click="removeBooking(data.id)"
				></Button>
			</template>
		</Column>
	</DataTable>
	<UniversalModal
		header="Create new booking"
		:show-form="showCreateBookingForm"
		@change-visibility="changeCreateFormVisibility"
		:fields="bookingFormFields"
		:form-resolver="bookingFormResolver"
		:data="newBooking"
		:call-back="createBooking"
		submit-label="Create"
		:options="bookingFormSelectOptions"
	/>
	<UniversalModal
		header="Edit booking"
		:show-form="showEditBookingForm"
		@change-visibility="changeEditFormVisibility"
		:fields="bookingFormFields"
		:form-resolver="bookingFormResolver"
		:data="currentBooking"
		:call-back="editBooking"
		submit-label="Save"
		:options="bookingFormSelectOptions"
	/>
</template>
