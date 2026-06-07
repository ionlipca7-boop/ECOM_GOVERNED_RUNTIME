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
    caseNamespace: "case.route_01_new_product",
    agentId: "product_intake_agent",
    bridgeTarget: "server_bridge.product_intake",
    instructions: "Вставьте ссылку поставщика, название, текст товара, цены, остаток, доставку и комментарий Ion.",
    next: "Черновик становится Shared Case JSON и ждёт решения маршрута 07.",
  },
  route_02_variant_product: {
    label: "02 Вариант продукта",
    role: "Блок товара с вариантами",
    purpose: "Создать мастер-товар с вариантами, SKU, количеством, ценами и фото.",
    safeNextAction:
      "Проверить матрицу вариантов и остаток по каждому SKU, затем передать на одобрение в маршрут 07.",
    caseNamespace: "case.route_02_variant_product",
    agentId: "variant_matrix_agent",
    bridgeTarget: "server_bridge.variant_matrix",
    instructions: "Опишите мастер-товар, варианты, цены, остатки и соответствие фото.",
    next: "Кейс идёт в placeholder агента матрицы вариантов без live-действий.",
  },
  route_03_listing_studio: {
    label: "03 Студия размещения объявлений",
    role: "Блок экспериментов с листингом",
    purpose: "Улучшать угол подачи листинга через A/B/C-черновики без клонов одного покупательского намерения.",
    safeNextAction:
      "Сравнить варианты черновиков, оставить доказательства только для чтения и запросить одобрение маршрута 07.",
    caseNamespace: "case.route_03_listing_studio",
    agentId: "listing_studio_agent",
    bridgeTarget: "server_bridge.listing_studio",
    instructions: "Вставьте SKU или URL листинга, идею эксперимента, угол заголовка и покупательское намерение.",
    next: "Кейс идёт в listing studio agent placeholder и затем в route 07.",
  },
  route_04_marketplace_lifecycle: {
    label: "04 Жизненный цикл торговой площадки",
    role: "Блок жизненного цикла листингов",
    purpose: "Наблюдать состояние листингов и показывать только полезные сигналы внимания.",
    safeNextAction:
      "Определить состояние листинга, подготовить рекомендацию без боевых действий и провести решение через маршрут 07.",
    caseNamespace: "case.route_04_marketplace_lifecycle",
    agentId: "lifecycle_monitor_agent",
    bridgeTarget: "server_bridge.lifecycle_monitor",
    instructions: "Укажите листинг/SKU, проблему метрик, рекомендацию и нужное решение.",
    next: "Кейс идёт в lifecycle monitor placeholder и ждёт approval gate.",
  },
  route_05_finance_inventory: {
    label: "05 Финансы / Инвентаризация",
    role: "Блок правды по складу и деньгам",
    purpose: "Поддерживать единый источник правды по складу, себестоимости, деньгам и SKU.",
    safeNextAction:
      "Проверить чеки, себестоимость, остатки и конфликты до того, как другие маршруты будут опираться на эти данные.",
    caseNamespace: "case.route_05_finance_inventory",
    agentId: "finance_stock_agent",
    bridgeTarget: "server_bridge.finance_stock",
    instructions: "Введите SKU/товар, остаток, себестоимость, продажи, прибыль и решение по дозакупке.",
    next: "Кейс идёт в finance stock placeholder без записи на сервер.",
  },
  route_06_product_radar: {
    label: "06 Продуктовый радар",
    role: "Блок исследования товаров",
    purpose: "Оценивать идеи товаров до покупки или размещения.",
    safeNextAction:
      "Собрать исследовательскую карточку только для чтения: доказательства, риск, маржа и запрос решения Ion.",
    caseNamespace: "case.route_06_product_radar",
    agentId: "product_radar_agent",
    bridgeTarget: "server_bridge.product_radar",
    instructions: "Опишите идею товара, источник, цену поставщика, спрос, конкурентов и решение.",
    next: "Кейс идёт в product radar placeholder только для исследования.",
  },
  route_07_decision_center: {
    label: "07 Решения / отчёты / агенты",
    role: "Блок решений и безопасных ворот",
    purpose: "Держать одобрения, отчёты, заблокированные случаи, ожидания решений и точные безопасные ворота действий.",
    safeNextAction:
      "Показать короткую безопасную карточку решения и записать точный маркер одобрения или блокировки.",
    caseNamespace: "case.route_07_decision_center",
    agentId: "decision_dispatcher_agent",
    bridgeTarget: "server_bridge.decision_dispatcher",
    instructions: "Опишите решение, что нужно одобрить, варианты, приоритет и срок.",
    next: "Кейс остаётся в decision dispatcher placeholder до точного решения Ion.",
  },
  route_08_memory_teacher: {
    label: "08 Система / память",
    role: "Блок автономной памяти проекта",
    purpose: "Вести автономную память проекта: уроки, правила, указатели архива, доказательства и безопасность.",
    safeNextAction:
      "Сохранять только уроки с доказательствами, а конфликты маршрутов возвращать в маршрут 07 для решения Ion.",
    caseNamespace: "case.route_08_memory_teacher",
    agentId: "system_memory_agent",
    bridgeTarget: "server_bridge.system_memory",
    instructions: "Опишите системную заметку, память, правило или диагностику. Не вставляйте секреты.",
    next: "Кейс идёт в system memory placeholder без записи в память до approval gate.",
  },
};

