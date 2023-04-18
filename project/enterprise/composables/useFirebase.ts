import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "@firebase/auth";
import { getStorage } from "@firebase/storage";

export default function () {
  // Load environment variables
  const config = useRuntimeConfig();

  const firebaseConfig = {
    apiKey: config.public.fbApiKey,
    authDomain: config.public.fbAuthDomain,
    projectId: config.public.fbProjectId,
    storageBucket: config.public.fbStorageBucket,
    messagingSenderId: config.public.fbMessagingSenderId,
    appId: config.public.fbAppId,
  };

  const firebaseApp = initializeApp(firebaseConfig);

  // Firebase services
  const firestore = getFirestore(firebaseApp);
  const auth = getAuth(firebaseApp);
  const storage = getStorage(firebaseApp);

  return {
    auth,
    firestore,
    storage,
  };
}
