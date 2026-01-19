import { unloader } from "../utils"
import { initTabProjects, setGlobalListerner } from "../scripts/projectsService"

export async function renderProjects() {
    document.getElementById('main').innerHTML = `
     <div
      class="main-content d-flex justify-content-center align-items-center vh-100"
      id="main-content-loader"
    >
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div class="main-content d-none" id="main-content-unloader">
      <div id="projects" class="view-section active">
            <div class="alert alert-danger d-none" id="error-global" role="alert"></div>
        <div class="header d-flex justify-content-between align-items-center">
          <div>
            <h1><i class="fas fa-project-diagram"></i> Gestion des Projets</h1>
          </div>
          <div class="d-flex justify-content-end gap-2">
          <button class="btn btn-primary" id="new-proj">
            <i class="fas fa-plus"></i>
          </button>
 <button class="btn btn-dark border-0 proj-ext" style="background-color: #cb4e18" id="gitlab">
            <i class="fa-brands fa-gitlab"></i>
          </button>
 <button class="btn btn-dark proj-ext" id="github">
            <i class="fa-brands fa-github"></i> Github
          </button>
          </div>
        </div>


        <div class="card">
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <!-- <th>Visibilite</th> -->
                    <th>Titre</th>
                    <th>Date debut</th>
                    <th>Status</th>
                    <th>Technologies</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody id="projectsList">
                  
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="projectModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="projectModalTitle">Nouveau Projet</h5>
            <button
              type="button"
              class="btn-close btn-close-white"
              id="btn-close-project"
              data-bs-dismiss="modal"
            ></button>
          </div>
          <div class="modal-body">
            <div class="alert alert-danger d-none" id="error-modal" role="alert">
</div>
            <form id="projectForm">
              <input type="hidden" id="projectId" />
              <div class="mb-3">
                <label class="form-label">Titre</label>
                <input
                  type="text"
                  class="form-control"
                  id="projectTitle"
                  required
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Description</label>
                <textarea
                  class="form-control"
                  id="projectDescription"
                  rows="3"
                  required
                ></textarea>
              </div>
              <div class="row">
                <div class="mb-3 col-6">
                  <label class="form-label">Status</label>
                  <select class="form-select" id="projectStatus" required>
                    <option value="planning">Planifie</option>
                    <option value="in_progress">En cours</option>
                    <option value="finished">Termine</option>
                  </select>
                </div>
                <div class="mb-3 col-6">
                  <label class="form-label">Visibility</label>
                  <select class="form-select" id="projectVisibility" required>
                    <option value="private">Prive</option>
                    <option value="published">Publique</option>
                  </select>
                </div>
              </div>

              <div class="mb-3">
                <label class="form-label">Technologies</label>
                <!-- Dropdowns -->
                <div class="dropdown w-100">
                  <button
                    class="form-control w-100 dropdown-toggle"
                    type="input"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    La liste des technologies
                  </button>
                  <ul class="dropdown-menu w-100 p-3" id="dropdown-tech"></ul>
                </div>

                <div class="mt-1">
                  Stack :
                  <span class="form-text" id="stacks"></span>
                </div>
              </div>
              <div class="row">
                <div class="mb-3 col-6">
                  <label class="form-label">Date debut</label>
                  <input
                    type="date"
                    class="form-control"
                    id="projectDateStart"
                    required
                  />
                </div>
                <div class="mb-3 col-6">
                  <label class="form-label">Date fin</label>
                  <input
                    type="date"
                    class="form-control"
                    id="projectDateEnd"
                    required
                  />
                </div>
              </div>
              <div class="mb-3">
                <label class="form-label">Couverture</label>
                <input type="url" class="form-control" id="projectCover" />
              </div>

              <div class="mb-3">
                <label class="form-label">URL du projet</label>
                <input type="url" class="form-control" id="projectUrl" />
              </div>
              <div class="mb-3">
                <label class="form-label">Repo du projet</label>
                <input type="url" class="form-control" id="projectRepoUrl" />
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
            <button type="button" class="btn btn-primary" id="saveProject">
              Enregistrer
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal suppression -->
<div class="modal fade" id="projectModalDel" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="techModalTitle">
                Suppression Projet
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
              <button type="button" class="btn btn-danger" id="btn-del-proj">
                Supprimer
              </button>
            </div>
          </div>
        </div>
      </div>
<div class="modal fade" id="projectModalTech" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" >
                Les technologies
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body" id="body-tech-proj">
              
            </div>
            
          </div>
        </div>
      </div>

      <div class="modal fade" id="modal-git" tabindex="-1">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" >
                Chercher votre repo
              </h5>
              <button
                type="button"
                class="btn-close btn-close-white"
                data-bs-dismiss="modal"
              ></button>
            </div>
            <div class="modal-body" id="body-proj-repo">
            <div class="d-flex justify-content-around align-items-center gap-2">
              <input class="form-control" id="repo-value" placeholder="Entrez le nom du repo" />
              <input type="button" class="btn btn-primary" id="q-repo" value="rechercher"/>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    
    `
  initTabProjects().then(async () => {
    setGlobalListerner().then(() => {

    unloader()
    })
  })
  
  
}