// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue'; // Import the plugin

export default defineConfig({
  plugins: [
    vue(), // Add the plugin to the plugins array
    // ... other plugins
  ],
});
