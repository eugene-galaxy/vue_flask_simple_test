<template>
	<h1>🏆 Top GC</h1>
	<p>This is a list of users in our database sorted by their <a href="https://en.wikipedia.org/wiki/GC-content">GC-content</a>. We hope you find it useful.</p>
	<SuperTable :keys="['score', 'name', 'age', 'description']" :rows="topGC"/>
</template>

<script setup>
import {api} from '@/script/utils';
import {ref, onMounted} from 'vue';
import SuperTable from '@/component/SuperTable';

const topGC = ref([]);

onMounted(async () => {
	topGC.value = await api('topgc');
});
</script>