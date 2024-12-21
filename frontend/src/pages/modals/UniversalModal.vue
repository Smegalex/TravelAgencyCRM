<script setup>
const {
	showForm,
	header,
	fields,
	formResolver,
	data,
	callBack,
	submitLabel = "Submit",
	submitButtonType = "p-button-primary",
} = defineProps({
	showForm: {
		type: Boolean,
		required: true,
	},
	header: {
		type: String,
		default: "Form",
	},
	fields: {
		type: Array,
		required: true,
	},
	formResolver: {
		type: Function,
		required: false,
	},
	data: {
		type: Object,
		required: true,
	},
	callBack: {
		type: Function,
		required: true,
	},
	submitLabel: {
		type: String,
		required: false,
	},
	submitButtonType: {
		type: String,
		required: false,
	},
});

console.log(data);
</script>

<template>
	<Dialog
		:visible="showForm"
		@update:visible="$emit('changeVisibility')"
		:header="header"
		:closable="true"
		:modal="true"
		:style="{ width: '450px' }"
	>
		<Form
			v-slot="$form"
			class="form-container flex flex-column gap-3"
			:model="data"
			:resolver="formResolver"
			:initial-values="data"
			@submit="callBack"
		>
			<div
				v-for="field in fields"
				:key="field.name"
				class="p-field flex flex-column"
			>
				<InputText
					:name="field.name"
					v-bind="field.props"
					v-model="data[field.name]"
					:placeholder="field.placeholder"
					:model-value="data[field.name]"
					class="mb-0"
					fluid
				/>
				<Message
					v-if="$form[field.name]?.invalid"
					severity="error"
					size="small"
					variant="simple"
					class="text-red-500"
				>
					{{ $form[field.name]?.error?.message }}
				</Message>
			</div>
			<Button
				:label="submitLabel"
				:class="submitButtonType"
				type="submit"
			/>
		</Form>
	</Dialog>
</template>
