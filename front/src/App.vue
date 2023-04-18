<template>
	<header>
		<RouterLink to="/" class="logo">🧬Gen-o-matic</RouterLink>
		<RouterLink to="/order">🤑 Order a kit</RouterLink>
		<RouterLink to="/topgc">🏆 Top GC</RouterLink>
		<RouterLink to="/roots">🌴 Your roots</RouterLink>
	</header>
	<main>
		<RouterView/>
	</main>
</template>

<script setup>
import {RouterLink, RouterView} from 'vue-router'
</script>

<style>
* {
	box-sizing: border-box;
}
:root {
	--black: #260d21;
	--black2: #611552;
	--black2-transparent: #61155240;
	--white: #ffffff;
	--white2: #fafafa;
	--white3: #a7a0a3;
	--pink: #cfbdd8;
}
body {
	margin: 0;
	display: flex;
	font: 18px/125% ui-sans-serif, sans-serif;
	background: var(--white2);
	color: var(--black);
	height: 100vh;
	overflow: hidden;
}
header {
	display: flex;
	flex-direction: column;
	background: var(--black);
	color: var(--white3);
}
header a {
	color: inherit;
	font-weight: bold;
	text-decoration: none;
	padding: 1rem 0 1rem 1.25rem;
	white-space: nowrap;
}
header a:hover {
	background: var(--black2);
	color: var(--white);
}
.logo {
	color: var(--white);
	font: bolder 1.5rem cursive;
	padding: 1.5rem 1.5rem 1.5rem 1rem;
	margin-bottom: 2rem;
}
main {
	flex-grow: 1;
	padding: 1rem 2rem 10rem;
	height: 100vh;
	overflow-y: scroll;
}
h1 {
	margin: 1rem -.5rem 2rem
}
h2 {
	margin: 1rem -.5rem 1rem;
}
input, button, textarea {
	font: inherit;
}
.required::after {
	content: '*';
	color: red;
}
.error {
	color: red;
}
.success {
	color: green;
}
</style>