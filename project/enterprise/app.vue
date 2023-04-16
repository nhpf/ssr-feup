<template>
  <div class="bg-container">
    <div class="top-gradient" />
    <img
      src="/favicon.ico"
      width="38"
      alt="favicon"
      style="position: absolute; top: 12px; left: 10px"
    />
    <h1 style="position: absolute; top: 10px; left: 50px">EnterpriseVault</h1>
    <div
      style="width: 100%; height: 100%; position: relative; z-index: 2"
      class="is-flex is-align-items-center is-justify-content-center"
    >
      <RouterView />
    </div>
    <div class="bottom-gradient" />
  </div>
</template>

<script setup lang="ts"></script>

<style lang="sass">
@import "@/assets/styles.sass"
@import "bulma/bulma.sass"
h1
  font-size: xx-large
  font-weight: bold
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
