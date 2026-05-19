<script>
	import '$lib/styles.css'
	let { children } = $props();
</script>

<svelte:head>
	<title>VS Char Website | Homepage</title>
</svelte:head>

{@render children()}
