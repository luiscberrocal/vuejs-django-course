// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    ssr: false,
    devtools: {enabled: true},
    modules: [
        '@nuxtjs/tailwindcss',
        '@pinia/nuxt',
    ],
    pinia: {
        storesDirs: ['./stores/**',],
    },
    app: {
        head: {
            title: 'Boring Stugg',
            meta: [
                {charset: 'utf-8'},
                {name: 'viewport', content: 'width=device-width, initial-scale=1'},
                {name: 'description', content: 'Boring stugg application'},
            ],
            link: [
                {rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined'},
            ]
        }
    },
})
