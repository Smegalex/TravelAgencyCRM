const fetchClients = async () => {
	try {
		const response = await fetch("http://127.0.0.1:5000/clients");
		return await response.json();
	} catch (error) {
		console.error("Error fetching clients:", error);
	}
};

const fetchClient = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/clients/${id}`);
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error fetching client (id: ${id}):`, error);
	}
};

const addClient = async (client) => {
	try {
		const response = await fetch("http://127.0.0.1:5000/clients", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(client),
		});
		return await response.json();
	} catch (error) {
		console.error("Error adding trip:", error);
	}
};

const updateClient = async (client) => {
	try {
		const id = client["id"];
		const response = await fetch(`http://127.0.0.1:5000/clients/${id}`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(client), // Directly use validated form values
		});
		return (await response.json())[0];
	} catch (error) {
		console.error("Error adding trip:", error);
	}
};

const deleteClient = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/clients/${id}`, {
			method: "DELETE",
		});
	} catch (error) {
		console.error("Error deleting client:", error);
	}
};
export { fetchClients, fetchClient, addClient, updateClient, deleteClient };
