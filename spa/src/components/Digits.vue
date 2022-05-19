<template>
  <div>
    <div id="canvas" class='place-content-center w-100 grid gap-0 grid-cols-25 border'>
      <div class ="w-4 h-4 border" v-for="(n, i) in 625" :key='i' v-bind:id="i" @mouseover="draw(i)" @click="draw(i, click=true)"></div>
    </div>
    <button class="border" @click="printCanvas()">Print Canvas</button>
    <p></p><br>
    <button class="border" @click="classifyDigit()">Classify</button>
  </div>
</template>


<script>
import "../util/request"
let isDrawing = false

export default {
  data() {
    return{
      canvasArray: []
    }  
  },
  mounted: function(){
    (this.canvasArray = []).length = 625; this.canvasArray.fill(0)
    const c = document.getElementById('canvas');
    c.addEventListener('mousedown', e => {
      isDrawing = true
      //console.log(isDrawing)
    })
    c.addEventListener('mouseup', e => {
      isDrawing = false
      //console.log(isDrawing)
    })
  },

  methods: {
    draw(i, click){
      if(isDrawing){
        document.getElementById(i).classList.add('bg-black')
        this.canvasArray[i] = 1
      } else if(click === true){
        document.getElementById(i).classList.add('bg-black')
        this.canvasArray[i] = 1
      }
    },
    printCanvas(){
      console.log(this.canvasArray)
    },
    classifyDigit(){
      this.$store.dispatch('Digit', [1,2,3,4,5])
      console.log(this.$store.state.classification)
    }
  }
}

</script>



