<template>
    <input type={{type}} class="shadow border rounded text-gray-700 py-1 px-3 hover:shadow-inner transition">
</template>

<script>
export default {
    name: "TInput",
    props: {
        type: String
    }
}
</script>