<script setup>
import { ref } from "vue";
import { fetchAdminRights, fetchUsername, fetchUserId, login } from "@/requests/sessionRequests";
import { useRouter } from "vue-router";
import { useMainStore } from "@/stores/mainStore";
import { useToast } from "primevue/usetoast";

// Yup
import * as yup from "yup";
import { yupResolver } from "@primevue/forms/resolvers/yup";

const router = useRouter();
const store = useMainStore();
const toast = useToast();
const loginCredentials = ref({ email: "", password: "" });

const errorMessage = ref(null);

const resolver = yupResolver(
	yup.object().shape({
		email: yup
			.string()
			.email("Invalid email format.")
			.required("Email is required."),
		password: yup.string().required("Password is required."),
	})
);

const showError = () => {
	toast.add({ severity: 'error', summary: 'Error', detail: errorMessage.value, life: 3000 });
};

const handleLogin = async () => {
	// console.log(email.value);
	try {
		const response = await login(loginCredentials.value);

		if (!response.ok) {
			throw new Error("Invalid credentials");
		}

		const data = await response.json();
		// console.log(data);
		store.setUser(await fetchUsername());
		store.setRights(await fetchAdminRights());
		store.setId(await fetchUserId());
		router.push("/"); // Перехід на головну сторінку
	} catch (error) {
		errorMessage.value = error.message;
		showError();
	}
};
</script>

<template>
	<div id="page-wrapper">
		<Toast />
		<header>
			<CustomHeader active-page="login" />
		</header>
		<main class="flex flex-1 justify-content-center align-items-center">
			<Card class="surface-900 w-25rem">
				<template #title>
					<div class="w-full text-center text-white">Login</div>
				</template>
				<template #content>
					<Form
						v-slot="$form"
						@submit="handleLogin"
						:resolver="resolver"
						:model="loginCredentials"
						class="flex flex-column gap-3"
					>
						<div class="p-field flex flex-column">
							<FloatLabel variant="on">
								<InputText
									name="email"
									id="email"
									v-model="loginCredentials.email"
									class="mb-0"
									fluid
								/>
								<label for="email">Email*</label>
							</FloatLabel>
							<Message
								v-if="$form.email?.invalid"
								severity="error"
								size="small"
								variant="simple"
								class="text-red-500"
							>
								{{ $form.email?.error?.message }}
							</Message>
						</div>
						<div class="p-field flex flex-column">
							<FloatLabel variant="on">
								<Password
									name="password"
									id="password"
									v-model="loginCredentials.password"
									class="mb-0"
									:feedback="false"
									toggleMask
									fluid
								/>
								<label for="password">Password*</label>
							</FloatLabel>
							<Message
								v-if="$form.password?.invalid"
								severity="error"
								size="small"
								variant="simple"
								class="text-red-500"
							>
								{{ $form.password?.error?.message }}
							</Message>
						</div>
						<Button label="Login" type="submit" />
					</Form>
				</template>
			</Card>
		</main>

		<CustomFooter />
	</div>
</template>

<style>
#page-wrapper {
	display: flex;
	flex-direction: column;
	min-height: 100vh;
}

footer {
	margin-top: auto;
}
</style>
