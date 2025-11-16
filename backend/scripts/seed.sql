USE portfoliodb;

-- safe mode: désactive checks FK pendant le seed
SET FOREIGN_KEY_CHECKS = 0;

-- ======================
-- TECHNOLOGIES (8)
-- ======================
SET @t1 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t1, 'Python', 'python', 'backend', 'https://cdn.example.com/icons/python.svg');

SET @t2 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t2, 'FastAPI', 'fastapi', 'backend', 'https://cdn.example.com/icons/fastapi.svg');

SET @t3 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t3, 'React', 'react', 'frontend', 'https://cdn.example.com/icons/react.svg');

SET @t4 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t4, 'PostgreSQL', 'postgresql', 'db', 'https://cdn.example.com/icons/postgres.svg');

SET @t5 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t5, 'Docker', 'docker', 'devops', 'https://cdn.example.com/icons/docker.svg');

SET @t6 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t6, 'AWS', 'aws', 'devops', 'https://cdn.example.com/icons/aws.svg');

SET @t7 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t7, 'React Native', 'react-native', 'mobile', 'https://cdn.example.com/icons/react-native.svg');

SET @t8 = short_id6();
INSERT INTO technologies (id, name, slug, type, icon_url)
VALUES (@t8, 'CLI Tool', 'cli-tool', 'tool', 'https://cdn.example.com/icons/cli.svg');

-- ======================
-- COLLABORATORS (6) - on génère les UUIDs et on les stocke
-- ======================
SET @c1 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c1, 'Alice', 'Martin', 'Backend Developer', 'https://alice.example.com', 'https://github.com/alicem', 'https://linkedin.com/in/alicem');

SET @c2 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c2, 'Bob', 'Durand', 'Frontend Developer', NULL, 'https://github.com/bobd', 'https://linkedin.com/in/bobd');

SET @c3 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c3, 'Caroline', 'Petit', 'Fullstack', 'https://caroline.example.com', 'https://github.com/carolinep', NULL);

SET @c4 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c4, 'David', 'Moreau', 'DevOps', NULL, 'https://github.com/davidm', 'https://linkedin.com/in/davidm');

SET @c5 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c5, 'Emma', 'Leroy', 'Designer', 'https://emma.example.com', 'https://github.com/emmal', 'https://linkedin.com/in/emmal');

SET @c6 = UUID();
INSERT INTO collaborators (id, first_name, last_name, role, portfolio_url, github_url, linkedin_url)
VALUES (@c6, 'Fabrice', 'Nguyen', 'Architect', NULL, 'https://github.com/fabrice', 'https://linkedin.com/in/fabrice');

-- ======================
-- PROJECTS (6) - pid short ids via short_id6()
-- ======================
SET @p1 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p1, 'Portfolio Website', 'portfolio-website',
 'Site perso affichant projets et blog.', 'in_progress', 'published',
 'https://cdn.example.com/covers/portfolio.jpg', 'https://portfolio.example.com', 'https://github.com/alicem/portfolio');

SET @p2 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p2, 'Recettes API', 'recettes-api',
 'API pour gérer des recettes de cuisine.', 'finished', 'published',
 'https://cdn.example.com/covers/recettes.jpg', 'https://recettes.example.com', 'https://github.com/bobd/recettes-api');

SET @p3 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p3, 'Realtime Chat', 'realtime-chat',
 'Application de chat en temps réel (mobile + web).', 'planning', 'private',
 'https://cdn.example.com/covers/chat.jpg', NULL, 'https://github.com/carolinep/realtime-chat');

SET @p4 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p4, 'Data ETL', 'data-etl',
 'Pipeline ETL pour rapports métier.', 'in_progress', 'private',
 'https://cdn.example.com/covers/etl.jpg', NULL, 'https://github.com/davidm/data-etl');

SET @p5 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p5, 'Mobile Shop', 'mobile-shop',
 'Application e-commerce sur mobile.', 'in_progress', 'published',
 'https://cdn.example.com/covers/mobile-shop.jpg', 'https://shop.example.com', 'https://github.com/emmal/mobile-shop');

SET @p6 = short_id6();
INSERT INTO projects (pid, title, slug, description, status, visibility, cover_image_url, liveUrl, repoUrl)
VALUES (@p6, 'Dev Tools', 'dev-tools',
 'Outillage CLI et automatisation.', 'finished', 'published',
 'https://cdn.example.com/covers/devtools.jpg', NULL, 'https://github.com/fabrice/dev-tools');

-- ======================
-- PROJECT IMAGES
-- ======================
-- Pour p1
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/portfolio/1.png', 'home page', 'screenshot', @p1);

INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/portfolio/logo.png', 'logo', 'logo', @p1);

-- Pour p2
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/recettes/1.png', 'list recipes', 'screenshot', @p2);

-- Pour p3
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/chat/1.png', 'chat screen', 'screenshot', @p3);

-- p4
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/etl/1.png', 'etl graph', 'diagram', @p4);

-- p5
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/mobile-shop/1.png', 'catalog', 'screenshot', @p5);

-- p6
INSERT INTO project_image (id, image_url, alt_text, kind, project_pid)
VALUES (UUID(), 'https://cdn.example.com/projects/dev-tools/1.png', 'cli screenshot', 'screenshot', @p6);

-- ======================
-- COLLABORATOR_PROJECT links
-- ======================
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p1, @c1);
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p1, @c5);

INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p2, @c2);
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p2, @c3);

INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p3, @c3);
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p3, @c6);

INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p4, @c4);

INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p5, @c5);
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p5, @c2);

INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p6, @c6);
INSERT INTO collaborator_project (project_pid, collaborator_id) VALUES (@p6, @c1);

-- ======================
-- TECHNOLOGIES_PROJECT links
-- ======================
-- p1: Python, FastAPI, React
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p1, @t1);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p1, @t2);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p1, @t3);

-- p2: Python, FastAPI, PostgreSQL, Docker
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p2, @t1);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p2, @t2);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p2, @t4);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p2, @t5);

-- p3: React, React Native, AWS
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p3, @t3);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p3, @t7);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p3, @t6);

-- p4: Python, Docker, PostgreSQL
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p4, @t1);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p4, @t5);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p4, @t4);

-- p5: React Native, AWS, CLI tool (tool)
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p5, @t7);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p5, @t6);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p5, @t8);

-- p6: Docker, CLI tool
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p6, @t5);
INSERT INTO technologies_project (project_pid, technology_id) VALUES (@p6, @t8);

-- Réactive les checks FK
SET FOREIGN_KEY_CHECKS = 1;

-- fin du seed

