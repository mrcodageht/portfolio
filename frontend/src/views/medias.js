import { initMedia, setupAllEventListener } from "../scripts/mediasService"
import { unloader } from "../utils"

export async function renderMedias() {
    document.getElementById("main").innerHTML = `

    <div
      class="main-content d-flex justify-content-center align-items-center vh-100"
      id="main-content-loader"
    >
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    <div class="main-content" id="main-content-unloader">
      <div id="medias" class="view-section active">
        <div class="header d-flex justify-content-between align-items-center">
          <div>
            <h1><i class="fa-solid fa-photo-film"></i> Gestion des Medias</h1>
          </div>
          <button class="btn btn-primary" id="btn-add-media">
            <i class="fas fa-plus"></i> Ajouter un media
          </button>
        </div>
        <div class="mb-3">
          <form action="#" class="d-flex gap-2">
            <select class="form-select" name="q-project" id="query">
              <option value="">Selectionner un projet</option>
              <option value="proj1">Projet 1</option>
              <option value="proj2">Projet 2</option>
              <option value="proj3">Projet 3</option>
              <option value="proj4">Projet 4</option>
              <option value="proj5">Projet 5</option>
            </select>
            <!-- <input type="submit" class="btn btn-primary" value="Voir les medias"> -->
          </form>
        </div>

        <div
          class="d-flex justify-content-start gap-2 flex-wrap"
          id="rendu-medias"
        >
          <p class="text-center w-100 text-secondary">
            Aucun projet selectionne.
          </p>
      </div>
      </div>

      <!-- Modal -->
      <div class="modal fade" id="mediaModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="mediaModalTitle">
                Nouveau Media
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body">
              <form id="mediaForm" enctype="multipart/form-data">
                <input type="hidden" id="mediaId" />
                <div class="mb-3">
                  <label class="form-label">Projet</label>
                  <select class="form-select" id="mediaProject" required>
                    <option value="">Selectionner le projet</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label class="form-label">Alt text</label>
                  <input
                    type="text"
                    class="form-control"
                    id="mediaAltText"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label class="form-label">Type</label>
                  <select class="form-select" id="mediaKind">
                    <option value="screenshot">Capture d'ecran</option>
                    <option value="logo">Logo</option>
                    <option value="diagram">Diagramme</option>
                    <option value="thumb">Vignette</option>
                    <option value="video">Video</option>
                  </select> 
                </div>
                <div class="mb-3">
  <label for="formFile" class="form-label">Media</label>
  <input class="form-control" type="file" id="mediaFile" required>
                </div>
                              </form>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Annuler
              </button>
              <button
                type="button"
                class="btn btn-primary"
                id="btn-save-media"
              >
                Enregistrer
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="mediaModalDel" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="techModalTitle">
                Suppression Media
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body">
              <p id="text-del"></p>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Annuler
              </button>
              <button type="button" class="btn btn-danger" id="btn-del-media">
                Supprimer
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    `
  await initMedia()
  await setupAllEventListener()    
   unloader()
}