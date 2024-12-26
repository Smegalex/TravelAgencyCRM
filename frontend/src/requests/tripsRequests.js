const fetchTrips = async () => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/trips`);
		return await response.json();
	} catch (error) {
		console.error(`Error fetching trips:`, error);
		throw new Error(`Error fetching trips.`);
	}
};

const fetchTrip = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/trips/${id}`);
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error fetching trip (id: ${id}):`, error);
		throw new Error(`Error fetching trip (id: ${id}).`);
	}
};

const addTrip = async (trip) => {
	try {
		const response = await fetch("http://localhost:5000/trips", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(trip), // Directly use validated form values
		});
		return await response.json();
	} catch (error) {
		console.error("Error adding trip:", error);
		throw new Error(`Error adding trip.`);
	}
};

const updateTrip = async (trip) => {
	try {
		const id = trip["id"];
		const response = await fetch(`http://127.0.0.1:5000/trips/${id}`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(trip), // Directly use validated form values
		});
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error updating trip (id: ${trip["id"]}):`, error);
		throw new Error(`Error updating trip (id: ${trip["id"]}).`);
	}
};

export { fetchTrips, fetchTrip, addTrip, updateTrip };
