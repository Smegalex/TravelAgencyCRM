const fetchUsername = async () => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/session/username`, {
			method: "GET",
			credentials: "include",
		});
		return await response.json();
	} catch (error) {
		console.error(`Error fetching username:`, error);
	}
};

const fetchAdminRights = async () => {
	try {
		const response = await fetch(
			`http://127.0.0.1:5000/session/adminRights`,
			{
				method: "GET",
				credentials: "include",
			}
		);
		return await response.json();
	} catch (error) {
		console.error(`Error fetching admin rights:`, error);
	}
};

const fetchUserId = async () => {
	try {
		const response = await fetch(`http://127.0.0.1:5000/session/userId`, {
			method: "GET",
			credentials: "include",
		});
		return await response.json();
	} catch (error) {
		console.error(`Error fetching user id:`, error);
	}
};

const login = async (loginCredentials) => {
	const response = await fetch("http://127.0.0.1:5000/login", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(loginCredentials),
		credentials: "include",
	});
	return await response;
};

const logout = async () => {
	const response = await fetch("http://127.0.0.1:5000/logout", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(loginCredentials),
		credentials: "include",
	});
	return await response.json();
};

export { fetchAdminRights, fetchUsername, fetchUserId, login, logout};
