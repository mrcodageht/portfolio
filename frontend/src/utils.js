import { router } from "./router";

export function unloader() {
    const loader = document.getElementById("main-content-loader");
      const unloader = document.getElementById("main-content-unloader");
      
      if (loader != undefined && unloader != undefined) {
          loader.classList.add("d-none");
          unloader.classList.remove("d-none");
      }
}

export async function reload() {
    const url = window.location.pathname
    history.pushState({}, "", url)
    await router()
}