const fetchManager = async (id) => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/managers/${id}`);
		return (await response.json())[0];
	} catch (error) {
		console.error(`Error fetching manager (id: ${id}):`, error);
	}
};

export { fetchManager };
