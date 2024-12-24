const fetchBookings_by_ClientID = async (client_id) => {
	try {
		const response = await fetch(
			`http://127.0.0.1:5000/clients/${client_id}/bookings`
		);
		return await response.json();
	} catch (error) {
		console.error(
			`Error fetching client bookings (id: ${client_id}):`,
			error
		);
	}
};

export { fetchBookings_by_ClientID };
