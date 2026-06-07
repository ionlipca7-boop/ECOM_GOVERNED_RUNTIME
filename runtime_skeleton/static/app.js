const payload = window.__DASHBOARD_PAYLOAD__ || {};

const state = {
  routes: payload.routes || [],
  routeMap: Object.create(null),
  selectedRouteId: null,
  history: [],
  stopped: false,
};

const routeDisplay = {
  route_01_new_product: {
    label: "01 Новый продукт",
    role: "Блок простого товара",
    purpose: "Создать чистый пакет листинга для одного товара без вариантов.",
    safeNextAction:
      "Собрать факты о товаре, фото, себестоимость и остаток, затем передать черновик в маршрут 07 до любых боевых действий.",
  },
  route_02_variant_product: {
    label: "02 Вариант продукта",
    role: "Блок товара с вариантами",
    purpose: "Создать мастер-товар с вариантами, SKU, количеством, ценами и фото.",
    safeNextAction:
      "Проверить матрицу вариантов и остаток по каждому SKU, затем передать на одобрение в маршрут 07.",
  },
  route_03_listing_studio: {
    label: "03 Студия размещения объявлений",
    role: "Блок экспериментов с листингом",
    purpose: "Улучшать угол подачи листинга через A/B/C-черновики без клонов одного покупательского намерения.",
    safeNextAction:
      "Сравнить варианты черновиков, оставить доказательства только для чтения и запросить одобрение маршрута 07.",
  },
  route_04_marketplace_lifecycle: {
    label: "04 Жизненный цикл торговой площадки",
    role: "Блок жизненного цикла листингов",
    purpose: "Наблюдать состояние листингов и показывать только полезные сигналы внимания.",
    safeNextAction:
      "Определить состояние листинга, подготовить рекомендацию без боевых действий и провести решение через маршрут 07.",
  },
  route_05_finance_inventory: {
    label: "05 Финансы / Инвентаризация",
    role: "Блок правды по складу и деньгам",
    purpose: "Поддерживать единый источник правды по складу, себестоимости, деньгам и SKU.",
    safeNextAction:
      "Проверить чеки, себестоимость, остатки и конфликты до того, как другие маршруты будут опираться на эти данные.",
  },
  route_06_product_radar: {
    label: "06 Продуктовый радар",
    role: "Блок исследования товаров",
    purpose: "Оценивать идеи товаров до покупки или размещения.",
    safeNextAction:
      "Собрать исследовательскую карточку только для чтения: доказательства, риск, маржа и запрос решения Ion.",
  },
  route_07_decision_center: {
    label: "07 Решения / отчёты / агенты",
    role: "Блок решений и безопасных ворот",
    purpose: "Держать одобрения, отчёты, заблокированные случаи, ожидания решений и точные безопасные ворота действий.",
    safeNextAction:
      "Показать короткую безопасную карточку решения и записать точный маркер одобрения или блокировки.",
  },
  route_08_memory_teacher: {
    label: "08 Система / память",
    role: "Блок автономной памяти проекта",
    purpose: "Вести автономную память проекта: уроки, правила, указатели архива, доказательства и безопасность.",
    safeNextAction:
      "Сохранять только уроки с доказательствами, а конфликты маршрутов возвращать в маршрут 07 для решения Ion.",
  },
};

const statusLabels = {
  PASS: "ПРОЙДЕНА",
  UNKNOWN: "НЕИЗВЕСТНО",
  blocked_until_route_07_approval: "Ожидает одобрения маршрута 07",
  guarded_by_contract_blocks: "Под защитой контрактных блоков",
  stopped_locally_no_action: "Остановлено локально, без внешних действий",
  local_ui_missing_route: "Маршрут не найден в локальном UI",
};

const globalRuleDisplay = {
  Back: {
    title: "Назад",
    body: "Вернуться к предыдущей карточке маршрута или последней безопасной точке решения; данные маршрутов не изменяются.",
  },
  Home: {
    title: "Главная",
    body: "Вернуться к стартовой карточке панели маршрутов и сохранить независимость всех восьми блоков.",
  },
  Stop: {
    title: "Стоп",
    body: "Остановить только локальный экран: без боевых действий, рестарта, удаления, Telegram, eBay, коммита или отправки в удалённый репозиторий.",
  },
};

