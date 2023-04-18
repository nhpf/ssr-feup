<template>
  <div class="bg-container">
    <div class="top-gradient" />
    <img
      src="/favicon.ico"
      width="38"
      alt="favicon"
      style="position: absolute; top: 12px; left: 10px"
    />
    <h1 style="position: absolute; top: 10px; left: 50px" class="is-clickable">
      <nuxt-link to="/">EnterpriseVault</nuxt-link>
    </h1>
    <button
      v-if="isLoggedIn"
      @click="signOutHandler"
      class="button is-small is-danger is-action"
      style="position: absolute; top: 16px; right: 10px; z-index: 9"
    >
      Sign Out
    </button>
    <img src="@/assets/icons/vault.svg" alt="Vault" class="vault-img" />
    <div
      style="width: 100%; height: 100%; position: relative; z-index: 2"
      class="is-flex is-align-items-center is-justify-content-center"
    >
      <!--TODO: do proper routing redirection later-->
      <vault v-if="isLoggedIn" />
      <RouterView v-else />
    </div>
    <div class="bottom-gradient" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { onAuthStateChanged, signOut } from "@firebase/auth";
import Vault from "~/pages/vault.vue";

const isLoggedIn = useState("isLoggedIn", () => false);
const userId = useState("userId", () => "");

const { auth } = useFirebase();
onMounted(() => {
  onAuthStateChanged(auth, (user) => {
    console.log("AUTH WATCHER!");
    isLoggedIn.value = !!user;
    userId.value = user ? user.uid : "";
  });
});

const router = useRouter();
const signOutHandler = () => {
  signOut(auth).then(() => {
    isLoggedIn.value = false;
    router.push({ path: "/" });
  });
};
</script>

<style lang="sass">
@import "@/assets/styles.sass"
@import "bulma/bulma.sass"
h1
  font-size: xx-large
  font-weight: bold
  z-index: 9
h1 > a
  color: $text !important
.bg-container
  background-color: $background
  height: 100vh
.vault-img
  position: absolute
  top: 50%
  left: 50%
  width: min(70vw, 80vh)
  height: min(70vw, 80vh)
  margin-top: max(-35vw, -40vh)
  margin-left: max(-35vw, -40vh)
  z-index: 1
  opacity: 0.02
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
