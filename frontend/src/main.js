import { router } from "./router.js";
import { log, TYPE } from "./scripts/log.js";
import { renderSidebar } from "./components/sidebar.js";
import './style.css'
import { login } from "./views/login.js";

log(TYPE.DEBUG, "Script charge!");


login().then(() => {
  router()
  renderSidebar()
})

