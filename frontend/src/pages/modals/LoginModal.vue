<script setup>
import CustomHeader from "@/components/CustomHeader.vue";
import CustomFooter from "@/components/CustomFooter.vue";
</script>

<template>
  <div class="page-container">
    <header>
      <CustomHeader active-page="login" />
    </header>
    <main class="content">
      <div class="login-container">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
          <div class="form-group">
            <input
              type="email"
              id="email"
              v-model="email"
              required
              placeholder="Email*"
              class="form-input"
            />
          </div>
          <div class="form-group">
            <input
              type="password"
              id="password"
              v-model="password"
              required
              placeholder="Password*"
              class="form-input"
            />
          </div>
          <button type="submit" class="form-button">Login</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
    </main>
    <footer>
      <CustomFooter />
    </footer>
  </div>
</template>


<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      errorMessage: null,
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch("http://127.0.0.1:5000/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        if (!response.ok) {
          throw new Error("Invalid credentials");
        }

        const data = await response.json();
        this.$router.push('/'); // Перехід на головну сторінку
      } catch (error) {
        this.errorMessage = error.message;
      }
    },
  },
}
</script>

<style>
.page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ffffff; /* Темний фон */
}

.login-container {
  background-color: #1e1e1e;
  padding: 20px 30px;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

h2 {
  color: #ffffff;
  margin-bottom: 20px;
  font-size: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-input {
  width: 100%;
  padding: 10px 15px;
  font-size: 14px;
  color: #ffffff;
  background-color: #121212;
  border: 1px solid #333333;
  border-radius: 4px;
  outline: none;
  transition: border-color 0.3s ease;
}

.form-input::placeholder {
  color: #666666;
}

.form-input:focus {
  border-color: #1db954; /* Зелений акцент */
}

.form-button {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #ffffff;
  background-color: #1db954; /* Зелений акцент */
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-button:hover {
  background-color: #1aa34a;
}

footer {
  margin-top: auto;
}
</style>
