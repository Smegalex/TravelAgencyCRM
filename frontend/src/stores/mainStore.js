import { defineStore } from "pinia";
// import { reactive } from "vue";

export const useMainStore = defineStore("main", {
	state: () => ({
		username: undefined,
		adminRights: undefined,
		userId: undefined,
	}),
	getters: {
		getUsername: (state) => state.username,
		getRights: (state) => state.adminRights,
		getId: (state) => state.userId,
	},
	actions: {
		setUser(name) {
			// console.log("username changed");
			this.username = name;
		},
		setRights(rights) {
			// console.log("rights changed");
			this.adminRights = rights;
		},
		setId(id) {
			// console.log("id changed");
			this.userId = id;
		},
	},
	persist: {
		storage: sessionStorage,
	},
});
