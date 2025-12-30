import { TechnologyCreate } from "../class.js";
import {
  addTechnology,
  delTechnology,
  fetchTechs,
  updateTechonology,
} from "../function.js";

function setupAllEventListener() {
  document.body.addEventListener("click", (e) => {
    if (e.target.id === "new-tech") {
      openTechModal();
      return;
    }
  });
}

async function openTechModal(id = null) {
  const alert = document.getElementById("tech-error");
  alert.innerHTML = "";
  alert.classList.add("d-none");
  const modal = new bootstrap.Modal(document.getElementById("techModal"));
  const title = document.getElementById("techModalTitle");
  const selectList = document.getElementById("techCategory");
  // let compt = 0
  // for (const t of technologies) {
  //     compt++
  //     selectList.innerHTML += `
  //         <option value="">${t.type}</option>

  //     `
  // }
  if (id) {
    const tech = await fetchTechs(id);
    title.textContent = "Modifier la Technologie";
    document.getElementById("techId").value = tech.id;
    document.getElementById("techName").value = tech.name;
    document.getElementById("techCategory").value = tech.type;
    document.getElementById("techIcon").value = tech.icon_url;
  } else {
    title.textContent = "Nouvelle Technologie";
    document.getElementById("techForm").reset();
    document.getElementById("techId").value = "";
  }

  modal.show();
}

async function saveTech() {
  const alert = document.getElementById("tech-error");
  const id = document.getElementById("techId").value;
  const category = document.getElementById("techCategory").value;
  if (category === "") {
    alert.innerHTML = "Categorie requise";
    alert.classList.remove("d-none");
    return;
  }
  const tech = new TechnologyCreate(
    document.getElementById("techName").value,
    document.getElementById("techCategory").value,
    document.getElementById("techIcon").value
  );
  if (id) {
    try {
      await updateTechonology(tech, id);
    } catch (error) {
      if (error.code != null && error.code === "ERR_409") {
        const alert = document.getElementById("tech-error");
        alert.innerHTML = error.message;
        alert.classList.remove("d-none");
        return;
      }
      console.error(error);
    }
  } else {
    try {
      await addTechnology(tech);
    } catch (error) {
      if (error.code != null && error.code === "ERR_409") {
        alert.innerHTML = error.message;
        alert.classList.remove("d-none");
        return;
      }
      console.error(error);
    }
  }

  //renderTechnologies();
  //updateStats();
  bootstrap.Modal.getInstance(document.getElementById("techModal")).hide();

  window.location.href = window.location.href;
}

function deleteTech(id) {
  const modal = new bootstrap.Modal(document.getElementById("techModalDel"));

  document.getElementById("text-del").innerHTML =
    "Êtes-vous sûr de vouloir supprimer cette technologie ?";
  modal.show();
  btnDelTech.addEventListener("click", async () => {
    try {
      await delTechnology(id);

      window.location.href = window.location.href;
    } catch (error) {
      console.log(error);
      window.location.href = window.location.href;
    }
  });
}

async function renderTechnologies() {
  const list = document.getElementById("techList");
  const technologies = await fetchTechs();
  list.innerHTML = "";

  //<td>${t.level}</td>
  for (const t of technologies) {
    let idEdit = `edit-${t.id}`;
    let idDelete = `delete-${t.id}`;
    list.innerHTML += `
                <tr>
                    <td>
                        <img width="30" height="30" src="${t.icon_url}">
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
            `;
  }
}

await renderTechnologies();
setupAllEventListener();
const allBtnDelete = document.querySelectorAll(".delete-tech");

const allBtnEdit = document.querySelectorAll(".edit-tech");
const btnSaveTech = document.getElementById("btn-save-tech");
const btnDelTech = document.getElementById("btn-del-tech");

allBtnDelete.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const id = btn.id.split("-");
    deleteTech(id[1]);
  });
});
allBtnEdit.forEach((btn) => {
  btn.addEventListener("click", async () => {
    const id = btn.id.split("-");
    await openTechModal(id[1]);
  });
});

btnSaveTech.addEventListener("click", () => {
  saveTech();
});
