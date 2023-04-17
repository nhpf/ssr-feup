<template>
  <div
    class="section is-flex is-flex-direction-column is-fullwidth is-fullheight is-align-items-center"
  >
    <div class="card is-centered">
      <div class="card-content">
        <p class="title">Log into your vault</p>
        <div>
          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input
                class="input"
                :class="{
                  'is-danger': email.length && !isEmailValid,
                  'is-success': email.length && isEmailValid,
                }"
                type="email"
                placeholder="Email input"
                v-model="email"
              />
            </div>
            <p v-if="email.length && !isEmailValid" class="help is-danger">
              This email is invalid
            </p>
          </div>

          <div class="field">
            <label class="label">Password</label>
            <div class="control has-icons-right">
              <input
                class="input"
                :class="{
                  'is-danger': isPasswordTooShort || isPasswordTooLong,
                  'is-success':
                    password.length &&
                    !isPasswordTooShort &&
                    !isPasswordTooLong,
                }"
                :type="displayPassword ? 'text' : 'password'"
                placeholder="Password"
                v-model="password"
              />
              <span
                v-if="password.length"
                class="icon is-small is-right is-action"
                @click="displayPassword = !displayPassword"
              >
                <img src="@/assets/icons/eye.svg" alt="toogle visibility" />
              </span>
            </div>
            <p v-show="isPasswordTooShort" class="help is-danger">
              Your password is too short!
            </p>
            <p v-show="isPasswordTooLong" class="help is-danger">
              Your password is too long!
            </p>
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <div class="card-footer-item">
          <button
            @click="loginAction"
            class="button is-primary is-medium"
            style="width: 200px"
            :disabled="!isEmailValid || isPasswordTooShort || isPasswordTooLong"
          >
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

<script lang="ts">
import { ref, computed } from "vue";
import { signInWithEmailAndPassword } from "@firebase/auth";
export default {
  setup() {
    const email = ref("");
    const password = ref("");
    const displayPassword = ref(false);

    const isEmailValid = computed(() => {
      const emailRegex =
        /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
      return emailRegex.test(email.value);
    });

    const isPasswordTooShort = computed(
      () => password.value.length > 0 && password.value.length < 6
    );
    const isPasswordTooLong = computed(() => password.value.length > 20);

    const { auth } = useFirebase();
    const router = useRouter();
    const loginAction = () => {
      signInWithEmailAndPassword(auth, email.value, password.value)
        .then(() => {
          router.push({ path: "/vault" });
        })
        .catch((e) => {
          console.log(e);
          alert(e.message);
        });
    };

    return {
      email,
      password,
      displayPassword,
      isEmailValid,
      isPasswordTooShort,
      isPasswordTooLong,
      loginAction,
    };
  },
};
</script>
