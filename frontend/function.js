import { log, logObj, TYPE } from "./log.js";

const API_BASE_URL = "http://localhost:8079/api/v1";
export async function fetchProjects(id = null) {
  let resp = null;
  if (id) {
    resp = await fetch(`${API_BASE_URL}/projects/${id}?techs=true`);
  } else {
    resp = await fetch(`${API_BASE_URL}/projects?techs=true`);
  }

  const projects = await resp.json();

  logObj(TYPE.DEBUG, projects);
  return projects;
}

export async function fetchTechs(id = null) {
  let resp = null;
  if (id) {
    resp = await fetch(`${API_BASE_URL}/technologies/${id}`);
  } else {
    resp = await fetch(`${API_BASE_URL}/technologies`);
  }
  const techs = await resp.json();
  logObj(TYPE.DEBUG, techs);
  return techs;
}
export async function fetchCollabs(id = null) {
  let resp = null;
  if (id) {
    log(TYPE.DEBUG, `id : ${id}`);
    resp = await fetch(`${API_BASE_URL}/collaborators/${id}`);
  } else {
    resp = await fetch(`${API_BASE_URL}/collaborators`);
  }

  const collabs = await resp.json();
  logObj(TYPE.DEBUG, collabs);
  return collabs;
}

export async function fetchStats() {
  const resp = await fetch(`${API_BASE_URL}/stats`);
  const stats = await resp.json();
  logObj(TYPE.DEBUG, stats);
  return stats;
}

export async function updateProject(pid, project) {
  const token = localStorage.getItem("token-portfolio");

  const resp = await fetch(`${API_BASE_URL}/projects/${pid}`, {
    method: "PUT",
    body: JSON.stringify(project),
    headers: {
      Authorization: `Bearer ${token}`,
    },
  }).catch((err) => {
    console.error(`${TYPE.INFO} => `, err);
  });

  if (resp.ok) {
    const projectUpdated = await resp.json();
    return projectUpdated();
  }
}

export async function login(credentials) {
  const resp = await fetch(`${API_BASE_URL}/users/login`, {
    method: "POST",
    body: credentials,
  }).catch((err) => console.error("Error => ", err));

  if (resp.ok) {
    const token = await resp.json();
    return token;
  }

  return null;
}
