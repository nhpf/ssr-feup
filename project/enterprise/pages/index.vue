<template>
  <section class="section">
    <div class="container">
      <h1 class="title">
        This is the Enterprise Vault app
      </h1>
      <p class="subtitle">
        Here you can safely store an image and a secret phrase.<br>
        <strong>Login</strong> below to start using it.
      </p>
      <nuxt-link to="/login" class="button is-primary is-large is-link">
        Let's Go!
      </nuxt-link>
    </div>
  </section>
</template>

<script>
export default {
  name: "index"
}
</script>

<style scoped>

</style>
