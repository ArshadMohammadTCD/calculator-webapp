<template>
  <div class="calculator_background p-3 rounded">

    <div class="result_window m-1 p-3 rounded lead">
      {{ calculation_value || 0 }}
    </div>

    <div class="row no-gutters">
      <div class="col-3" v-for="n in calculator_buttons" :key="n">
        <div class="calculator_button lead text-white text-center m-1 p-2 rounded hovering" :class="{
          'operator_button': ['(', ')', 'exp', 'log', '+', '-', '*', '^', '/'].includes(n),
          'clear_button': ['AC'].includes(n),
          'equals_button': ['='].includes(n),
          'del_button': ['Del'].includes(n),
          'blank': n === ''
        }" @click="buttonPress(n)">
          {{ n }}
        </div>

      </div>
    </div>
  </div>


</template>

<script>
import axios from 'axios';

export default {
  name: 'CalculatorApp',
  props: {
    msg: String
  },

  data() {
    return {
      calculation_value: '',
      calculator_buttons: ['(', ')', 'exp', 'log', 7, 8, 9, '+', 4, 5, 6,
        '-', 1, 2, 3, '*', 0, '.', '^', '/', 'AC', 'Del', '=']
    }
  },

  methods: {
    buttonPress(n) {

      // Numeric value or operator
      if (!(['AC', '=', 'exp', 'log', 'Del'].includes(n))) {
        this.calculation_value += n + '';
      }

      // Clear button
      if (n === 'AC') {
        this.calculation_value = '';
      }

      // exp and log buttons
      if (n === 'exp' || n === 'log') {
        this.calculation_value += n + '(';
      }

      // Del button
      if (n === 'Del') {
        this.calculation_value = this.calculation_value.slice(0, this.calculation_value.length - 1);
      }

      // Equals button
      if (n === '=') {
        this.calculate();
      }
    },
    calculate:function() {

      const path = 'http://localhost:6969/users' // Not sure on the correct path
      axios.post(path, { params: this.calculation_value})

        .then((res) => {
          this.calculation_value = res.data;
        }) 
        .catch((error) => {
          console.error(error);
        })
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
  background-color: #13a527;
  width: 123px;
}

.del_button {
  background-color: #EDAE49
}

.blank {
  visibility: hidden;
}
</style>
