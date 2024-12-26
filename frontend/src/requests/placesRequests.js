const fetchPlaces = async () => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/places`);
		return await response.json();
	} catch (error) {
		console.error(`Error fetching places:`, error);
	}
};

const fetchPlace = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/places/${id}`);
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error fetching place (id: ${id}):`, error);
	}
};

export { fetchPlaces, fetchPlace };
