<template>
	<img alt="Vue logo" src="./assets/logo.png">
	<!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<!-- <HomePage msg="1st dont by shy"/> -->
	<p>Choose what part of this page you want to see:</p>
	<router-link to="/home">Home</router-link><br>
	<router-link to="/about">About</router-link><br>
	<div>
		<router-view></router-view>
	</div>
</template>

<script lang="en">
	// import HomePage from './components/views/HomeView.vue'
	// import HelloWorld from './components/HelloWorld.vue'

	export default {
		name: 'ExampleApp',
		components: {
			// HelloWorld,
			// HomePage
		}
	}

</script>

<style>
</style>
