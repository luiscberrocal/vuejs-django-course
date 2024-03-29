// composables/useLogin.js
import {ref} from 'vue';
import {useAuthStore} from '@/stores/auth'; // Import your auth store

export function useLoginComposable() {
    const username = ref('');
    const password = ref('');
    const errorMessage = ref('');

    const authStore = useAuthStore();

    const login = async () => {
        try {
            const {token} = await $fetch('http://127.0.0.1:8000/api/auth-token/', {
                method: 'POST',
                body: JSON.stringify({username: username.value, password: password.value}),
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Request-Headers': 'Content-Type, Authorization', // This line is not a fix for CORS but demonstrates how to add headers
                    'Access-Control-Request-Method': 'POST', // This line is not a fix for CORS but demonstrates how to add headers
                },
            }) //.then(res => res.json());
            //console.log('response', response)
            authStore.setToken(token); // Save the token using your auth store
            errorMessage.value = '';
            console.log('token', token);
            // Redirect or perform additional actions on successful login
        } catch (error) {
            console.error("ERROR:", error)
            errorMessage.value = 'Failed to login. Please check your credentials.';
        }
    };

    return {
        username,
        password,
        login,
        errorMessage,
    };
}
