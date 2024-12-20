import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import CustomHeader from "./components/CustomHeader.vue";
import CustomFooter from "./components/CustomFooter.vue";
import Nora from "@primevue/themes/nora";
import "primeflex/primeflex.css";
import "@/styles/styles.scss";

const app = createApp(App);

app.use(PrimeVue, {
	theme: {
		preset: Nora,
	},
});


app.component("CustomHeader", CustomHeader);
app.component("CustomFooter", CustomFooter);

app.mount("#app");
export default app;
