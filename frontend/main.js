import { fetchStats } from "./function.js";
import { log, TYPE } from "./log.js";

log(TYPE.DEBUG, "Script charge!");

// Fonction pour gérer le toggle de la sidebar
document.addEventListener("DOMContentLoaded", function () {
  // Créer le bouton hamburger
  const hamburger = document.createElement("button");
  hamburger.className = "hamburger-btn";
  hamburger.innerHTML = '<i class="fas fa-bars"></i>';
  hamburger.setAttribute("aria-label", "Toggle menu");
  document.body.appendChild(hamburger);

  // Créer l'overlay
  const overlay = document.createElement("div");
  overlay.className = "sidebar-overlay";
  document.body.appendChild(overlay);

  const hamburgerBtn = document.querySelector(".hamburger-btn");
  const sidebar = document.querySelector(".sidebar");
  const sidebarOverlay = document.querySelector(".sidebar-overlay");
  const menuLinks = document.querySelectorAll(".sidebar-menu a");

  // Toggle sidebar
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

  // Fermer la sidebar
  function closeSidebar() {
    sidebar.classList.remove("active");
    sidebarOverlay.classList.remove("active");
    const icon = hamburgerBtn.querySelector("i");
    icon.className = "fas fa-bars";
  }

  // Event listeners
  hamburgerBtn.addEventListener("click", toggleSidebar);
  sidebarOverlay.addEventListener("click", closeSidebar);

  // Fermer la sidebar quand on clique sur un lien (mobile)
  menuLinks.forEach((link) => {
    link.addEventListener("click", function () {
      if (window.innerWidth <= 992) {
        closeSidebar();
      }
    });
  });

  // Fermer la sidebar quand on redimensionne la fenêtre
  window.addEventListener("resize", function () {
    if (window.innerWidth > 992) {
      closeSidebar();
    }
  });
});
function updateStats(stats) {
  try {
    document.getElementById("projectCount").textContent = stats.projects;
    document.getElementById("techCount").textContent = stats.technologies;
    document.getElementById("collabCount").textContent = stats.collaborators;
  } catch (e) {
    return;
  }
}

const init = async () => {
  let collaborators = [];
  const stats = await fetchStats();

  // Initialize with sample data
  // Initial render
  // renderProjects();
  // renderTechnologies();
  // renderCollaborators();
  updateStats(stats);
};

await init();
