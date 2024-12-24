import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";

// Components
import CustomHeader from "./components/CustomHeader.vue";
import CustomFooter from "./components/CustomFooter.vue";
import UniversalModal from "./pages/modals/UniversalModal.vue";
import ClientViewTable from "./components/tables/ClientViewTable.vue";

// Primeflex
import Nora from "@primevue/themes/nora";
import "primeflex/primeflex.css";
import "@/styles/styles.scss";

const app = createApp(App).use(router);

app.use(PrimeVue, {
	theme: {
		preset: Nora,
		options: {
			prefix: "",
		},
	},
});

app.component("CustomHeader", CustomHeader);
app.component("CustomFooter", CustomFooter);
app.component("UniversalModal", UniversalModal);
app.component("ClientViewTable", ClientViewTable);

app.mount("#app");
export default app;