const inputLabels = {
  "Ion link": "Ссылка от Ion",
  "Ion photo": "Фото от Ion",
  "Ion text": "Текст от Ion",
  receipt: "Чек",
  "supplier source": "Источник поставщика",
  "product idea": "Идея товара",
  "product with variants": "Товар с вариантами",
  "variant photos": "Фото вариантов",
  "cost per variant": "Себестоимость по вариантам",
  "quantity per variant": "Количество по вариантам",
  source_package: "Пакет источника",
  existing_listing_ref: "Ссылка на существующий листинг",
  draft_ref: "Ссылка на черновик",
  weak_listing_signal: "Сигнал слабого листинга",
  product_opportunity: "Возможность по товару",
  live_listing_ref: "Ссылка на live-листинг",
  snapshot: "Снимок состояния",
  performance_note: "Заметка по эффективности",
  route_refs: "Ссылки на маршруты",
  receipts: "Чеки",
  supplier_costs: "Себестоимость поставщика",
  stock_counts: "Остатки",
  normalized_site_records: "Нормализованные записи площадок",
  "Ion idea": "Идея от Ion",
  link: "Ссылка",
  screenshot: "Скриншот",
  "route signal": "Сигнал маршрута",
  decision_case_from_any_route: "Случай решения из любого маршрута",
  lesson: "Урок",
  rule: "Правило",
  archive_ref: "Ссылка на архив",
  conflict: "Конфликт",
  evidence_ref: "Ссылка на доказательство",
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
  fields.validationBadge.textContent = `ПРОВЕРКА: ${getStatusLabel(status)}`;
  fields.validationBadge.className = status === "PASS" ? "badge pass" : "badge block";
}

function renderGlobalRules(rules) {
  fields.globalRules.replaceChildren();

  for (const item of rules) {
    const display = globalRuleDisplay[item.name] || {
      title: item.name,
      body: item.rule,
    };
    const card = document.createElement("article");
    card.className = "rule-card";

    const title = document.createElement("h3");
    title.textContent = display.title;

    const body = document.createElement("p");
    body.textContent = display.body;

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
    status.textContent = getStatusLabel(route.status);

    const action = document.createElement("span");
    action.className = "route-action";
    action.textContent = getSafeNextAction(route);

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

  fields.routeId.textContent = `ID маршрута: ${route.route_id}`;
  fields.routeButton.textContent = getRouteLabel(route);
  fields.routeStatus.textContent = getStatusLabel(route.status);
  fields.callback.textContent = route.callback;
  fields.role.textContent = getRoleLabel(route);
  fields.purpose.textContent = getPurpose(route);
  fields.safeNextAction.textContent = getSafeNextAction(route);
  fields.contractFile.textContent = route.contract_file;

  renderList(fields.inputs, route.inputs, inputLabels);
  renderList(fields.outputs, route.outputs);
  renderList(fields.agents, route.agents);
  renderList(fields.blocks, route.blocks);
  renderList(fields.handoffs, route.handoffs);
  renderList(fields.rules, route.rules);
}

function renderMissingRoute(routeId) {
  fields.routeId.textContent = `ID маршрута: ${routeId}`;
  fields.routeButton.textContent = "Маршрут не найден";
  fields.routeStatus.textContent = getStatusLabel("local_ui_missing_route");
  fields.callback.textContent = "-";
  fields.role.textContent = "-";
  fields.purpose.textContent =
    "Выбранный route_id отсутствует в локальной карте маршрутов. Остальные кнопки маршрутов продолжают работать независимо.";
  fields.safeNextAction.textContent =
    "Проверьте локальные данные панели и реестр маршрутов. Серверные, Telegram, eBay или боевые действия не выполнялись.";
  fields.contractFile.textContent = "-";

  renderList(fields.inputs, []);
  renderList(fields.outputs, []);
  renderList(fields.agents, []);
  renderList(fields.blocks, []);
  renderList(fields.handoffs, []);
  renderList(fields.rules, []);
}

function getRouteDisplay(route) {
  return routeDisplay[route.route_id] || {};
}

function getRouteLabel(route) {
  return getRouteDisplay(route).label || route.button || route.route_id;
}

function getStatusLabel(status) {
  return statusLabels[status] || status || statusLabels.UNKNOWN;
}

function getRoleLabel(route) {
  return getRouteDisplay(route).role || route.role || "-";
}

function getPurpose(route) {
  return getRouteDisplay(route).purpose || route.purpose_ru || route.purpose || "-";
}

function getSafeNextAction(route) {
  return getRouteDisplay(route).safeNextAction || route.safe_next_action || "-";
}

function renderList(element, values = [], displayMap = {}) {
  element.replaceChildren();
  if (!values.length) {
    const empty = document.createElement("li");
    empty.textContent = "Нет данных";
    element.append(empty);
    return;
  }

  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = displayMap[value] || value;
    element.append(item);
  }
}

function renderMeta() {
  const validation = payload.validation || {};
  const archive = payload.archive || {};
  const archiveStatus = archive.status === "loaded" ? "архив загружен" : archive.status || "неизвестно";
  fields.meta.textContent =
    `Версия ${payload.version || "V7.3C"} | ` +
    `Маршрутов: ${validation.route_count || state.routes.length} | ` +
    `Контракты: ${payload.source_paths?.contracts || "storage/contracts/v7_3c"} | ` +
    `Архив: ${archiveStatus} | ` +
    "Отчёт: runtime_skeleton/_output/validation_report.json";
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
  fields.routeStatus.textContent = getStatusLabel("stopped_locally_no_action");
  fields.safeNextAction.textContent =
    "Локальный экран остановлен. Без рестарта, удаления, Telegram, eBay, коммита или отправки в удалённый репозиторий.";
  renderButtons();
});

initDashboard();
