/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [],
    theme: {
        extend: {
            container: {
                center: true,
                padding: {
                    DEFAULT: '1rem',
                    sm: '2rem',
                    lg: '4rem',
                    xl: '5rem'

                }
            },
            colors: {
                'primary': '#FF6363',
                'secondary': {
                    100: '#E2E2D5',
                    200: '#888883'
                }
            }
        }
    },
}
