
const projects = [
    {
        pid: 'p001',
        name: 'E-Commerce Platform',
        description: 'Plateforme e-commerce complète avec panier et paiement',
        tech: ['React', 'Node.js', 'MongoDB', 'Stripe'],
        status: 'Production',
        github: 'https://github.com/mrcodage/ecommerce',
        demo: 'https://demo.example.com'
    },
    {
        pid: 'p002',
        name: 'Task Manager App',
        description: 'Application de gestion de tâches avec collaboration',
        tech: ['Vue.js', 'Express', 'PostgreSQL'],
        status: 'En développement',
        github: 'https://github.com/mrcodage/taskmanager',
        demo: null
    },
    {
        pid: 'p003',
        name: 'Weather Dashboard',
        description: 'Dashboard météo avec prévisions et cartes interactives',
        tech: ['JavaScript', 'API REST', 'Chart.js'],
        status: 'Production',
        github: 'https://github.com/mrcodage/weather',
        demo: 'https://weather.example.com'
    }
];

const skills = {
    frontend: ['HTML/CSS', 'JavaScript', 'React', 'Vue.js', 'Tailwind'],
    backend: ['Node.js', 'Express', 'Python', 'PHP'],
    database: ['MongoDB', 'PostgreSQL', 'MySQL'],
    tools: ['Git', 'Docker', 'VS Code', 'Figma']
};

const commandHistory = [];
let historyIndex = -1;

const input = document.getElementById('terminal-input');
const output = document.getElementById('terminal-output');

input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const command = input.value.trim();
        if (command) {
            commandHistory.unshift(command);
            historyIndex = -1;
            addOutput(`<span class="prompt">visitor@mrcodage:~$</span> <span class="command">${command}</span>`);
            executeCommand(command);
        }
        input.value = '';
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (historyIndex < commandHistory.length - 1) {
            historyIndex++;
            input.value = commandHistory[historyIndex];
        }
    } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (historyIndex > 0) {
            historyIndex--;
            input.value = commandHistory[historyIndex];
        } else if (historyIndex === 0) {
            historyIndex = -1;
            input.value = '';
        }
    }
});

function addOutput(html) {
    const line = document.createElement('div');
    line.className = 'terminal-line';
    line.innerHTML = html;
    output.appendChild(line);
    output.scrollTop = output.scrollHeight;
}

function executeCommand(cmd) {
    const parts = cmd.toLowerCase().split(' ');
    const command = parts[0];

    switch (command) {
        case 'help':
            showHelp();
            break;
        case 'about':
            showAbout();
            break;
        case 'projects':
            if (parts[1]) {
                showProjectDetail(parts[1]);
            } else {
                showProjects();
            }
            break;
        case 'skills':
            showSkills();
            break;
        case 'contact':
            showContact();
            break;
        case 'clear':
            output.innerHTML = '';
            break;
        default:
            addOutput(`<span class="error">Commande inconnue: ${command}</span>`);
            addOutput(`Tapez <span class="info">'help'</span> pour voir les commandes disponibles`);
    }
    addOutput('');
}

function showHelp() {
    addOutput('<span class="success">Commandes disponibles:</span>');
    addOutput('  <span class="info">help</span>              - Affiche cette aide');
    addOutput('  <span class="info">about</span>             - À propos de moi');
    addOutput('  <span class="info">projects</span>          - Liste tous les projets');
    addOutput('  <span class="info">projects {pid}</span>    - Détails d\'un projet spécifique');
    addOutput('  <span class="info">skills</span>            - Mes compétences techniques');
    addOutput('  <span class="info">contact</span>           - Informations de contact');
    addOutput('  <span class="info">clear</span>             - Efface le terminal');
}

function showAbout() {
    addOutput('<span class="success">À propos de mrcodage</span>');
    addOutput('');
    addOutput('Développeur Full-Stack passionné par la création d\'applications web modernes.');
    addOutput('Spécialisé dans les technologies JavaScript et les architectures évolutives.');
    addOutput('');
    addOutput('🎯 Focus: Applications web performantes et expériences utilisateur exceptionnelles');
    addOutput('📍 Localisation: Canada');
    addOutput('💼 Statut: Disponible pour des projets freelance');
}

function showProjects() {
    addOutput('<span class="success">Liste des projets:</span>');
    addOutput('');

    let grid = '<div class="project-grid">';
    projects.forEach(project => {
        grid += `
                    <div class="project-card">
                        <h3>${project.name}</h3>
                        <div class="project-id">PID: ${project.pid}</div>
                        <p>${project.description}</p>
                        <p style="margin-top: 0.5rem; color: #888;">Status: ${project.status}</p>
                    </div>
                `;
    });
    grid += '</div>';

    addOutput(grid);
    addOutput(`<span class="info">Tapez 'projects {pid}' pour plus de détails (ex: projects p001)</span>`);
}

function showProjectDetail(pid) {
    const project = projects.find(p => p.pid === pid);

    if (!project) {
        addOutput(`<span class="error">Projet non trouvé: ${pid}</span>`);
        addOutput(`<span class="info">Projets disponibles: ${projects.map(p => p.pid).join(', ')}</span>`);
        return;
    }

    addOutput(`<span class="success">Détails du projet: ${project.name}</span>`);
    addOutput('');

    let detail = `
                <div class="detail-section">
                    <h4>📋 Informations générales</h4>
                    <p><strong>Nom:</strong> ${project.name}</p>
                    <p><strong>PID:</strong> ${project.pid}</p>
                    <p><strong>Status:</strong> ${project.status}</p>
                    <p><strong>Description:</strong> ${project.description}</p>
                </div>
                
                <div class="detail-section">
                    <h4>🛠️ Technologies utilisées</h4>
                    <div>
                        ${project.tech.map(t => `<span class="tech-tag">${t}</span>`).join('')}
                    </div>
                </div>
                
                <div class="detail-section">
                    <h4>🔗 Liens</h4>
                    <p><strong>GitHub:</strong> ${project.github}</p>
                    ${project.demo ? `<p><strong>Demo:</strong> ${project.demo}</p>` : '<p><strong>Demo:</strong> Bientôt disponible</p>'}
                </div>
            `;

    addOutput(detail);
}

function showSkills() {
    addOutput('<span class="success">Compétences techniques:</span>');
    addOutput('');

    let table = `
                <table>
                    <tr>
                        <th>Catégorie</th>
                        <th>Technologies</th>
                    </tr>
                    <tr>
                        <td>Frontend</td>
                        <td>${skills.frontend.join(', ')}</td>
                    </tr>
                    <tr>
                        <td>Backend</td>
                        <td>${skills.backend.join(', ')}</td>
                    </tr>
                    <tr>
                        <td>Base de données</td>
                        <td>${skills.database.join(', ')}</td>
                    </tr>
                    <tr>
                        <td>Outils</td>
                        <td>${skills.tools.join(', ')}</td>
                    </tr>
                </table>
            `;

    addOutput(table);
}

function showContact() {
    addOutput('<span class="success">Contactez-moi:</span>');
    addOutput('');
    addOutput('📧 Email: contact@mrcodage.dev');
    addOutput('🐙 GitHub: github.com/mrcodage');
    addOutput('💼 LinkedIn: linkedin.com/in/mrcodage');
    addOutput('🐦 Twitter: @mrcodage');
    addOutput('');
    addOutput('<span class="info">N\'hésitez pas à me contacter pour discuter de vos projets!</span>');
}

input.focus();
document.addEventListener('click', () => input.focus());
