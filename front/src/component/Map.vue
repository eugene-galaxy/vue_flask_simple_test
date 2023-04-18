<template>
	<div class="map">
		<img src="map.svg">
		<div v-for="p in points" :key="p" class="point" :style="`left:${p.x * 100}%;top:${p.y * 100}%`">
			{{ p.name }}
		</div>
	</div>
</template>

<script setup>
const props = defineProps({
	points: {type: Array, default: () => []}
});
</script>

<style scoped>
.map {
	position: relative;
	width: calc(100vw - 20rem);
}
.map img {
	display: block;
	width: 100%;
}
.map .point {
	position: absolute;
	transform: translate(-50%, -50%);
	padding: .25rem;
	background: var(--black);
	color: var(--white);
	text-align: center;
	border-radius: .5rem;
}
</style>