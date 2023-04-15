<template>
  <div class="section is-flex is-flex-direction-column is-fullwidth is-fullheight is-align-items-center">
    <div class="card is-centered">
      <div class="card-content">
        <p class="title">
          Log into your vault
        </p>
        <div>
          <div class="field">
            <label class="label">Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="Text input">
            </div>
          </div>

          <div class="field">
            <label class="label">Email</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input is-danger" type="email" placeholder="Email input" value="hello@">
              <span class="icon is-small is-left">
                <i class="fas fa-envelope"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-exclamation-triangle"></i>
              </span>
            </div>
            <p class="help is-danger">This email is invalid</p>
          </div>

          <div class="field">
            <label class="label">Password</label>
            <div class="control has-icons-left has-icons-right">
              <input class="input is-success" type="text" placeholder="Password" value="bulma">
              <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
              </span>
              <span class="icon is-small is-right">
                <i class="fas fa-check"></i>
              </span>
            </div>
            <p class="help is-success">This username is available</p>
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <div class="card-footer-item">
          <button class="button is-primary is-medium" style="width: 200px">
            Login
          </button>
        </div>
      </footer>
    </div>
    <div class="is-centered has-text-centered mt-6">
      <h2 class="is-italic">Don't have an account yet?</h2>
      <nuxt-link to="/signup" class="button is-primary is-large is-link mt-2">
        Click here to create one!
      </nuxt-link>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
