<template>
	<h1>🧬 Welcome to Gen-o-matic!</h1>
	<p>We are a leader DNA-testing company that helps you find your roots.</p>
	<p>To get started, follow this simple process:</p>
	<div class="steps">
		<div>
			<var>1</var>
			<span>🧪</span>
			<h2>Order a kit</h2>
			<p>For just $99, we'll send a plastic tube to your home.</p>
		</div>
		<div>
			<var>2</var>
			<span>💌</span>
			<h2>Send your DNA</h2>
			<p>Deliver spittle at your own postage expense.</p>
		</div>
		<div>
			<var>3</var>
			<span>👩‍💻</span>
			<h2>Get a long string</h2>
			<p>We will mail you a long string with your genome.</p>
		</div>
	</div>
</template>

<style scoped>
.steps {
	display: flex;
	gap: 2rem;
}
.steps div {
	position: relative;
	width: 15rem;
	padding: 4rem 1rem 1rem;
	text-align: center;
	background: var(--pink);
	border-radius: .5rem;
}
.steps var {
	position: absolute;
	top: 1rem;
	left: 1rem;
	font-weight: bold;
}
.steps span {
	font-size: 3rem;
}
</style>