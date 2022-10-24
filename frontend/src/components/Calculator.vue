<template>
  <div class="calculator_background p-3 rounded">

    <div class="result_window m-1 p-3 rounded lead">
      {{ calculation_value || 0 }}
    </div>

    <div class="row no-gutters">
      <div class="col-3" v-for="n in calculator_buttons" :key="n">
        <div class="calculator_button lead text-white text-center m-1 p-2 rounded hovering" :class="{
          'operator_button': ['(', ')', 'exp', 'log', '+', '-', '*', '/'].includes(n),
          'clear_button': ['AC'].includes(n),
          'equals_button': ['='].includes(n),
          'blank': n === ''
        }" @click="buttonPress(n)">
          {{ n }}
        </div>
      </div>
    </div>
  </div>


</template>

<script>
export default {
  name: 'CalculatorApp',
  props: {
    msg: String
  },

  data() {
    return {
      calculation_value: '',
      calculator_buttons: ['(', ')', 'exp', 'log', 7, 8, 9, '+', 4, 5, 6,
        '-', 1, 2, 3, '*', 0, '.', 'Del', '/', 'AC', '', '=']
    }
  },

  methods: {
    buttonPress(n) {

      // Numeric value or operator
      if (!(['AC', '=', 'exp', 'log'].includes(n))) {
        this.calculation_value += n + '';
      }

      // Clear button
      if (n === 'AC') {
        this.calculation_value = '';
      }

      // exp and log buttons
      if (n === 'exp' || n === 'log') {
        this.calculation_value += n + '('
      }

      // Equals button
      if (n === '=') {
        // TODO: Call function here
        this.calculation_value = '';
      }
    }
  }
}
</script>
  
<style scoped>
.calculator_background {
  width: 300px;
  margin: 50px auto;
  background: #003D5B
}

.result_window {
  background: white;
  font-weight: bold;
  text-align: right;
  color: black;
}

.calculator_button {
  background: #30638E;
}

.hovering:hover {
  cursor: pointer;
  background: rgb(108, 63, 152);
}

.operator_button {
  background-color: #00798C;
}

.clear_button {
  background-color: #D1495B;
}

.equals_button {
  background-color: #EDAE49;
  width: 123px;
}

.blank {
  visibility: hidden;
}
</style>
