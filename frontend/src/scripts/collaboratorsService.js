import { navigateTo } from "../components/sidebar";
import { CollaboratorCreate } from "/src/scripts/class.js";
import {
  addCollaborator,
  delCollaborator,
  fetchCollabs,
  updateCollaborator,
} from "/src/scripts/function.js";

export function setupAllEventListener() {
const allBtnEdit = document.querySelectorAll(".edit-collab");
const allBtnDelete = document.querySelectorAll(".delete-collab");
const btnSaveCollab = document.getElementById("btn-save-collab");
const btnAddCollab = document.getElementById("btn-add-collab");

allBtnDelete.forEach((btn) => {
  btn.addEventListener("click", () => {
    const id = btn.id.split("_")[1];
    deleteCollab(id);
  });
});
allBtnEdit.forEach((btn) => {
  btn.addEventListener("click", async () => {
    const id = btn.id.split("_")[1];
    await openCollabModal(id);
  });
});

btnSaveCollab.addEventListener("click", async () => {
  await saveCollab();
});

btnAddCollab.addEventListener("click", () => {
  openCollabModal().then((r) => {});
});

}

async function openCollabModal(id = null) {
  const modal = new bootstrap.Modal(document.getElementById("collabModal"));
  const title = document.getElementById("collabModalTitle");

  if (id) {
    const collab = await fetchCollabs(id);
    title.textContent = "Modifier le Collaborateur";
    document.getElementById("collabId").value = collab.id;
    document.getElementById("collabFirstname").value = collab.first_name;

    document.getElementById("collabLastname").value = collab.last_name;
    document.getElementById("collabRole").value = collab.role;
    document.getElementById("collabPortfolio").value =
      collab.portfolio_url || "";
    document.getElementById("collabLinkedin").value = collab.linkedin_url || "";
    document.getElementById("collabGithub").value = collab.github_url || "";
  } else {
    title.textContent = "Nouveau Collaborateur";
    document.getElementById("collabForm").reset();
    document.getElementById("collabId").value = "";
  }

  modal.show();
}

async function saveCollab() {
  const id = document.getElementById("collabId").value;
  const collab = new CollaboratorCreate(
    document.getElementById("collabFirstname").value,

    document.getElementById("collabLastname").value,
    document.getElementById("collabRole").value,
    document.getElementById("collabPortfolio").value,
    document.getElementById("collabGithub").value,
    document.getElementById("collabLinkedin").value
  );

  if (id) {
    try {
      await updateCollaborator(collab, id);
    } catch (error) {
      console.error(error);
    }
  } else {
    try {
      await addCollaborator(collab);
    } catch (error) {
      console.error(error);
    }
  }

  bootstrap.Modal.getInstance(document.getElementById("collabModal")).hide();

  navigateTo("collaborators")
}

function deleteCollab(id) {
  const modal = new bootstrap.Modal(document.getElementById("collabModalDel"));

  document.getElementById("text-del").innerHTML =
    "Êtes-vous sûr de vouloir supprimer ce collaborateur ?";
  modal.show();
  document.getElementById("btn-del-collab").addEventListener("click", async () => {
    try {
      await delCollaborator(id);
    } catch (error) {
      console.log(error);
    }
    modal.hide()
    navigateTo("collaborators")
  });
}

export async function initTabCollabs() {
  const list = document.getElementById("collabList");
  const collabs = await fetchCollabs();
  for (const c of collabs) {
    const fullname = `${c.first_name} ${c.last_name}`;
    const idEdit = `edit_${c.id}`;
    const idDelete = `delete_${c.id}`;
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
                        <img alt="portfolio url ${fullname}"  src="/code-solid.svg" width=20 height=20/>
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
        `;
  }
}

