import { renderCollaborators } from "./views/collaborators.js";
import { renderHome } from "./views/home.js";
import { login, renderLogin } from "./views/login.js";
import { renderMedias } from "./views/medias.js";
import { renderProjects } from "./views/projects.js";
import { renderTechnologies } from "./views/technologies.js";

const routes = {
    "":renderHome,
    "/": renderHome,
    "/login": login,
    "/projects": renderProjects,
    "/collaborators": renderCollaborators,
    "/technologies": renderTechnologies,
    "/medias":renderMedias
}

export function router() {
    const path = window.location.pathname;
    routes[path]?.();
}