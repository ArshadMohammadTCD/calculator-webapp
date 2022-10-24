<template>
  <div id="app">
    <CalculatorApp></CalculatorApp>
    <AppFooter></AppFooter>>
  </div>

</template>

<script>
import CalculatorApp from './components/Calculator.vue'
import AppFooter from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    CalculatorApp,
    AppFooter
  }
}
</script>

<style>

</style>
