import { navigateTo } from "../components/sidebar.js";
import { cleanToatsError, errorToasts, PROVIDER, toasts } from "../utils.js";
import { Project, TechnologyProjectCreate } from "./class.js";
import { addCollaboratorIntoProject, fetchCollabs, fetchCollabsProject, fetchRepoGithub, removeCollaboratorIntoProject } from "./function.js";
import {
  addProject,
  addTechIntoProject,
  delProject,
  fetchProjects,
  fetchTechs,
  fetchTechsProject,
  removeTechIntoProject,
  updateProject,
} from "/src/scripts/function.js";

export async function setGlobalListerner() {
  const allBtnEdit = document.querySelectorAll(".edit-project");
  const allBtnDelete = document.querySelectorAll(".delete-project");
  const btnSaveProject = document.getElementById("saveProject");
  const technologies = await fetchTechs();

  allBtnDelete.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const id = btn.id.split("-");
      deleteProject(id[1]);
    });
  });

  allBtnEdit.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const id = btn.id.split("-");
      openProjectModal(technologies, id[1]);
    });
  });

  btnSaveProject.addEventListener("click", async (e) => {
    const form = document.getElementById("projectForm");
    await saveProject(form);
    cleanToatsError();
  });

  document.querySelectorAll(".proj-ext").forEach((btn) => {
    btn.addEventListener("click", () => {
      const modal = new bootstrap.Modal(document.getElementById("modal-git"));
      cleanToatsError("error-global");
      document.getElementById("q-repo").addEventListener("click", async () => {
        const repoInput = document.getElementById("repo-value");
        const repoName = repoInput.value;
        console.log("repo name : ", repoName);
        repoInput?.blur();
        modal.hide();
        const provider =
          btn.id === "gitlab" ? PROVIDER.GITLAB : PROVIDER.GITHUB;
        await openModalProjectGithub(technologies, repoName, provider);
      });
      modal.show();
    });
  });
  document.getElementById("new-proj").addEventListener("click", (e) => {
    openProjectModal(technologies);
  });
  

  document.querySelectorAll(".link-collab-project").forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const pid = e.currentTarget.dataset.projectId
      openModalLinkCollab(pid);
    });
  });
}

