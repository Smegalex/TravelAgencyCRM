<template>
	<div>
		<h1>User Registration Form</h1>
		<form @submit.prevent="handleSubmit">
			<label>Name:</label>
			<input v-model="newUser.name" type="text" required />
			<br />
			<label>Surname:</label>
			<input v-model="newUser.surname" type="text" required />
			<br />
			<label>Gender:</label>
			<select v-model="newUser.gender" required>
				<option value="male">Male</option>
				<option value="female">Female</option>
			</select>
			<br />
			<label>Phone:</label>
			<input
				type="text"
				v-model="newUser.phone"
				v-mask="'(###) ###-####'"
				placeholder="(123) 456-7890"
			/>
			<br />
			<label>Email:</label>
			<input v-model="newUser.email" type="email" required />
			<br />
			<button type="submit">Add User</button>
		</form>

		<h2>Users Table</h2>
		<table border="1">
			<thead>
				<tr>
					<th>Select</th>
					<th>Name</th>
					<th>Surname</th>
					<th>Gender</th>
					<th>Phone</th>
					<th>Email</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="user in users" :key="user.id">
					<td>
						<input
							type="checkbox"
							:value="user"
							v-model="selectedUsers"
						/>
					</td>
					<td>{{ user.name }}</td>
					<td>{{ user.surname }}</td>
					<td>{{ user.gender }}</td>
					<td>{{ user.phone }}</td>
					<td>{{ user.email }}</td>
				</tr>
			</tbody>
		</table>

		<button @click="duplicateSelected">Duplicate Selected</button>
		<button @click="deleteSelected">Delete Selected</button>
	</div>
</template>

<script>
import { mask } from "vue-the-mask";

export default {
	directives: {
		mask,
	},
	data() {
		return {
			newUser: {
				id: 0,
				name: "",
				surname: "",
				gender: "",
				phone: "",
				email: "",
			},
			users: [],
			selectedUsers: [],
			nextId: 1,
		};
	},
	methods: {
		handleSubmit() {
			this.users.push({ ...this.newUser });
			this.newUser = {
				id: this.nextId++,
				name: "",
				surname: "",
				gender: "",
				phone: "",
				email: "",
			};
			console.log(this.newUser);
			console.log(this.nextId);
		},
		duplicateSelected() {
			this.selectedUsers.forEach((user) => {
				const userCopy = {
					...JSON.parse(JSON.stringify(user)),
					id: this.nextId++,
				}; // Deep copy with unique ID
				this.users.push(userCopy);
			});
			this.selectedUsers = []; // Clear selected users after duplication
		},
		deleteSelected() {
			// Filter out selected users from the main users array
			this.users = this.users.filter(
				(user) => !this.selectedUsers.includes(user)
			);
			// Clear selected users after deletion
			this.selectedUsers = [];
		},
	},
};
</script>
