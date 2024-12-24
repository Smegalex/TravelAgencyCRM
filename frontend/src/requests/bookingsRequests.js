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

const addBooking = async (booking) => {
	try {
		const response = await fetch("http://127.0.0.1:5000/bookings", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(booking),
		});
		return await response.json();
	} catch (error) {
		console.error("Error adding booking:", error);
	}
};

const updateBooking = async (booking) => {
	try {
		const id = booking["id"];
		const response = await fetch(`http://127.0.0.1:5000/bookings/${id}`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(booking), // Directly use validated form values
		});
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error updating booking (id: ${booking['id']}):`, error);
	}
};

const deleteBooking = async (id) => {
	try {
		await fetch(`http://127.0.0.1:5000/bookings/${id}`, {
			method: "DELETE",
		});
	} catch (error) {
		console.error(`Error deleting booking (id: ${id}):`, error);
	}
};

export { fetchBookings_by_ClientID, addBooking, updateBooking, deleteBooking};
