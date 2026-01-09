import { reload } from "../utils.js";
import {
  Collaborator,
  CollaboratorCreate,
  MediaProject,
  ProjectResponse,
  Technology,
  TechnologyAlreadyExists,
  TechnologyCreate,
  TechnologyProjectCreate,
} from "./class.js";
import { log, logObj, TYPE } from "./log.js";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
export const COOKIE_NAME_TOKEN = "portfolio-token";

export async function fetchProjects(id = null) {
  let resp = null;
  if (id) {
    resp = await fetch(`${API_BASE_URL}/projects/${id}?techs=true`);
  } else {
    resp = await fetch(`${API_BASE_URL}/projects?techs=true`);
  }

  const data = await resp.json();

  logObj(TYPE.DEBUG, data,"","fetch project");
  const projects = [];
  /* for (const d of data) {
    projects.push(ProjectResponse.fromResponse(d));
  } */
  return data;
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

export async function fetchTechsProject(pid) {
  const resp = await fetch(`${API_BASE_URL}/technologies/project/${pid}`);
  if (resp.ok) {
    const techs = [];
    const technologies = await resp.json();
    for (const t of technologies) {
      techs.push(Technology.fromResponse(t));
    }
    return techs;
  }
  throw new Error(`Response status : ${resp.status}`);
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
  try {
    const resp = await fetch(`${API_BASE_URL}/projects/${pid}`, {
      method: "PUT",
      body: JSON.stringify(project),

      headers: {
        Authorization: getAuthToken(),
        "Content-Type": "application/json",
      },
    });

    if (resp.ok) {
      const projectUpdated = await resp.json();
      const projectToReturn = ProjectResponse.fromResponse(projectUpdated);
      return projectToReturn;
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}
/**
 * Suppression d'un projet par son pid
 * @param {string} pid 
 */
export async function delProject(pid) {
  const resp = await fetch(`${API_BASE_URL}/projects/${pid}`, {
    method: "DELETE",
    headers: {
      Authorization: getAuthToken()
    }
  })
  if (resp.ok) {
    return
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  } 
}

export async function addProject(project) {
  try{
  const resp = await fetch(`${API_BASE_URL}/projects`, {
    method: "POST", 
    body: JSON.stringify(project),
    headers: {
      Authorization: getAuthToken(),
      "Content-Type":"application/json"
    }
  })
  if (resp.ok) {
      const data = await resp.json();
      return ProjectResponse.fromResponse(data);
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }

}


/**
 *
 * @param {TechnologyProjectCreate[]} techs
 * @param {string} pid
 */
export async function addTechIntoProject(techs, pid) {
  try {
    const resp = await fetch(`${API_BASE_URL}/projects/${pid}/technologies`, {
      method: "PATCH",
      body: JSON.stringify(techs),
      headers: {
        Authorization: getAuthToken(),
        "Content-Type": "application/json",
      },
    });

    if (resp.ok) {
      const projectUpdated = await resp.json();
      const projectToReturn = ProjectResponse.fromResponse(projectUpdated);
      return projectToReturn;
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}

export async function removeTechIntoProject(slug, pid) {
  try {
    const resp = await fetch(
      `${API_BASE_URL}/projects/${pid}/technologies/${slug}`,
      {
        method: "DELETE",
        headers: {
          Authorization: getAuthToken(),
        },
      }
    );

    if (resp.ok) {
      const projectUpdated = await resp.json();
      const projectToReturn = ProjectResponse.fromResponse(projectUpdated);
      return projectToReturn;
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}

/**
 *
 * @param {TechnologyCreate} tech
 * @param {string} tid
 * @returns
 */
export async function updateTechonology(tech, tid) {
  try {
    const resp = await fetch(`${API_BASE_URL}/technologies/${tid}`, {
      method: "PUT",
      body: JSON.stringify(tech),
      headers: {
        Authorization: getAuthToken(),
        "Content-Type": "application/json",
      },
    });

    if (resp.ok) {
      const technology = await resp.json();
      return Technology.fromResponse(technology);
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}

export async function addTechnology(tech) {
  try {
    const resp = await fetch(`${API_BASE_URL}/technologies`, {
      method: "POST",
      body: JSON.stringify(tech),
      headers: {
        Authorization: getAuthToken(),
        "Content-Type": "application/json",
      },
    });
    if (resp.ok) {
      const technology = await resp.json();
      return Technology.fromResponse(technology);
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      } else if (resp.status === 409) {
        throw new TechnologyAlreadyExists(
          "Technology existe deja avec ce nom",
          "ERR_409"
        );
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}

export async function delTechnology(tid) {
  try {
    const resp = await fetch(`${API_BASE_URL}/technologies/${tid}`, {
      method: "DELETE",
      headers: {
        Authorization: getAuthToken(),
      },
    });
    if (resp.ok) {
      return;
    } else {
      if (resp.status === 401) {
        // supprimer le token
        deleteCookie(COOKIE_NAME_TOKEN);
        await reload()
        throw new Error("Not authenticated or token expires");
      }
      throw new Error(`Response status : ${resp.status}`);
    }
  } catch (error) {
    throw error;
  }
}

/**
 *
 * @param {CollaboratorCreate} collab
 */
export async function addCollaborator(collab) {
  const resp = await fetch(`${API_BASE_URL}/collaborators`, {
    method: "POST",
    body: JSON.stringify(collab),
    headers: {
      Authorization: getAuthToken(),
      "Content-Type": "application/json",
    },
  });

  if (resp.ok) {
    const data = await resp.json();
    return Collaborator.fromResponse(data);
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  }
}

export async function updateCollaborator(collab, cid) {
  const resp = await fetch(`${API_BASE_URL}/collaborators/${cid}`, {
    method: "PUT",
    body: JSON.stringify(collab),
    headers: {
      Authorization: getAuthToken(),
      "Content-Type": "application/json",
    },
  });

  if (resp.ok) {
    const data = await resp.json();
    return Collaborator.fromResponse(data);
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  }
}

export async function delCollaborator(cid) {
  const resp = await fetch(`${API_BASE_URL}/collaborators/${cid}`, {
    method: "DELETE",
    headers: {
      Authorization: getAuthToken(),
    },
  });

  if (resp.ok) {
    return;
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  }
}

export async function fetchMediasProject(pid) {
  const resp = await fetch(`${API_BASE_URL}/projects/${pid}/medias`);

  if (resp.ok) {
    const data = await resp.json();
    const medias = [];
    for (const d of data) {
      medias.push(MediaProject.fromResponse(d));
    }
    return medias;
  } 
}

export async function addMediaToProject(media, pid) {
  const resp = await fetch(`${API_BASE_URL}/projects/${pid}/medias`, {
    method: "POST",
    body: media,
    headers: {
      Authorization: getAuthToken(),
    },
  });

  if (resp.ok) {
    const data = await resp.json();
    return MediaProject.fromResponse(data);
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  }
}

export async function deleteMediaProject(id) {
  const resp = await fetch(`${API_BASE_URL}/projects/medias/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: getAuthToken(),
    },
  });

  if (resp.ok) {
    return;
  } else {
    if (resp.status === 401) {
      // supprimer le token
      deleteCookie(COOKIE_NAME_TOKEN);
      await reload()
      throw new Error("Not authenticated or token expires");
    }
    throw new Error(`Response status : ${resp.status}`);
  }
}

export async function postLogin(credentials) {
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

export function setCookie(name, value, days) {
  const expire = new Date();
  expire.setTime(expire.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = `${name}=${value};expires=${expire.toUTCString()};path=/;SameSite=Strict`;
}

export function getCookie(name) {
  const nameEQ = name + "=";
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(nameEQ) === 0) {
      return cookie.substring(nameEQ.length);
    }
  }
  return null;
}

function getAuthToken() {
  const token = getCookie(COOKIE_NAME_TOKEN);
  const authHeader = `Bearer ${token}`;
  return authHeader;
}

function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;SameSite=Strict`;
}
