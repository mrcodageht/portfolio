import { initStats } from "../scripts/homeService"
import { unloader } from "../utils"

export function renderHome() {

  const main = document.getElementById('main')
  if (main == undefined && main==null) {
      return
    }
    main.innerHTML = `
    
    <div
        class="main-content d-flex justify-content-center align-items-center vh-100"
        id="main-content-loader"
      >
        <div class="spinner-border" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>

      <div class="main-content" id="main-content-unloader">
        <!-- Dashboard View -->
        <div id="dashboard" class="view-section active">
          <div class="header">
            <h1><i class="fas fa-chart-line"></i> Dashboard</h1>
            <p class="text-muted mb-0">Vue d'ensemble de votre portfolio</p>
          </div>

          <div class="row">
            <div class="col-md-4">
              <div class="stats-card">
                <i class="fas fa-project-diagram fa-2x"></i>
                <h3 id="projectCount">0</h3>
                <p>Projets</p>
              </div>
            </div>
            <div class="col-md-4">
              <div
                class="stats-card"
                style="
                  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                "
              >
                <i class="fas fa-code fa-2x"></i>
                <h3 id="techCount">0</h3>
                <p>Technologies</p>
              </div>
            </div>
            <div class="col-md-4">
              <div
                class="stats-card"
                style="
                  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                "
              >
                <i class="fas fa-users fa-2x"></i>
                <h3 id="collabCount">0</h3>
                <p>Collaborateurs</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    
    
    `
  initStats().then(() => {

    unloader()
  })
}