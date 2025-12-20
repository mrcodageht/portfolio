import { fetchProjects, fetchTechs } from "./function.js";
import { log, TYPE } from "./log.js";

log(TYPE.DEBUG, "Script charge!")



const init = async () => {
    let collaborators = [];

    // Update dashboard stats>
    function updateStats() {
        document.getElementById('projectCount').textContent = projects.length;
        document.getElementById('techCount').textContent = technologies.length;
        document.getElementById('collabCount').textContent = collaborators.length;
    }

    // Initialize with sample data
    // Initial render
    // renderProjects();
    // renderTechnologies();
    // renderCollaborators();
    // updateStats();
}


await init()