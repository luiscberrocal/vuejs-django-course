// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: {enabled: true},
    modules: [
        '@nuxtjs/tailwindcss',
        '@nuxtjs/color-mode',
        '@nuxt/content',
    ],
    app: {
        pageTransition: {name: 'page', mode: 'out-in'}
    },
    colorMode: {
        classSuffix: ''
    },
    content: {
        watch: {
            ws: {
                hostname: 'localhost'
            }
        },
        highlight: {
            theme: {
                // Default theme (same as single string)
                default: 'github-light',
                // Theme used if `html.dark`
                dark: 'github-dark',
                // Theme used if `html.sepia`
                sepia: 'monokai'
            }
        }
    },
    nitro: {
        prerender: {
            routes: ['/sitemap.xml']
        }
    }

})
