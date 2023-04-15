<template>
  <div class="bg-container">
    <div class="top-gradient"/>
    <div style="width: 100%; position: relative; z-index: 2;">
      <RouterView/>
    </div>
    <div class="bottom-gradient"/>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="sass">
@import "@/assets/styles.sass"
@import "bulma/bulma.sass"
.bg-container
  background-color: $background
  height: 100vh
.top-gradient
  position: fixed
  top: 0
  width: 100vw
  height: 70vh
  background: linear-gradient($grey-dark, $background)
  opacity: 0.4
  z-index: 0
.bottom-gradient
  position: fixed
  bottom: 0
  width: 100vw
  height: 30vh
  background: linear-gradient($background, #000000)
  opacity: 0.4
  z-index: 0
</style>
