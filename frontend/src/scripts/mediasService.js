import {
  addMediaToProject,
  deleteMediaProject,
  fetchMediasProject,
  fetchProjects,
} from "/src/scripts/function.js";


export async function setupAllEventListener() {
  document.getElementById("query").addEventListener("input", async (e) => {
    console.log("Selected proj : ", e.target.value);
    await rendu(e.target.value);

    const allBtndel = document.querySelectorAll(".delMedia");

    allBtndel.forEach((btn) => {
      btn.addEventListener("click", () => {
        const modal = new bootstrap.Modal(
          document.getElementById("mediaModalDel")
        );
        const id = btn.id.split("_")[1];
        document.getElementById("text-del").innerHTML =
          "Êtes-vous sûr de vouloir supprimer ce media ?";
        document
          .getElementById("btn-del-media")
          .addEventListener("click", async () => {
            await deleteMedia(id);
          });
        modal.show();
      });
    });
  });

  document.getElementById("btn-add-media").addEventListener("click", () => {
    openModalMedia();
  });

  document.getElementById("btn-save-media").addEventListener("click", () => {
    saveMedia();
  });
}

async function openModalMedia() {
  const modal = new bootstrap.Modal(document.getElementById("mediaModal"));
  const mediaProjectSelect = document.getElementById("mediaProject");
  const title = document.getElementById("mediaModalTitle");
  const projects = await fetchProjects();

  mediaProjectSelect.innerHTML = "";

  projects.forEach((p) => {
    mediaProjectSelect.innerHTML += `
        <option value="${p.pid}">${p.title}</option>
        `;
  });

  modal.show();
}

async function deleteMedia(id) {
  try {
    await deleteMediaProject(id);

    window.location.href = window.location.href;
  } catch (error) {
    console.log(error);
    window.location.href = window.location.href;
  }
}

async function saveMedia() {
  const modal = new bootstrap.Modal(document.getElementById("mediaModal"));
  const projectId = document.getElementById("mediaProject").value;
  const fd = new FormData();
  fd.append("alt_text", document.getElementById("mediaAltText").value);
  fd.append("kind", document.getElementById("mediaKind").value);
  fd.append("file", document.getElementById("mediaFile").files[0]);
  try {
    await addMediaToProject(fd, projectId);
  } catch (err) {
    console.error(err);
    return;
  }
  window.location.href = window.location.href;

  modal.hide();
}

function mediaRendu(media) {
  if (media.kind === "video") {
    return `
        <video src="${media.media_url}" class="object-fit-contain" controls></video>

        
        `;
  }
  return `
    
              <img width="200" height="200" src="${media.media_url}" class="card-img-top" alt="${media.alt_text}" />
    `;
}

const rendu = async (pid) => {
  const mediasCont = document.getElementById("rendu-medias");
  mediasCont.innerHTML = "";

  const data = await fetchMediasProject(pid);
  
  if (data.length > 0) {

    for (const d of data) {
      mediasCont.innerHTML += `
        <div class="card" style="width: 18rem">
            ${mediaRendu(d)}
              <div class="card-body">
                <p class="card-text">
                  ${d.alt_text}
                </p>
                <div class="d-flex justify-content-between align-items-center">
                <span class="badge text-bg-info">${d.kind}</span>

                <button class="btn btn-danger fs-6 delMedia" id="delete_${d.id
        }"><i class="fa-solid fa-trash"></i></button>
                </div>
              </div>
            </div>
        `;
    }
  } else {
    mediasCont.innerHTML = `
    <p class="text-center w-100 text-secondary">
            Pas de media pour ce projet.
          </p>
    ` 
  }
};

export const initMedia = async () => {
  const select = document.getElementById("query");
  const projects = await fetchProjects();

  select.innerHTML = `<option value="">Selectionner un projet</option>`;

  projects.forEach((p) => {
    select.innerHTML += `
            <option value="${p.pid}">${p.title}</option>
        `;
  });
};

