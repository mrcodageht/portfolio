export class Project {
  constructor(
    title,
    description,
    status,
    visibility,
    start_at,
    end_at,
    cover_image_url,
    live_url,
    repo_url
  ) {
    (this.title = title),
      (this.description = description),
      (this.status = status),
      (this.visibility = visibility),
      (this.start_at = start_at),
      (this.end_at = end_at),
      (this.cover_image_url = cover_image_url),
      (this.live_url = live_url),
      (this.repo_url = repo_url);
  }
}

export class ProjectResponse extends Project {
  constructor(
    title,
    description,
    status,
    visibility,
    start_at,
    end_at,
    cover_image_url,
    live_url,
    repo_url,
    slug,
    pid
  ) {
    super(
      title,
      description,
      status,
      visibility,
      start_at,
      end_at,
      cover_image_url,
      live_url,
      repo_url
    );
    this.slug = slug;
    this.pid = pid;
  }
  static fromResponse(data) {
    return new ProjectResponse(
      data.title,
      data.description,
      data.status,
      data.visibility,
      data.start_at,
      data.end_at,
      data.cover_image_url,
      data.live_url,
      data.repo_url,
      data.slug,
      data.pid
    );
  }
}

export class Technology {
  constructor(name, type, icon_url, id, slug) {
    (this.name = name),
      (this.type = type),
      (this.icon_url = icon_url),
      (this.id = id),
      (this.slug = slug);
  }

  static fromResponse(data) {
    return new Technology(
      data.name,
      data.type,
      data.icon_url,
      data.id,
      data.slug
    );
  }
}

export class TechnologyCreate {
  constructor(name, type, icon_url) {
    (this.name = name), (this.type = type), (this.icon_url = icon_url);
  }
}

export class TechnologyProjectCreate {
  constructor(slug) {
    this.slug = slug;
  }
}

export class TechnologyAlreadyExists extends Error {
  constructor(message, code = null) {
    super(message);
    this.name = this.constructor.name;
    this.code = code;
    Error.captureStackTrace(this, this.constructor);
  }
}

export class Collaborator {
  constructor(
    id,
    first_name,
    last_name,
    role,
    portfolio_url,
    github_url,
    linkedin_url
  ) {
    (this.id = id),
      (this.first_name = first_name),
      (this.last_name = last_name),
      (this.role = role),
      (this.portfolio_url = portfolio_url),
      (this.github_url = github_url),
      (this.linkedin_url = linkedin_url);
  }

  static fromResponse(data) {
    return new Collaborator(
      data.id,
      data.first_name,
      data.last_name,
      data.role,
      data.portfolio_url,
      data.github_url,
      data.linkedin_url
    );
  }
}

export class CollaboratorCreate {
  constructor(
    first_name,
    last_name,
    role,
    portfolio_url,
    github_url,
    linkedin_url
  ) {
    (this.first_name = first_name),
      (this.last_name = last_name),
      (this.role = role),
      (this.portfolio_url = portfolio_url),
      (this.github_url = github_url),
      (this.linkedin_url = linkedin_url);
  }
}
