import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import piniaPluginPersistedState from "pinia-plugin-persistedstate";

// Components
import CustomHeader from "./components/CustomHeader.vue";
import CustomFooter from "./components/CustomFooter.vue";
import UniversalModal from "./pages/modals/UniversalModal.vue";
import ClientViewTable from "./components/tables/ClientViewTable.vue";

// Primeflex
import Nora from "@primevue/themes/nora";
import Aura from "@primevue/themes/aura";
import PrimeVue from "primevue/config";
import { definePreset } from "@primevue/themes";
import "primeflex/primeflex.css";
import "@/styles/styles.scss";
import Tooltip from "primevue/tooltip";
import ToastService from "primevue/toastservice";
import ConfirmationService from "primevue/confirmationservice";

//FontAwesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { fas } from "@fortawesome/free-solid-svg-icons";
library.add(fas);
library.add(far);
library.add(fab);

const pinia = createPinia();
pinia.use(piniaPluginPersistedState);

const app = createApp(App).use(router);

app.use(pinia);

const stylePreset = definePreset(Aura, {
	semantic: {
		primary: {
			50: "{emerald.50}",
			100: "{emerald.100}",
			200: "{emerald.200}",
			300: "{emerald.300}",
			400: "{emerald.400}",
			500: "{emerald.500}",
			600: "{emerald.600}",
			700: "{emerald.700}",
			800: "{emerald.800}",
			900: "{emerald.900}",
			950: "{emerald.950}",
		},
		colorScheme: {
			light: {
				surface: {
					0: "#ffffff",
					50: "{neutral.50}",
					100: "{neutral.100}",
					200: "{neutral.200}",
					300: "{neutral.300}",
					400: "{neutral.400}",
					500: "{neutral.500}",
					600: "{neutral.600}",
					700: "{neutral.700}",
					800: "{neutral.800}",
					900: "{neutral.900}",
					950: "{neutral.950}",
				},
			},
		},
	},
});

app.use(PrimeVue, {
	theme: {
		preset: stylePreset,
		options: {
			prefix: "",
		},
		darkModeSelector: "system",
	},
}).use(ToastService).use(ConfirmationService);

app.component("CustomHeader", CustomHeader);
app.component("CustomFooter", CustomFooter);
app.component("UniversalModal", UniversalModal);
app.component("ClientViewTable", ClientViewTable);
app.component("font-awesome-icon", FontAwesomeIcon);
app.directive("tooltip", Tooltip);

app.mount("#app");
export default app;
