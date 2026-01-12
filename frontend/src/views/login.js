
import { postLogin } from "../scripts/function";
import { COOKIE_NAME_TOKEN, getCookie, setCookie } from "/src/scripts/function.js";

export async function renderLogin() {
    
    document.body.innerHTML = `
    <div class="d-flex justify-content-center align-items-center w-100 vh-100 login">
       <form id="login-form">
    
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Courriel</label>
        <input type="email" name="email" class="form-control" id="email" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Mot de passe</label>
        <input type="password" name="password" class="form-control" id="password">
      </div>
      <span id="span-error" class="text-danger mb-3 fw-semibold fst-italic"></span>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Se souvenir</label>
      </div>
      <button type="submit" class="btn btn-primary w-100">Connecter</button>
    </form> 
    </div>
    `
  
}

export async function login() {
  const token = getCookie(COOKIE_NAME_TOKEN);
  if (token === undefined || token === null) {
    renderLogin().then(r => {
const loginForm = document.getElementById("login-form");

      loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const fd = new FormData();
        const form = {
          username: document.getElementById("email").value,
          password: document.getElementById("password").value,
        };

        fd.append("username", form.username);
        fd.append("password", form.password);


        const token = await postLogin(fd);
        if (token === null) {
          document.getElementById("span-error").innerHTML =
            "Identifiants de connexions invalides";
        } else {

          setCookie(COOKIE_NAME_TOKEN, token.access_token, 1);
          const loader = document.getElementById("main-content-loader");
          const unloader = document.getElementById("main-content-unloader");
          if (loader && unloader) {
            loader.classList.add("d-none");
            unloader.classList.remove("d-none");
          }
          window.location.href = window.location.href;
        }
      });
    })
      
  } else {
    
    
  }
}
