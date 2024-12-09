<script lang="ts">
	import { onMount } from "svelte";

	// Existing props
	export let value: object | null;
	export let type: "gallery" | "table";
	export let selected = false;

	let size: number;
	let el: HTMLDivElement;

	function set_styles(element: HTMLElement, el_width: number): void {
		element.style.setProperty(
			"--local-text-width",
			`${el_width && el_width < 150 ? el_width : 200}px`,
		);
		element.style.whiteSpace = "unset";
	}

	onMount(() => {
		set_styles(el, size);
	});

	// Additional props passed by Gradio
	export let visible: boolean = true;
	export let elem_id: string | null = null;
	export let elem_classes: string[] = [];
	export let render: boolean = true;
	export let key: string | number | null = null;
	export let samples_dir: string | null = null;
	export let index: number | null = null;
	export let root: string | null = null;
</script>

<div
	bind:clientWidth={size}
	bind:this={el}
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
>
	{value ? value.company_name : ""}
</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}

	div {
		overflow: hidden;
		min-width: var(--local-text-width);

		white-space: nowrap;
	}
</style>
