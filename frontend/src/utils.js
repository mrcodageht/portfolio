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


export async function toasts(params) {
    document.getElementById('main').innerHTML += `
    <div class="toast align-items-center text-bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>
    `
}

export async function errorToasts(message) {
    const errorModal = document.getElementById("error-modal")

    if (errorModal === undefined) return
    
    errorModal.innerText = message
    errorModal.classList.remove('d-none')
}

export async function cleanToatsError() {
    const errorModal = document.getElementById("error-modal")

    if (errorModal === undefined) return
    errorModal.innerText = ""
    errorModal.classList.add('d-none')

}