async function openProjectModal(technologies, id = null) {
  const modal = new bootstrap.Modal(document.getElementById("projectModal"));
  const title = document.getElementById("projectModalTitle");
  cleanToatsError();

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

async function openModalProjectGithub(
  technologies,
  repoName,
  provider = PROVIDER.GITHUB,
) {
  const modal = new bootstrap.Modal(document.getElementById("projectModal"));
  const modalGit = new bootstrap.Modal(document.getElementById("modal-git"));
  const project = await fetchRepoGithub(repoName, provider).catch((err) => {
    console.error(err);
    errorToasts(err.message, "error-global");
    return;
  });

  //document.getElementById("projectId").value = project.pid;
  document.getElementById("projectTitle").value = project.title;
  document.getElementById("projectDescription").value = project.description;
  document.getElementById("projectStatus").value = project.status;
  document.getElementById("projectVisibility").value = project.visibility;
  document.getElementById("projectUrl").value = project.live_url || "";
  document.getElementById("projectRepoUrl").value = project.repo_url || "";

  const dropdownTech = document.getElementById("dropdown-tech");
  const stacks = document.getElementById("stacks");
  stacks.innerHTML = "";

  dropdownTech.innerHTML = ""; // reset

  for (const t of technologies) {
    let isSelected = "";
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
  modalGit.hide();
  modal.show();
}

async function saveProject(form) {
  const modalEl = document.getElementById("projectModal");
  const modal = bootstrap.Modal.getInstance(modalEl);

  const id = document.getElementById("projectId").value;
  const technologies = document.getElementsByName("stack-tech");
  const endDate = document.getElementById("projectDateEnd").value;
  let techs = [];

  technologies.forEach((t) => {
    if (t.checked) {
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
    document.getElementById("projectUrl").value,
    document.getElementById("projectRepoUrl").value,
  );

  if (id) {
    const projectUpdated = await updateProject(id, project);
    //   on va mettre a jour les technologies du projects aussi
    let techsProject = await fetchTechsProject(projectUpdated.pid);
    const techMapped = [];
    for (const t of techsProject) {
      techMapped.push(new TechnologyProjectCreate(t.slug));
    }
    //    les technologie a enlever
    techMapped.forEach(async (t) => {
      const isExists = techs.find((tp) => tp.slug === t.slug);
      if (!isExists) {
        // on enleve
        await removeTechIntoProject(t.slug, projectUpdated.pid);
      }
    });

    await addTechIntoProject(techs, projectUpdated.pid);
    modal.hide();
    return;
  } else {
    addProject(project)
      .then(async (projectCreated) => {
        await addTechIntoProject(techs, projectCreated.pid);
        modal.hide();
        navigateTo("projects");
      })
      .catch((err) => {
        console.error(err.message);
        errorToasts(err.message);
      });
    // return
  }
}

function deleteProject(pid) {
  const modal = new bootstrap.Modal(document.getElementById("projectModalDel"));

  document.getElementById("text-del").innerHTML =
    "Êtes-vous sûr de vouloir supprimer ce projet ?";
  document
    .getElementById("btn-del-proj")
    .addEventListener("click", async () => {
      delProject(pid)
        .then(() => {
          modal.hide();
          navigateTo("projects");
        })
        .catch((err) => {
          console.error(err);
          modal.hide();
          navigateTo("projects");
        });
    });

  modal.show();
}

function openModalGithub() {}

export async function initTabProjects() {
  const list = document.getElementById("projectsList");
  list.innerHTML = "";
  const projects = await fetchProjects();
  if (projects.length < 1) {
    list.innerHTML = `
      <tr class="w-100">
        <span class="text-center w-100 text-secondary">Pas de projects</span>
      </tr>
    `;
  } else {
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
                    
                    <a class="btn btn-primary btn-sm voir-tech" data-tech-id="${p.pid}">Voir techs</a>
                    </td>
                    <td class="table-actions">
                        <button class="btn btn-sm btn-warning edit-project" id="${idEdit}">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger delete-project" id="${idDelete}">
                            <i class="fas fa-trash"></i>
                        </button>
                        <button class="btn btn-sm btn-dark link-collab-project" data-project-id="${p.pid}">
                          <i class="fa-solid fa-link"></i>
                        </button>
                    </td>
                </tr>
            `;

    }

    document.querySelectorAll(".voir-tech").forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        const modal = new bootstrap.Modal(
          document.getElementById("projectModalTech"),
        );
        const pid = e.currentTarget.getAttribute("data-tech-id");

        const bodyTech = document.getElementById("body-tech-proj");
        bodyTech.innerHTML = "";
        const techs = await fetchTechsProject(pid);
        techs.forEach((t) => {
          bodyTech.innerHTML += ` 
        <span class="badge-tech">${t.name}</span>
        `;
        });
        modal.show();
      });
    });
  }
}

async function openModalLinkCollab(pid){
  const modal = new bootstrap.Modal(document.getElementById("modal-add-collab"))
  const [collaborators, collaboratorsProject] = await fetchData(pid)
  renderTab(collaborators, collaboratorsProject, pid)
  modal.show()
}

function addCollaboratorProject(pid, cid){
  addCollaboratorIntoProject(pid, cid).then(async () => {
      const [collaborators, collaboratorsProject] = await fetchData(pid)
      renderTab(collaborators, collaboratorsProject, pid)
  })
}

function removeCollaboratorProject(pid, cid){
  removeCollaboratorIntoProject(pid, cid).then(async () => {
      const [collaborators, collaboratorsProject] = await fetchData(pid)
      renderTab(collaborators, collaboratorsProject, pid)
  })
}

async function fetchData(pid){
  const collaborators = await fetchCollabs()
  const collaboratorsProject = await fetchCollabsProject(pid)
  return [collaborators, collaboratorsProject]
}

const renderTab = (collaborators, collaboratorsProject, pid) => {
  const listCollab = document.getElementById("collabList")
  listCollab.innerHTML = ``
  collaborators.forEach(c => {
    let classBtn = 'btn-primary project-add-collab'
    let icon ='<i class="fa-solid fa-plus"></i>'
    const collab = collaboratorsProject.filter(c1 => c.id === c1.id).at(0)
    if(collab !== undefined){
      classBtn = "btn-danger project-remove-collab"
      icon = '<i class="fa-solid fa-trash"></i>'
    }else{
      classBtn = 'btn-primary project-add-collab'
      icon ='<i class="fa-solid fa-plus"></i>'
    }
    listCollab.innerHTML +=`
      <tr>
        <td>${c.first_name} ${c.last_name}</td>
        <td class="text-end">
          <button class="btn btn-sm ${classBtn}" data-collab-id="${c.id}">
            ${icon}
          </button>
        </td>
      </tr>
    `
  })

  document.querySelectorAll(".project-add-collab").forEach(btn => {
    btn.addEventListener('click', (e) => {
      const cid = e.currentTarget.dataset.collabId
      addCollaboratorProject(pid, cid)
    })
  })

  document.querySelectorAll(".project-remove-collab").forEach(btn =>{
    btn.addEventListener('click', (e) => {
      const cid = e.currentTarget.dataset.collabId
      removeCollaboratorProject(pid, cid)
    })
  })
}

