const menuLinks = document.querySelectorAll('.menu-link')
const renduSidebar = () => {
    return /* html */ `
        <div class="sidebar-brand">
            <i class="fas fa-briefcase"></i> Mrcfolio CMS
        </div>
        <ul class="sidebar-menu">
            <li>
                <a href="index.html" class="menu-link" id="dashboard-link" data-view="dashboard">
                <i class="fas fa-home"></i> Dashboard</a>
            </li>
            <li>
                <a href="projects.html" id="project-link" class="menu-link" data-view="projects"
                ><i class="fas fa-project-diagram"></i> Projets</a
                >
            </li>
            <li>
                <a href="technologies.html" id="tech-link" class="menu-link" data-view="technologies"
                ><i class="fas fa-code"></i> Technologies</a
                >
            </li>
            <li>
                <a
                href="collaborators.html"
                class="menu-link"
                id="collab-link"
                data-view="collaborators"
                ><i class="fas fa-users"></i> Collaborateurs</a
                >
            </li>
<li>
                <a
                href="medias.html"
                class="menu-link"
                id="media-link"
                data-view="medias"
                ><i class="fa-solid fa-photo-film"></i> Medias</a
                >
            </li>
        </ul>
        <div class="d-flex justify-content-center align-items-end w-100 mt-5">
            <button class="btn btn-danger w-100 mx-2">Deconnexion</button>
        </div>
    
    `;
}
const cleanNav = () => {
    menuLinks.forEach(m => m.classList.remove('active')) 
}
const nav = () => {
    const url = window.location.href
    cleanNav()
    if (url.includes('projects')) {
        document.getElementById("project-link").classList.add('active')
    }else if (url.includes('collaborators')) {
        document.getElementById("collab-link").classList.add('active')
    }else if (url.includes('medias')) {
        document.getElementById("media-link").classList.add('active')
    }else if (url.includes('technologies')) {
        document.getElementById("tech-link").classList.add('active')
    }else if (url.includes('index')) {
        document.getElementById("dashboard-link").classList.add('active')
    }
}

document.querySelector('.sidebar').innerHTML = renduSidebar()

menuLinks.forEach(menu => {
    menu.addEventListener('click', () => {
        cleanNav()
        menu.classList.add('active')
    })
})
nav()



