import { Project, TechnologyProjectCreate } from "../class.js";
import {
  addProject,
  addTechIntoProject,
  delProject,
  fetchProjects,
  fetchTechs,
  fetchTechsProject,
  removeTechIntoProject,
  updateProject,
} from "../function.js";
import { log, logObj, TYPE } from "../log.js";

function setGlobalListerner() {
  const allBtnEdit = document.querySelectorAll(".edit-project");
  const allBtnDelete = document.querySelectorAll(".delete-project");
  const btnSaveProject = document.getElementById("saveProject");

  allBtnDelete.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const id = btn.id.split("-");
      deleteProject(id[1]);
    });
  });

  allBtnEdit.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const id = btn.id.split("-");
      log(TYPE.DEBUG, `Edit du projet ${id[1]}`);
      openProjectModal(technologies, id[1]);
    });
  });

  btnSaveProject.addEventListener("click", (e) => {
    const form = document.getElementById("projectForm");
    saveProject(form);
  });
}

async function openProjectModal(technologies, id = null) {
  const modal = new bootstrap.Modal(document.getElementById("projectModal"));
  const title = document.getElementById("projectModalTitle");

  if (id) {
    const project = await fetchProjects(id);
    title.textContent = "Modifier le Projet";
    document.getElementById("projectId").value = project.pid;
    document.getElementById("projectTitle").value = project.title;
    document.getElementById("projectDescription").value = project.description;
    document.getElementById("projectStatus").value = project.status;
    document.getElementById("projectVisibility").value = project.visibility;
    document.getElementById("projectUrl").value = project.live_url || "";
    document.getElementById("projectRepoUrl").value = project.repo_url || "";
    document.getElementById("projectCover").value =
      project.cover_image_url || "";
    const dropdownTech = document.getElementById("dropdown-tech");
    const stacks = document.getElementById("stacks");
    stacks.innerHTML = "";

    dropdownTech.innerHTML = ""; // reset

    for (const t of technologies) {
      let isSelected = "";
      for (const tp of project.technologies) {
        if (tp.name === t.name) {
          stacks.innerHTML += `${t.name},`;
          isSelected = "checked";
          break;
        }
      }
      dropdownTech.innerHTML += `
        <div class="form-check">
            <input
                class="form-check-input"
                        type="checkbox"
                        value="${t.slug}"
                        id="check-${t.id}"
                        name="stack-tech"
                        ${isSelected}
                      />
                      <label class="form-check-label" for="checkDefault">
                        ${t.name}
                      </label>
                    </div>
    `;
    }

    document.getElementById("projectDateStart").value = project.start_at
      ? new Date(project.start_at).toISOString().split("T")[0]
      : "";
    document.getElementById("projectDateEnd").value = project.end_at
      ? new Date(project.end_at).toISOString().split("T")[0]
      : "";
  } else {
    title.textContent = "Nouveau Projet";
    document.getElementById("projectForm").reset();
    document.getElementById("projectId").value = "";
    const dropdownTech = document.getElementById("dropdown-tech");
    const stacks = document.getElementById("stacks");
    stacks.innerHTML = "";

    dropdownTech.innerHTML = ""; // reset

    for (const t of technologies) {
      
      dropdownTech.innerHTML += `
        <div class="form-check">
            <input
                class="form-check-input"
                        type="checkbox"
                        value="${t.slug}"
                        id="check-${t.id}"
                        name="stack-tech"
                      />
                      <label class="form-check-label" for="checkDefault">
                        ${t.name}
                      </label>
                    </div>
    `;
    }
  }

  modal.show();
}

