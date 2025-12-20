import { fetchTechs } from "../function.js";

function setupAllEventListener() {
    document.body.addEventListener('click', e => {
        if (e.target.id === "new-tech") {
            openTechModal()
            return
        }


    })
}

async function openTechModal(id = null) {

    const technologies = await fetchTechs()
    const modal = new bootstrap.Modal(document.getElementById('techModal'));
    const title = document.getElementById('techModalTitle');
    const selectList = document.getElementById("techCategory")
    // let compt = 0
    // for (const t of technologies) {
    //     compt++
    //     selectList.innerHTML += `
    //         <option value="">${t.type}</option>

    //     `
    // }
    if (id) {
        const tech = technologies.find(t => t.id === id);
        title.textContent = 'Modifier la Technologie';
        document.getElementById('techId').value = tech.id;
        document.getElementById('techName').value = tech.name;
        document.getElementById('techCategory').value = tech.type;
        document.getElementById('techIcon').value = tech.icon_url;
    } else {
        title.textContent = 'Nouvelle Technologie';
        document.getElementById('techForm').reset();
        document.getElementById('techId').value = '';
    }

    modal.show();
}

function saveTech() {
    const id = document.getElementById('techId').value;
    const tech = {
        id: id || Date.now(),
        name: document.getElementById('techName').value,
        category: document.getElementById('techCategory').value,
        level: document.getElementById('techLevel').value
    };

    if (id) {
        const index = technologies.findIndex(t => t.id == id);
        technologies[index] = tech;
    } else {
        technologies.push(tech);
    }

    renderTechnologies();
    updateStats();
    bootstrap.Modal.getInstance(document.getElementById('techModal')).hide();
}

function deleteTech(id) {
    if (confirm('Êtes-vous sûr de vouloir supprimer cette technologie ?')) {
        technologies = technologies.filter(t => t.id !== id);
        renderTechnologies();
        updateStats();
    }
}

async function renderTechnologies() {
    const list = document.getElementById('techList');
    const technologies = await fetchTechs()

    //<td>${t.level}</td>
    for (const t of technologies) {
        let idEdit = `edit-${t.id}`
        let idDelete = `delete-${t.id}`
        list.innerHTML += `
                <tr>
                    <td>
                        <img width="40" height="40" src="https://cdn.jsdelivr.net/gh/homarr-labs/dashboard-icons/svg/java.svg">
                    </td>
                    <td><strong>${t.name}</strong></td>
                    <td><span class="badge bg-primary">${t.type}</span></td>
                    <td class="table-actions">
                        <button class="btn btn-sm btn-warning edit-tech" id="${idEdit}">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger delete-tech" id="${idDelete}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                </tr>
            `
    }
}

await renderTechnologies()
setupAllEventListener()
const allBtnDelete = document.querySelectorAll(".delete-tech")

const allBtnEdit = document.querySelectorAll(".edit-tech")

allBtnDelete.forEach(btn => {
    btn.addEventListener('click', e => {
        const id = btn.id.split("-")
        deleteTech(id[1])
    })
})
allBtnEdit.forEach(btn => {
    btn.addEventListener('click', async () => {
        const id = btn.id.split("-")
        await openTechModal(id[1])
    })
})

