const fetchTrips = async () => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/trips`);
		return await response.json();
	} catch (error) {
		console.error(`Error fetching trips:`, error);
	}
};

const fetchTrip = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/trips/${id}`);
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error fetching trip (id: ${id}):`, error);
	}
};

export { fetchTrips, fetchTrip };
