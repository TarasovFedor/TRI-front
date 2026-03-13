// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules:['@pinia/nuxt'],
  typescript:{
    strict:true,
    typeCheck:true,
  },
  ssr:true,
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true }
})
