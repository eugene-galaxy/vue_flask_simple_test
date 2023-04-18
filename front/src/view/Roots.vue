<template>
	<h1>🌴 Discover your roots</h1>
	<form @submit="locate" ref="form">
		<input name="genome" placeholder="Paste your DNA string here">
		<button>Locate</button>
		<span class="message" ref="message"></span>
	</form>
	<p>Submit your genome and we will show here the 5 most similar people in our database.</p>
	<Map :points="people"/>
</template>

<script setup>
import {api, formToJson} from '@/script/utils';
import {ref} from 'vue';
import Map from '@/component/Map';

const people = ref([]);
const form = ref(null);
const message = ref(null);

async function locate(event) {
	event.preventDefault();
	message.value.innerHTML = 'Loading...';
	message.value.classList.remove('error');
	try {
		const res = await api('roots', formToJson(form.value));
		if (!res.error) {
			people.value = res;
			message.value.innerHTML = '';
			return;
		}
		message.value.innerHTML = res.error;
	} catch (error) {
		message.value.innerHTML = error;
	}
	message.value.classList.add('error');
}
</script>

<style scoped>
form {
	display: flex;
	gap:.5rem;
	align-items: center;
}
</style>