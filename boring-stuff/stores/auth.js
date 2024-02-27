// stores/auth.js
import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
  }),
  actions: {
    setToken(newToken) {
      this.token = newToken;
      localStorage.setItem('authToken', newToken); // Save the token to local storage
    },
    getToken() {
      this.token = localStorage.getItem('authToken');
    },
  },
});
