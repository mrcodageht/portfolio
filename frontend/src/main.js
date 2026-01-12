import { router } from "./router.js";
import { renderSidebar } from "./components/sidebar.js";
import './style.css'
import { login } from "./views/login.js";



export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

login().then(() => {
  router()
  renderSidebar()
})

