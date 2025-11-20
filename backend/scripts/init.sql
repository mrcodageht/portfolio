-- Utilise ta DB
CREATE DATABASE IF NOT EXISTS portfoliodb DEFAULT CHARACTER SET = utf8mb4 DEFAULT COLLATE = utf8mb4_unicode_ci;

USE portfoliodb;

-- Supprimer anciennes définitions si elles existent (sécurise re-run)
DROP TRIGGER IF EXISTS trg_projects_before_insert;

DROP TRIGGER IF EXISTS trg_technologies_before_insert;

# DROP FUNCTION IF EXISTS short_id6;

DELIMITER $$

-- Fonction qui génère un identifiant court (6 chars)
CREATE FUNCTION IF NOT EXISTS short_id6()
RETURNS VARCHAR(6)
DETERMINISTIC
BEGIN
    RETURN SUBSTRING(
        REPLACE(TO_BASE64(UUID_TO_BIN(UUID())), '=', ''),
        1, 6
    );
END$$

DELIMITER;

-- ======================
-- TABLE : projects  (pid = CHAR(6) WITHOUT DEFAULT)
-- ======================
CREATE TABLE IF NOT EXISTS projects (
    pid CHAR(6) NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(150) UNIQUE,
    description VARCHAR(1000),
    start_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_at TIMESTAMP NULL DEFAULT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    status ENUM(
        'IN_PROGRESS',
        'FINISHED',
        'ARCHIVED',
        'PLANNING'
    ) NOT NULL DEFAULT 'IN_PROGRESS',
    visibility ENUM('PUBLISHED', 'PRIVATE') NOT NULL DEFAULT 'PRIVATE',
    cover_image_url TEXT,
    liveUrl TEXT,
    repoUrl TEXT,
    INDEX idx_projects_slug (slug)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TABLE : technologies  (id = CHAR(6) WITHOUT DEFAULT)
-- ======================
CREATE TABLE IF NOT EXISTS technologies (
    id CHAR(6) NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(150) UNIQUE,
    type ENUM(
        'BACKEND',
        'FRONTEND',
        'DB',
        'DEVOPS',
        'MOBILE',
        'TOOL',
        'OTHER'
    ),
    icon_url TEXT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TABLE : collaborators (UUID CHAR(36))
-- ======================
CREATE TABLE IF NOT EXISTS collaborators (
    id CHAR(36) NOT NULL PRIMARY KEY DEFAULT(UUID()),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role TEXT,
    portfolio_url TEXT,
    github_url TEXT,
    linkedin_url TEXT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TABLE : project_image (UUID CHAR(36))
-- ======================
CREATE TABLE IF NOT EXISTS project_image (
    id CHAR(36) NOT NULL PRIMARY KEY DEFAULT(UUID()),
    image_url TEXT NOT NULL,
    alt_text TEXT NOT NULL,
    kind ENUM(
        'SCREENSHOT',
        'LOGO',
        'DIAGRAM',
        'THUMB'
    ) NOT NULL DEFAULT 'SCREENSHOT',
    project_pid CHAR(6) NOT NULL,
    CONSTRAINT fk_projectimage_project FOREIGN KEY (project_pid) REFERENCES projects (pid) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TABLE : collaborator_project
-- ======================
CREATE TABLE IF NOT EXISTS collaborator_project (
    project_pid CHAR(6) NOT NULL,
    collaborator_id CHAR(36) NOT NULL,
    PRIMARY KEY (project_pid, collaborator_id),
    CONSTRAINT fk_collproj_project FOREIGN KEY (project_pid) REFERENCES projects (pid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_collproj_collaborator FOREIGN KEY (collaborator_id) REFERENCES collaborators (id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TABLE : technologies_project
-- ======================
CREATE TABLE IF NOT EXISTS technologies_project (
    project_pid CHAR(6) NOT NULL,
    technology_id CHAR(6) NOT NULL,
    PRIMARY KEY (project_pid, technology_id),
    CONSTRAINT fk_techproj_project FOREIGN KEY (project_pid) REFERENCES projects (pid) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_techproj_technology FOREIGN KEY (technology_id) REFERENCES technologies (id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- ======================
-- TRIGGERS: peupler pid/id si NULL ou vide
-- ======================
DELIMITER $$

CREATE TRIGGER trg_projects_before_insert
BEFORE INSERT ON projects
FOR EACH ROW
BEGIN
  IF NEW.pid IS NULL OR NEW.pid = '' THEN
     SET NEW.pid = short_id6();
  END IF;
END$$

CREATE TRIGGER trg_technologies_before_insert
BEFORE INSERT ON technologies
FOR EACH ROW
BEGIN
  IF NEW.id IS NULL OR NEW.id = '' THEN
     SET NEW.id = short_id6();
  END IF;
END$$

DELIMITER;