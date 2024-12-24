<script setup>
// Vue
import { ref, onMounted } from "vue";

// Router
import { useRouter, useRoute } from "vue-router";

// Requests
import { fetchClient } from "@/requests/clientsRequests";
import { fetchBookings_by_ClientID } from "@/requests/bookingsRequests";
import { fetchTrip } from "@/requests/tripsRequests";
import { fetchManager } from "@/requests/managersRequests";

// Yup
import * as yup from "yup";
import {yupResolver} from "@primevue/forms/resolvers/yup"

const { id } = defineProps({
	id: {
		type: String,
		required: true,
	},
});

const client = ref({
	id: undefined,
	name: "",
	surname: null,
	email: "",
});
const bookings = ref([]);


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

const getBookings = async () => {
	const bookingsRaw = await fetchBookings_by_ClientID(id);
	for (let i = 0; i < bookingsRaw.length; i++) {
		let booking = bookingsRaw[i];
		const manager = await fetchManager(booking["idmanager"]);
		const trip = await fetchTrip(booking["idtrip"]);
		bookings.value[i] = {
			id: booking["id"],
			manager: manager,
			trip: trip,
			people_amount: booking["people_amount"],
		};
	}
};

const getClient = async () => {
	client.value = await fetchClient(id);
	await getBookings();
};

onMounted(getClient);
</script>

<template>
	<div id="page-wrapper" class="h-screen overflow-y-scroll flex flex-column">
		<!-- Header -->
		<header>
			<CustomHeader />
		</header>
		<main>
			<Splitter class="h-full">
				<SplitterPanel
					class="flex items-center justify-center"
					:size="25"
					:minSize="25"
				>
					<Form
						v-slot="$form"
						class="form-container flex flex-column gap-3"
						:model="client"
						:resolver="clientFormResolver"
						:initial-values="client"
						@submit="callBack"
					>
					</Form>
					<div class="buttons-container">
						<Button
							pButton
							label="Edit"
							icon="pi pi-pencil"
							variant="outlined"
							class="p-mb-3"
							@click="editClient = true"
						></Button>
						<Button
							pButton
							label="Delete"
							icon="pi pi-trash"
							severity="danger"
							class="p-mb-3"
							@click="removeClient()"
						></Button>
					</div>
				</SplitterPanel>
				<SplitterPanel
					class="flex items-center justify-center"
					:size="75"
					:minSize="65"
				>
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
								<span class="text-xl font-bold"
									>Client's bookings</span
								>
								<Button
									icon="pi pi-refresh"
									severity="secondary"
									rounded
									raised
									@click="getBookings"
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
										data.manager.name +
										' ' +
										data.manager.surname
									"
									variant="link"
									as="router-link"
									:to="'/managers/' + data.manager.id"
								/>
							</template>
						</Column>
						<Column
							field="trip"
							header="Trip"
							:sortable="true"
							style="width: 40%"
						>
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

main {
	flex: 1;
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
