import { fetchCollabs } from "../function.js";
import { log, logObj, TYPE } from "../log.js";



async function openCollabModal(id = null) {
    const modal = new bootstrap.Modal(document.getElementById('collabModal'));
    const title = document.getElementById('collabModalTitle');
    if (id) {
        const collab = await fetchCollabs(id);
        title.textContent = 'Modifier le Collaborateur';
        document.getElementById('collabId').value = collab.id;
        document.getElementById('collabFirstname').value = collab.first_name;

        document.getElementById('collabLastname').value = collab.last_name;
        document.getElementById('collabRole').value = collab.role;
        document.getElementById('collabPortfolio').value = collab.portfolio_url || '';
        document.getElementById('collabLinkedin').value = collab.linkedin_url || '';
        document.getElementById('collabGithub').value = collab.github_url || '';
    } else {
        title.textContent = 'Nouveau Collaborateur';
        document.getElementById('collabForm').reset();
        document.getElementById('collabId').value = '';
    }

    modal.show();
}

function saveCollab() {
    const id = document.getElementById('collabId').value;
    const collab = {
        id: id || Date.now(),
        name: document.getElementById('collabName').value,
        role: document.getElementById('collabRole').value,
        email: document.getElementById('collabEmail').value,
        linkedin: document.getElementById('collabLinkedin').value
    };

    if (id) {
        const index = collaborators.findIndex(c => c.id == id);
        collaborators[index] = collab;
    } else {
        collaborators.push(collab);
    }

    renderCollaborators();
    updateStats();
    bootstrap.Modal.getInstance(document.getElementById('collabModal')).hide();
}

function deleteCollab(id) {
    if (confirm('Êtes-vous sûr de vouloir supprimer ce collaborateur ?')) {
        collaborators = collaborators.filter(c => c.id !== id);
        renderCollaborators();
        updateStats();
    }
}

async function renderCollaborators() {
    const list = document.getElementById('collabList');
    const collabs = await fetchCollabs()
    for (const c of collabs) {
        const fullname = `${c.first_name} ${c.last_name}`
        const idEdit = `edit_${c.id}`
        const idDelete = `delete_${c.id}`
        list.innerHTML += `
            <tr>
                <td><strong>${fullname}</strong></td>
                <td>${c.role}</td>
            <td class="">
                    <a href="${c.linkedin_url}" target="_blank" style="text-decoration: none">
                        <img alt="linkedin url ${fullname}" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/linkedin.svg" width=20 height=20/>
                    </a>
                    <a href="${c.github_url}" target="_blank" style="text-decoration: none">
                        <img alt="github url ${fullname}" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/github.svg" width=20 height=20/>
                    </a>
                    <a href="${c.portfolio_url}" target="_blank" style="text-decoration: none">
                        <img alt="portfolio url ${fullname}"  src="/code.png" width=20 height=20/>
                    </a>
                </td>
                <td class="table-actions">
                    <button class="btn btn-sm btn-warning edit-collab" id="${idEdit}">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button class="btn btn-sm btn-danger delete-collab" id="${idDelete}">
                        <i class="fas fa-trash"></i>
                    </button>
                </td>
            </tr>
        `
    }
}


await renderCollaborators()
const allBtnEdit = document.querySelectorAll(".edit-collab")
const allBtnDelete = document.querySelectorAll(".delete-collab")

allBtnDelete.forEach(btn => {
    btn.addEventListener('click', () => {
        const id = btn.id.split("_")[1]
        log(TYPE.DEBUG, `Open modal id : ${id}`)
        deleteCollab(id)
    })
})
allBtnEdit.forEach(btn => {
    btn.addEventListener('click', async () => {
        const id = btn.id.split("_")[1]
        log(TYPE.DEBUG, `Open modal id : ${id}`)
        await openCollabModal(id)
    })
})