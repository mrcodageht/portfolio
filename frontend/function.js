import { log, logObj, TYPE } from "./log.js"

const API_BASE_URL = "http://localhost:8079/api/v1"
export async function fetchProjects(id = null) {

    let resp = null
    if (id) {

        resp = await fetch(`${API_BASE_URL}/projects/${id}`)
    } else {
        resp = await fetch(`${API_BASE_URL}/projects`)
    }

    const projects = await resp.json()

    logObj(TYPE.DEBUG, projects)
    return projects
}


export async function fetchTechs(id = null) {
    let resp = null
    if (id) {
        resp = await fetch(`${API_BASE_URL}/technologies/${id}`)
    } else {
        resp = await fetch(`${API_BASE_URL}/technologies`)
    }
    const techs = await resp.json()
    logObj(TYPE.DEBUG, techs)
    return techs
}
export async function fetchCollabs(id = null) {
    let resp = null
    if (id) {
        log(TYPE.DEBUG, `id : ${id}`)
        resp = await fetch(`${API_BASE_URL}/collaborators/${id}`)
    } else {
        resp = await fetch(`${API_BASE_URL}/collaborators`)
    }

    const collabs = await resp.json()
    logObj(TYPE.DEBUG, collabs)
    return collabs
}
