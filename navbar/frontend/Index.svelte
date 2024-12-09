<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";

	export let gradio: Gradio<{
		change: never;
		submit: never;
		input: never;
		clear_status: LoadingStatus;
	}>;
	// svelte-ignore unused-export-let
	export let label = "";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: {
		company_logo_url: string;
		company_name: string;
		logout_link: string;
		username: string;
		profile_photo_url: string;
	} = {
		company_logo_url: "https://www.gravatar.com/avatar",
		company_name: "Digitalkin",
		logout_link: "/logout",
		username: "Jane Doe",
		profile_photo_url:
			"https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
	};
	// svelte-ignore unused-export-let
	export let show_label: boolean;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus | undefined = undefined;
	// svelte-ignore unused-export-let
	export let interactive: boolean;
	// export let rtl = false;
	// svelte-ignore unused-export-let
	export let root: string;

	// Additional props passed by Gradio
	// svelte-ignore unused-export-let
	export let key: string | number | null = null;
	// svelte-ignore unused-export-let
	export let name: string | null = null;
	// svelte-ignore unused-export-let
	export let _selectable: boolean = false;
	// svelte-ignore unused-export-let
	export let type: string | null = null;
	// svelte-ignore unused-export-let
	export let render: boolean = true;
	// svelte-ignore unused-export-let
	export let server: any = null;
	// svelte-ignore unused-export-let
	export let theme_mode: string | null = null;
	// svelte-ignore unused-export-let
	export let target: any = null;
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	{scale}
	{min_width}
	allow_overflow={false}
	padding={true}
>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
			on:clear_status={() =>
				gradio.dispatch("clear_status", loading_status)}
		/>
	{/if}

	<nav class="navbar">
		<div class="navbar-left">
			<img
				src={value.company_logo_url}
				alt="Company Logo"
				class="company-logo"
			/>
			<span class="company-name">{value.company_name}</span>
		</div>
		<div class="navbar-right">
			<a href={value.logout_link} class="logout-button">Logout</a>
			<span class="username">{value.username}</span>
			<img
				src={value.profile_photo_url}
				alt="User Profile"
				class="profile-photo"
			/>
		</div>
	</nav>
	<!-- Include a slot to accept any default content -->
	<slot></slot>
</Block>

<style>
	.navbar {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 10px;
		background-color: var(--navbar-background-color, #f8f8f8);
	}

	.navbar-left {
		display: flex;
		align-items: center;
	}

	.company-logo {
		height: 40px;
		margin-right: 10px;
	}

	.company-name {
		font-size: 1.5em;
		font-weight: bold;
		color: var(--navbar-text-color, #333);
		text-overflow: ellipsis;
		overflow: hidden;
		width: 100%;
		white-space: nowrap;
		display: inline-block;
	}

	.navbar-right {
		display: flex;
		align-items: center;
	}

	.logout-button {
		margin-right: 15px;
		color: var(--navbar-link-color, #007bff);
		text-decoration: none;
	}

	.logout-button:hover {
		text-decoration: underline;
	}

	.username {
		margin-right: 15px;
		font-size: 1em;
		color: var(--navbar-text-color, #333);
		text-overflow: ellipsis;
		overflow: hidden;
		width: 100%;
		white-space: nowrap;
		display: inline-block;
	}

	.profile-photo {
		width: 40px;
		height: 40px;
		border-radius: 50%;
	}
</style>
