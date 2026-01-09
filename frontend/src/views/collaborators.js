import { initTabCollabs, setupAllEventListener } from "../scripts/collaboratorsService"
import { unloader } from "../utils"

export async function renderCollaborators() {
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
      <div id="collaborators" class="view-section active">
        <div class="header d-flex justify-content-between align-items-center">
          <div>
            <h1><i class="fas fa-users"></i> Gestion des Collaborateurs</h1>
          </div>
          <button class="btn btn-primary" id="btn-add-collab">
            <i class="fas fa-plus"></i> Nouveau Collaborateur
          </button>
        </div>

        <div class="card">
          <div class="card-body">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Nom complet</th>
                  <th>Rôle</th>
                  <th>Reseaux</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody id="collabList"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Modal -->
      <div class="modal fade" id="collabModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="collabModalTitle">
                Nouveau Collaborateur
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body">
              <form id="collabForm">
                <input type="hidden" id="collabId" />
                <div class="mb-3">
                  <label class="form-label">Prenom</label>
                  <input
                    type="text"
                    class="form-control"
                    id="collabFirstname"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label class="form-label">Nom</label>
                  <input
                    type="text"
                    class="form-control"
                    id="collabLastname"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label class="form-label">Rôle</label>
                  <input
                    type="text"
                    class="form-control"
                    id="collabRole"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label class="form-label">Portfolio</label>
                  <input type="url" class="form-control" id="collabPortfolio" />
                </div>
                <div class="mb-3">
                  <label class="form-label">LinkedIn</label>
                  <input type="url" class="form-control" id="collabLinkedin" />
                </div>
                <div class="mb-3">
                  <label class="form-label">Github</label>
                  <input type="url" class="form-control" id="collabGithub" />
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
                id="btn-save-collab"
              >
                Enregistrer
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="collabModalDel" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="techModalTitle">
                Suppression Collaborator
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
              <button type="button" class="btn btn-danger" id="btn-del-collab">
                Supprimer
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    `
  initTabCollabs().then(async () => {
    setupAllEventListener()
    unloader()
  })
    
}