async function saveProject(form) {
  const id = document.getElementById("projectId").value;
  const technologies = document.getElementsByName("stack-tech");
  const endDate = document.getElementById("projectDateEnd").value;
  let techs = [];

  technologies.forEach((t) => {
    if (t.checked) {
      console.log("Tech checked : ", t.value);
      techs.push(new TechnologyProjectCreate(t.value));
    }
  });

  const project = new Project(
    document.getElementById("projectTitle").value,
    document.getElementById("projectDescription").value,
    document.getElementById("projectStatus").value,
    document.getElementById("projectVisibility").value,
    document.getElementById("projectDateStart").value,
    endDate !== "" ? endDate : null,
    document.getElementById("projectCover").value,
    document.getElementById("projectUrl").value,
    document.getElementById("projectRepoUrl").value
  );

  if (id) {
    logObj(TYPE.DEBUG, project, "project a cree : ");
    try {
      const projectUpdated = await updateProject(id, project);
      //   on va mettre a jour les technologies du projects aussi
      let techsProject = await fetchTechsProject(projectUpdated.pid);
      console.log("techs project : ", techsProject);
      const techMapped = [];
      for (const t of techsProject) {
        techMapped.push(new TechnologyProjectCreate(t.slug));
      }
      //    les technologie a enlever
      techMapped.forEach(async (t) => {
        console.log("tech : ", t);
        const isExists = techs.find((tp) => tp.slug === t.slug);
        if (!isExists) {
          // on enleve
          await removeTechIntoProject(t.slug, projectUpdated.pid);
        }
      });

      await addTechIntoProject(techs, projectUpdated.pid);
    } catch (error) {
      // on recharge la page
      console.error(error);
      window.location.href = window.location.href;
      return;
    }
  } else {
    try {
      const projectCreated = await addProject(project)
      
      await addTechIntoProject(techs, projectCreated.pid);
    } catch (error) {
      console.error(error);
      window.location.href = window.location.href;
      return;
    }
    projects.push(project);
  }

  const modalEl = document.getElementById("projectModal");
  const modal = bootstrap.Modal.getInstance(modalEl);
  modal.hide();

  window.location.href = window.location.href;
}

function deleteProject(pid) {

  const modal = new bootstrap.Modal(document.getElementById("projectModalDel"));

  document.getElementById("text-del").innerHTML = "Êtes-vous sûr de vouloir supprimer ce projet ?"
  document.getElementById("btn-del-proj").addEventListener('click', async () => {
    console.log("Demande de suppression");
    try {
      await delProject(pid)
    } catch (error) {
        console.error(error);
      }
    window.location.href = window.location.href;
  })
  
  modal.show()
}

async function renderProjects() {
  const list = document.getElementById("projectsList");
  list.innerHTML = "";
  const projects = await fetchProjects();
  logObj(TYPE.INFO, projects);
  for (const p of projects) {

  
    let idEdit = `edit-${p.pid}`;
    let idDelete = `delete-${p.pid}`;
    let badgeClass = "";
    if (p.status === "in_progress") {
      badgeClass = "text-bg-success";
    } else if (p.status === "planning") {
      badgeClass = "text-bg-warning";
    } else if (p.status === "finished") {
      badgeClass = "text-bg-secondary";
    }
    
        list.innerHTML += `
                <tr>
                    <td><strong>${p.title}</strong></td>

                    
                    
                    <td>${new Date(p.start_at).toLocaleDateString("fr-FR")}</td>
                    <td>
                        <span class="badge rounded-pill ${badgeClass}">${
      p.status
    }</span>
                    </td>
                    <td>
                    
                    <a class="btn btn-primary voir-tech" data-tech-id="${p.pid}">Voir techs</a>
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
            `;

    /* document.getElementById(idEdit).addEventListener('click', e => openProjectModal(p.pid))
        document.getElementById(idDelete).addEventListener('click', e => deleteProject(p.pid)) */
  }

  document.querySelectorAll(".voir-tech").forEach(btn => {
    btn.addEventListener('click', async (e) => {

  const modal = new bootstrap.Modal(document.getElementById("projectModalTech"));
      const pid = e.currentTarget.getAttribute("data-tech-id")

      const bodyTech = document.getElementById("body-tech-proj")
      bodyTech.innerHTML = ""
      const techs = await fetchTechsProject(pid)
      techs.forEach(t => {
       bodyTech.innerHTML +=` 
        <span class="badge-tech">${t.name}</span>
        `
      })
      modal.show()
    })
  })
}

const technologies = await fetchTechs();
await renderProjects();
document.getElementById("new-proj").addEventListener("click", (e) => {
  openProjectModal(technologies);
});
setGlobalListerner();
