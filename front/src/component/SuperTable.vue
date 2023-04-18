<template>
  <div class="pagination" v-if="pageCount > 1">
    <p>{{ rows.length }} results</p>
    <button @click="page = 0" :disabled="page === 0">1</button>
    <template v-if="page > 2">
      <span>...</span>
    </template>
    <button
      v-for="n in visiblePages"
      :key="n"
      @click="page = n - 1"
      :class="{
        active: page === n - 1,
      }"
      :disabled="page === n - 1"
    >
      {{ n }}
    </button>
    <template v-if="page < pageCount - 3">
      <span>...</span>
    </template>
    <button @click="page = pageCount - 1" :disabled="page === pageCount - 1">
      {{ pageCount }}
    </button>
    <button @click="page++" :disabled="page === pageCount - 1">Next</button>
  </div>
  <table v-if="pageCount > 0">
    <tr>
      <th v-for="key in keys">{{ key }}</th>
    </tr>
    <tr v-for="row in pageRows">
      <td v-for="key in keys">{{ row[key] }}</td>
    </tr>
  </table>
</template>

<script setup>
import { computed, defineProps, ref } from "vue";

const props = defineProps({
  keys: { type: Array, default: () => [] },
  rows: { type: Array, required: true },
  rowsPerPage: { type: Number, default: 5 },
});

const page = ref(0);
const pageRows = computed(() =>
  props.rows.slice(
    page.value * props.rowsPerPage,
    (page.value + 1) * props.rowsPerPage
  )
);
const pageCount = computed(() =>
  Math.ceil(props.rows.length / props.rowsPerPage)
);

const visiblePages = computed(() => {
  const range = 1;
  let start = Math.max(2, page.value);
  let end = Math.min(pageCount.value - 1, page.value + range + 1);

  if (end - start < range * 2) {
    const missing = range * 2 - (end - start);
    start = Math.max(2, start - missing);
    end = Math.min(pageCount.value - 1, end + missing);
  }

  const pages = [];
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
tr {
  border-bottom: 1px solid var(--black2-transparent);
}
th {
  text-transform: capitalize;
  background: var(--black2);
  color: var(--white);
}
th,
td {
  text-align: left;
  padding: 0.5rem;
}
.pagination {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  height: 2rem;
  justify-content: flex-end;
}
.pagination button {
  border: 0;
  font-weight: bold;
  cursor: pointer;
}
.pagination button:first-of-type {
  margin-left: 2rem;
}
.pagination button.active {
  color: white;
  background-color: rgb(57, 85, 179);
}
.current {
  pointer-events: none;
  background: var(--white3);
}
</style>
