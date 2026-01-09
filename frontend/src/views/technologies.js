import { unloader } from "../utils"
import { initTabTechs, setupAllEventListener } from "../scripts/techsService"

export async function renderTechnologies() {
   
    document.getElementById("main").innerHTML = `
    <div
      class="main-content d-flex justify-content-center align-items-center vh-100"
      id="main-content-loader"
    >
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div class="main-content d-none" id="main-content-unloader">
      <div id="technologies" class="view-section active">
        <div class="header d-flex justify-content-between align-items-center">
          <div>
            <h1><i class="fas fa-code"></i> Gestion des Technologies</h1>
          </div>
          <button class="btn btn-primary" id="new-tech">
            <i class="fas fa-plus"></i> Nouvelle Technologie
          </button>
        </div>

        <div class="card">
          <div class="card-body">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Icone</th>
                  <th>Nom</th>
                  <th>Catégorie</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody id="techList"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Modal  -->
      <div class="modal fade" id="techModal" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="techModalTitle">
                Nouvelle Technologie
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body">
              <div
                class="alert alert-danger d-none"
                id="tech-error"
                role="alert"
              >
                <!-- Alert will be injected here -->
              </div>
              <form id="techForm">
                <input type="hidden" id="techId" />
                <div class="mb-3">
                  <label class="form-label">Nom</label>
                  <input
                    type="text"
                    class="form-control"
                    id="techName"
                    required
                  />
                </div>
                <div class="mb-3">
                  <label class="form-label">Catégorie</label>
                  <select class="form-select" id="techCategory" required>
                    <option value="" selected="true">Sélectionner...</option>
                    <option value="backend">Backend</option>
                    <option value="frontend">Frontend</option>
                    <option value="devops">DevOps</option>
                    <option value="db">Base de donnees</option>
                    <option value="tool">Outils</option>
                    <option value="mobile">Mobile</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label class="form-label">Lien d'icone</label>
                  <input
                    type="text"
                    class="form-control"
                    id="techIcon"
                    required
                  />
                  <p class="from-text">
                    ressource:
                    <a href="https://dashboardicons.com" target="_blank"
                      >Dashboard icons</a
                    >
                  </p>
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
              <button type="button" class="btn btn-primary" id="btn-save-tech">
                Enregistrer
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="techModalDel" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="techModalTitle">
                Suppression technology
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
              <button type="button" class="btn btn-danger" id="btn-del-tech">
                Supprimer
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    `
  initTabTechs().then(async () => {
    setupAllEventListener()        
    unloader()
  
    })
}