const routeFields = {
  route_01_new_product: [
    ["supplier_url", "Ссылка поставщика", "input"],
    ["product_name", "Название товара", "input"],
    ["product_text", "Текст товара", "textarea"],
    ["photo_notes", "Фото / файлы / заметки", "textarea"],
    ["receipt_notes", "Чек / закупка", "textarea"],
    ["cost_price", "Цена закупки", "input"],
    ["sell_price", "Цена продажи", "input"],
    ["stock_qty", "Количество", "input"],
    ["shipping_notes", "Доставка", "textarea"],
    ["ion_comments", "Комментарии Ion", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_02_variant_product: [
    ["master_product_name", "Название мастер-товара", "input"],
    ["variants_notes", "Заметки по вариантам", "textarea"],
    ["variant_price_qty_notes", "Цены и количество вариантов", "textarea"],
    ["photo_mapping_notes", "Соответствие фото вариантам", "textarea"],
    ["ion_comments", "Комментарии Ion", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_03_listing_studio: [
    ["listing_url_or_sku", "URL листинга или SKU", "input"],
    ["experiment_idea", "Идея эксперимента", "textarea"],
    ["title_angle", "Угол заголовка", "input"],
    ["buyer_intent", "Покупательское намерение", "textarea"],
    ["notes", "Заметки", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_04_marketplace_lifecycle: [
    ["listing_url_or_sku", "URL листинга или SKU", "input"],
    ["metric_problem_notes", "Проблема метрик", "textarea"],
    ["recommendation_notes", "Рекомендация", "textarea"],
    ["action_decision", "Решение по действию", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_05_finance_inventory: [
    ["product_or_sku", "Товар или SKU", "input"],
    ["stock_qty", "Количество", "input"],
    ["cost_notes", "Заметки по себестоимости", "textarea"],
    ["sales_notes", "Заметки по продажам", "textarea"],
    ["profit_notes", "Заметки по прибыли", "textarea"],
    ["reorder_decision", "Решение по дозакупке", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_06_product_radar: [
    ["product_idea", "Идея товара", "input"],
    ["source_url", "Источник / URL", "input"],
    ["supplier_price", "Цена поставщика", "input"],
    ["demand_proof_notes", "Доказательства спроса", "textarea"],
    ["competitor_notes", "Конкуренты", "textarea"],
    ["decision_notes", "Заметки по решению", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_07_decision_center: [
    ["decision_title", "Название решения", "input"],
    ["approval_needed", "Что нужно одобрить", "textarea"],
    ["options", "Варианты", "textarea"],
    ["priority", "Приоритет", "input"],
    ["deadline", "Срок", "input"],
    ["next_action", "Следующее действие", "input"],
  ],
  route_08_memory_teacher: [
    ["system_note", "Системная заметка", "textarea"],
    ["memory_note", "Заметка памяти", "textarea"],
    ["rule_note", "Правило", "textarea"],
    ["diagnostic_note", "Диагностика", "textarea"],
    ["next_action", "Следующее действие", "input"],
  ],
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
  operatorTitle: document.querySelector("#operatorTitle"),
  operatorPurpose: document.querySelector("#operatorPurpose"),
  operatorInstructions: document.querySelector("#operatorInstructions"),
  operatorNext: document.querySelector("#operatorNext"),
  operatorChain: document.querySelector("#operatorChain"),
  operatorForm: document.querySelector("#operatorForm"),
  draftStatus: document.querySelector("#draftStatus"),
  previewCard: document.querySelector("#previewCard"),
  caseJsonOutput: document.querySelector("#caseJsonOutput"),
  saveDraftButton: document.querySelector("#saveDraftButton"),
  buildCardButton: document.querySelector("#buildCardButton"),
  exportJsonButton: document.querySelector("#exportJsonButton"),
  clearFormButton: document.querySelector("#clearFormButton"),
};

function initDashboard() {
  buildRouteMap();
  renderValidation(payload.validation || {});
  renderGlobalRules(payload.global_rules || []);
  renderButtons();
  bindWorkspaceButtons();

  const firstRouteId = state.routes[0]?.route_id || null;
  selectRoute(firstRouteId, false);
  renderMeta();
}

function buildRouteMap() {
  state.routeMap = Object.create(null);
  for (const route of state.routes) {
    if (route?.route_id) {
      state.routeMap[route.route_id] = route;
    }
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
    const display = globalRuleDisplay[item.name] || { title: item.name, body: item.rule };
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
  renderOperatorWorkspace(route);
}

function renderRoute(route) {
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

function renderOperatorWorkspace(route) {
  const display = getRouteDisplay(route);
  fields.operatorTitle.textContent = `Черновик: ${getRouteLabel(route)}`;
  fields.operatorPurpose.textContent = getPurpose(route);
  fields.operatorInstructions.textContent = display.instructions || "Заполните заметки оператора для этого маршрута.";
  fields.operatorNext.textContent = display.next || "Кейс остаётся локальным dry JSON до approval gate.";
  fields.operatorChain.textContent =
    `Telegram → Browser → Case JSON → Server bridge (${display.bridgeTarget || "server_bridge.placeholder"}) → Agent (${display.agentId || "agent_placeholder"})`;

  fields.operatorForm.replaceChildren();
  const draft = loadDraft(route.route_id);
  for (const [name, label, kind] of getRouteFields(route.route_id)) {
    const wrapper = document.createElement("label");
    wrapper.className = "operator-field";
    wrapper.dataset.fieldName = name;
    const caption = document.createElement("span");
    caption.textContent = label;
    const control =
      kind === "textarea" ? document.createElement("textarea") : document.createElement("input");
    control.name = name;
    control.dataset.caseField = name;
    control.value = draft[name] || "";
    if (kind === "textarea") {
      control.rows = 3;
    } else {
      control.type = "text";
    }
    wrapper.append(caption, control);
    fields.operatorForm.append(wrapper);
  }

  fields.draftStatus.textContent = draft.__updated_at
    ? `Черновик восстановлен из localStorage: ${draft.__updated_at}`
    : "Черновик хранится только в этом браузере.";
  fields.previewCard.textContent = "Заполните поля и нажмите «Собрать карточку».";
  fields.caseJsonOutput.textContent = JSON.stringify(buildCaseJson(route), null, 2);
}

function bindWorkspaceButtons() {
  fields.saveDraftButton.addEventListener("click", () => {
    const route = getSelectedRoute();
    if (!route) return;
    saveDraft(route.route_id);
    fields.draftStatus.textContent = "Черновик сохранён локально для этого route_id.";
  });

  fields.buildCardButton.addEventListener("click", () => {
    const route = getSelectedRoute();
    if (!route) return;
    saveDraft(route.route_id);
    renderPreview(route);
  });

  fields.exportJsonButton.addEventListener("click", () => {
    const route = getSelectedRoute();
    if (!route) return;
    saveDraft(route.route_id);
    const caseJson = buildCaseJson(route);
    fields.caseJsonOutput.textContent = JSON.stringify(caseJson, null, 2);
    fields.draftStatus.textContent = "Case JSON собран локально. Ничего не отправлено.";
  });

  fields.clearFormButton.addEventListener("click", () => {
    const route = getSelectedRoute();
    if (!route) return;
    localStorage.removeItem(getDraftKey(route.route_id));
    renderOperatorWorkspace(route);
    fields.draftStatus.textContent = "Форма очищена только для текущего маршрута.";
  });
}

function renderPreview(route) {
  const caseJson = buildCaseJson(route);
  fields.previewCard.replaceChildren();
  const title = document.createElement("h4");
  title.textContent = caseJson.route_name;
  const caseId = document.createElement("p");
  caseId.textContent = `Кейс: ${caseJson.case_id}`;
  const status = document.createElement("p");
  status.textContent = `Статус: ${caseJson.status}; approval: ${caseJson.approval_state}`;
  const next = document.createElement("p");
  next.textContent = `Следующее действие: ${caseJson.next_action || "не указано"}`;
  const chain = document.createElement("p");
  chain.textContent =
    `Цепочка: Telegram → Browser → Case JSON → Server bridge (${getRouteDisplay(route).bridgeTarget}) → Agent (${caseJson.assigned_agent})`;
  const locks = document.createElement("p");
  locks.textContent = "Safety: без Telegram patch, без server write, без eBay, без delete.";
  fields.previewCard.append(title, caseId, status, next, chain, locks);
  fields.caseJsonOutput.textContent = JSON.stringify(caseJson, null, 2);
}

function buildCaseJson(route) {
  const values = getFormValues();
  const now = new Date().toISOString();
  const routeInfo = getRouteDisplay(route);
  const caseId = `case_${route.route_id}_${stableTimestamp(now)}`;
  return {
    case_id: values.case_id || caseId,
    route_id: route.route_id,
    route_name: getRouteLabel(route),
    case_namespace: routeInfo.caseNamespace || `case.${route.route_id}`,
    source_channel: "browser",
    status: "draft_local_only",
    created_at: values.__created_at || now,
    updated_at: now,
    operator_inputs: values,
    supplier_url: values.supplier_url || values.source_url || "",
    product_name: values.product_name || values.master_product_name || values.product_idea || values.product_or_sku || "",
    product_text: values.product_text || values.notes || values.experiment_idea || "",
    photo_notes: values.photo_notes || values.photo_mapping_notes || "",
    receipt_notes: values.receipt_notes || values.cost_notes || "",
    files_notes: values.files_notes || values.photo_notes || values.photo_mapping_notes || "",
    cost_price: values.cost_price || values.supplier_price || "",
    sell_price: values.sell_price || "",
    stock_qty: values.stock_qty || "",
    shipping_notes: values.shipping_notes || "",
    ion_comments: values.ion_comments || values.decision_notes || "",
    next_action: values.next_action || "",
    approval_state: "approval_required_before_live_action",
    assigned_agent: routeInfo.agentId || "agent_placeholder",
    agent_notes: "",
    server_bridge_status: "dry_not_sent",
    report_refs: [`runtime_skeleton/_output/reports/${route.route_id}`],
    checkpoint_refs: [`runtime_skeleton/_output/checkpoints/${route.route_id}`],
    history: [
      {
        at: now,
        channel: "browser",
        event: "local_case_json_built",
      },
    ],
    safety_locks: {
      no_live_telegram_patch: true,
      no_server_write: true,
      no_ebay_action: true,
      no_delete: true,
      approval_required_for_live: true,
    },
  };
}

function getFormValues() {
  const values = {};
  for (const control of fields.operatorForm.querySelectorAll("[data-case-field]")) {
    values[control.dataset.caseField] = control.value.trim();
  }
  return values;
}

function saveDraft(routeId) {
  const current = loadDraft(routeId);
  const now = new Date().toISOString();
  const draft = {
    ...current,
    ...getFormValues(),
    __created_at: current.__created_at || now,
    __updated_at: now,
  };
  localStorage.setItem(getDraftKey(routeId), JSON.stringify(draft));
  return draft;
}

function loadDraft(routeId) {
  try {
    return JSON.parse(localStorage.getItem(getDraftKey(routeId)) || "{}");
  } catch {
    return {};
  }
}

function getDraftKey(routeId) {
  return `v73c.integrationDraft.${routeId}`;
}

function getRouteFields(routeId) {
  return routeFields[routeId] || [["notes", "Заметки", "textarea"], ["next_action", "Следующее действие", "input"]];
}

function getSelectedRoute() {
  return state.routeMap[state.selectedRouteId] || null;
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

function stableTimestamp(value) {
  return value.replace(/[^0-9]/g, "").slice(0, 14);
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
