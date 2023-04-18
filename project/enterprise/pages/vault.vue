<template>
  <div
    class="section is-flex is-flex-direction-column is-fullwidth is-fullheight is-align-items-center"
  >
    <div v-if="user.name.length" class="card is-centered">
      <div class="card-content">
        <p class="title">{{ user.name }}'s Vault</p>
        <div v-if="!isEditing">
          <div><b>Secret</b>: {{ user.secret }}</div>
          <div>
            <b>Image</b>:
            <template v-if="user.imageUrl.length">
              <br /><img :src="user.imageUrl" alt="Your image" width="250" />
            </template>
            <span v-else>None</span>
          </div>
        </div>

        <button
          @click="isEditing = !isEditing"
          class="button is-medium is-fullwidth"
          :class="{
            'is-primary mt-4': !isEditing,
            'is-danger mb-4': isEditing,
          }"
        >
          {{ isEditing ? "Stop editing" : "Edit" }}
        </button>

        <div v-if="isEditing">
          <div class="field">
            <label class="label">Secret</label>
            <div class="control">
              <input
                class="input"
                type="text"
                placeholder="Secret"
                v-model="newSecret"
              />
            </div>
          </div>

          <div class="file has-name is-boxed">
            <label class="file-label">
              <input
                class="file-input"
                type="file"
                accept="image/png"
                name="image"
                @change="handleFileChange"
              />
              <span class="file-cta">
                <span class="file-label"> Choose an image </span>
              </span>
              <span v-if="selectedFileName.length" class="file-name">{{
                selectedFileName
              }}</span>
            </label>
          </div>

          <button
            @click="updateUserData"
            class="button is-primary is-medium is-fullwidth mt-4"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
    <div v-else class="is-centered"><i>Loading...</i></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { doc, getDoc, updateDoc } from "@firebase/firestore";
import {
  ref as storageRef,
  uploadBytes,
  getDownloadURL,
} from "firebase/storage";

const isEditing = ref(false);
const newSecret = ref("");

const user = ref<User>({
  name: "",
  secret: "",
  imageUrl: "",
});
const userId = useState("userId", () => "");

// Fetch user data
const { usersCol } = useDBSchema();
onMounted(() => {
  getDoc(doc(usersCol, userId.value)).then((doc) => {
    if (doc.exists()) {
      user.value = doc.data();
      newSecret.value = user.value.secret;
    }
  });
});

let selectedFile = null;
const selectedFileName = ref("");
const { storage } = useFirebase();
const handleFileChange = (e) => {
  if (e.target.files.length) {
    selectedFile = e.target.files[0];
    selectedFileName.value = e.target.files[0].name;
  }
};

const updateUserData = () => {
  if (selectedFile) {
    const userImageRef = storageRef(storage, `users/${userId.value}.png`);
    uploadBytes(userImageRef, selectedFile)
      .then(async (res) => {
        getDownloadURL(res.ref).then((downloadURL) => {
          updateDoc(doc(usersCol, userId.value), {
            imageUrl: downloadURL,
          });
          user.value.imageUrl = downloadURL;
        });
      })
      .catch((e) => console.log(e));
  }
  if (selectedFile || user.value.secret !== newSecret.value) {
    updateDoc(doc(usersCol, userId.value), {
      name: user.value.name,
      secret: newSecret.value,
    })
      .then(() => {
        console.log("Added a new secret");
        user.value.secret = newSecret.value;
      })
      .catch((e) => console.log(e));
  }
  isEditing.value = false;
};
</script>
