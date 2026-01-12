-- Utilise ta DB
CREATE DATABASE IF NOT EXISTS portfoliodb DEFAULT CHARACTER SET = utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;

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
    DECLARE clean_str VARCHAR(255);
    
    -- 1. On récupère le Base64
    -- 2. On remplace + par 'A', / par 'B' et on supprime le =
    SET clean_str = REPLACE(
                        REPLACE(
                            REPLACE(TO_BASE64(UUID_TO_BIN(UUID())), '=', ''),
                        '+', 'A'),
                    '/', 'B');
    
    -- 3. On retourne les 6 premiers caractères
    RETURN SUBSTRING(clean_str, 1, 6);
END$$

DELIMITER ;

CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) NOT NULL PRIMARY KEY DEFAULT(UUID()),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    admin TINYINT(1) NOT NULL DEFAULT 0,
    is_valid TINYINT(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- ======================
-- TABLE : projects  (pid = CHAR(6) WITHOUT DEFAULT)
-- ======================
CREATE TABLE IF NOT EXISTS projects (
    pid CHAR(6) NOT NULL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(150) UNIQUE NOT NULL,
    description VARCHAR(1000) NOT NULL,
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
    live_url TEXT NULL,
    repo_url TEXT NULL,
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
CREATE TABLE IF NOT EXISTS project_media (
    id CHAR(36) NOT NULL PRIMARY KEY DEFAULT(UUID()),
    media_url TEXT NOT NULL,
    alt_text TEXT NOT NULL,
    kind ENUM(
        'SCREENSHOT',
        'LOGO',
        'DIAGRAM',
        'THUMB',
        'VIDEO'
    ) NOT NULL DEFAULT 'SCREENSHOT',
    project_pid CHAR(6) NOT NULL,
    CONSTRAINT fk_projectmedia_project FOREIGN KEY (project_pid) REFERENCES projects (pid) ON DELETE CASCADE ON UPDATE CASCADE
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

DELIMITER ;
