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
