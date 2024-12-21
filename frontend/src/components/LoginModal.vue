<template>
  <div>
    <button @click="openModal">Login</button>

    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
          <div>
            <label for="email">Email:</label>
            <input
              type="email"
              id="email"
              v-model="email"
              required
            />
          </div>
          <div>
            <label for="password">Password:</label>
            <input
              type="password"
              id="password"
              v-model="password"
              required
            />
          </div>
          <button type="submit">Submit</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      email: "",
      password: "",
      errorMessage: null,
    };
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
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
        alert("Login successful!");
        this.showModal = false;
      } catch (error) {
        this.errorMessage = error.message;
      }
    },
  },
};
</script>

<style>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 300px;
}

.close {
  cursor: pointer;
  float: right;
  font-size: 20px;
}

.error {
  color: red;
}
</style>
