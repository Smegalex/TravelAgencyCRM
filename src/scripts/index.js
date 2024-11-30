// Завдання 1: Розрахунок вартості путівки
function calculatePrice() {
	const price = parseFloat(document.getElementById("price").value);
	const discount = parseFloat(document.getElementById("discount").value);

	// Якщо поля пусті, просто очищуємо виведення результату
	if (
		document.getElementById("price").value === "" ||
		document.getElementById("discount").value === ""
	) {
		document.getElementById("finalPrice").textContent = "";
		return;
	}

	// Валідація введених значень
	if (
		isNaN(price) ||
		isNaN(discount) ||
		price <= 0 ||
		discount < 0 ||
		discount > 100
	) {
		return; // Не показуємо попередження при некоректних даних, просто не рахуємо
	}

	// Обчислення нової вартості
	const finalPrice = price - price * (discount / 100);
	document.getElementById("finalPrice").textContent = finalPrice.toFixed(2);
}

// Додавання слухачів подій для автоматичного обчислення при зміні значень
document.getElementById("price").addEventListener("input", calculatePrice);
document.getElementById("discount").addEventListener("input", calculatePrice);

// Завдання 2: Чат
function sendMessage(user) {
	const chatBox = document.getElementById("chatBox");
	const messageInput1 = document.getElementById("messageInput1");
	const messageInput2 = document.getElementById("messageInput2");
	let message = "";

	// Вибираємо повідомлення від користувача 1 або 2
	if (user === 1) {
		message = messageInput1.value.trim();
		if (message === "") return;
	} else {
		message = messageInput2.value.trim();
		if (message === "") return;
	}

	// Створення нового блоку для повідомлення
	const messageElement = document.createElement("div");
	messageElement.className = "message";
	messageElement.textContent = message;

	// Встановлення повідомлення ліворуч або праворуч залежно від користувача
	if (user === 1) {
		messageElement.classList.add("left");
	} else {
		messageElement.classList.add("right");
	}

	// Додавання повідомлення в чат
	chatBox.appendChild(messageElement);
	chatBox.scrollTop = chatBox.scrollHeight; // Прокручування вниз

	// Очищення поля введення відповідного користувача
	if (user === 1) {
		messageInput1.value = "";
	} else {
		messageInput2.value = "";
	}
}

function detectedMess(event, num) {
	if (event.repeat) {
		return;
	}
	if (event.key === "Enter") {
		sendMessage(num);
	}
}

document
	.getElementById("messageInput1")
	.addEventListener("keypress", (event) => detectedMess(event, 1));
document
	.getElementById("messageInput2")
	.addEventListener("keypress", (event) => detectedMess(event, 2));

// Завдання 3: Транслітерація
const transliterationRules = {
	а: "a",
	б: "b",
	в: "v",
	г: "h",
	ґ: "g",
	д: "d",
	е: "e",
	є: "ie",
	ж: "zh",
	з: "z",
	и: "y",
	і: "i",
	ї: "i",
	й: "i",
	к: "k",
	л: "l",
	м: "m",
	н: "n",
	о: "o",
	п: "p",
	р: "r",
	с: "s",
	т: "t",
	у: "u",
	ф: "f",
	х: "kh",
	ц: "ts",
	ч: "ch",
	ш: "sh",
	щ: "shch",
	ю: "iu",
	я: "ia",
	ь: "",
	" ": " ",
};

function transliterate(text) {
	let convert = (char) => {
		return transliterationRules[char.toLowerCase()] || char;
	};
	return text
		.split("")
		.map((char) =>
			char.toLowerCase() != char
				? convert(char).toUpperCase()
				: convert(char)
		)
		.join("");
}

document.getElementById("ukrainianText").addEventListener("input", function () {
	const ukrainianText = this.value;
	document.getElementById("transliteratedText").value =
		transliterate(ukrainianText);
});
