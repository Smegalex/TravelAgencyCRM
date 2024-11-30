import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import CustomHeader from "./components/CustomHeader.vue";
	
const app = createApp(App);

app.use(PrimeVue, {
	theme: {
		preset: "Nora",
	},
});

app.component("CustomHeader", CustomHeader);

app.mount("#app");
export default app;
