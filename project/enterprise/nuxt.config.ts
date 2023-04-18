// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Create a SPA
  ssr: false,

  // Enable nuxt inspection devtools
  // devtools: true,

  app: {
    head: {
      charset: "utf-8",
      viewport: "width=device-width, initial-scale=1",
      title: "Enterprise Vault",
    },
  },

  runtimeConfig: {
    public: {
      fbApiKey: process.env.FB_API_KEY,
      fbAuthDomain: process.env.FB_AUTH_DOMAIN,
      fbProjectId: process.env.FB_PROJECT_ID,
      fbStorageBucket: process.env.FB_STORAGE_BUCKET,
      fbMessagingSenderId: process.env.FB_MESSAGING_SENDER_ID,
      fbAppId: process.env.FB_APP_ID,
    },
  },
});
