import { router } from "./router.js";
import { renderSidebar } from "./components/sidebar.js";
import './style.css'
import { login } from "./views/login.js";



export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export const COOKIE_NAME_TOKEN = import.meta.env.VITE_COOKIE_NAME_TOKEN??'access_token';

login().then(() => {
  router()
  renderSidebar()
})

