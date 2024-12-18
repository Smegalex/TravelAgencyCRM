const nameRegex = /^[a-zA-Zа-яА-я]+$/;
const passwordRegex = /^[a-zA-Zа-яА-Я0-9.!?-_]{6,20}$/;
const emailRegex = /^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/;
let isValid = true;

// Перевірка імені
function checkName() {
	let value = $("#nameRegister").val();
	if (value === "") {
		$("#nameError").text("Please enter your name");
		isValid = false;
	} else if (!nameRegex.test(value)) {
		$("#nameError").text("Please only enter letters");
		isValid = false;
	} else {
		$("#nameError").text("");
	}
}

// Перевірка прізвища
function checkSurname() {
	let value = $("#surnameRegister").val();
	if (value === "") {
		$("#surnameError").text("Please enter your surname");
		isValid = false;
	} else if (!nameRegex.test(value)) {
		$("#surnameError").text("Please only enter letters");
		isValid = false;
	} else {
		$("#surnameError").text("");
	}
}

function checkPhone() {
	let value = $("#phoneRegister").val();
	if (value.length !== 18) {
		$("#phoneError").text("Please enter a valid phone number");
		isValid = false;
	} else {
		$("#phoneError").text("");
	}
}

function checkGender() {
	let value = $(
		"input[type='radio'][name=gender]:checked",
		"#registrationForm"
	).val();

	if (!value) {
		$("#genderError").text("Please choose a gender");
		isValid = false;
	} else {
		$("#genderError").text("");
	}
}

function checkEmail() {
	let value = $("#emailRegister").val();
	if (!emailRegex.test(value)) {
		$("#emailError").text("Enter valid email");
		isValid = false;
	} else {
		$("#emailError").text("");
	}
}

function checkPassword() {
	let value = $("#passwordRegister").val();
	if (!passwordRegex.test(value)) {
		$("#passwordError").text(
			"Password should be 6-20 characters long and can contain letters, numbers and certain special characters"
		);
		isValid = false;
	} else {
		$("#passwordError").text("");
	}
}

function checkPasswordConf() {
	let value = $("#confirmPasswordRegister").val();
	let checking = $("#passwordRegister").val();
	if (checking === "") {
		$("#confirmPasswordError").text("");
		return;
	}

	if (value === "") {
		$("#confirmPasswordError").text("You have to confirm your password");
		isValid = false;
	} else if (value !== checking) {
		$("#confirmPasswordError").text("This does not match your password");
		isValid = false;
	} else {
		$("#confirmPasswordError").text("");
	}
}

$(document).ready(function () {
	// Маска для телефону
	$("#phoneRegister").mask("+38(000) 000-00-00");

	// Валідація форми
	$(".onChangeValidation").change(function (e) {
		let field_id = e.currentTarget.id;
		let field_classes = e.currentTarget.classList;
		// console.log(field_id);
		// console.log(field_classes);

		switch (field_id) {
			case "nameRegister":
				checkName();
				break;
			case "surnameRegister":
				checkSurname();
				break;
			case "phoneRegister":
				checkPhone();
				break;
			case "passwordRegister":
				checkPassword();
				break;
			case "confirmPasswordRegister":
				checkPasswordConf();
				break;
			case "emailRegister":
				checkEmail();
				break;
		}

		if (field_classes.contains("genderRegister")) {
			checkGender();
		}
	});

	$("#registerButton").click(function () {
		isValid = true;
		checkName();
		checkSurname();
		checkPhone();
		checkGender();
		checkEmail();
		checkPassword();
		checkPasswordConf();

		if (isValid) {
			// Додавання даних до таблиці
			const name = $("#nameRegister").val();
			const surname = $("#surnameRegister").val();
			const gender = $('input[name="gender"]:checked').val();
			const dob = $("#dobRegister").val();
			const phone = $("#phoneRegister").val();
			const email = $("#emailRegister").val();
			const role = $("#roleSelect").val();

			$("#userTable").append(`
			<tr>
				<td><input type="checkbox" class="row-checkbox"></td>
				<td>${name}</td>
				<td>${surname}</td>
				<td>${gender}</td>
				<td>${dob}</td>
				<td>${phone}</td>
				<td>${email}</td>
				<td>${role}</td>
			</tr>
		`);

			// Очищення форми
			$("#registrationForm")[0].reset();
		}
	});

	// Видалення обраних рядків
	$("#deleteButton").click(function () {
		$("input.row-checkbox:checked").closest("tr").remove();
	});

	// Дублювання обраних рядків
	$("#duplicateButton").click(function () {
		$("input.row-checkbox:checked").each(function () {
			const row = $(this).closest("tr").clone();
			row.find(".row-checkbox").prop("checked", false);
			$("#userTable").append(row);
		});
	});
});
