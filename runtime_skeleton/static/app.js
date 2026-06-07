const state = {
  routes: [],
  selectedRouteId: null,
};

const fields = {
  routeButtons: document.querySelector("#routeButtons"),
  validationBadge: document.querySelector("#validationBadge"),
  reloadButton: document.querySelector("#reloadButton"),
  routeId: document.querySelector("#routeId"),
  routeButton: document.querySelector("#routeButton"),
  callback: document.querySelector("#callback"),
  role: document.querySelector("#role"),
  purpose: document.querySelector("#purpose"),
  inputs: document.querySelector("#inputs"),
  outputs: document.querySelector("#outputs"),
  agents: document.querySelector("#agents"),
  blocks: document.querySelector("#blocks"),
  handoffs: document.querySelector("#handoffs"),
  rules: document.querySelector("#rules"),
  meta: document.querySelector("#meta"),
};

async function loadDashboard() {
  fields.validationBadge.textContent = "Проверка...";
  const [contractsResponse, validationResponse] = await Promise.all([
    fetch("/api/contracts"),
    fetch("/api/validation"),
  ]);

  const contracts = await contractsResponse.json();
  const validation = await validationResponse.json();

  state.routes = contracts.routes || [];
  state.selectedRouteId = state.selectedRouteId || state.routes[0]?.route_id;

  renderValidation(validation);
  renderButtons();
  renderRoute(state.routes.find((route) => route.route_id === state.selectedRouteId));

  fields.meta.textContent =
    `Версия ${contracts.version || "V7.3C"} | ` +
    `JSON: ${validation.json_count} | ` +
    `Маршрутов: ${validation.route_count} | ` +
    `Отчёт: runtime_skeleton/_output/validation_report.json`;
}

function renderValidation(validation) {
  fields.validationBadge.textContent =
    validation.status === "PASS" ? "VALIDATION PASS" : "VALIDATION BLOCK";
  fields.validationBadge.className =
    validation.status === "PASS" ? "badge pass" : "badge block";
}

function renderButtons() {
  fields.routeButtons.replaceChildren();

  for (const route of state.routes) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = route.route_id === state.selectedRouteId ? "route active" : "route";
    button.textContent = route.button;
    button.addEventListener("click", () => {
      state.selectedRouteId = route.route_id;
      renderButtons();
      renderRoute(route);
    });
    fields.routeButtons.append(button);
  }
}

function renderRoute(route) {
  if (!route) {
    return;
  }

  fields.routeId.textContent = route.route_id;
  fields.routeButton.textContent = route.button;
  fields.callback.textContent = route.callback;
  fields.role.textContent = route.role;
  fields.purpose.textContent = route.purpose_ru;

  renderList(fields.inputs, route.inputs);
  renderList(fields.outputs, route.outputs);
  renderList(fields.agents, route.agents);
  renderList(fields.blocks, route.blocks);
  renderList(fields.handoffs, route.handoffs);
  renderList(fields.rules, route.rules);
}

function renderList(element, values = []) {
  element.replaceChildren();
  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = value;
    element.append(item);
  }
}

fields.reloadButton.addEventListener("click", loadDashboard);
loadDashboard().catch((error) => {
  fields.validationBadge.textContent = "LOCAL ERROR";
  fields.validationBadge.className = "badge block";
  fields.meta.textContent = error.message;
});
