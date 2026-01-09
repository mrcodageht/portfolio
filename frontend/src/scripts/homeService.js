import { fetchStats } from "./function";

export const initStats = async () => {
  const stats = await fetchStats();
  updateStats(stats);
};



function updateStats(stats) {
  try {
    document.getElementById("projectCount").textContent = stats.projects;
    document.getElementById("techCount").textContent = stats.technologies;
    document.getElementById("collabCount").textContent = stats.collaborators;
  } catch (e) {
    return;
  }
}