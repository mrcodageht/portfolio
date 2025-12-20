import { fetchProjects } from "../function.js";
import { log, logObj, TYPE } from "../log.js";

async function openProjectModal(id = null) {
    const modal = new bootstrap.Modal(document.getElementById('projectModal'));
    const title = document.getElementById('projectModalTitle');

    if (id) {
        const project = await fetchProjects(id);
        title.textContent = 'Modifier le Projet';
        document.getElementById('projectId').value = project.pid;
        document.getElementById('projectTitle').value = project.title;
        document.getElementById('projectDescription').value = project.description;
        document.getElementById('projectStatus').value = project.status;
        document.getElementById('projectVisibility').value = project.visibility;
        document.getElementById('projectUrl').value = project.live_url || '';
        document.getElementById('projectRepoUrl').value = project.repo_url || '';
        document.getElementById('projectCover').value = project.cover_image_url || '';
        //document.getElementById('projectTech').value = project.technologies.join(', ');
        document.getElementById('projectDateStart').value =
            project.start_at
                ? new Date(project.start_at).toISOString().split('T')[0]
                : '';
        document.getElementById('projectDateEnd').value =
            project.end_at
                ? new Date(project.end_at).toISOString().split('T')[0]
                : '';

    } else {
        title.textContent = 'Nouveau Projet';
        document.getElementById('projectForm').reset();
        document.getElementById('projectId').value = '';
    }

    modal.show();
}

function saveProject() {
    const id = document.getElementById('projectId').value;
    const project = {
        id: id || Date.now(),
        title: document.getElementById('projectTitle').value,
        description: document.getElementById('projectDescription').value,
        url: document.getElementById('projectUrl').value,
        technologies: document.getElementById('projectTech').value.split(',').map(t => t.trim()),
        date: document.getElementById('projectDate').value
    };


    document.getElementById("new-proj").addEventListener('click', e => {
        openProjectModal()
    })
    aw
    if (id) {
        const index = projects.findIndex(p => p.id == id);
        projects[index] = project;
    } else {
        projects.push(project);
    }

    renderProjects();
    updateStats();
    bootstrap.Modal.getInstance(document.getElementById('projectModal')).hide();
}

function deleteProject(pid) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce projet ?')) {
        projects = projects.filter(p => p.pid !== pid);
        renderProjects();
        updateStats();
    }
}

async function renderProjects() {
    const list = document.getElementById('projectsList');
    const projects = await fetchProjects()
    logObj(TYPE.INFO, projects)
    // <td>${p.technologies.map(t => `<span class="badge-tech">${t}</span>`).join('')}</td>
    for (const p of projects) {
        let idEdit = `edit-${p.pid}`
        let idDelete = `delete-${p.pid}`
        let badgeClass = ""
        if (p.status === "in_progress") {
            badgeClass = "text-bg-success"
        } else if (p.status === "planning") {
            badgeClass = "text-bg-warning"
        } else if (p.status === "finished") {
            badgeClass = "text-bg-secondary"
        }
        const iconVisibility = p.visibility === "private" ? '<i class="fa-solid fa-lock"></i>' : '<i class="fa-solid fa-lock-open"></i>'
        list.innerHTML += `
                <tr>
                    <td>${iconVisibility}</td>
                    <td><strong>${p.title}</strong></td>
                    <td></td>
                    
                    <td>${new Date(p.start_at).toLocaleDateString('fr-FR')}</td>
                    <td>
                        <span class="badge rounded-pill ${badgeClass}">${p.status}</span>
                    </td>
                    <td class="table-actions">
                        <button class="btn btn-sm btn-warning edit-project" id="${idEdit}">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger delete-project" id="${idDelete}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `

        /* document.getElementById(idEdit).addEventListener('click', e => openProjectModal(p.pid))
        document.getElementById(idDelete).addEventListener('click', e => deleteProject(p.pid)) */

    }
}


document.getElementById("new-proj").addEventListener('click', e => {
    openProjectModal()
})
await renderProjects()

const allBtnEdit = document.querySelectorAll(".edit-project")
const allBtnDelete = document.querySelectorAll(".delete-project")

allBtnDelete.forEach(btn => {
    btn.addEventListener('click', e => {
        const id = btn.id.split("-")
        deleteProject(id[1])
    })
})

allBtnEdit.forEach(btn => {
    btn.addEventListener('click', e => {
        const id = btn.id.split("-")
        log(TYPE.DEBUG, `Edit du projet ${id[1]}`)
        openProjectModal(id[1])
    })

})