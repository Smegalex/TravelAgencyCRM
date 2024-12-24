<script setup>
// Vue
import { ref, onMounted } from "vue";

// Router
import { useRouter } from "vue-router";

// Requests
import {
	fetchClient,
	deleteClient,
	updateClient,
} from "@/requests/clientsRequests";
import { fetchBookings_by_ClientID } from "@/requests/bookingsRequests";
import { fetchTrip } from "@/requests/tripsRequests";
import { fetchManager } from "@/requests/managersRequests";

// Yup
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

const router = useRouter();

const { id } = defineProps({
	id: {
		type: String,
		required: true,
	},
});

const client = ref({
	id: undefined,
	name: "Load",
	surname: null,
	email: "load@email",
});
const bookings = ref([]);
const editClient = ref(false);

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
			idclient: id,
			idmanager: booking["idmanager"],
			manager: manager,
			idtrip: booking["idtrip"],
			trip: trip,
			people_amount: booking["people_amount"],
		};
	}
};

const getClient = async () => {
	client.value = await fetchClient(id);
	await getBookings();
};

const removeClient = async () => {
	await deleteClient(id);
	router.push("/clients");
};

const saveChanges = async ({ valid }) => {
	// console.log(client.value);
	// console.log(valid);
	if (valid) {
		await updateClient(client.value);
		editClient.value = false;
	}
};

const changeBookings = (newBookings) => {
	bookings.value = newBookings;
}

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
						class="form-container flex flex-column gap-5 w-full p-3"
						:model="client"
						:resolver="clientFormResolver"
						:initial-values="client"
						@submit="saveChanges"
					>
						<span class="text-2xl font-bold">Client's record</span>
						<div
							class="inputs-container flex flex-column gap-3"
							key="name"
						>
							<div class="p-field flex flex-column">
								<label for="name" class="text-lg font-bold">
									Name:
								</label>
								<InputText
									name="name"
									v-model="client.name"
									placeholder="Client's name*"
									class="mb-0"
									:model-value="client.name"
									fluid
									:disabled="!editClient"
								/>
								<Message
									v-if="$form['name']?.invalid"
									severity="error"
									size="small"
									variant="simple"
									class="text-red-500"
								>
									{{ $form["name"]?.error?.message }}
								</Message>
							</div>
							<div class="p-field flex flex-column">
								<label for="surname" class="text-lg font-bold"
									>Surname:</label
								>
								<InputText
									name="surname"
									v-model="client.surname"
									placeholder="Client's surname"
									class="mb-0"
									fluid
									:disabled="!editClient"
								/>
							</div>
							<div class="p-field flex flex-column">
								<label for="surname" class="text-lg font-bold"
									>Email:</label
								>
								<InputText
									name="email"
									v-model="client.email"
									:model-value="client.email"
									placeholder="Client's email*"
									class="mb-0"
									fluid
									:disabled="!editClient"
								/>
								<Message
									v-if="$form['email']?.invalid"
									severity="error"
									size="small"
									variant="simple"
									class="text-red-500"
								>
									{{ $form["email"]?.error?.message }}
								</Message>
							</div>
						</div>
						<div
							class="buttons-container flex justify-content-around"
						>
							<Button
								pButton
								label="Edit"
								icon="pi pi-pencil"
								variant="outlined"
								class="p-mb-3"
								@click="editClient = true"
								v-if="!editClient"
							></Button>
							<Button
								pButton
								label="Delete"
								icon="pi pi-trash"
								severity="danger"
								class="p-mb-3"
								@click="removeClient()"
								v-if="!editClient"
							></Button>
							<Button
								pButton
								label="Save"
								icon="pi pi-save"
								class="p-mb-3"
								type="submit"
								v-if="editClient"
							></Button>
							<Button
								pButton
								label="Cancel"
								icon="pi pi-times"
								severity="secondary"
								class="p-mb-3"
								@click="editClient = !editClient"
								v-if="editClient"
							></Button>
						</div>
					</Form>
				</SplitterPanel>
				<SplitterPanel
					class="flex items-center justify-center"
					:size="75"
					:minSize="65"
				>
					<ClientViewTable :bookings="bookings" :change-bookings="changeBookings" :idclient="id"/>
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
