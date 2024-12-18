<script setup>
defineProps({
  visible: {
    type: Boolean,
    required: true,
  },
  activePage: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div>
    <!-- Кнопка відкриття модального вікна -->
    <Button label="Open Login Form" @click="showDialog = true" />

    <!-- Модальне вікно -->
    <Dialog
      :visible="showDialog"
      style="width: 30vw"
      :modal="true"
      :closable="true"
      header="Форма Авторизації"
      @hide="showDialog = false"
    >
      <template>
        <form @submit.prevent="onSubmit">
          <div class="p-field">
            <label for="emailLogin">Email</label>
            <InputText
              id="emailLogin"
              v-model="email"
              type="email"
              placeholder="Enter email"
              class="p-inputtext-sm"
            />
          </div>
          <div class="p-field">
            <label for="passwordLogin">Password</label>
            <InputText
              id="passwordLogin"
              v-model="password"
              type="password"
              placeholder="Password"
              class="p-inputtext-sm"
            />
          </div>
          <Button
            label="Login"
            type="submit"
            class="p-button-primary mt-3"
          />
        </form>
      </template>
    </Dialog>
  </div>
</template>

<script>
import { ref } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";

export default {
  components: {
    Button,
    Dialog,
    InputText,
  },
  setup() {
    const showDialog = ref(false);
    const email = ref("");
    const password = ref("");

    const onSubmit = () => {
      console.log("Email:", email.value, "Password:", password.value);
      showDialog.value = false; // Закрити діалог після авторизації
    };

    return { showDialog, email, password, onSubmit };
  },
};
</script>
