import { router } from "../router.js";

export async function renderSidebar() {
    document.querySelector('.sidebar').innerHTML =  /* html */ `
        <div class="sidebar-brand">
            <i class="fas fa-briefcase"></i> Mrcfolio CMS
        </div>
        <ul class="sidebar-menu">
            <li>
                <a href="#" class="menu-link" id="dashboard-link" data-view="dashboard">
                <i class="fas fa-home"></i> Dashboard</a>
            </li>
            <li>
                <a href="projects.html" id="project-link" class="menu-link" data-view="projects"
                ><i class="fas fa-project-diagram"></i> Projets</a
                >
            </li>
            <li>
                <a href="technologies.html" id="tech-link" class="menu-link" data-view="technologies"
                ><i class="fas fa-code"></i> Technologies</a
                >
            </li>
            <li>
                <a
                href="collaborators.html"
                class="menu-link"
                id="collab-link"
                data-view="collaborators"
                ><i class="fas fa-users"></i> Collaborateurs</a
                >
            </li>
<li>
                <a
                href="medias.html"
                class="menu-link"
                id="media-link"
                data-view="medias"
                ><i class="fa-solid fa-photo-film"></i> Medias</a
                >
            </li>
        </ul>
        <div class="d-flex justify-content-center align-items-end w-100 mt-5">
            <button class="btn btn-danger w-100 mx-2">Deconnexion</button>
        </div>
    
    `;
    
    setupNavigation()
    setupAllEventListener()
    setNav()
    
}
const cleanNav = () => {
    document.querySelectorAll(".menu-link").forEach(m => m.classList.remove('active')) 
}

export function setNav(url = undefined) {
    cleanNav()
    url = window.location.pathname
    const sidebar = document.querySelector('.sidebar')
    if (sidebar == undefined && sidebar == null) {
        return
    }
    if (url === "/projects") {
        document.getElementById("project-link").classList.add('active')
    }else if ( url === "/collaborators") {
        document.getElementById("collab-link").classList.add('active')
    }else if (url === "/medias") {
        document.getElementById("media-link").classList.add('active')
    }else if ( url === "/technologies") {
        document.getElementById("tech-link").classList.add('active')
    }else if ( url ==="/" ) {
        document.getElementById("dashboard-link").classList.add('active')
    }
}

function navigateTo(view) {
  const map = {
    dashboard: "/",
    projects: "/projects",
    collaborators: "/collaborators",
    technologies: "/technologies",
    medias: "/medias",
  };

  history.pushState({}, "", map[view]);
  router();
    setNav()
}

function setupNavigation() {
  document.querySelector(".sidebar").addEventListener("click", e => {
    const link = e.target.closest(".menu-link");
    if (!link) return;

    e.preventDefault();
    const view = link.dataset.view;
    navigateTo(view);
  });
}
function setupAllEventListener() {
    document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.createElement("button");
  hamburger.className = "hamburger-btn";
  hamburger.innerHTML = '<i class="fas fa-bars"></i>';
  hamburger.setAttribute("aria-label", "Toggle menu");
  document.body.appendChild(hamburger);

  const overlay = document.createElement("div");
  overlay.className = "sidebar-overlay";
  document.body.appendChild(overlay);

  const hamburgerBtn = document.querySelector(".hamburger-btn");
  const sidebar = document.querySelector(".sidebar");
  const sidebarOverlay = document.querySelector(".sidebar-overlay");
  const menuLinks = document.querySelectorAll(".sidebar-menu a");

  function toggleSidebar() {
    sidebar.classList.toggle("active");
    sidebarOverlay.classList.toggle("active");

    const icon = hamburgerBtn.querySelector("i");
    if (sidebar.classList.contains("active")) {
      icon.className = "fas fa-times";
    } else {
      icon.className = "fas fa-bars";
    }
  }

  function closeSidebar() {
    sidebar.classList.remove("active");
    sidebarOverlay.classList.remove("active");
    const icon = hamburgerBtn.querySelector("i");
    icon.className = "fas fa-bars";
  }

  hamburgerBtn.addEventListener("click", toggleSidebar);
  sidebarOverlay.addEventListener("click", closeSidebar);

  menuLinks.forEach((link) => {
    link.addEventListener("click", function () {
      if (window.innerWidth <= 992) {
        closeSidebar();
      }
    });
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 992) {
      closeSidebar();
    }
  });
});

}




