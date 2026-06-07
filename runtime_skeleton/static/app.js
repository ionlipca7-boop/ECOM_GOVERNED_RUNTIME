const payload = window.__DASHBOARD_PAYLOAD__ || {};

const state = {
  routes: payload.routes || [],
  routeMap: Object.create(null),
  selectedRouteId: null,
  history: [],
  stopped: false,
};

const routeLabels = {
  route_01_new_product: "01 Новый продукт",
  route_02_variant_product: "02 Вариант продукта",
  route_03_listing_studio: "03 Студия размещения объявлений",
  route_04_marketplace_lifecycle: "04 Жизненный цикл торговой площадки",
  route_05_finance_inventory: "05 Финансы / Инвентаризация",
  route_06_product_radar: "06 Продуктовый радар",
  route_07_decision_center: "07 Решения / отчёты / агенты",
  route_08_memory_teacher: "08 Система / память",
};

const fields = {
  routeButtons: document.querySelector("#routeButtons"),
  validationBadge: document.querySelector("#validationBadge"),
  homeButton: document.querySelector("#homeButton"),
  backButton: document.querySelector("#backButton"),
  stopButton: document.querySelector("#stopButton"),
  globalRules: document.querySelector("#globalRules"),
  routeId: document.querySelector("#routeId"),
  routeButton: document.querySelector("#routeButton"),
  routeStatus: document.querySelector("#routeStatus"),
  callback: document.querySelector("#callback"),
  role: document.querySelector("#role"),
  purpose: document.querySelector("#purpose"),
  safeNextAction: document.querySelector("#safeNextAction"),
  contractFile: document.querySelector("#contractFile"),
  inputs: document.querySelector("#inputs"),
  outputs: document.querySelector("#outputs"),
  agents: document.querySelector("#agents"),
  blocks: document.querySelector("#blocks"),
  handoffs: document.querySelector("#handoffs"),
  rules: document.querySelector("#rules"),
  meta: document.querySelector("#meta"),
};

function initDashboard() {
  buildRouteMap();
  renderValidation(payload.validation || {});
  renderGlobalRules(payload.global_rules || []);
  renderButtons();

  const firstRouteId = state.routes[0]?.route_id || null;
  selectRoute(firstRouteId, false);
  renderMeta();
}

function buildRouteMap() {
  state.routeMap = Object.create(null);

  for (const route of state.routes) {
    if (!route?.route_id) {
      continue;
    }

    state.routeMap[route.route_id] = route;
  }
}

function renderValidation(validation) {
  const status = validation.status || "UNKNOWN";
  fields.validationBadge.textContent = `VALIDATION ${status}`;
  fields.validationBadge.className = status === "PASS" ? "badge pass" : "badge block";
}

function renderGlobalRules(rules) {
  fields.globalRules.replaceChildren();

  for (const item of rules) {
    const card = document.createElement("article");
    card.className = "rule-card";

    const title = document.createElement("h3");
    title.textContent = item.name;

    const body = document.createElement("p");
    body.textContent = item.rule;

    card.append(title, body);
    fields.globalRules.append(card);
  }
}

function renderButtons() {
  fields.routeButtons.replaceChildren();

  for (const route of state.routes) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = route.route_id === state.selectedRouteId ? "route active" : "route";
    button.dataset.routeId = route.route_id;
    button.setAttribute("aria-pressed", String(route.route_id === state.selectedRouteId));
    button.addEventListener("click", () => selectRoute(button.dataset.routeId, true));

    const title = document.createElement("span");
    title.className = "route-title";
    title.textContent = getRouteLabel(route);

    const status = document.createElement("span");
    status.className = "route-status";
    status.textContent = route.status;

    const action = document.createElement("span");
    action.className = "route-action";
    action.textContent = route.safe_next_action;

    button.append(title, status, action);
    fields.routeButtons.append(button);
  }
}

function selectRoute(routeId, trackHistory) {
  if (!routeId) {
    return;
  }

  const route = state.routeMap[routeId];
  if (!route) {
    renderMissingRoute(routeId);
    return;
  }

  if (trackHistory && state.selectedRouteId && state.selectedRouteId !== routeId) {
    state.history.push(state.selectedRouteId);
  }

  state.selectedRouteId = routeId;
  renderButtons();
  renderRoute(route);
}

function renderRoute(route) {
  if (!route) {
    renderMissingRoute("unknown");
    return;
  }

  fields.routeId.textContent = route.route_id;
  fields.routeButton.textContent = getRouteLabel(route);
  fields.routeStatus.textContent = route.status;
  fields.callback.textContent = route.callback;
  fields.role.textContent = route.role;
  fields.purpose.textContent = route.purpose;
  fields.safeNextAction.textContent = route.safe_next_action;
  fields.contractFile.textContent = route.contract_file;

  renderList(fields.inputs, route.inputs);
  renderList(fields.outputs, route.outputs);
  renderList(fields.agents, route.agents);
  renderList(fields.blocks, route.blocks);
  renderList(fields.handoffs, route.handoffs);
  renderList(fields.rules, route.rules);
}

function renderMissingRoute(routeId) {
  fields.routeId.textContent = routeId;
  fields.routeButton.textContent = "Route block not found";
  fields.routeStatus.textContent = "local_ui_missing_route";
  fields.callback.textContent = "-";
  fields.role.textContent = "-";
  fields.purpose.textContent =
    "The selected route_id is not present in the local route registry. Other route buttons remain independent.";
  fields.safeNextAction.textContent =
    "Check the local static dashboard payload and route registry; no server or live action was called.";
  fields.contractFile.textContent = "-";

  renderList(fields.inputs, []);
  renderList(fields.outputs, []);
  renderList(fields.agents, []);
  renderList(fields.blocks, []);
  renderList(fields.handoffs, []);
  renderList(fields.rules, []);
}

function getRouteLabel(route) {
  return routeLabels[route.route_id] || route.button || route.route_id;
}

function renderList(element, values = []) {
  element.replaceChildren();
  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = value;
    element.append(item);
  }
}

function renderMeta() {
  const validation = payload.validation || {};
  const archive = payload.archive || {};
  fields.meta.textContent =
    `Version ${payload.version || "V7.3C"} | ` +
    `Routes ${validation.route_count || state.routes.length} | ` +
    `Contracts ${payload.source_paths?.contracts || "storage/contracts/v7_3c"} | ` +
    `Archive ${archive.status || "unknown"} | ` +
    "Report runtime_skeleton/_output/validation_report.json";
}

fields.homeButton.addEventListener("click", () => {
  state.stopped = false;
  const firstRouteId = state.routes[0]?.route_id || null;
  if (state.selectedRouteId && state.selectedRouteId !== firstRouteId) {
    state.history.push(state.selectedRouteId);
  }
  selectRoute(firstRouteId, false);
});

fields.backButton.addEventListener("click", () => {
  const previousRouteId = state.history.pop();
  if (previousRouteId) {
    selectRoute(previousRouteId, false);
  }
});

fields.stopButton.addEventListener("click", () => {
  state.stopped = true;
  fields.routeStatus.textContent = "stopped_locally_no_action";
  fields.safeNextAction.textContent =
    "Local runtime flow is stopped. No restart, delete, Telegram patch, eBay action, commit, or push.";
  renderButtons();
});

initDashboard();
