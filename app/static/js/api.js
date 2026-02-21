/**
 * API client for Labor costs backend.
 * Uses cookie-based auth (labor_costs_access_token); include credentials on all requests.
 */
const API = {
  base: "",
  async request(path, options = {}) {
    const url = path.startsWith("http") ? path : `${this.base}${path}`;
    const opts = {
      ...options,
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        ...options.headers,
      },
    };
    if (opts.body && typeof opts.body === "object" && !(opts.body instanceof FormData)) {
      if (typeof opts.body !== "string") opts.body = JSON.stringify(opts.body);
    }
    const res = await fetch(url, opts);
    const text = await res.text();
    let data = null;
    try {
      data = text ? JSON.parse(text) : null;
    } catch (_) {
      data = text;
    }
    if (!res.ok) {
      const err = new Error(data?.detail || data?.message || res.statusText || "Request failed");
      err.status = res.status;
      err.data = data;
      throw err;
    }
    return data;
  },
  get(path) {
    return this.request(path, { method: "GET" });
  },
  post(path, body) {
    return this.request(path, { method: "POST", body });
  },
  put(path, body) {
    return this.request(path, { method: "PUT", body });
  },
  patch(path, body) {
    return this.request(path, { method: "PATCH", body });
  },
  delete(path) {
    return this.request(path, { method: "DELETE" });
  },
  // List helpers: API returns 404 when empty; treat as []
  async list(path) {
    try {
      return await this.get(path);
    } catch (e) {
      if (e.status === 404) return [];
      throw e;
    }
  },
};

// User / auth
API.login = (email, password) =>
  API.post("/user/login", { email, password });
API.logout = () =>
  API.post("/user/logout");
API.register = (data) =>
  API.post("/user/register", data);

// Entities
API.organizations = {
  list: () => API.list("/organizations/all"),
  get: (id) => API.get(`/organizations/${id}`),
  create: (data) => API.post("/organizations/add", data),
  update: (id, data) => API.put(`/organizations/${id}`, data),
  delete: (id) => API.delete(`/organizations/${id}`),
};
API.projects = {
  list: () => API.list("/project/all"),
  get: (id) => API.get(`/project/${id}`),
  create: (data) => API.post("/project/add", data),
  update: (id, data) => API.put(`/project/${id}`, data),
  delete: (id) => API.delete(`/project/${id}`),
};
API.divisions = {
  list: () => API.list("/division/all"),
  get: (id) => API.get(`/division/${id}`),
  create: (data) => API.post("/division/add", data),
  update: (id, data) => API.put(`/division/${id}`, data),
  delete: (id) => API.delete(`/division/${id}`),
};
API.activityTypes = {
  list: () => API.list("/activity_type/all"),
  get: (id) => API.get(`/activity_type/${id}`),
  create: (data) => API.post("/activity_type/add", data),
  update: (id, data) => API.put(`/activity_type/${id}`, data),
  delete: (id) => API.delete(`/activity_type/${id}`),
};
API.tasks = {
  list: () => API.list("/task/all"),
  get: (id) => API.get(`/task/${id}`),
  create: (data) => API.post("/task/add", data),
  update: (id, data) => API.put(`/task/${id}`, data),
  delete: (id) => API.delete(`/task/${id}`),
};
