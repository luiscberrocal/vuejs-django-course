// composables/useLogin.js
import { ref } from 'vue';
//import axios from 'axios';
import { useAuthStore } from '@/stores/auth'; // Import your auth store

export function useLoginComposable() {
  const username = ref('');
  const password = ref('');
  const errorMessage = ref('');

  const authStore = useAuthStore();

  const login = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth-token/', {
        username: username.value,
        password: password.value,
      });
      authStore.setToken(response.data.token); // Save the token using your auth store
      errorMessage.value = '';
      // Redirect or perform additional actions on successful login
    } catch (error) {
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
