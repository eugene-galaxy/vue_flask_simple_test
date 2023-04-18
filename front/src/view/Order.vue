<template>
	<h1>🚚 Order a kit</h1>
	<p>Fill this form and we will deliver the test kit to your home. No need to pay right now, you can include your payment in the envelope when delivering the sample to our labs. We accept dollar bills, checks and Walmart coupons.</p>
	<form @submit="order" ref="form">
		<table>
			<tr>
				<th>Full name</th>
				<td><input name="name" type="text" placeholder="John Doe" autofocus autocomplete="name"></td>
				<td>Should be 4-32 characters long and have exactly two words, capitalized.</td>
			</tr>
			<tr>
				<th>Password</th>
				<td><input name="password" type="password" placeholder="5UPer$afe" autocomplete="new-password"></td>
				<td>Should be 12-32 characters long, start with a number, contain two uppercase letters one after another, and at least one symbol.</td>
			</tr>
			<tr>
				<th>Age</th>
				<td><input name="age" type="text" placeholder="66"></td>
				<td>This is optional. I you provide it, it should be an integer between 18 and 125.</td>
			</tr>
			<tr>
				<th>Location</th>
				<td>(<input name="x" type="text" placeholder="43.12%">, <input name="y" type="text" placeholder="99%">)</td>
				<td>Should be a percentage with optional decimals that represents your relative position in a <a href="https://en.wikipedia.org/wiki/Robinson_projection">Robinson projection</a> of the world.</td>
			</tr>
			<tr>
				<th>Description</th>
				<td><textarea name="description" placeholder="Tell us about yourself"></textarea></td>
				<td>This is also optional. If you provide it, it should have 10-500 characters.</td>
			</tr>
			<tr>
				<td colspan="2"><input type="checkbox" name="public"> Include me in the list of people who ordered a kit</td>
				<td>This is optional.</td>
			</tr>
			<tr>
				<td colspan="2"><input type="checkbox" name="sell" checked> I want my data to be sold to third parties</td>
				<td>This is optional.</td>
			</tr>
			<tr>
				<td colspan="2"><input type="checkbox" name="terms"> I accept the <RouterLink to="/">terms and conditions</RouterLink></td>
				<td>You should check this.</td>
			</tr>
			<tr>
				<td><button>Order</button></td>
				<td colspan="2" class="message" ref="message"></td>
			</tr>
		</table>
	</form>
</template>

<script setup>
import {api, formToJson} from '@/script/utils';
import {ref} from 'vue';

const form = ref(null);
const message = ref(null);

async function order(event) {
	message.value.innerHTML = 'Loading...';
	message.value.classList.remove('error', 'success');
	event.preventDefault();
	try {
		const res = await api('order', formToJson(form.value));
		if (res.id) {
			form.value.reset();
			message.value.innerHTML = `Order #${res.id} placed!`;
			message.value.classList.add('success');
			return;
		} else {
			message.value.innerHTML = res.error;
		}
	} catch (error) {
		message.value.innerHTML = error;
	}
	message.value.classList.add('error');
}
</script>

<style scoped>
table {
	border-collapse: collapse;
}
th, td {
	padding: .5rem .25rem;
}
tr td:last-child {
	opacity: .7;
}
input[type=text], input[type=password], textarea {
	width: 20rem;
	resize: none;
}
textarea {
	height: 10rem;
}
input[name=x], input[name=y] {
	width: 5rem;
	text-align: center;
}
</style>