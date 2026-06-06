import os, json, time, datetime, urllib.parse, urllib.request
import subprocess
from pathlib import Path

# ECOM_SMART_ALBUM_ROUTER_V2_PATCH_START

# === OPERATOR_COCKPIT_V2_RAW_UPDATE_PATCH_BEGIN ===
# R66D candidate: raw Telegram update dict model. No eBay/delete/cleanup. Restart is separate gate.
try:
    import sys as _oc2_sys
    _oc2_sys.path.insert(0, "/home/ionlipca7/ecom_governed_runtime/storage/runtime_bridge/candidates/R64_OPERATOR_COCKPIT_V2_PATCH_CANDIDATE_20260527T173222Z")
    from operator_cockpit_v2_candidate import oc2_get_main_message, oc2_resolve_callback, oc2_validate_pack
    OPERATOR_COCKPIT_V2_RAW_AVAILABLE = bool(oc2_validate_pack().get("ok"))
except Exception:
    OPERATOR_COCKPIT_V2_RAW_AVAILABLE = False

def _oc2_raw_is_callback(data):
    return isinstance(data, str) and (data.startswith("m:") or data.startswith("a:") or data.startswith("nav:"))

def _oc2_raw_send_screen(chat_id, screen):
    try:
        text = screen.get("text", "⚠️ Нет текста экрана.")
        markup = screen.get("reply_markup")
        try:
            return ecom_cockpit_v2_send_message(chat_id, text, markup)
        except TypeError:
            return ecom_cockpit_v2_send_message(chat_id, text)
    except Exception:
        return False

def _oc2_raw_try_handle_callback(chat_id, callback_id, callback_data):
    if not OPERATOR_COCKPIT_V2_RAW_AVAILABLE:
        return False
    if not _oc2_raw_is_callback(callback_data):
        return False
    try:
        ecom_cockpit_v2_answer_callback(callback_id)
    except Exception:
        pass
    screen = oc2_resolve_callback(callback_data)
    _oc2_raw_send_screen(chat_id, screen)
    return True
# === OPERATOR_COCKPIT_V2_RAW_UPDATE_PATCH_END ===

def ecom_smart_album_router_v2_register(saved_photo_path, media_group_id=None, chat_id=None, msg_id=None, file_id=None, caption=""):
    try:
        import importlib.util as _ecom_importlib_util
        from pathlib import Path as _EcomPath
        _module_path = _EcomPath("/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_album_router/smart_telegram_album_photo_router_v2_candidate.py")
        _spec = _ecom_importlib_util.spec_from_file_location("smart_telegram_album_photo_router_v2_candidate", str(_module_path))
        _mod = _ecom_importlib_util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        return _mod.register_album_photo(
            saved_photo_path,
            media_group_id=media_group_id,
            msg_id=msg_id,
            chat_id=chat_id,
            file_id=file_id,
            caption=caption or ""
        )
    except Exception as _ecom_album_router_error:
        try:
            import json as _ecom_json
            import datetime as _ecom_dt
            from pathlib import Path as _EcomPath2
            _root = _EcomPath2("/home/ionlipca7/ecom_governed_runtime")
            _err_dir = _root / "storage/state_control"
            _err_dir.mkdir(parents=True, exist_ok=True)
            _err = {
                "status": "SMART_ALBUM_ROUTER_V2_RUNTIME_ERROR_NO_CRASH",
                "created_utc": _ecom_dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
                "error": str(_ecom_album_router_error),
                "saved_photo_path": str(saved_photo_path),
                "live_ebay_allowed": False
            }
            (_err_dir / "SMART_ALBUM_ROUTER_V2_RUNTIME_LAST_ERROR.json").write_text(
                _ecom_json.dumps(_err, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
        except Exception:
            pass
        return {"status": "SMART_ALBUM_ROUTER_V2_ERROR_NO_CRASH"}

def ecom_virtual_button_tester_v2_run_no_telegram_api():
    try:
        import importlib.util as _ecom_importlib_util
        from pathlib import Path as _EcomPath
        _module_path = _EcomPath("/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_virtual_button_tester/telegram_virtual_button_tester_v2_candidate.py")
        _spec = _ecom_importlib_util.spec_from_file_location("telegram_virtual_button_tester_v2_candidate", str(_module_path))
        _mod = _ecom_importlib_util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        return _mod.run_virtual_button_matrix()
    except Exception as _ecom_button_tester_error:
        return {
            "status": "VIRTUAL_BUTTON_TESTER_V2_ERROR_NO_CRASH",
            "error": str(_ecom_button_tester_error),
            "live_allowed": False
        }
# ECOM_SMART_ALBUM_ROUTER_V2_PATCH_END



# ECOM_PHOTO_PRODUCT_ROUTER_V6_5_PATCH_START
def ecom_photo_router_v6_5_route(saved_photo_path, chat_id=None, msg_id=None, file_id=None, caption=""):
    try:
        import importlib.util as _ecom_importlib_util
        from pathlib import Path as _EcomPath
        _module_path = _EcomPath("/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_photo_router/telegram_photo_product_router_v6_5_candidate.py")
        _spec = _ecom_importlib_util.spec_from_file_location("telegram_photo_product_router_v6_5_candidate", str(_module_path))
        _mod = _ecom_importlib_util.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        return _mod.route_saved_telegram_photo(
            saved_photo_path,
            chat_id=chat_id,
            msg_id=msg_id,
            file_id=file_id,
            caption=caption or ""
        )
    except Exception as _ecom_photo_router_error:
        try:
            import json as _ecom_json
            import datetime as _ecom_dt
            from pathlib import Path as _EcomPath2
            _root = _EcomPath2("/home/ionlipca7/ecom_governed_runtime")
            _err_dir = _root / "storage/state_control"
            _err_dir.mkdir(parents=True, exist_ok=True)
            _err = {
                "status": "PHOTO_ROUTER_RUNTIME_ERROR_NO_CRASH",
                "created_utc": _ecom_dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
                "error": str(_ecom_photo_router_error),
                "saved_photo_path": str(saved_photo_path),
                "live_ebay_allowed": False
            }
            (_err_dir / "PHOTO_ROUTER_RUNTIME_LAST_ERROR.json").write_text(
                _ecom_json.dumps(_err, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
        except Exception:
            pass
        return {"status": "PHOTO_ROUTER_ERROR_NO_CRASH"}
# ECOM_PHOTO_PRODUCT_ROUTER_V6_5_PATCH_END



# ECOM_COCKPIT_V2_INLINE_START
# ECOM_COCKPIT_WAITING_V3_ACTIVE_NO_BACKSLASH_NEWLINE
import json as _cj
import datetime as _cdt
from pathlib import Path as _CP
_CROOT = _CP(__file__).resolve().parent
_CSTATE = _CROOT / 'storage/state_control/OPERATOR_INPUTS_CURRENT_PRODUCT_V1.json'
_CPRODUCT = 'aliexpress:1005005252938636'
_NL = chr(10)
_FIELDS = {
    '1': ('quantity', 'Количество'),
    '2': ('purchase_price', 'Закупка/цена'),
    '3': ('target_price', 'Желаемая цена'),
    '4': ('shipping', 'Доставка'),
    '5': ('photos', 'Фото'),
    '6': ('product_confirmed', 'Товар подтверждаю'),
    '7': ('category', 'Категория'),
    '8': ('competitors_price', 'Конкуренты/цена'),
    '9': ('status', 'Статус'),
    '10': ('next', 'Дальше'),
}

def _ct():
    return _cdt.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')

def _load_cstate():
    try:
        if _CSTATE.exists():
            d = _cj.loads(_CSTATE.read_text(encoding='utf-8'))
            if isinstance(d, dict):
                d.setdefault('active_product_key', _CPRODUCT)
                d.setdefault('operator_inputs', {})
                d.setdefault('cockpit', {})
                d['cockpit'].setdefault('waiting_mode', {'active': False})
                return d
    except Exception:
        pass
    return {'status':'OPERATOR_INPUTS_CURRENT_PRODUCT_V1','active_product_key':_CPRODUCT,'operator_inputs':{},'cockpit':{'waiting_mode':{'active':False}},'publication_status':{'live_gate':'CLOSED','message':'Публикация на eBay не запускается. Live закрыт.'}}

def _save_cstate(d):
    d['updated_utc'] = _ct()
    _CSTATE.parent.mkdir(parents=True, exist_ok=True)
    _CSTATE.write_text(_cj.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')


# RUNTIME_ROUTER_V1_PATCH_START
def _rt_state_path():
    return 'storage/runtime_state/runtime_state_v1.json'

def _rt_load():
    import json, os
    p = _rt_state_path()
    if not os.path.exists(p):
        return {'current_screen':'MAIN_MENU','previous_screen':None,'breadcrumbs':['MAIN_MENU'],'waiting_mode':{'active':False,'field':None,'product_key':None},'live_gate':'CLOSED','restart_gate':'CLOSED','mode':'CANDIDATE_RUNTIME_ONLY'}
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def _rt_save(rt):
    import json, os
    os.makedirs('storage/runtime_state', exist_ok=True)
    with open(_rt_state_path(), 'w', encoding='utf-8') as f:
        json.dump(rt, f, ensure_ascii=False, indent=2)

def _rt_navigate(screen):
    rt = _rt_load()
    prev = rt.get('current_screen')
    rt['previous_screen'] = prev
    rt['current_screen'] = screen
    crumbs = list(rt.get('breadcrumbs') or [])
    if not crumbs or crumbs[-1] != screen:
        crumbs.append(screen)
    rt['breadcrumbs'] = crumbs[-8:]
    _rt_save(rt)
    return rt

def _rt_back():
    rt = _rt_load()
    crumbs = list(rt.get('breadcrumbs') or ['MAIN_MENU'])
    if len(crumbs) > 1:
        crumbs.pop()
    screen = crumbs[-1] if crumbs else 'MAIN_MENU'
    rt['previous_screen'] = rt.get('current_screen')
    rt['current_screen'] = screen
    rt['breadcrumbs'] = crumbs or ['MAIN_MENU']
    _rt_save(rt)
    return rt

def _rt_cancel_waiting():
    rt = _rt_load()
    rt['waiting_mode'] = {'active': False, 'field': None, 'product_key': rt.get('active_product_key')}
    _rt_save(rt)
    return rt

def _rt_label():
    rt = _rt_load()
    return 'Экран: ' + str(rt.get('current_screen','MAIN_MENU')) + '\nLive закрыт. Публикация не запускается.'
# RUNTIME_ROUTER_V1_PATCH_END


def ecom_cockpit_v2_menu_text():
    return """ECOM OS V7.3 — главное меню

📌 Статус:
• Telegram bot активен.
• Memory V2 активна.
• GitHub = source of truth.
• eBay live/create/publish/revise закрыты.

🧩 Основные разделы:
01. Новый товар
02. Товар с вариантами
03. Листинг-студия
04. Marketplace / Lifecycle
05. Финансы / склад
06. Поиск товаров / закупка
07. Решения / отчёты / агенты
08. Система / память

Безопасность:
• active patch только после approval.
• restart только после отдельного approval.
• eBay live закрыт."""

def _status_text(d):
    inp = d.get('operator_inputs', {})
    def v(k):
        x = inp.get(k)
        return x.get('value') if isinstance(x, dict) else None
    q = v('quantity')
    pp = v('purchase_price')
    tp = v('target_price')
    sh = v('shipping')
    ph = v('photos')
    cat = v('category')
    blocks = []
    if not q: blocks.append('Количество ещё не заполнено')
    if not tp: blocks.append('Желаемая цена ещё не заполнена')
    if not ph: blocks.append('Фото ещё не заполнено/не подтверждено')
    if not cat: blocks.append('Категория ещё не подтверждена')
    return _NL.join([
        'Короткий вывод',
        'Пульт товара работает в безопасном режиме.',
        '',
        'Что готово',
        'Количество: ' + (str(q) if q else 'не заполнено'),
        'Закупка/цена: ' + (str(pp) if pp else 'не заполнено'),
        'Желаемая цена: ' + (str(tp) if tp else 'не заполнено'),
        'Доставка: ' + (str(sh) if sh else 'не заполнено'),
        'Фото: ' + (str(ph) if ph else 'не заполнено'),
        'Категория: ' + (str(cat) if cat else 'не заполнено'),
        '',
        'Что блокирует публикацию',
        'БЛОК / BLOCK: ' + (', '.join(blocks) if blocks else 'для cockpit-ввода критичных блокеров нет'),
        '',
        'Следующий безопасный шаг',
        'Заполни недостающие поля или напиши Дальше после проверки.',
        '',
        'Live статус',
        'Публикация на eBay не запускается. Live закрыт.'
    ])


def ecom_cockpit_v2_keyboard_markup():
    return ecom_cockpit_main_inline_keyboard()

def ecom_cockpit_main_inline_keyboard():
    return {
        "inline_keyboard": [
            [
                {"text": "01. Новый товар", "callback_data": "menu:new_product"},
                {"text": "02. Товар с вариантами", "callback_data": "menu:variants"}
            ],
            [
                {"text": "03. Листинг-студия", "callback_data": "menu:listing_studio"},
                {"text": "04. Marketplace / Lifecycle", "callback_data": "menu:marketplace_lifecycle"}
            ],
            [
                {"text": "05. Финансы / склад", "callback_data": "menu:finance_stock"},
                {"text": "06. Поиск товаров / закупка", "callback_data": "menu:product_search"}
            ],
            [
                {"text": "07. Решения / отчёты / агенты", "callback_data": "menu:decisions_agents"},
                {"text": "08. Система / память", "callback_data": "menu:system_memory"}
            ]
        ]
    }

def ecom_cockpit_price_keyboard():
    return {'inline_keyboard': [
        [{'text': 'Закупка/цена', 'callback_data': 'cockpit_wait:purchase_price'}, {'text': 'Желаемая цена', 'callback_data': 'cockpit_wait:target_price'}],
        [{'text': 'Проверить цену', 'callback_data': 'cockpit_price_check'}, {'text': '⬅️ Назад', 'callback_data': 'cockpit_menu'}]
    ]}

def ecom_cockpit_category_keyboard():
    return {'inline_keyboard': [
        [{'text': 'Ввести категорию', 'callback_data': 'cockpit_wait:category'}, {'text': 'Статус категории', 'callback_data': 'c_status'}],
        [{'text': 'Проверить specifics позже', 'callback_data': 'cockpit_category_check'}, {'text': '⬅️ Назад', 'callback_data': 'cockpit_menu'}]
    ]}

def ecom_cockpit_photo_keyboard():
    return {'inline_keyboard': [
        [{'text': 'Фото подтверждаю', 'callback_data': 'cockpit_wait:photos'}, {'text': 'Статус фото', 'callback_data': 'c_status'}],
        [{'text': 'Загрузить фото обычным сообщением', 'callback_data': 'cockpit_photo_help'}, {'text': '⬅️ Назад', 'callback_data': 'cockpit_menu'}]
    ]}

def ecom_cockpit_html_keyboard():
    return {'inline_keyboard': [
        [{'text': 'Ввести заметку HTML', 'callback_data': 'cockpit_wait:html_description'}, {'text': 'Проверить описание позже', 'callback_data': 'cockpit_html_check'}],
        [{'text': '⬅️ Назад', 'callback_data': 'cockpit_menu'}]
    ]}

def ecom_cockpit_approval_keyboard():
    return {'inline_keyboard': [
        [{'text': 'Финальная проверка', 'callback_data': 'c_status'}],
        [{'text': 'Черновик подтверждаю без live', 'callback_data': 'cockpit_wait:draft_approval'}],
        [{'text': '⬅️ Назад', 'callback_data': 'cockpit_menu'}, {'text': '❌ Отмена', 'callback_data': 'c_cancel'}]
    ]}

_COCKPIT_LABELS = {
    'quantity': 'Количество',
    'purchase_price': 'Закупка/цена',
    'target_price': 'Желаемая цена',
    'shipping': 'Доставка',
    'photos': 'Фото',
    'category': 'Категория',
    'html_description': 'HTML / описание',
    'draft_approval': 'Подтверждение черновика',
    'product_confirmed': 'Товар подтверждаю',
    'competitors': 'Конкуренты/цена'
}

def ecom_cockpit_v2_send_message(chat_id, text, reply_markup=None):
    try:
        import requests
        import os as _os
        tok = _os.environ.get('TELEGRAM_BOT_TOKEN')
        if not tok:
            return False
        payload = {'chat_id': chat_id, 'text': text}
        if reply_markup is not None:
            payload['reply_markup'] = reply_markup
        r = requests.post('https://api.telegram.org/bot' + str(tok) + '/sendMessage', json=payload, timeout=20)
        try:
            from pathlib import Path as _Path
            _Path('/home/ionlipca7/runtime_eco_v1/storage/state_control/telegram_last_send_response_debug_v1.json').write_text(__import__('json').dumps({'status_code': r.status_code, 'text': r.text[:1000], 'has_reply_markup': reply_markup is not None}, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
        return bool(getattr(r, 'ok', False))
    except Exception as _e:
        try:
            from pathlib import Path as _Path
            _Path('/home/ionlipca7/runtime_eco_v1/storage/state_control/telegram_last_send_response_debug_v1.json').write_text(__import__('json').dumps({'exception': repr(_e), 'has_reply_markup': reply_markup is not None}, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
        return False

def ecom_cockpit_v2_answer_callback(callback_id):
    try:
        import requests
        import os as _os
        tok = _os.environ.get('TELEGRAM_BOT_TOKEN')
        if not tok or not callback_id:
            return False
        requests.post('https://api.telegram.org/bot' + str(tok) + '/answerCallbackQuery', json={'callback_query_id': callback_id}, timeout=10)
        return True
    except Exception:
        return False

def _cockpit_set_wait(chat_id, d, field_key):
    fl = _COCKPIT_LABELS.get(field_key, field_key)
    d.setdefault('cockpit', {})['waiting_mode'] = {'active': True, 'field_key': field_key, 'field_label': fl, 'started_utc': _ct()}
    _save_cstate(d)
    ecom_cockpit_v2_send_message(chat_id, _NL.join(['Введи значение для поля: ' + str(fl), 'Публикация на eBay не запускается. Live закрыт.']))
    return True

def _c_cancel(chat_id, d):
    d.setdefault('cockpit', {})['waiting_mode'] = {'active': False}
    _save_cstate(d)
    ecom_cockpit_v2_send_message(chat_id, _NL.join(['ГОТОВО / PASS', 'Ожидание ввода отменено.', 'Публикация на eBay не запускается. Live закрыт.']), ecom_cockpit_v2_keyboard_markup())
    return True

# === R75E_ENRICHED_RAW_HANDLER_START ===
def _r75e_previous_ecom_cockpit_v2_try_handle_update(update):
    try:
        cb = update.get('callback_query') or {}
        callback_id = cb.get('id')
        callback_data = str(cb.get('data') or '').strip()
        callback_msg = cb.get('message') or {}
        msg = update.get('message') or update.get('edited_message') or callback_msg or {}
        chat_id = (msg.get('chat') or {}).get('id')
        text = str(msg.get('text') or '').strip()

        if not chat_id:
            return False
        # OPERATOR_COCKPIT_V2_RAW_CALLBACK_INTERCEPT_BEGIN
        if _oc2_raw_try_handle_callback(chat_id, callback_id, callback_data):
            return True
        # OPERATOR_COCKPIT_V2_RAW_CALLBACK_INTERCEPT_END

        d = _load_cstate()
        wait = (d.get('cockpit') or {}).get('waiting_mode') or {}

        if callback_data:
            ecom_cockpit_v2_answer_callback(callback_id)

            if callback_data == 'cockpit_menu':
                _rt_navigate('MAIN_MENU')
                d.setdefault('cockpit', {})['waiting_mode'] = {'active': False}
                _save_cstate(d)
                ecom_cockpit_v2_send_message(chat_id, ecom_cockpit_v2_menu_text(), ecom_cockpit_main_inline_keyboard())
                return True

            if callback_data.startswith('cockpit_wait:'):
                return _cockpit_set_wait(chat_id, d, callback_data.split(':', 1)[1].strip())

            if callback_data in ('c_new', 'cockpit_new_product'):
                _rt_navigate('NEW_PRODUCT')
                ecom_cockpit_v2_send_message(chat_id, _NL.join([
                    '🆕 Новый товар',
                    '',
                    'Безопасный режим.',
                    'Отправь ссылку товара или фото/данные товара.',
                    'Старый товар не смешивается.',
                    'Live закрыт.'
                ]), ecom_cockpit_main_inline_keyboard())
                return True

            if callback_data in ('c_agents', 'cockpit_agents_menu'):
                _rt_navigate('LISTING_AGENTS')
                ecom_cockpit_v2_send_message(chat_id, _NL.join([
                    '🧠 Агенты листинга',
                    '',
                    'Доступно по порядку:',
                    '1. Паспорт товара',
                    '2. Заголовок для поиска',
                    '3. Категория / характеристики',
                    '4. Описание товара',
                    '5. Доставка',
                    '6. Финальная проверка',
                    '',
                    'Сначала заполняем текущий товар.',
                    'Live закрыт.'
                ]), ecom_cockpit_main_inline_keyboard())
                return True

            if callback_data in ('c_status', 'cockpit_status'):
                _rt_navigate('CURRENT_PRODUCT')
                ecom_cockpit_v2_send_message(chat_id, _status_text(d), ecom_cockpit_v2_keyboard_markup())
                return True

            if callback_data in ('c_cancel', 'cockpit_cancel'):
                _rt_cancel_waiting()
                return _c_cancel(chat_id, d)

            if callback_data in ('c_price', 'cockpit_price_menu'):
                _rt_navigate('PRICE_COMPETITORS')
                ecom_cockpit_v2_send_message(chat_id, 'Раздел: Цена. Выбери действие.', ecom_cockpit_price_keyboard())
                return True

            if callback_data in ('c_cat', 'cockpit_category_menu'):
                _rt_navigate('CATEGORY_ASPECTS')
                ecom_cockpit_v2_send_message(chat_id, 'Раздел: Категория. Выбери действие.', ecom_cockpit_category_keyboard())
                return True

            if callback_data in ('c_photo', 'cockpit_photo_menu'):
                _rt_navigate('PHOTO_GALLERY')
                ecom_cockpit_v2_send_message(chat_id, 'Раздел: Фото. Выбери действие.', ecom_cockpit_photo_keyboard())
                return True

            if callback_data in ('c_desc', 'cockpit_html_menu'):
                _rt_navigate('DESCRIPTION_DE')
                ecom_cockpit_v2_send_message(chat_id, 'Раздел: HTML / описание. Выбери действие.', ecom_cockpit_html_keyboard())
                return True

            if callback_data in ('c_check', 'cockpit_approval_menu'):
                _rt_navigate('CRITIC')
                ecom_cockpit_v2_send_message(chat_id, 'Раздел: Подтверждение. Live закрыт, публикация не запускается.', ecom_cockpit_approval_keyboard())
                return True

            if callback_data in ('cockpit_price_check', 'cockpit_category_check', 'cockpit_photo_help', 'cockpit_html_check'):
                ecom_cockpit_v2_send_message(chat_id, _NL.join(['ВНИМАНИЕ / WARN', 'Этот helper найден как donor и будет подключён через router следующим шагом.', 'Сейчас live закрыт, старые ветки не запускаются.']), ecom_cockpit_v2_keyboard_markup())
                return True

            return False

        if not text:
            return False

        low = text.lower()

        if bool(wait.get('active')) and wait.get('field_key'):
            fk = wait.get('field_key')
            fl = wait.get('field_label') or _COCKPIT_LABELS.get(fk, fk)
            d.setdefault('operator_inputs', {})[fk] = {'value': text, 'source': 'telegram_operator', 'status': 'operator_entered', 'updated_utc': _ct()}
            d.setdefault('cockpit', {})['waiting_mode'] = {'active': False}
            _save_cstate(d)
            ecom_cockpit_v2_send_message(chat_id, _NL.join(['ГОТОВО / PASS', 'Поле сохранено: ' + str(fl) + ' = ' + text, 'Публикация на eBay не запускается. Live закрыт.']), ecom_cockpit_v2_keyboard_markup())
            return True

        # ECOM_RU_KEYBOARD_HELPER_CALL_CURRENT_START
        try:
            from storage.tools.ecom_os_v3.ru_keyboard_handlers_current import handle_ru_keyboard
            if handle_ru_keyboard(chat_id, text, globals().get('API_URL'), ecom_cockpit_v2_keyboard_markup(), ecom_cockpit_v2_menu_text()):
                return True
        except Exception as e:
            print('ECOM_RU_KEYBOARD_HELPER_CALL_ERROR: ' + repr(e), flush=True)
        # ECOM_RU_KEYBOARD_HELPER_CALL_CURRENT_END

        if low in ('/cockpit', 'cockpit', 'пульт', '/menu', 'menu', '🏠 главное меню', 'главное меню', 'меню'):
            d.setdefault('cockpit', {})['waiting_mode'] = {'active': False}
            _save_cstate(d)
            ecom_cockpit_v2_send_message(chat_id, ecom_cockpit_v2_menu_text(), ecom_cockpit_main_inline_keyboard())
            return True

        if low in ('статус', 'status', 'сводка') or text == '9':
            ecom_cockpit_v2_send_message(chat_id, _status_text(d), ecom_cockpit_v2_keyboard_markup())
            return True

        if low in ('отмена', 'cancel'):
            return _c_cancel(chat_id, d)

        if text in _FIELDS:
            fk, fl = _FIELDS[text]
            if fk in ('status', 'next'):
                ecom_cockpit_v2_send_message(chat_id, _status_text(d), ecom_cockpit_v2_keyboard_markup())
                return True
            return _cockpit_set_wait(chat_id, d, fk)

        return False
    except Exception as _e:
        try:
            from pathlib import Path as _Path
            _Path('/home/ionlipca7/runtime_eco_v1/storage/state_control/ecom_cockpit_v2_handler_exception_v1.json').write_text(__import__('json').dumps({'exception': repr(_e)}, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
        return False


import json as _r75e_json
ECOM_COCKPIT_R75_PACK = _r75e_json.loads('{\n  "report": "R72_REVIEW_RICH_PREVIEW_AND_CREATE_ENRICHMENT_PATCH_GATE_NO_RESTART",\n  "created_utc": "20260527T175914Z",\n  "status": "PASS_R72_POLISHED_RICH_CONTENT_PACK_AND_GATE_READY_NO_ACTIVE_PATCH",\n  "source_r71_pointer": "[internal reference]",\n  "source_r70_pointer": "[internal reference]",\n  "source_pack": "[internal reference]",\n  "precheck": {\n    "r71_pass": true,\n    "preview_sent": true,\n    "r70_pass": true,\n    "pack_exists": true,\n    "r69_pass": true,\n    "no_active_patch": true,\n    "no_restart": true,\n    "no_ebay": true,\n    "no_delete_cleanup": true\n  },\n  "review": {\n    "screens_count": 18,\n    "problems_before_count": 4,\n    "problems_before": [\n      {\n        "screen": "02",\n        "problem": "server_path_in_text"\n      },\n      {\n        "screen": "05",\n        "problem": "server_path_in_text"\n      },\n      {\n        "screen": "09",\n        "problem": "raw_no_pointer_phrase"\n      },\n      {\n        "screen": "16",\n        "problem": "raw_no_pointer_phrase"\n      }\n    ],\n    "problems_after_count": 3,\n    "problems_after": [\n      {\n        "screen": "02",\n        "problem": "raw_status_code_visible_review_needed"\n      },\n      {\n        "screen": "15",\n        "problem": "raw_status_code_visible_review_needed"\n      },\n      {\n        "screen": "17",\n        "problem": "raw_status_code_visible_review_needed"\n      }\n    ],\n    "server_paths_removed_from_operator_text": true,\n    "raw_no_pointer_phrase_removed": true\n  },\n  "real_status_inputs": {\n    "pointer_records_read": 80,\n    "pointer_status_counter": {\n      "PASS": 65,\n      "BLOCK": 9,\n      "OTHER": 6\n    },\n    "images_total": 399,\n    "images_older_12h": 399,\n    "latest_image_parent": "[internal reference]",\n    "top_image_folders": [\n      {\n        "folder": "[internal reference]",\n        "count": 44\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 32\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 22\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 21\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 16\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 12\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 12\n      },\n      {\n        "folder": "[internal reference]",\n        "count": 12\n      }\n    ],\n    "runtime_status": {\n      "bot_alive_after_r67": true,\n      "tmux_ok_after_r67": true,\n      "patch_present_r67": true,\n      "bad_log_signals_r67": [],\n      "r66e_patch_scope": "callback_only_raw_update_m_a_nav_callbacks",\n      "start_touched_after": false\n    },\n    "latest_cockpit": [\n      {\n        "name": "R69_RUNTIME_VERIFY_RESULT_POINTER.json",\n        "status": "PASS_R69_CORE_RUNTIME_VERIFY_RECORDED_NEEDS_RICH_CONTENT_PACK",\n        "updated_utc": "20260527T175146Z",\n        "next_safe_action": "R70_CREATE_RICH_COCKPIT_CONTENT_PACK_FROM_REAL_PROJECT_STATUS_NO_ACTIVE_PATCH",\n        "path": "[internal reference]"\n      },\n      {\n        "name": "R68_RUNTIME_VERIFY_COCKPIT_TEST_PANEL_POINTER.json",\n        "status": "PASS_R68_TEST_PANEL_SENT_READY_FOR_OPERATOR_BUTTON_TEST",\n        "updated_utc": "20260527T174528Z",\n        "next_safe_action": "OPERATOR_PRESS_R68_TEST_BUTTONS_THEN_R69_RECORD_RUNTIME_VERIFY_RESULT",\n        "path": "[internal reference]"\n      },\n      {\n        "name": "R67_RAW_UPDATE_COCKPIT_RESTART_POINTER.json",\n        "status": "PASS_R67_RAW_UPDATE_COCKPIT_BOT_RESTARTED_AND_ALIVE",\n        "updated_utc": "20260527T174354Z",\n        "next_safe_action": "R68_RUNTIME_VERIFY_COCKPIT_CALLBACKS_OPERATOR_TEST_NO_EBAY",\n        "path": "[internal reference]"\n      },\n      {\n        "name": "R66E_RAW_UPDATE_CALLBACK_ONLY_ACTIVE_PATCH_POINTER.json",\n        "status": "PASS_R66E_RAW_UPDATE_CALLBACK_ONLY_ACTIVE_PATCH_COMPILE_OK_NO_RESTART",\n        "updated_utc": "20260527T174242Z",\n        "next_safe_action": "R67_CONTROLLED_RESTART_RAW_UPDATE_COCKPIT_PATCH",\n        "path": "[internal reference]"\n      },\n      {\n        "name": "R66D_RAW_UPDATE_COCKPIT_CANDIDATE_POINTER.json",\n        "status": "PASS_R66D_RAW_UPDATE_CALLBACK_CANDIDATE_READY_NO_ACTIVE_WRITE",\n        "updated_utc": "20260527T174037Z",\n        "next_safe_action": "R66E_APPLY_RAW_UPDATE_CALLBACK_ONLY_ACTIVE_PATCH_NO_RESTART_WITH_BACKUP",\n        "path": "[internal reference]"\n      }\n    ],\n    "latest_quarantine": [\n      {\n        "name": "R66Q_QUARANTINE_LEDGER_POINTER.json",\n        "status": "PASS_R66Q_QUARANTINE_LEDGER_READY_NO_DELETE_NO_MOVE",\n        "updated_utc": "20260527T174141Z",\n        "next_safe_action": "R66E_APPLY_RAW_UPDATE_CALLBACK_ONLY_ACTIVE_PATCH_NO_RESTART_WITH_BACKUP",\n        "path": "[internal reference]"\n      }\n    ]\n  },\n  "screens": [\n    {\n      "n": "01",\n      "title": "Новый товар",\n      "goal": "Запустить intake нового товара через фото + описание.",\n      "text": "01. Новый товар\\n🎯 Задача\\nЗапустить intake нового товара через фото + описание.\\n\\n📊 Сейчас\\n• Новый live-запуск не открыт.\\n• Текущий фокус: довести Cockpit UX и проверки до стабильного слоя.\\n\\n➡️ Дальше\\n• После UX — вернуться к intake товара.\\n• Для live/eBay нужен отдельный gate.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "📷 Фото",\n        "📝 Описание",\n        "✅ Проверить ввод"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "01",\n        "operator_title": "Новый товар",\n        "primary_callback": "m:01",\n        "safe_callbacks": {\n          "open": "m:01",\n          "action": "a:01",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "02",\n      "title": "Текущий товар",\n      "goal": "Показать состояние текущего товара и готовность draft-пакета.",\n      "text": "02. Текущий товар\\n🎯 Задача\\nПоказать состояние текущего товара и готовность draft-пакета.\\n\\n📊 Сейчас\\n• Dry-review статус: PASS_FINAL_DRY_RUN_REVIEW_CONFIRMED_NO_EBAY_API\\n• Папка последних фото: папка галереи текущего товара\\n• Бот после restart работает\\n\\n➡️ Дальше\\n• Проверить паспорт товара.\\n• Проверить фото и approval перед live-gate.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "📦 Паспорт",\n        "🖼 Фото",\n        "✅ Готовность"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "02",\n        "operator_title": "Текущий товар",\n        "primary_callback": "m:02",\n        "safe_callbacks": {\n          "open": "m:02",\n          "action": "a:02",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "03",\n      "title": "Паспорт товара",\n      "goal": "Проверить поля товара и недостающие данные.",\n      "text": "03. Паспорт товара\\n🎯 Задача\\nПроверить поля товара и недостающие данные.\\n\\n📊 Сейчас\\n• Pointers PASS/BLOCK/OTHER: {\'PASS\': 65, \'BLOCK\': 9, \'OTHER\': 6}\\n• Нужен отдельный field-level audit перед финальным листингом.\\n\\n➡️ Дальше\\n• Собрать required fields.\\n• Проверить category/specs связку.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🔎 Недостаёт",\n        "📋 Все поля",\n        "✅ Проверить"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "03",\n        "operator_title": "Паспорт товара",\n        "primary_callback": "m:03",\n        "safe_callbacks": {\n          "open": "m:03",\n          "action": "a:03",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "04",\n      "title": "Источники",\n      "goal": "Показать источники, ссылки, доказательства и риски.",\n      "text": "04. Источники\\n🎯 Задача\\nПоказать источники, ссылки, доказательства и риски.\\n\\n📊 Сейчас\\n• Live actions закрыты.\\n• Источник должен быть виден перед описанием и pricing.\\n\\n➡️ Дальше\\n• Проверить ссылки.\\n• Отделить operator notes от publish-ready data.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🔗 Добавить",\n        "📚 Список",\n        "⚠️ Риски"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "04",\n        "operator_title": "Источники",\n        "primary_callback": "m:04",\n        "safe_callbacks": {\n          "open": "m:04",\n          "action": "a:04",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "05",\n      "title": "Фото / галерея",\n      "goal": "Проверить фото, галерею, visual audit и cleanup gate.",\n      "text": "05. Фото / галерея\\n🎯 Задача\\nПроверить фото, галерею, visual audit и cleanup gate.\\n\\n📊 Сейчас\\n• Фото всего: 399\\n• Фото старше 12 часов: 399\\n• Главная папка фото: Telegram inbox с загруженными фото\\n\\n➡️ Дальше\\n• Сделать photo-status rich card.\\n• Cleanup только отдельным cleanup gate.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🖼 Статус",\n        "🧠 Visual",\n        "🧹 План очистки"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "05",\n        "operator_title": "Фото / галерея",\n        "primary_callback": "m:05",\n        "safe_callbacks": {\n          "open": "m:05",\n          "action": "a:05",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "06",\n      "title": "Заголовок / SEO",\n      "goal": "Подготовить title и ключевые слова.",\n      "text": "06. Заголовок / SEO\\n🎯 Задача\\nПодготовить title и ключевые слова.\\n\\n📊 Сейчас\\n• SEO-карточка ещё базовая.\\n• Нужен rich pack из текущего товара и DE marketplace context.\\n\\n➡️ Дальше\\n• Создать title draft.\\n• Проверить длину/ключи/DE-читабельность.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "✍️ Draft",\n        "🔍 SEO",\n        "🇩🇪 DE-check"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "06",\n        "operator_title": "Заголовок / SEO",\n        "primary_callback": "m:06",\n        "safe_callbacks": {\n          "open": "m:06",\n          "action": "a:06",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "07",\n      "title": "Описание DE",\n      "goal": "Собрать немецкое описание и HTML.",\n      "text": "07. Описание DE\\n🎯 Задача\\nСобрать немецкое описание и HTML.\\n\\n📊 Сейчас\\n• Описание не должно уходить live без approval.\\n• Нужен отдельный DE polish card.\\n\\n➡️ Дальше\\n• Собрать описание из паспорта.\\n• Проверить HTML и human-readable preview.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🇩🇪 Создать",\n        "🧾 HTML",\n        "🧠 Улучшить"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "07",\n        "operator_title": "Описание DE",\n        "primary_callback": "m:07",\n        "safe_callbacks": {\n          "open": "m:07",\n          "action": "a:07",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "08",\n      "title": "Категория / specs",\n      "goal": "Проверить категорию и item specifics.",\n      "text": "08. Категория / specs\\n🎯 Задача\\nПроверить категорию и item specifics.\\n\\n📊 Сейчас\\n• Category/specs не должны быть guessed-live.\\n• Нужен required-specifics audit.\\n\\n➡️ Дальше\\n• Показать missing specifics.\\n• Сделать no-live validation.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "📂 Категория",\n        "📌 Недостаёт",\n        "✅ Required"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "08",\n        "operator_title": "Категория / specs",\n        "primary_callback": "m:08",\n        "safe_callbacks": {\n          "open": "m:08",\n          "action": "a:08",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "09",\n      "title": "Цена / конкуренты",\n      "goal": "Показать price/competitor status.",\n      "text": "09. Цена / конкуренты\\n🎯 Задача\\nПоказать price/competitor status.\\n\\n📊 Сейчас\\n• Price audit: свежий отчёт ещё не найден — нужен audit\\n• Цена пока не меняет marketplace.\\n• Нужен richer competitor summary.\\n\\n➡️ Дальше\\n• Собрать конкурентов.\\n• Отделить recommendation от live price action.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "💶 Статус",\n        "📊 Отчёт",\n        "🧠 Price"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "09",\n        "operator_title": "Цена / конкуренты",\n        "primary_callback": "m:09",\n        "safe_callbacks": {\n          "open": "m:09",\n          "action": "a:09",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "10",\n      "title": "Количество / склад",\n      "goal": "Проверить quantity/stock.",\n      "text": "10. Количество / склад\\n🎯 Задача\\nПроверить quantity/stock.\\n\\n📊 Сейчас\\n• Stock/quantity live не менялись.\\n• Нужен human confirmation перед any revise.\\n\\n➡️ Дальше\\n• Показать quantity draft.\\n• Проверить риск oversell.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "📦 Кол-во",\n        "⚠️ Риски",\n        "✅ Confirm draft"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "10",\n        "operator_title": "Количество / склад",\n        "primary_callback": "m:10",\n        "safe_callbacks": {\n          "open": "m:10",\n          "action": "a:10",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "11",\n      "title": "Доставка",\n      "goal": "Проверить shipping logic.",\n      "text": "11. Доставка\\n🎯 Задача\\nПроверить shipping logic.\\n\\n📊 Сейчас\\n• Shipping live не менялся.\\n• Нужны вес/размер/страна доставки.\\n\\n➡️ Дальше\\n• Проверить shipping policy.\\n• Собрать размеры/вес.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🚚 Map",\n        "📏 Вес/размер",\n        "⚠️ Риски"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "11",\n        "operator_title": "Доставка",\n        "primary_callback": "m:11",\n        "safe_callbacks": {\n          "open": "m:11",\n          "action": "a:11",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "12",\n      "title": "Бизнес-политики",\n      "goal": "Проверить payment/return/shipping policies.",\n      "text": "12. Бизнес-политики\\n🎯 Задача\\nПроверить payment/return/shipping policies.\\n\\n📊 Сейчас\\n• Policy live не менялась.\\n• Нужен policy compatibility check перед listing.\\n\\n➡️ Дальше\\n• Сверить payment/return/shipping.\\n• Зафиксировать выбранные policy IDs без секретов.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "💳 Payment",\n        "↩️ Return",\n        "🚚 Shipping"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "12",\n        "operator_title": "Бизнес-политики",\n        "primary_callback": "m:12",\n        "safe_callbacks": {\n          "open": "m:12",\n          "action": "a:12",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "13",\n      "title": "Проверка / критика",\n      "goal": "Quality review перед любым финальным gate.",\n      "text": "13. Проверка / критика\\n🎯 Задача\\nQuality review перед любым финальным gate.\\n\\n📊 Сейчас\\n• Cockpit core verified.\\n• Rich content ещё создаётся.\\n• Full menu patch пока закрыт.\\n\\n➡️ Дальше\\n• Запустить финальный quality audit.\\n• Собрать список remaining gaps.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🧪 Quality",\n        "⚠️ Риски",\n        "🧭 Что исправить"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "13",\n        "operator_title": "Проверка / критика",\n        "primary_callback": "m:13",\n        "safe_callbacks": {\n          "open": "m:13",\n          "action": "a:13",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "14",\n      "title": "Агенты листинга",\n      "goal": "Показать роли агентов и их состояние.",\n      "text": "14. Агенты листинга\\n🎯 Задача\\nПоказать роли агентов и их состояние.\\n\\n📊 Сейчас\\n• Legacy tester в карантине.\\n• Clean source: R66D raw-update candidate.\\n• Агенты должны отвечать по формату result → next step.\\n\\n➡️ Дальше\\n• Обогатить agent cards.\\n• Разделить Visual/Price/Guard/Archivist.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🤖 Список",\n        "🔔 Разбудить",\n        "🗂 Архивист"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "14",\n        "operator_title": "Агенты листинга",\n        "primary_callback": "m:14",\n        "safe_callbacks": {\n          "open": "m:14",\n          "action": "a:14",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "15",\n      "title": "Digest / отчёты",\n      "goal": "Показать digest, отчёты и расписание.",\n      "text": "15. Digest / отчёты\\n🎯 Задача\\nПоказать digest, отчёты и расписание.\\n\\n📊 Сейчас\\n• Digest pointer: PASS_FINAL_TELEGRAM_DIGEST_RUNTIME_V2E_ACTIVE_AND_DELIVERED\\n• Telegram delivery target закреплён.\\n• Секреты не печатались.\\n\\n➡️ Дальше\\n• Показать последний отчёт.\\n• Проверить расписание digest.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "📰 Статус",\n        "⏰ Расписание",\n        "📨 Повтор"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "15",\n        "operator_title": "Digest / отчёты",\n        "primary_callback": "m:15",\n        "safe_callbacks": {\n          "open": "m:15",\n          "action": "a:15",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "16",\n      "title": "Live Guard",\n      "goal": "Показать live/eBay safety gates.",\n      "text": "16. Live Guard\\n🎯 Задача\\nПоказать live/eBay safety gates.\\n\\n📊 Сейчас\\n• Guard audit: свежий отчёт ещё не найден — нужен audit\\n• eBay/create/publish/revise/delete закрыты.\\n• Команда [start-route] не тронута; тестовый Cockpit работает отдельно\\n\\n➡️ Дальше\\n• Проверить separate live gate.\\n• Открывать live только отдельным подтверждением.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🛡 Статус",\n        "🔒 Gate",\n        "🚫 Что закрыто"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "16",\n        "operator_title": "Live Guard",\n        "primary_callback": "m:16",\n        "safe_callbacks": {\n          "open": "m:16",\n          "action": "a:16",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "17",\n      "title": "Approval",\n      "goal": "Показать approval ledger и pending gates.",\n      "text": "17. Approval\\n🎯 Задача\\nПоказать approval ledger и pending gates.\\n\\n📊 Сейчас\\n• Approval статус: PASS_PRE_LIVE_APPROVAL_PACKET_REFRESH_READY_FOR_OPERATOR_REVIEW_NO_EBAY_API\\n• Полная замена меню пока закрыта до enrichment gate.\\n• Следующий шаг: проверить rich-preview и затем отдельный enrichment gate.\\n\\n➡️ Дальше\\n• Сформировать pending approvals.\\n• Отделить preview approval от live approval.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "✅ Статус",\n        "⏳ Ожидает",\n        "🧾 Gate-карта"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "17",\n        "operator_title": "Approval",\n        "primary_callback": "m:17",\n        "safe_callbacks": {\n          "open": "m:17",\n          "action": "a:17",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    },\n    {\n      "n": "18",\n      "title": "STOP",\n      "goal": "Безопасная остановка/operator safety.",\n      "text": "18. STOP\\n🎯 Задача\\nБезопасная остановка/operator safety.\\n\\n📊 Сейчас\\n• STOP screen работает в R68 test.\\n• Ничего не публикуется, не удаляется и не меняется.\\n\\n➡️ Дальше\\n• Использовать STOP при сомнении.\\n• Вернуться в меню через nav:home.\\n\\n🔒 Безопасность\\n• eBay/create/publish/revise/delete/cleanup не запускаются без отдельного gate.",\n      "actions": [\n        "🛑 Стоп",\n        "🏠 Меню",\n        "🧭 Health"\n      ],\n      "nav": [\n        "⬅️ Назад",\n        "🏠 Главное меню",\n        "🔄 Обновить",\n        "🛑 STOP"\n      ],\n      "polish_applied": true,\n      "r73_enrichment": {\n        "block": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART",\n        "source": "R72_POLISHED_RICH_COCKPIT_CONTENT_PACK",\n        "screen_id": "18",\n        "operator_title": "STOP",\n        "primary_callback": "m:18",\n        "safe_callbacks": {\n          "open": "m:18",\n          "action": "a:18",\n          "home": "nav:home",\n          "stop": "nav:stop"\n        },\n        "runtime_scope": "content_only_candidate_for_existing_raw_update_callbacks",\n        "do_not_patch_start": true,\n        "server_paths_visible_to_operator": false,\n        "r74_review_required": true,\n        "r75_active_patch_requires_separate_gate": true\n      }\n    }\n  ],\n  "enrichment_patch_gate": {\n    "gate_status": "DRAFT_READY_NO_ACTIVE_PATCH",\n    "allowed_next": "create candidate module from polished rich pack, compile, then active patch only after separate gate",\n    "must_not_do": [\n      "do not patch [start-route] yet",\n      "do not delete old images",\n      "do not cleanup",\n      "do not touch eBay/create/publish/revise/delete",\n      "do not show server paths in Telegram operator text"\n    ],\n    "patch_scope_candidate": "replace Operator Cockpit V2 pack content only; keep raw-update callback layer",\n    "restart_required_after_active_patch": true\n  },\n  "safety": {\n    "active_bot_write_done": false,\n    "patch_done": false,\n    "restart_done": false,\n    "delete_done": false,\n    "cleanup_done": false,\n    "ebay_api_called": false,\n    "create_done": false,\n    "publish_done": false,\n    "revise_done": false,\n    "existing_listing_touched": false,\n    "private_values_printed": false,\n    "secret_values_printed": false\n  },\n  "next_safe_action": "R73_CREATE_ENRICHED_COCKPIT_PACK_PATCH_CANDIDATE_NO_ACTIVE_WRITE_NO_RESTART"\n}')

def _r75e_find_screens(obj):
    if isinstance(obj, dict):
        for k in ("screens", "items", "cards", "cockpit_screens"):
            v = obj.get(k)
            if isinstance(v, list) and len(v) == 18:
                return v
        for v in obj.values():
            hit = _r75e_find_screens(v)
            if hit:
                return hit
    if isinstance(obj, list):
        for v in obj:
            hit = _r75e_find_screens(v)
            if hit:
                return hit
    return []

def _r75e_sid(screen, i):
    e = screen.get("r73_enrichment") if isinstance(screen, dict) else {}
    raw = str((e or {}).get("screen_id") or screen.get("id") if isinstance(screen, dict) else i)
    digits = "".join(ch for ch in raw if ch.isdigit())
    return (digits or f"{i:02d}").zfill(2)[-2:]

def _r75e_clean(x):
    return " ".join(str(x).replace("/home/", "[internal]/").replace("None", "").split())[:260]

def _r75e_title(screen, sid):
    if isinstance(screen, dict):
        e = screen.get("r73_enrichment") or {}
        for k in ("operator_title", "title", "name", "headline"):
            v = e.get(k) or screen.get(k)
            if v:
                return _r75e_clean(v)[:120]
    return "Раздел " + sid

def _r75e_collect(obj, out, depth=0):
    if depth > 3 or len(out) >= 12:
        return
    if isinstance(obj, str):
        t = _r75e_clean(obj)
        if t and "[internal]/" not in t:
            out.append(t)
    elif isinstance(obj, dict):
        for k in ("status", "summary", "operator_text", "text", "body", "description", "note", "next", "recommendation"):
            if k in obj:
                _r75e_collect(obj[k], out, depth+1)
    elif isinstance(obj, list):
        for v in obj[:8]:
            _r75e_collect(v, out, depth+1)

def _r75e_screens():
    return _r75e_find_screens(ECOM_COCKPIT_R75_PACK)

def _r75e_map():
    return {_r75e_sid(s, i): s for i, s in enumerate(_r75e_screens(), start=1)}

def _r75e_home_text():
    rows = ["🧭 ECOM Operator Cockpit", "", "Выбери раздел:"]
    for i, s in enumerate(_r75e_screens(), start=1):
        sid = _r75e_sid(s, i)
        rows.append(f"{sid} — {_r75e_title(s, sid)}")
    return "\n".join(rows)[:3600]

def _r75e_keyboard(sid=None):
    if sid:
        return {"inline_keyboard": [[{"text":"🏠 Домой","callback_data":"nav:home"},{"text":"⛔ Стоп","callback_data":"nav:stop"}],[{"text":"Действие","callback_data":"a:"+sid}]]}
    rows, row = [], []
    for i, s in enumerate(_r75e_screens(), start=1):
        sid = _r75e_sid(s, i)
        row.append({"text": sid, "callback_data": "m:"+sid})
        if len(row) == 3:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([{"text":"⛔ Стоп","callback_data":"nav:stop"}])
    return {"inline_keyboard": rows}

def _r75e_render(sid, action=False):
    s = _r75e_map().get(sid)
    if not s:
        return "Раздел не найден. Нажми Домой."
    rows = [f"🧭 {sid} — {_r75e_title(s, sid)}", ""]
    if action:
        rows += ["Действие подготовлено в безопасном режиме.", "Live/eBay операции требуют отдельный gate.", ""]
    collected = []
    _r75e_collect(s, collected)
    rows += list(dict.fromkeys(collected))[:10] or ["Информация загружена из enriched content pack."]
    rows += ["", "Навигация: Домой / Стоп"]
    return "\n".join(rows)[:3600]


# === R83_V72_TELEGRAM_MENU_ACTIVE_PATCH_START ===
# R83 active V7.2 Telegram menu layer.
# Old Telegram handler is preserved below as fallback. No restart here.

def _r83_previous_ecom_cockpit_v2_try_handle_update(update):
    try:
        cb = update.get("callback_query") if isinstance(update, dict) else None
        data = str((cb or {}).get("data") or "")
        if not (data.startswith("m:") or data.startswith("a:") or data.startswith("nav:")):
            return _r75e_previous_ecom_cockpit_v2_try_handle_update(update)

        ecom_cockpit_v2_answer_callback((cb or {}).get("id"))
        msg = (cb or {}).get("message") or {}
        chat_id = (msg.get("chat") or {}).get("id") or ((cb or {}).get("from") or {}).get("id")
        if not chat_id:
            return True

        if data == "nav:home":
            return ecom_cockpit_v2_send_message(chat_id, _r75e_home_text(), _r75e_keyboard())
        if data == "nav:stop":
            return ecom_cockpit_v2_send_message(chat_id, "Остановлено. Для продолжения нажми Домой.", None)
        if data.startswith("m:"):
            sid = data.split(":", 1)[1].zfill(2)[-2:]
            return ecom_cockpit_v2_send_message(chat_id, _r75e_render(sid, False), _r75e_keyboard(sid))
        if data.startswith("a:"):
            sid = data.split(":", 1)[1].zfill(2)[-2:]
            return ecom_cockpit_v2_send_message(chat_id, _r75e_render(sid, True), _r75e_keyboard(sid))
        return True
    except Exception:
        return _r75e_previous_ecom_cockpit_v2_try_handle_update(update)

import json as _r83_json
ECOM_V72_MENU = _r83_json.loads('{\n  "status": "R81_V72_TELEGRAM_MENU_CANDIDATE_READY_NO_ACTIVE_WRITE",\n  "created_utc": "20260528T181714Z",\n  "source_r79_pointer": "/home/ionlipca7/ecom_governed_runtime/storage/control_room/R79_TELEGRAM_REMOTE_CONTROL_V72_BASELINE_POINTER.json",\n  "source_r80_pointer": "/home/ionlipca7/ecom_governed_runtime/storage/control_room/R80_V72_BUTTON_REVIEW_POINTER.json",\n  "menu_title": "🏠 ECOM OS — пульт оператора",\n  "home_text": "🏠 ECOM OS — пульт оператора\\n\\nВыбери сценарий. Каждая кнопка запускает не один текст, а рабочую цепочку агентов.\\n\\nЖивые действия на маркетплейсах закрыты до отдельного разрешения.",\n  "screens": [\n    {\n      "id": "01",\n      "label": "🆕 Новый товар",\n      "title": "🆕 Новый товар",\n      "text": [\n        "Сценарий для обычного товара без сложных вариантов.",\n        "Ты даёшь ссылку, фото, чек, комментарий или количество.",\n        "Система сама собирает товар, цену, фото, описание и черновик.",\n        "Чек уходит в финансы, фото живут во временном буфере 12 часов.",\n        "В конце ты получаешь готовый результат: принять, переделать или посмотреть подробнее."\n      ],\n      "buttons": [\n        "🔗 Ссылка",\n        "📷 Фото",\n        "🧾 Чек",\n        "🧠 Собрать",\n        "👁 Результат",\n        "✅ К проверке"\n      ]\n    },\n    {\n      "id": "02",\n      "label": "🧬 Товар с вариантами",\n      "title": "🧬 Товар с вариантами",\n      "text": [\n        "Сценарий для товара с цветами, длиной, мощностью, комплектами или размерами.",\n        "Система создаёт мастер-товар и таблицу вариантов.",\n        "Для каждого варианта можно хранить количество, себестоимость, фото и отличия.",\n        "Подходит, когда один товар продаётся в нескольких исполнениях."\n      ],\n      "buttons": [\n        "🔗 Ссылка",\n        "📷 Фото вариантов",\n        "🧾 Чек",\n        "🧬 Матрица",\n        "📝 Черновик",\n        "✅ К проверке"\n      ]\n    },\n    {\n      "id": "03",\n      "label": "📝 Листинг-студия",\n      "title": "📝 Листинг-студия",\n      "text": [\n        "Здесь создаются новые версии листинга для уже существующего товара.",\n        "Можно сделать разные углы продажи: для поиска, для покупателя, для конкуренции.",\n        "Система меняет заголовок, описание, порядок фото, структуру карточки и цену.",\n        "Перед публикацией проверяется, что это не простой дубль."\n      ],\n      "buttons": [\n        "🧠 3 варианта",\n        "🔎 Для поиска",\n        "🤖 Для ИИ",\n        "👤 Для покупателя",\n        "🧪 Дубли",\n        "✅ К проверке"\n      ]\n    },\n    {\n      "id": "04",\n      "label": "🛒 Маркетплейсы / жизнь листингов",\n      "title": "🛒 Маркетплейсы / жизнь листингов",\n      "text": [\n        "Центр контроля карточек на eBay и будущих маркетплейсах.",\n        "Показывает статус, слабые листинги, дубли и кандидаты на улучшение.",\n        "Проверки идут по дням: 3, 5, 7, 14/15.",\n        "Любые живые изменения закрыты до отдельного разрешения."\n      ],\n      "buttons": [\n        "🛒 eBay",\n        "📊 3/5/7 дней",\n        "🔁 Улучшить",\n        "📉 Слабые",\n        "💶 Расходы",\n        "✅ К проверке"\n      ]\n    },\n    {\n      "id": "05",\n      "label": "📊 Финансы / склад",\n      "title": "📊 Финансы / склад",\n      "text": [\n        "Здесь считается реальная прибыль и остатки.",\n        "Учитываются закупка, количество, упаковка, комиссии, реклама, этикетка доставки и возвраты.",\n        "Доставка не отдельный процесс, но её стоимость входит в расчёт прибыли.",\n        "Можно увидеть, сколько куплено, продано, осталось и сколько товар реально заработал."\n      ],\n      "buttons": [\n        "🧾 Чеки",\n        "📦 Остаток",\n        "📮 Упаковка",\n        "💶 Прибыль",\n        "📉 Продажи",\n        "🔔 Докупить"\n      ]\n    },\n    {\n      "id": "06",\n      "label": "🧭 Поиск товаров / закупка",\n      "title": "🧭 Поиск товаров / закупка",\n      "text": [\n        "Агенты ищут новые идеи товаров и кандидатов для закупки.",\n        "Источники: AliExpress, Alibaba, Temu, Amazon, eBay и конкуренты.",\n        "Система оценивает спрос, риски, конкуренцию и примерную маржу.",\n        "Хорошие идеи попадают во входящие решения."\n      ],\n      "buttons": [\n        "🔎 Найти идеи",\n        "🧪 Риск",\n        "💶 Маржа",\n        "🛒 Где купить",\n        "📈 Тренды",\n        "📥 В решения"\n      ]\n    },\n    {\n      "id": "07",\n      "label": "📥 Решения / отчёты / агенты",\n      "title": "📥 Решения / отчёты / агенты",\n      "text": [\n        "Главные входящие для всех агентов.",\n        "Сюда приходят отчёты, предупреждения, идеи, просьбы принять решение и утренние/вечерние сводки.",\n        "Ты не ищешь, что делать дальше — система сама приносит карточки решений.",\n        "Каждая карточка должна иметь понятные кнопки: принять, переделать, подробнее, позже."\n      ],\n      "buttons": [\n        "📥 Входящие",\n        "👥 Агенты",\n        "📬 Сводка",\n        "⚠️ Важно",\n        "✅ Принять",\n        "🔁 Переделать"\n      ]\n    },\n    {\n      "id": "08",\n      "label": "⚙️ Система / память",\n      "title": "⚙️ Система / память",\n      "text": [\n        "Технический раздел, не для ежедневной работы.",\n        "Показывает состояние бота, память проекта, архивы, безопасные границы и будущую связку Helper/Canvas.",\n        "Здесь нельзя запускать опасные действия без отдельного разрешения."\n      ],\n      "buttons": [\n        "🟢 Статус",\n        "🧠 Память",\n        "🧾 Архив",\n        "🚧 Карантин",\n        "🛡 Безопасность",\n        "🔄 Продолжить"\n      ]\n    }\n  ],\n  "global_buttons": [\n    "🏠 Домой",\n    "⛔ Стоп",\n    "❓ Помощь"\n  ],\n  "callback_prefix": "v72",\n  "operator_text_rules": [\n    "Не показывать технические коды.",\n    "Не показывать серверные пути.",\n    "Не показывать внутренние статусы.",\n    "Писать коротко и по-русски.",\n    "Одна карточка — одно решение или один статус."\n  ],\n  "safety": {\n    "active_bot_write_done": false,\n    "restart_done": false,\n    "ebay_api_called": false,\n    "delete_done": false,\n    "cleanup_done": false,\n    "helper_patch_done": false\n  }\n}')


def _r83_find_screen(screen_id):
    sid = str(screen_id).zfill(2)[-2:]
    for screen in ECOM_V72_MENU.get("screens", []):
        if str(screen.get("id")).zfill(2)[-2:] == sid:
            return screen
    return None

def _r83_home_text():
    return ECOM_V72_MENU.get("home_text") or "🏠 ECOM OS — пульт оператора"

def _r83_home_keyboard():
    rows = []
    row = []
    for screen in ECOM_V72_MENU.get("screens", []):
        row.append({"text": screen.get("label", "Раздел"), "callback_data": "v72:" + str(screen.get("id")).zfill(2)[-2:]})
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    rows.append([
        {"text": "❓ Помощь", "callback_data": "v72:help"},
        {"text": "⛔ Стоп", "callback_data": "v72:stop"}
    ])
    return {"inline_keyboard": rows}

def _r83_screen_text(screen_id):
    screen = _r83_find_screen(screen_id)
    if not screen:
        return "Раздел не найден. Вернись в главное меню."
    lines = [str(screen.get("title") or screen.get("label") or "Раздел"), ""]
    for item in screen.get("text", []):
        lines.append("• " + str(item))
    lines.append("")
    lines.append("Выбери действие ниже.")
    return "\n".join(lines)[:3600]

def _r83_screen_keyboard(screen_id):
    screen = _r83_find_screen(screen_id)
    rows = []
    if screen:
        row = []
        for idx, label in enumerate(screen.get("buttons", []), start=1):
            row.append({"text": str(label), "callback_data": "v72:" + str(screen.get("id")).zfill(2)[-2:] + ":b" + str(idx)})
            if len(row) == 2:
                rows.append(row)
                row = []
        if row:
            rows.append(row)
    rows.append([
        {"text": "🏠 Домой", "callback_data": "v72:home"},
        {"text": "⛔ Стоп", "callback_data": "v72:stop"}
    ])
    return {"inline_keyboard": rows}

def _r83_help_text():
    return (
        "❓ Помощь\n\n"
        "Это пульт ECOM OS. Выбери сценарий, а система запустит нужных агентов.\n"
        "Публикация, изменение и удаление на маркетплейсах закрыты до отдельного разрешения."
    )

# === R88_V72_SUBACTION_BEHAVIOR_ACTIVE_PATCH_START ===
# R88: V7.2 sub-action behavior cards. No real marketplace/live actions here.
ECOM_V72_SUBACTION_BEHAVIOR = _r83_json.loads('{\n  "status": "R86_V72_SUBACTION_BEHAVIOR_CANDIDATE_READY_NO_ACTIVE_WRITE",\n  "created_utc": "20260528T183253Z",\n  "principle": "Под-кнопка не должна быть пустой заглушкой. Она должна открыть понятную карточку, принять данные, поставить задачу агенту или отправить результат в Решения.",\n  "global_rules": [\n    "Не показывать служебные коды, серверные пути, внутренние технические статусы.",\n    "Любое live/eBay действие только через отдельный approval gate.",\n    "Если действие пока не подключено к реальному агенту, показывать честно: подготовлено, следующий слой подключит агента.",\n    "Одна карточка = одно действие или одно решение.",\n    "Все входные данные должны сохраняться в правильный ledger: чек в финансы, фото в 12h buffer, ссылка в evidence/source."\n  ],\n  "screens": [\n    {\n      "id": "01",\n      "name": "🆕 Новый товар",\n      "subactions": [\n        {\n          "button": "🔗 Ссылка",\n          "type": "intake",\n          "agent": "Intake + Source Extractor",\n          "result_card": "Пришли URL товара. Я сохраню источник, извлеку характеристики и проверю, новый это товар или продолжение текущего.",\n          "artifact": "source_evidence"\n        },\n        {\n          "button": "📷 Фото",\n          "type": "media_intake",\n          "agent": "Photo Intake + Photo Critic",\n          "result_card": "Пришли фото или скриншоты. Я сохраню их во временный буфер на 12 часов, разложу по товару и отмечу качество.",\n          "artifact": "photo_temp_buffer"\n        },\n        {\n          "button": "🧾 Чек",\n          "type": "finance_intake",\n          "agent": "Receipt Parser + Finance Ledger",\n          "result_card": "Пришли чек. Я извлеку закупку, количество и цену за штуку, затем отправлю данные в финансы.",\n          "artifact": "purchase_ledger"\n        },\n        {\n          "button": "🧠 Собрать",\n          "type": "orchestrate",\n          "agent": "Product Crew + Draft Crew + Critic Council",\n          "result_card": "Запускаю сбор товара: источник, фото, закупка, конкуренты, описание, цена и черновик.",\n          "artifact": "product_draft_candidate"\n        },\n        {\n          "button": "👁 Результат",\n          "type": "preview",\n          "agent": "Decision Inbox",\n          "result_card": "Покажу текущий собранный результат: что готово, чего не хватает, какие риски и что можно принять.",\n          "artifact": "product_result_preview"\n        },\n        {\n          "button": "✅ К проверке",\n          "type": "approval_prepare",\n          "agent": "Critic Council + Approval Agent",\n          "result_card": "Подготовлю карточку проверки. Live/eBay останется закрыт до отдельного разрешения.",\n          "artifact": "approval_candidate"\n        }\n      ]\n    },\n    {\n      "id": "02",\n      "name": "🧬 Товар с вариантами",\n      "subactions": [\n        {\n          "button": "🔗 Ссылка",\n          "type": "variant_source",\n          "agent": "Variation Intake",\n          "result_card": "Пришли ссылку на товар с вариантами. Я попробую определить цвета, размеры, длины, мощность или комплекты.",\n          "artifact": "variant_source_evidence"\n        },\n        {\n          "button": "📷 Фото вариантов",\n          "type": "variant_photo",\n          "agent": "Photo Match Agent",\n          "result_card": "Пришли фото вариантов. Я свяжу фото с цветом, размером, комплектом или другим вариантом.",\n          "artifact": "variant_photo_map"\n        },\n        {\n          "button": "🧾 Чек",\n          "type": "variant_cost",\n          "agent": "Receipt Parser + Variation Matrix Agent",\n          "result_card": "Пришли чек. Я разнесу закупку и количество по вариантам, если это возможно.",\n          "artifact": "variant_cost_ledger"\n        },\n        {\n          "button": "🧬 Матрица",\n          "type": "variant_matrix",\n          "agent": "Variation Matrix Agent",\n          "result_card": "Покажу таблицу вариантов: SKU, количество, себестоимость, фото и отличия.",\n          "artifact": "variation_matrix"\n        },\n        {\n          "button": "📝 Черновик",\n          "type": "variant_draft",\n          "agent": "Listing Draft Crew",\n          "result_card": "Соберу черновик для товара с вариантами или предложу несколько вариантов листинга.",\n          "artifact": "variant_listing_draft"\n        },\n        {\n          "button": "✅ К проверке",\n          "type": "variant_approval",\n          "agent": "Critic Council + Approval Agent",\n          "result_card": "Проверю матрицу, фото и описание вариантов перед approval.",\n          "artifact": "variant_approval_candidate"\n        }\n      ]\n    },\n    {\n      "id": "03",\n      "name": "📝 Листинг-студия",\n      "subactions": [\n        {\n          "button": "🧠 3 варианта",\n          "type": "multi_draft",\n          "agent": "Listing Studio Crew",\n          "result_card": "Создам 3 разных версии листинга для одного товара: не копии, а разные углы продажи.",\n          "artifact": "three_listing_angles"\n        },\n        {\n          "button": "🔎 Для поиска",\n          "type": "seo_draft",\n          "agent": "Title SEO Agent",\n          "result_card": "Соберу вариант листинга с упором на поиск: заголовок, ключевые слова, характеристики.",\n          "artifact": "seo_listing_draft"\n        },\n        {\n          "button": "🤖 Для ИИ",\n          "type": "aeo_draft",\n          "agent": "AEO Agent",\n          "result_card": "Соберу вариант под AI-search: понятные факты, назначение товара и короткая структура.",\n          "artifact": "aeo_listing_draft"\n        },\n        {\n          "button": "👤 Для покупателя",\n          "type": "buyer_draft",\n          "agent": "Buyer Perspective Agent",\n          "result_card": "Соберу вариант для обычного покупателя: польза, понятность, доверие, аккуратное описание.",\n          "artifact": "human_buyer_draft"\n        },\n        {\n          "button": "🧪 Дубли",\n          "type": "duplicate_guard",\n          "agent": "Duplicate Guard",\n          "result_card": "Проверю, не получается ли простой дубль старого листинга.",\n          "artifact": "duplicate_guard_report"\n        },\n        {\n          "button": "✅ К проверке",\n          "type": "listing_approval",\n          "agent": "Critic Council + Approval Agent",\n          "result_card": "Подготовлю выбранный вариант листинга к проверке.",\n          "artifact": "listing_approval_candidate"\n        }\n      ]\n    },\n    {\n      "id": "04",\n      "name": "🛒 Marketplace + Lifecycle",\n      "subactions": [\n        {\n          "button": "🛒 eBay",\n          "type": "marketplace_status",\n          "agent": "Marketplace Status Agent",\n          "result_card": "Покажу статус eBay-листингов: draft, active, ended, sold out, слабые и кандидаты на улучшение.",\n          "artifact": "ebay_status_snapshot"\n        },\n        {\n          "button": "📊 3/5/7 дней",\n          "type": "lifecycle_check",\n          "agent": "Lifecycle Monitor",\n          "result_card": "Покажу проверки по дням: 3, 5, 7, 14/15 — просмотры, клики, слабые сигналы и предложения.",\n          "artifact": "lifecycle_report"\n        },\n        {\n          "button": "🔁 Улучшить",\n          "type": "revise_candidate",\n          "agent": "Revision Proposal Agent",\n          "result_card": "Подготовлю предложение улучшения. Живые изменения не запускаются без approval.",\n          "artifact": "revise_proposal"\n        },\n        {\n          "button": "📉 Слабые",\n          "type": "weak_listings",\n          "agent": "Weak Listing Detector",\n          "result_card": "Покажу слабые листинги и причину: фото, цена, заголовок, просмотры или конкуренты.",\n          "artifact": "weak_listing_report"\n        },\n        {\n          "button": "💶 Расходы",\n          "type": "marketplace_costs",\n          "agent": "Marketplace Cost Import Agent",\n          "result_card": "Покажу комиссии, рекламу, shipping label cost и другие расходы, если они доступны.",\n          "artifact": "marketplace_cost_snapshot"\n        },\n        {\n          "button": "✅ К проверке",\n          "type": "marketplace_approval",\n          "agent": "Approval Agent + Live Guard",\n          "result_card": "Подготовлю safe approval. Publish/revise/delete закрыты до отдельного gate.",\n          "artifact": "marketplace_approval_candidate"\n        }\n      ]\n    },\n    {\n      "id": "05",\n      "name": "📊 Финансы / склад",\n      "subactions": [\n        {\n          "button": "🧾 Чеки",\n          "type": "receipts",\n          "agent": "Purchase Ledger Agent",\n          "result_card": "Покажу закупки, чеки, количество и цену за штуку.",\n          "artifact": "purchase_report"\n        },\n        {\n          "button": "📦 Остаток",\n          "type": "stock",\n          "agent": "Stock Ledger Agent",\n          "result_card": "Покажу куплено, продано, осталось, зарезервировано, потеряно или повреждено.",\n          "artifact": "stock_report"\n        },\n        {\n          "button": "📮 Упаковка",\n          "type": "packaging",\n          "agent": "Packaging Cost Agent",\n          "result_card": "Покажу упаковку: конверты, коробки, плёнка, labels и стоимость на отправку/товар.",\n          "artifact": "packaging_cost_report"\n        },\n        {\n          "button": "💶 Прибыль",\n          "type": "profit",\n          "agent": "Profit Calculator",\n          "result_card": "Посчитаю реальную прибыль: выручка минус закупка, упаковка, комиссии, реклама, labels и возвраты.",\n          "artifact": "profit_report"\n        },\n        {\n          "button": "📉 Продажи",\n          "type": "sales",\n          "agent": "Sales Ledger Agent",\n          "result_card": "Покажу продажи по товару, варианту и листингу.",\n          "artifact": "sales_report"\n        },\n        {\n          "button": "🔔 Докупить",\n          "type": "reorder",\n          "agent": "Reorder Signal Agent",\n          "result_card": "Покажу, что стоит докупить, где заканчивается остаток и какая маржа.",\n          "artifact": "reorder_candidate"\n        }\n      ]\n    },\n    {\n      "id": "06",\n      "name": "🧭 Поиск товаров / закупка",\n      "subactions": [\n        {\n          "button": "🔎 Найти идеи",\n          "type": "scout",\n          "agent": "Scout Agent",\n          "result_card": "Запущу поиск идей товаров по источникам и конкурентам.",\n          "artifact": "product_idea_candidates"\n        },\n        {\n          "button": "🧪 Риск",\n          "type": "risk",\n          "agent": "Risk Agent",\n          "result_card": "Проверю запреты, брендовые риски, возвраты и слабую маржу.",\n          "artifact": "procurement_risk_report"\n        },\n        {\n          "button": "💶 Маржа",\n          "type": "margin",\n          "agent": "Margin Agent",\n          "result_card": "Оценю закупку, цену продажи, расходы и примерную прибыль.",\n          "artifact": "margin_estimate"\n        },\n        {\n          "button": "🛒 Где купить",\n          "type": "supplier",\n          "agent": "Supplier Agent",\n          "result_card": "Покажу возможные источники закупки: AliExpress, Alibaba, Temu, Amazon или другие.",\n          "artifact": "supplier_options"\n        },\n        {\n          "button": "📈 Тренды",\n          "type": "trends",\n          "agent": "Trend Agent",\n          "result_card": "Покажу сигналы трендов и конкуренции.",\n          "artifact": "trend_snapshot"\n        },\n        {\n          "button": "📥 В решения",\n          "type": "send_to_inbox",\n          "agent": "Decision Inbox Agent",\n          "result_card": "Отправлю кандидата товара во входящие решения.",\n          "artifact": "decision_inbox_item"\n        }\n      ]\n    },\n    {\n      "id": "07",\n      "name": "📥 Решения / отчёты / агенты",\n      "subactions": [\n        {\n          "button": "📥 Входящие",\n          "type": "inbox",\n          "agent": "Decision Inbox Agent",\n          "result_card": "Покажу карточки, где нужно твоё решение.",\n          "artifact": "decision_inbox"\n        },\n        {\n          "button": "👥 Агенты",\n          "type": "agent_status",\n          "agent": "Agent Status Agent",\n          "result_card": "Покажу, какие агенты активны, что сделали и где ждут данных.",\n          "artifact": "agent_status_report"\n        },\n        {\n          "button": "📬 Сводка",\n          "type": "digest",\n          "agent": "Digest Agent",\n          "result_card": "Покажу утреннюю/вечернюю сводку: важное, ожидания, риски, идеи.",\n          "artifact": "digest_report"\n        },\n        {\n          "button": "⚠️ Важно",\n          "type": "critical",\n          "agent": "Critical Alert Agent",\n          "result_card": "Покажу срочные предупреждения: слабые листинги, остатки, ошибки, safety.",\n          "artifact": "critical_alerts"\n        },\n        {\n          "button": "✅ Принять",\n          "type": "accept",\n          "agent": "Decision Agent",\n          "result_card": "Зафиксирую принятое решение в ledger.",\n          "artifact": "decision_accept_record"\n        },\n        {\n          "button": "🔁 Переделать",\n          "type": "rework",\n          "agent": "Rework Router",\n          "result_card": "Отправлю задачу на переделку нужной группе агентов.",\n          "artifact": "rework_task"\n        }\n      ]\n    },\n    {\n      "id": "08",\n      "name": "⚙️ Система / память",\n      "subactions": [\n        {\n          "button": "🟢 Статус",\n          "type": "status",\n          "agent": "System Status Agent",\n          "result_card": "Покажу состояние бота, сервера и текущего workflow.",\n          "artifact": "system_status"\n        },\n        {\n          "button": "🧠 Память",\n          "type": "memory",\n          "agent": "Memory Agent",\n          "result_card": "Покажу уроки, правила, ошибки и важные решения проекта.",\n          "artifact": "memory_snapshot"\n        },\n        {\n          "button": "🧾 Архив",\n          "type": "archive",\n          "agent": "Archivist Agent",\n          "result_card": "Покажу последние checkpoints, reports и сохранённые baseline.",\n          "artifact": "archive_snapshot"\n        },\n        {\n          "button": "🚧 Карантин",\n          "type": "quarantine",\n          "agent": "Quarantine Agent",\n          "result_card": "Покажу подозрительные или заблокированные элементы.",\n          "artifact": "quarantine_report"\n        },\n        {\n          "button": "🛡 Безопасность",\n          "type": "safety",\n          "agent": "Safety Gate Agent",\n          "result_card": "Покажу gates и действия, которые запрещены без разрешения.",\n          "artifact": "safety_gate_status"\n        },\n        {\n          "button": "🔄 Продолжить",\n          "type": "resume",\n          "agent": "Resume Agent",\n          "result_card": "Покажу, где остановились и какой следующий безопасный шаг.",\n          "artifact": "resume_pointer"\n        }\n      ]\n    }\n  ],\n  "next_patch_goal": "Future R88/R89 can replace placeholder subaction response with these behavior cards after review and approval."\n}')


def _r88_behavior_entry(screen_id, button_index):
    sid = str(screen_id).zfill(2)[-2:]
    try:
        idx = int(button_index)
    except Exception:
        idx = 0
    for screen in ECOM_V72_SUBACTION_BEHAVIOR.get("screens", []):
        if str(screen.get("id")).zfill(2)[-2:] == sid:
            actions = screen.get("subactions", [])
            if 1 <= idx <= len(actions):
                return screen, actions[idx - 1]
            return screen, None
    return None, None

def _r88_safe_text(value, fallback=""):
    text = str(value or fallback)
    replacements = {
        "callback": "служебный код",
        "NO_EBAY": "внутренний технический статус",
        "PASS_": "внутренний статус ",
        "/home/": "[сервер]/"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return " ".join(text.split())

def _r88_artifact_label(value):
    raw = _r88_safe_text(value, "рабочий артефакт")
    labels = {
        "source_evidence": "источник товара",
        "photo_temp_buffer": "временный буфер фото 12 часов",
        "purchase_ledger": "финансовый учёт закупки",
        "product_draft_candidate": "кандидат черновика товара",
        "product_result_preview": "предпросмотр результата",
        "approval_candidate": "кандидат на проверку",
        "variant_source_evidence": "источник товара с вариантами",
        "variant_photo_map": "карта фото по вариантам",
        "variant_cost_ledger": "учёт закупки по вариантам",
        "variation_matrix": "матрица вариантов",
        "variant_listing_draft": "черновик товара с вариантами",
        "variant_approval_candidate": "кандидат проверки вариантов",
        "three_listing_angles": "три варианта листинга",
        "seo_listing_draft": "листинг для поиска",
        "aeo_listing_draft": "листинг для ИИ-поиска",
        "human_buyer_draft": "листинг для покупателя",
        "duplicate_guard_report": "отчёт по дублям",
        "listing_approval_candidate": "кандидат листинга на проверку",
        "ebay_status_snapshot": "снимок статуса eBay",
        "lifecycle_report": "отчёт 3/5/7/14 дней",
        "revise_proposal": "предложение улучшения",
        "weak_listing_report": "отчёт по слабым листингам",
        "marketplace_cost_snapshot": "снимок расходов маркетплейса",
        "marketplace_approval_candidate": "кандидат проверки маркетплейса",
        "purchase_report": "отчёт по чекам и закупке",
        "stock_report": "отчёт по остаткам",
        "packaging_cost_report": "отчёт по упаковке",
        "profit_report": "отчёт по прибыли",
        "sales_report": "отчёт по продажам",
        "reorder_candidate": "кандидат на докупку",
        "product_idea_candidates": "кандидаты товаров",
        "procurement_risk_report": "отчёт по рискам закупки",
        "margin_estimate": "оценка маржи",
        "supplier_options": "варианты закупки",
        "trend_snapshot": "снимок трендов",
        "decision_inbox_item": "карточка во входящих решениях",
        "decision_inbox": "входящие решения",
        "agent_status_report": "отчёт по агентам",
        "digest_report": "сводка",
        "critical_alerts": "важные предупреждения",
        "decision_accept_record": "запись принятого решения",
        "rework_task": "задача на переделку",
        "system_status": "статус системы",
        "memory_snapshot": "снимок памяти",
        "archive_snapshot": "снимок архива",
        "quarantine_report": "отчёт карантина",
        "safety_gate_status": "статус безопасных границ",
        "resume_pointer": "точка продолжения"
    }
    return labels.get(raw, raw)

def _r83_action_text(screen_id, button_index):
    screen, entry = _r88_behavior_entry(screen_id, button_index)
    if not screen:
        return "Раздел не найден. Вернись в главное меню."

    title = _r88_safe_text(screen.get("name") or screen.get("title") or "Раздел")
    if not entry:
        return (
            title + "\n\n"
            "Действие не найдено.\n\n"
            "Вернись в раздел и выбери кнопку ещё раз.\n\n"
            "Безопасность: живые действия на маркетплейсах закрыты до отдельного разрешения."
        )[:3600]

    button = _r88_safe_text(entry.get("button"), "Действие")
    result_card = _r88_safe_text(entry.get("result_card"), "Подготовлю понятную карточку действия.")
    agent = _r88_safe_text(entry.get("agent"), "Агент сценария")
    artifact = _r88_artifact_label(entry.get("artifact"))

    lines = [
        title,
        "",
        "Выбрано: " + button,
        "",
        "Что сделаю:",
        "• " + result_card,
        "",
        "Кто работает:",
        "• " + agent,
        "",
        "Куда сохраню:",
        "• " + artifact,
        "",
        "Статус:",
        "• Поведение под-кнопки подключено.",
        "• Реальные агентные действия подключим следующим слоем.",
        "",
        "Безопасность:",
        "• Живые действия на маркетплейсах закрыты до отдельного разрешения.",
        "• Удаление и очистка не запускаются."
    ]
    return "\n".join(lines)[:3600]

# === R88_V72_SUBACTION_BEHAVIOR_ACTIVE_PATCH_END ===

def _r83_ack(cb):
    try:
        ecom_cockpit_v2_answer_callback((cb or {}).get("id"))
        return True
    except Exception:
        return False

def _r83_chat_id(cb):
    msg = (cb or {}).get("message") or {}
    chat_id = (msg.get("chat") or {}).get("id")
    if not chat_id:
        chat_id = ((cb or {}).get("from") or {}).get("id")
    return chat_id

def _r83_send(chat_id, text, keyboard=None):
    try:
        return ecom_cockpit_v2_send_message(chat_id, text, keyboard)
    except TypeError:
        try:
            return ecom_cockpit_v2_send_message(chat_id, text, reply_markup=keyboard)
        except Exception:
            return False
    except Exception:
        return False


# === R93_NEW_PRODUCT_REAL_INTAKE_ACTIVE_PATCH_START ===
# R93: New Product real intake layer. No restart here. No marketplace live actions.

def _r93_previous_ecom_cockpit_v2_try_handle_update(update):
    try:
        cb = update.get("callback_query") if isinstance(update, dict) else None
        if not isinstance(cb, dict):
            return _r83_previous_ecom_cockpit_v2_try_handle_update(update)

        data = cb.get("data") or ""
        if not isinstance(data, str) or not data.startswith("v72:"):
            return _r83_previous_ecom_cockpit_v2_try_handle_update(update)

        _r83_ack(cb)
        chat_id = _r83_chat_id(cb)
        if not chat_id:
            return True

        parts = data.split(":")
        if len(parts) < 2:
            return _r83_send(chat_id, _r83_home_text(), _r83_home_keyboard())

        command = parts[1]

        if command == "home":
            return _r83_send(chat_id, _r83_home_text(), _r83_home_keyboard())

        if command == "help":
            return _r83_send(chat_id, _r83_help_text(), {"inline_keyboard": [[{"text": "🏠 Домой", "callback_data": "v72:home"}]]})

        if command == "stop":
            return _r83_send(chat_id, "Остановлено. Данные не удалены. Можно вернуться в главное меню.", {"inline_keyboard": [[{"text": "🏠 Домой", "callback_data": "v72:home"}]]})

        if command.isdigit():
            sid = command.zfill(2)[-2:]
            if len(parts) >= 3 and parts[2].startswith("b"):
                try:
                    b_idx = int(parts[2][1:])
                except Exception:
                    b_idx = 0
                return _r83_send(chat_id, _r83_action_text(sid, b_idx), _r83_screen_keyboard(sid))
            return _r83_send(chat_id, _r83_screen_text(sid), _r83_screen_keyboard(sid))

        return _r83_send(chat_id, _r83_home_text(), _r83_home_keyboard())

    except Exception:
        try:
            return _r83_previous_ecom_cockpit_v2_try_handle_update(update)
        except Exception:
            return False


import json as _r93_json
import re as _r93_re
import hashlib as _r93_hashlib
from pathlib import Path as _r93_Path
from datetime import datetime as _r93_datetime, timezone as _r93_timezone

_R93_ROOT = _r93_Path("/home/ionlipca7/ecom_governed_runtime")
_R93_INTAKE_ROOT = _R93_ROOT / "storage/runtime_bridge/new_product_intake"
_R93_SESSION_DIR = _R93_INTAKE_ROOT / "sessions"
_R93_CASE_DIR = _R93_INTAKE_ROOT / "cases"
_R93_EVENT_DIR = _R93_INTAKE_ROOT / "events"
_R93_URL_RE = _r93_re.compile(r"https?://\S+", _r93_re.I)
_R93_QTY_RE = _r93_re.compile(r"\b(?:qty|quantity|кол-?во|количество|шт|pcs?)\b[:\s]*([0-9]{1,6})", _r93_re.I)
_R93_RECEIPT_RE = _r93_re.compile(r"\b(receipt|invoice|rechnung|чек|сч[её]т|накладн)\b", _r93_re.I)

def _r93_now():
    return _r93_datetime.now(_r93_timezone.utc).strftime("%Y%m%dT%H%M%SZ")

def _r93_chat_ref(chat_id):
    return _r93_hashlib.sha256(("r93:" + str(chat_id)).encode("utf-8")).hexdigest()[:18]

def _r93_safe_dirs():
    for p in (_R93_SESSION_DIR, _R93_CASE_DIR, _R93_EVENT_DIR):
        p.mkdir(parents=True, exist_ok=True)

def _r93_load_json(path, default):
    try:
        p = _r93_Path(path)
        if p.exists():
            return _r93_json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return default

def _r93_write_json(path, obj):
    _r93_safe_dirs()
    _r93_Path(path).write_text(_r93_json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def _r93_session_path(chat_ref):
    return _R93_SESSION_DIR / (str(chat_ref) + ".json")

def _r93_case_path(case_id):
    safe = "".join(ch for ch in str(case_id) if ch.isalnum() or ch in "_-")[:80]
    return _R93_CASE_DIR / (safe + ".json")

def _r93_mask_text(text):
    text = str(text or "")
    text = _r93_re.sub(r"\b\d{8,}:[A-Za-z0-9_-]{20,}\b", "[masked-token]", text)
    text = _r93_re.sub(r"(?i)(token|password|secret)\s*=\s*\S+", r"\1=[masked]", text)
    return text[:1200]

def _r93_new_case(chat_ref):
    ts = _r93_now()
    case_id = "np_" + ts + "_" + str(chat_ref)[:8]
    return {
        "case_id": case_id,
        "status": "collecting",
        "created_utc": ts,
        "updated_utc": ts,
        "source": {"urls": [], "source_type": "unknown"},
        "media": {"photo_ids": [], "document_refs": [], "temp_ttl_hours": 12, "quality_notes": []},
        "purchase": {"receipt_refs": [], "quantity": None, "total_cost": None, "currency": "EUR", "cost_per_unit": None},
        "operator_notes": [],
        "routing": {"finance_ledger": [], "photo_buffer": [], "source_evidence": [], "decision_inbox": []},
        "events": [],
        "safety": {"live_allowed": False, "requires_approval_for_marketplace_action": True}
    }

def _r93_get_session(chat_ref):
    return _r93_load_json(_r93_session_path(chat_ref), {})

def _r93_save_session(chat_ref, case_id, mode="collecting"):
    obj = {"chat_ref": chat_ref, "case_id": case_id, "mode": mode, "updated_utc": _r93_now()}
    _r93_write_json(_r93_session_path(chat_ref), obj)
    return obj

def _r93_get_case(chat_ref):
    session = _r93_get_session(chat_ref)
    case_id = session.get("case_id")
    if case_id:
        case_obj = _r93_load_json(_r93_case_path(case_id), None)
        if case_obj:
            return case_obj
    case_obj = _r93_new_case(chat_ref)
    _r93_write_json(_r93_case_path(case_obj["case_id"]), case_obj)
    _r93_save_session(chat_ref, case_obj["case_id"], "collecting")
    return case_obj

def _r93_extract_quantity(text):
    m = _R93_QTY_RE.search(text or "")
    if not m:
        return None
    try:
        return int(m.group(1))
    except Exception:
        return None

def _r93_classify_message(msg, expected="auto"):
    msg = msg or {}
    text = msg.get("text") or msg.get("caption") or ""
    urls = _R93_URL_RE.findall(text)
    qty = _r93_extract_quantity(text)
    photos = msg.get("photo") or []
    doc = msg.get("document") or {}
    mime = str(doc.get("mime_type") or "")
    has_photo = bool(photos)
    has_image_doc = mime.startswith("image/")
    has_pdf = mime == "application/pdf"

    if expected == "url" and urls:
        kind = "URL"
    elif expected == "photo" and (has_photo or has_image_doc):
        kind = "PHOTO"
    elif expected == "receipt" and (has_photo or has_image_doc or has_pdf or text.strip()):
        kind = "RECEIPT"
    elif has_photo or has_image_doc:
        kind = "PHOTO"
    elif has_pdf:
        kind = "RECEIPT"
    elif _R93_RECEIPT_RE.search(text):
        kind = "RECEIPT"
    elif urls:
        kind = "URL"
    elif qty is not None:
        kind = "QUANTITY"
    elif text.strip():
        kind = "COMMENT"
    else:
        kind = "EMPTY"

    return {
        "kind": kind,
        "urls": urls,
        "quantity": qty,
        "text": _r93_mask_text(text),
        "has_photo": has_photo,
        "has_document": bool(doc),
        "mime_type": mime[:120],
        "photo_file_id": (photos[-1].get("file_id") if isinstance(photos, list) and photos else None),
        "document_file_id": (doc.get("file_id") if isinstance(doc, dict) else None),
        "document_name": _r93_mask_text(doc.get("file_name") if isinstance(doc, dict) else "")
    }

def _r93_missing_data(case_obj):
    missing = []
    if not case_obj.get("source", {}).get("urls"):
        missing.append("ссылка")
    if not case_obj.get("media", {}).get("photo_ids") and not case_obj.get("media", {}).get("document_refs"):
        missing.append("фото")
    purchase = case_obj.get("purchase", {})
    if not purchase.get("receipt_refs") and not purchase.get("quantity"):
        missing.append("чек или количество")
    return missing

def _r93_update_status(case_obj):
    missing = _r93_missing_data(case_obj)
    case_obj["updated_utc"] = _r93_now()
    case_obj["status"] = "ready_for_draft" if not missing else "collecting"
    return missing

def _r93_apply_to_case(case_obj, classification):
    kind = classification.get("kind")
    ts = _r93_now()
    event_ref = "evt_" + ts + "_" + kind.lower()
    event = {"utc": ts, "kind": kind, "event_ref": event_ref}

    if kind == "URL":
        for url in classification.get("urls") or []:
            if url not in case_obj["source"]["urls"]:
                case_obj["source"]["urls"].append(url)
        case_obj["routing"]["source_evidence"].append(event_ref)

    elif kind == "PHOTO":
        ref = classification.get("photo_file_id") or classification.get("document_file_id") or event_ref
        case_obj["media"]["photo_ids"].append(ref)
        case_obj["routing"]["photo_buffer"].append(event_ref)

    elif kind == "RECEIPT":
        ref = classification.get("document_file_id") or classification.get("photo_file_id") or event_ref
        case_obj["purchase"]["receipt_refs"].append(ref)
        case_obj["routing"]["finance_ledger"].append(event_ref)

    elif kind == "QUANTITY":
        case_obj["purchase"]["quantity"] = classification.get("quantity")

    elif kind == "COMMENT":
        case_obj["operator_notes"].append({"utc": ts, "text": classification.get("text", "")})

    event["summary"] = {
        "urls_count": len(classification.get("urls") or []),
        "quantity": classification.get("quantity"),
        "has_photo": classification.get("has_photo"),
        "has_document": classification.get("has_document"),
        "mime_type": classification.get("mime_type")
    }
    case_obj["events"].append(event)
    _r93_update_status(case_obj)
    _r93_write_json(_r93_case_path(case_obj["case_id"]), case_obj)
    _r93_write_json(_R93_EVENT_DIR / (event_ref + ".json"), {"case_id": case_obj["case_id"], "classification": classification, "event": event})
    return case_obj

def _r93_case_summary(case_obj):
    missing = _r93_missing_data(case_obj)
    lines = [
        "🆕 Новый товар",
        "",
        "Собрано:",
        "• Ссылок: " + str(len(case_obj.get("source", {}).get("urls", []))),
        "• Фото/файлов: " + str(len(case_obj.get("media", {}).get("photo_ids", [])) + len(case_obj.get("media", {}).get("document_refs", []))),
        "• Чеков: " + str(len(case_obj.get("purchase", {}).get("receipt_refs", []))),
        "• Количество: " + (str(case_obj.get("purchase", {}).get("quantity")) if case_obj.get("purchase", {}).get("quantity") else "не указано"),
        "• Комментариев: " + str(len(case_obj.get("operator_notes", []))),
        "",
    ]
    if missing:
        lines.append("Не хватает:")
        for item in missing:
            lines.append("• " + item)
    else:
        lines.append("Статус:")
        lines.append("• Данных достаточно для следующего draft-слоя.")
    lines.extend([
        "",
        "Безопасность:",
        "• Живые действия на маркетплейсах закрыты до отдельного разрешения.",
        "• Удаление и очистка не запускаются."
    ])
    return "\n".join(lines)[:3600]

def _r93_keyboard():
    return {"inline_keyboard": [
        [{"text": "🔗 Добавить ссылку", "callback_data": "v72:01:b1"}, {"text": "📷 Добавить фото", "callback_data": "v72:01:b2"}],
        [{"text": "🧾 Добавить чек", "callback_data": "v72:01:b3"}, {"text": "🧠 Собрать", "callback_data": "v72:01:b4"}],
        [{"text": "👁 Результат", "callback_data": "v72:01:b5"}, {"text": "✅ К проверке", "callback_data": "v72:01:b6"}],
        [{"text": "🏠 Домой", "callback_data": "v72:home"}, {"text": "⛔ Стоп", "callback_data": "v72:stop"}]
    ]}

def _r93_chat_id_from_callback(cb):
    msg = (cb or {}).get("message") or {}
    chat_id = (msg.get("chat") or {}).get("id")
    if not chat_id:
        chat_id = ((cb or {}).get("from") or {}).get("id")
    return chat_id

def _r93_chat_id_from_message(msg):
    return ((msg or {}).get("chat") or {}).get("id")

def _r93_send(chat_id, text, keyboard=None):
    try:
        return ecom_cockpit_v2_send_message(chat_id, text, keyboard)
    except TypeError:
        try:
            return ecom_cockpit_v2_send_message(chat_id, text, reply_markup=keyboard)
        except Exception:
            return False
    except Exception:
        return False

def _r93_ack(cb):
    try:
        ecom_cockpit_v2_answer_callback((cb or {}).get("id"))
        return True
    except Exception:
        return False

def _r93_intake_prompt(mode):
    if mode == "url":
        return "🔗 Пришли ссылку на товар или поставщика. Я сохраню источник в карточку нового товара."
    if mode == "photo":
        return "📷 Пришли фото или скриншоты товара. Я сохраню их во временный буфер на 12 часов."
    if mode == "receipt":
        return "🧾 Пришли чек, Rechnung, PDF или скрин закупки. Я отправлю данные в финансовый учёт."
    return "🆕 Режим нового товара открыт. Пришли ссылку, фото, чек, комментарий или количество."

def _r93_handle_new_product_callback(data, cb):
    parts = str(data or "").split(":")
    if len(parts) < 3 or parts[0] != "v72" or parts[1] != "01":
        return False

    chat_id = _r93_chat_id_from_callback(cb)
    if not chat_id:
        return True

    _r93_ack(cb)
    chat_ref = _r93_chat_ref(chat_id)
    case_obj = _r93_get_case(chat_ref)
    button = parts[2]

    if button == "b1":
        _r93_save_session(chat_ref, case_obj["case_id"], "url")
        return _r93_send(chat_id, _r93_intake_prompt("url"), _r93_keyboard())

    if button == "b2":
        _r93_save_session(chat_ref, case_obj["case_id"], "photo")
        return _r93_send(chat_id, _r93_intake_prompt("photo"), _r93_keyboard())

    if button == "b3":
        _r93_save_session(chat_ref, case_obj["case_id"], "receipt")
        return _r93_send(chat_id, _r93_intake_prompt("receipt"), _r93_keyboard())

    if button == "b4":
        _r93_save_session(chat_ref, case_obj["case_id"], "collecting")
        return _r93_send(chat_id, _r93_case_summary(case_obj), _r93_keyboard())

    if button == "b5":
        return _r93_send(chat_id, _r93_case_summary(case_obj), _r93_keyboard())

    if button == "b6":
        missing = _r93_missing_data(case_obj)
        if missing:
            text = _r93_case_summary(case_obj) + "\n\nСначала лучше добавить недостающие данные."
        else:
            case_obj["status"] = "sent_to_decision_inbox"
            case_obj["routing"]["decision_inbox"].append("prepared_" + _r93_now())
            _r93_write_json(_r93_case_path(case_obj["case_id"]), case_obj)
            text = "📥 Товар подготовлен к проверке.\n\n" + _r93_case_summary(case_obj)
        return _r93_send(chat_id, text, _r93_keyboard())

    return False

def _r93_handle_intake_message(update):
    msg = {}
    if isinstance(update, dict):
        msg = update.get("message") or update.get("edited_message") or {}
    if not isinstance(msg, dict) or not msg:
        return False

    chat_id = _r93_chat_id_from_message(msg)
    if not chat_id:
        return False

    chat_ref = _r93_chat_ref(chat_id)
    session = _r93_get_session(chat_ref)
    if not session.get("case_id"):
        return False

    mode = session.get("mode") or "collecting"
    classification = _r93_classify_message(msg, expected=mode)
    if classification.get("kind") == "EMPTY":
        return False

    case_obj = _r93_get_case(chat_ref)
    case_obj = _r93_apply_to_case(case_obj, classification)
    _r93_save_session(chat_ref, case_obj["case_id"], "collecting")

    kind_ru = {
        "URL": "ссылка",
        "PHOTO": "фото",
        "RECEIPT": "чек/документ",
        "QUANTITY": "количество",
        "COMMENT": "комментарий"
    }.get(classification.get("kind"), "данные")

    text = (
        "✅ Данные приняты\n\n"
        "Что получил:\n"
        "• " + kind_ru + "\n\n"
        "Куда сохраню:\n"
        "• карточка нового товара\n\n"
        + _r93_case_summary(case_obj)
    )
    return _r93_send(chat_id, text, _r93_keyboard())


# === R98_NEW_PRODUCT_INTAKE_UX_RECEIPT_FIX_ACTIVE_PATCH_START ===
# R98: New Product intake fixes: photo batch, receipt parser v2, TTL 24h, case boundary, result card v2.
# No restart here. No marketplace live actions.

def _r98_previous_ecom_cockpit_v2_try_handle_update(update):
    try:
        if isinstance(update, dict):
            cb = update.get("callback_query")
            if isinstance(cb, dict):
                data = cb.get("data") or ""
                if isinstance(data, str) and data.startswith("v72:01:b"):
                    handled = _r93_handle_new_product_callback(data, cb)
                    if handled:
                        return True

            if _r93_handle_intake_message(update):
                return True

        return _r93_previous_ecom_cockpit_v2_try_handle_update(update)
    except Exception:
        try:
            return _r93_previous_ecom_cockpit_v2_try_handle_update(update)
        except Exception:
            return False


import re as _r98_re
import json as _r98_json
import hashlib as _r98_hashlib
from pathlib import Path as _r98_Path

_R98_PHOTO_TTL_HOURS = 24
_R98_MONEY_RE = _r98_re.compile(r"([0-9]+[,.][0-9]{2})\s*€?", _r98_re.I)

def _r98_money_to_float(value):
    if value is None:
        return None
    s = str(value).replace("€", "").replace("EUR", "").strip()
    s = s.replace(".", "").replace(",", ".") if "," in s else s
    try:
        return round(float(s), 2)
    except Exception:
        return None

def _r98_find_money_after_label(text, label):
    lines = [x.strip() for x in str(text or "").splitlines()]
    for i, line in enumerate(lines):
        if label.lower() in line.lower():
            for j in range(i + 1, min(i + 4, len(lines))):
                m = _R98_MONEY_RE.search(lines[j])
                if m:
                    return _r98_money_to_float(m.group(1))
    return None

def _r98_parse_receipt_v2(raw_text):
    text = str(raw_text or "")
    lines = [x.strip() for x in text.splitlines() if x.strip()]

    order_hash = None
    m_order = _r98_re.search(r"ID\s+заказа\s*:\s*([0-9]{6,})", text, _r98_re.I)
    if m_order:
        order_hash = _r98_hashlib.sha256(m_order.group(1).encode("utf-8")).hexdigest()[:12]

    paid_total = None
    m_paid = _r98_re.search(r"\bEUR\s*([0-9]+[,.][0-9]{2})", text, _r98_re.I)
    if m_paid:
        paid_total = _r98_money_to_float(m_paid.group(1))

    totals = [_r98_money_to_float(m.group(1)) for m in _r98_re.finditer(r"Итого\s*:\s*([0-9]+[,.][0-9]{2})\s*€", text, _r98_re.I)]
    totals = [x for x in totals if x is not None]

    discount = _r98_find_money_after_label(text, "Скидки")
    shipping = _r98_find_money_after_label(text, "Стоимость доставки")

    vat = None
    m_vat = _r98_re.search(r"([0-9]+[,.][0-9]{2})\s*€\s*НДС", text, _r98_re.I)
    if m_vat:
        vat = _r98_money_to_float(m_vat.group(1))

    qty = None
    unit_price = None
    item_title_detected = False
    supplier_detected = bool(_r98_re.search(r"\b(Store|Company|Manufactory|Official)\b", text, _r98_re.I))

    for i, line in enumerate(lines):
        q = _r98_re.fullmatch(r"x\s*([0-9]{1,5})", line, _r98_re.I) or _r98_re.fullmatch(r"([0-9]{1,5})\s*x", line, _r98_re.I)
        if q:
            qty = int(q.group(1))
            for back in range(i - 1, max(-1, i - 10), -1):
                pm = _R98_MONEY_RE.search(lines[back])
                if pm:
                    unit_price = _r98_money_to_float(pm.group(1))
                    break
            for back in range(i - 1, max(-1, i - 10), -1):
                if not _R98_MONEY_RE.search(lines[back]) and len(lines[back]) > 8:
                    item_title_detected = True
                    break
            break

    if qty is None:
        m_qty = _r98_re.search(r"\b(?:x|qty|количество|шт)\s*[: ]\s*([0-9]{1,5})\b", text, _r98_re.I)
        if m_qty:
            try:
                qty = int(m_qty.group(1))
            except Exception:
                qty = None

    line_total = round(unit_price * qty, 2) if unit_price is not None and qty is not None else None
    effective_unit = round(paid_total / qty, 2) if paid_total is not None and qty else None

    return {
        "order_id_hash": order_hash,
        "order_id_present": bool(order_hash),
        "paid_total_eur": paid_total,
        "subtotal_candidates_eur": totals[-3:] if totals else [],
        "discount_eur": discount,
        "shipping_eur": shipping,
        "vat_eur": vat,
        "quantity_detected": qty,
        "unit_price_eur": unit_price,
        "line_total_eur": line_total,
        "effective_unit_cost_eur": effective_unit,
        "item_title_detected": item_title_detected,
        "supplier_detected": supplier_detected,
        "privacy_raw_receipt_printed": False
    }

def _r98_receipt_safe_event_summary(parsed):
    return {
        "kind": "RECEIPT",
        "parser_v2": {
            "order_id_present": bool(parsed.get("order_id_hash")),
            "paid_total_eur": parsed.get("paid_total_eur"),
            "discount_eur": parsed.get("discount_eur"),
            "shipping_eur": parsed.get("shipping_eur"),
            "vat_eur": parsed.get("vat_eur"),
            "quantity_detected": parsed.get("quantity_detected"),
            "unit_price_eur": parsed.get("unit_price_eur"),
            "line_total_eur": parsed.get("line_total_eur"),
            "effective_unit_cost_eur": parsed.get("effective_unit_cost_eur"),
            "item_title_detected": parsed.get("item_title_detected"),
            "supplier_detected": parsed.get("supplier_detected"),
            "privacy_raw_receipt_printed": False
        }
    }

def _r98_case_has_data(case_obj):
    return bool(
        case_obj.get("source", {}).get("urls")
        or case_obj.get("media", {}).get("photo_ids")
        or case_obj.get("media", {}).get("document_refs")
        or case_obj.get("purchase", {}).get("receipt_refs")
        or case_obj.get("operator_notes")
        or case_obj.get("events")
    )

def _r98_new_case_with_session(chat_ref):
    case_obj = _r93_new_case(chat_ref)
    case_obj.setdefault("media", {})["temp_ttl_hours"] = _R98_PHOTO_TTL_HOURS
    _r93_write_json(_r93_case_path(case_obj["case_id"]), case_obj)
    _r93_save_session(chat_ref, case_obj["case_id"], "collecting")
    return case_obj

def _r98_save_case(case_obj):
    case_obj.setdefault("media", {})["temp_ttl_hours"] = _R98_PHOTO_TTL_HOURS
    case_obj["updated_utc"] = _r93_now()
    _r93_update_status(case_obj)
    _r93_write_json(_r93_case_path(case_obj["case_id"]), case_obj)
    return case_obj

def _r98_event_ref(kind):
    return "evt_" + _r93_now() + "_" + str(kind).lower()

def _r98_write_event(case_id, event_ref, safe_payload):
    try:
        _R93_EVENT_DIR.mkdir(parents=True, exist_ok=True)
        _r93_write_json(_R93_EVENT_DIR / (event_ref + ".json"), {"case_id": case_id, "event_ref": event_ref, **safe_payload})
    except Exception:
        pass

def _r98_apply_to_case(case_obj, classification):
    kind = classification.get("kind")
    event_ref = _r98_event_ref(kind)
    case_obj.setdefault("routing", {}).setdefault("source_evidence", [])
    case_obj.setdefault("routing", {}).setdefault("photo_buffer", [])
    case_obj.setdefault("routing", {}).setdefault("finance_ledger", [])
    case_obj.setdefault("routing", {}).setdefault("decision_inbox", [])
    case_obj.setdefault("media", {}).setdefault("photo_ids", [])
    case_obj.setdefault("media", {}).setdefault("document_refs", [])
    case_obj.setdefault("purchase", {}).setdefault("receipt_refs", [])
    case_obj.setdefault("operator_notes", [])
    case_obj.setdefault("events", [])
    case_obj.setdefault("media", {})["temp_ttl_hours"] = _R98_PHOTO_TTL_HOURS

    safe_payload = {"classification_kind": kind, "raw_receipt_printed": False, "private_values_printed": False}

    if kind == "URL":
        for url in classification.get("urls") or []:
            if url not in case_obj["source"]["urls"]:
                case_obj["source"]["urls"].append(url)
        case_obj["routing"]["source_evidence"].append(event_ref)

    elif kind == "PHOTO":
        ref = classification.get("photo_file_id") or classification.get("document_file_id") or event_ref
        if ref not in case_obj["media"]["photo_ids"]:
            case_obj["media"]["photo_ids"].append(ref)
        case_obj["routing"]["photo_buffer"].append(event_ref)
        safe_payload["media_group_id"] = classification.get("media_group_id")
        safe_payload["file_ref_saved"] = True

    elif kind == "RECEIPT":
        raw_text = classification.get("text") or ""
        # R98E_PATCH_MARKER_RECEIPT_APPLY_PARSED_RESULT_NO_RESTART
        parsed = classification.get("r98_parser_v2")
        if not isinstance(parsed, dict):
            safe_text_for_parser = raw_text
            if safe_text_for_parser == "receipt_text_masked_parser_v2_fields_saved":
                safe_text_for_parser = ""
            parsed = _r98_parse_receipt_v2(safe_text_for_parser)
        ref = classification.get("document_file_id") or classification.get("photo_file_id") or event_ref
        if ref not in case_obj["purchase"]["receipt_refs"]:
            case_obj["purchase"]["receipt_refs"].append(ref)
        case_obj["routing"]["finance_ledger"].append(event_ref)

        case_obj["purchase"]["parser_v2"] = parsed
        if parsed.get("quantity_detected") and not case_obj["purchase"].get("quantity"):
            case_obj["purchase"]["quantity"] = parsed.get("quantity_detected")
        if parsed.get("paid_total_eur") is not None:
            case_obj["purchase"]["total_cost"] = parsed.get("paid_total_eur")
        if parsed.get("effective_unit_cost_eur") is not None:
            case_obj["purchase"]["cost_per_unit"] = parsed.get("effective_unit_cost_eur")
        case_obj["purchase"]["unit_price_eur"] = parsed.get("unit_price_eur")
        case_obj["purchase"]["shipping_eur"] = parsed.get("shipping_eur")
        case_obj["purchase"]["discount_eur"] = parsed.get("discount_eur")
        case_obj["purchase"]["vat_eur"] = parsed.get("vat_eur")
        case_obj["purchase"]["line_total_eur"] = parsed.get("line_total_eur")
        safe_payload.update(_r98_receipt_safe_event_summary(parsed))

    elif kind == "QUANTITY":
        case_obj["purchase"]["quantity"] = classification.get("quantity")

    elif kind == "COMMENT":
        case_obj["operator_notes"].append({"utc": _r93_now(), "text": classification.get("text", "")})

    case_obj["events"].append({"utc": _r93_now(), "kind": kind, "event_ref": event_ref})
    _r98_save_case(case_obj)
    _r98_write_event(case_obj["case_id"], event_ref, safe_payload)
    return case_obj

def _r98_case_summary_v2(case_obj):
    source_urls = case_obj.get("source", {}).get("urls", [])
    media = case_obj.get("media", {})
    purchase = case_obj.get("purchase", {})
    photos_count = len(media.get("photo_ids", [])) + len(media.get("document_refs", []))
    receipts_count = len(purchase.get("receipt_refs", []))
    qty = purchase.get("quantity")
    parser = purchase.get("parser_v2") or {}

    lines = [
        "🆕 Новый товар",
        "",
        "Собрано:",
        "• Ссылок: " + str(len(source_urls)),
        "• Фото/файлов: " + str(photos_count),
        "• Чеков: " + str(receipts_count),
        "• Количество: " + (str(qty) if qty else "не указано"),
    ]

    if parser:
        lines.extend([
            "",
            "Финансы из чека:",
            "• Итог: " + (str(parser.get("paid_total_eur")) + " EUR" if parser.get("paid_total_eur") is not None else "не найдено"),
            "• Цена/шт: " + (str(parser.get("unit_price_eur")) + " EUR" if parser.get("unit_price_eur") is not None else "не найдено"),
            "• Себестоимость/шт после итоговой суммы: " + (str(parser.get("effective_unit_cost_eur")) + " EUR" if parser.get("effective_unit_cost_eur") is not None else "не найдено"),
            "• Доставка: " + (str(parser.get("shipping_eur")) + " EUR" if parser.get("shipping_eur") is not None else "не найдено"),
            "• Скидка: " + (str(parser.get("discount_eur")) + " EUR" if parser.get("discount_eur") is not None else "не найдено"),
            "• НДС включён: " + (str(parser.get("vat_eur")) + " EUR" if parser.get("vat_eur") is not None else "не найдено"),
        ])

    missing = _r93_missing_data(case_obj)
    lines.append("")
    if missing:
        lines.append("Не хватает:")
        for item in missing:
            lines.append("• " + item)
    else:
        lines.append("Статус:")
        lines.append("• Данных достаточно для следующего draft-слоя.")

    lines.extend([
        "",
        "Буфер фото:",
        "• 24 часа.",
        "",
        "Безопасность:",
        "• Живые действия на маркетплейсах закрыты до отдельного разрешения.",
        "• Удаление и очистка не запускаются.",
        "• Персональные данные и сырой чек не показываются."
    ])
    return "\n".join(lines)[:3600]

def _r98_keyboard():
    return {"inline_keyboard": [
        [{"text": "🔗 Добавить ссылку", "callback_data": "v72:01:b1"}, {"text": "📷 Добавить фото", "callback_data": "v72:01:b2"}],
        [{"text": "🧾 Добавить чек", "callback_data": "v72:01:b3"}, {"text": "🧠 Собрать", "callback_data": "v72:01:b4"}],
        [{"text": "👁 Результат", "callback_data": "v72:01:b5"}, {"text": "✅ К проверке", "callback_data": "v72:01:b6"}],
        [{"text": "🆕 Новый case", "callback_data": "r98:newcase"}, {"text": "🏠 Домой", "callback_data": "v72:home"}],
        [{"text": "⛔ Стоп", "callback_data": "v72:stop"}]
    ]}

def _r98_boundary_keyboard():
    return {"inline_keyboard": [
        [{"text": "➕ Добавить к текущему", "callback_data": "r98:add_current_url"}],
        [{"text": "🆕 Начать новый товар", "callback_data": "r98:start_new_with_url"}],
        [{"text": "🏠 Домой", "callback_data": "v72:home"}, {"text": "⛔ Стоп", "callback_data": "v72:stop"}]
    ]}

def _r98_photo_group_seen(chat_ref, media_group_id):
    if not media_group_id:
        return False
    session = _r93_get_session(chat_ref)
    seen = session.get("r98_media_groups_seen") or []
    return media_group_id in seen

def _r98_mark_photo_group_seen(chat_ref, media_group_id):
    if not media_group_id:
        return
    session = _r93_get_session(chat_ref)
    seen = session.get("r98_media_groups_seen") or []
    if media_group_id not in seen:
        seen.append(media_group_id)
    session["r98_media_groups_seen"] = seen[-20:]
    _r93_write_json(_r93_session_path(chat_ref), session)

def _r98_save_pending_url(chat_ref, urls):
    session = _r93_get_session(chat_ref)
    session["r98_pending_urls"] = list(urls or [])
    session["mode"] = "await_url_boundary_decision"
    session["updated_utc"] = _r93_now()
    _r93_write_json(_r93_session_path(chat_ref), session)

def _r98_take_pending_url(chat_ref):
    session = _r93_get_session(chat_ref)
    urls = session.get("r98_pending_urls") or []
    session["r98_pending_urls"] = []
    session["mode"] = "collecting"
    session["updated_utc"] = _r93_now()
    _r93_write_json(_r93_session_path(chat_ref), session)
    return urls

def _r98_handle_special_callback(data, cb):
    chat_id = _r93_chat_id_from_callback(cb)
    if not chat_id:
        return True
    chat_ref = _r93_chat_ref(chat_id)
    _r93_ack(cb)

    if data == "r98:newcase":
        case_obj = _r98_new_case_with_session(chat_ref)
        return _r93_send(chat_id, "🆕 Новый товар открыт.\n\nПришли ссылку, фото, чек или комментарий.", _r98_keyboard())

    if data == "r98:add_current_url":
        urls = _r98_take_pending_url(chat_ref)
        case_obj = _r93_get_case(chat_ref)
        if urls:
            case_obj = _r98_apply_to_case(case_obj, {"kind": "URL", "urls": urls})
        return _r93_send(chat_id, "✅ Ссылка добавлена к текущему товару.\n\n" + _r98_case_summary_v2(case_obj), _r98_keyboard())

    if data == "r98:start_new_with_url":
        urls = _r98_take_pending_url(chat_ref)
        case_obj = _r98_new_case_with_session(chat_ref)
        if urls:
            case_obj = _r98_apply_to_case(case_obj, {"kind": "URL", "urls": urls})
        return _r93_send(chat_id, "🆕 Начал новый товар и добавил ссылку.\n\n" + _r98_case_summary_v2(case_obj), _r98_keyboard())

    return False

def _r98_handle_new_product_callback(data, cb):
    if isinstance(data, str) and data.startswith("r98:"):
        return _r98_handle_special_callback(data, cb)

    parts = str(data or "").split(":")
    if len(parts) < 3 or parts[0] != "v72" or parts[1] != "01":
        return False

    chat_id = _r93_chat_id_from_callback(cb)
    if not chat_id:
        return True

    _r93_ack(cb)
    chat_ref = _r93_chat_ref(chat_id)
    case_obj = _r93_get_case(chat_ref)
    case_obj.setdefault("media", {})["temp_ttl_hours"] = _R98_PHOTO_TTL_HOURS
    _r98_save_case(case_obj)
    button = parts[2]

    if button == "b1":
        _r93_save_session(chat_ref, case_obj["case_id"], "url")
        return _r93_send(chat_id, "🔗 Пришли ссылку на товар.\n\nЕсли это другой товар, я спрошу: добавить к текущему или начать новый.", _r98_keyboard())

    if button == "b2":
        _r93_save_session(chat_ref, case_obj["case_id"], "photo")
        return _r93_send(chat_id, "📷 Пришли фото или скриншоты.\n\nЕсли это альбом, я сохраню фото пачкой и не буду спамить отдельными ответами.", _r98_keyboard())

    if button == "b3":
        _r93_save_session(chat_ref, case_obj["case_id"], "receipt")
        return _r93_send(chat_id, "🧾 Пришли чек/Rechnung/PDF или текст чека.\n\nЯ попробую разобрать количество, цену, доставку, скидку и НДС.", _r98_keyboard())

    if button in ("b4", "b5"):
        _r93_save_session(chat_ref, case_obj["case_id"], "collecting")
        return _r93_send(chat_id, _r98_case_summary_v2(case_obj), _r98_keyboard())

    if button == "b6":
        missing = _r93_missing_data(case_obj)
        if missing:
            text = _r98_case_summary_v2(case_obj) + "\n\nСначала лучше добавить недостающие данные."
        else:
            case_obj["status"] = "sent_to_decision_inbox"
            case_obj.setdefault("routing", {}).setdefault("decision_inbox", []).append("prepared_" + _r93_now())
            _r98_save_case(case_obj)
            text = "📥 Товар подготовлен к проверке.\n\n" + _r98_case_summary_v2(case_obj)
        return _r93_send(chat_id, text, _r98_keyboard())

    return False

def _r98_handle_intake_message(update):
    msg = {}
    if isinstance(update, dict):
        msg = update.get("message") or update.get("edited_message") or {}
    if not isinstance(msg, dict) or not msg:
        return False

    chat_id = _r93_chat_id_from_message(msg)
    if not chat_id:
        return False

    chat_ref = _r93_chat_ref(chat_id)
    session = _r93_get_session(chat_ref)
    if not session.get("case_id"):
        return False

    mode = session.get("mode") or "collecting"
    classification = _r93_classify_message(msg, expected=mode)
    if classification.get("kind") == "EMPTY":
        return False

    if classification.get("kind") == "RECEIPT":
        raw = classification.get("text") or ""
        parsed = _r98_parse_receipt_v2(raw)
        classification["r98_parser_v2"] = parsed
        classification["text"] = "receipt_text_masked_parser_v2_fields_saved"

    media_group_id = msg.get("media_group_id")
    if media_group_id:
        classification["media_group_id"] = str(media_group_id)

    case_obj = _r93_get_case(chat_ref)
    case_obj.setdefault("media", {})["temp_ttl_hours"] = _R98_PHOTO_TTL_HOURS

    if classification.get("kind") == "URL":
        new_urls = classification.get("urls") or []
        existing_urls = case_obj.get("source", {}).get("urls", [])
        different_new_url = bool(new_urls and existing_urls and any(u not in existing_urls for u in new_urls))
        if different_new_url and _r98_case_has_data(case_obj):
            _r98_save_pending_url(chat_ref, new_urls)
            return _r93_send(
                chat_id,
                "⚠️ Похоже, это ссылка на новый товар.\n\nЧто сделать?\n• Добавить к текущему товару\n• Начать новый товар",
                _r98_boundary_keyboard()
            )

    case_obj = _r98_apply_to_case(case_obj, classification)
    _r93_save_session(chat_ref, case_obj["case_id"], "collecting")

    kind = classification.get("kind")
    if kind == "PHOTO" and media_group_id:
        already = _r98_photo_group_seen(chat_ref, str(media_group_id))
        _r98_mark_photo_group_seen(chat_ref, str(media_group_id))
        if already:
            return True
        return _r93_send(
            chat_id,
            "📷 Фото-альбом принимаю.\n\nЯ сохраню фото пачкой и покажу итог в карточке «Результат».\n\n" + _r98_case_summary_v2(case_obj),
            _r98_keyboard()
        )

    kind_ru = {
        "URL": "ссылка",
        "PHOTO": "фото",
        "RECEIPT": "чек/документ",
        "QUANTITY": "количество",
        "COMMENT": "комментарий"
    }.get(kind, "данные")

    text = (
        "✅ Данные приняты\n\n"
        "Что получил:\n"
        "• " + kind_ru + "\n\n"
        + _r98_case_summary_v2(case_obj)
    )
    return _r93_send(chat_id, text, _r98_keyboard())

def ecom_cockpit_v2_try_handle_update(update):
    try:
        if isinstance(update, dict):
            cb = update.get("callback_query")
            if isinstance(cb, dict):
                data = cb.get("data") or ""
                if isinstance(data, str) and (data.startswith("v72:01:b") or data.startswith("r98:")):
                    handled = _r98_handle_new_product_callback(data, cb)
                    if handled:
                        return True

            if _r98_handle_intake_message(update):
                return True

        return _r98_previous_ecom_cockpit_v2_try_handle_update(update)
    except Exception:
        try:
            return _r98_previous_ecom_cockpit_v2_try_handle_update(update)
        except Exception:
            return False

# === R98_NEW_PRODUCT_INTAKE_UX_RECEIPT_FIX_ACTIVE_PATCH_END ===

# === R93_NEW_PRODUCT_REAL_INTAKE_ACTIVE_PATCH_END ===

# === R83_V72_TELEGRAM_MENU_ACTIVE_PATCH_END ===
# === R75E_ENRICHED_RAW_HANDLER_END ===

# ECOM_COCKPIT_V2_INLINE_END

# TELEGRAM_ACTIVE_ROUTER_BOUNDARY_SHELL_V1_START
# === ECOM_DIGEST_RAW_ROUTER_V2E_PATCH_BEGIN ===
# Raw-router digest sender. Supersedes old V2B marker. No secret print. No marketplace action. No delete/cleanup.
try:
    import sys as _ecom_sys
    from pathlib import Path as _EcomPath
    _ECOM_ROOT = _EcomPath("/home/ionlipca7/ecom_governed_runtime")
    if str(_ECOM_ROOT) not in _ecom_sys.path:
        _ecom_sys.path.insert(0, str(_ECOM_ROOT))
    from storage.tools.telegram_digest.telegram_digest_outbox_sender_raw_v2e_active import (
        ecom_digest_raw_router_v2e_process_update as _ecom_digest_raw_router_v2e_process_update
    )
except Exception:
    _ecom_digest_raw_router_v2e_process_update = None
# === ECOM_DIGEST_RAW_ROUTER_V2E_PATCH_END ===

# === ECOM_MENU18_AGENT_WAKE_HANDLER_V1_CANDIDATE_BEGIN ===
# Candidate only: menu18 route handler + agent wake/status/test/resend.
# Auto agents do not depend on menu buttons. No marketplace action. No delete/cleanup.
try:
    import importlib.util as _ecom_importlib_util
    _ECOM_MENU18_HANDLER_PATH = '/home/ionlipca7/ecom_governed_runtime/storage/runtime_bridge/candidates/MENU18_ROUTE_HANDLER_AGENT_WAKE_CANDIDATE_20260526T172556Z/menu18_route_handler_agent_wake_v1_candidate.py'
    _ecom_spec = _ecom_importlib_util.spec_from_file_location("ecom_menu18_route_handler_agent_wake_v1_candidate", _ECOM_MENU18_HANDLER_PATH)
    _ecom_menu18_module = _ecom_importlib_util.module_from_spec(_ecom_spec)
    _ecom_spec.loader.exec_module(_ecom_menu18_module)
    _ecom_menu18_route_handler_agent_wake_v1 = _ecom_menu18_module.ecom_menu18_route_handler_agent_wake_v1
except Exception:
    _ecom_menu18_route_handler_agent_wake_v1 = None
# === ECOM_MENU18_AGENT_WAKE_HANDLER_V1_CANDIDATE_END ===


# === ECOM_MENU18_RU_COPY_POLISH_V3_BEGIN ===
# RU copy polish V3. Main menu blocks + Russian cards. No marketplace action. No delete/cleanup.
try:
    import importlib.util as _ecom_ru_copy_v3_importlib_util
    _ECOM_MENU18_RU_COPY_V3_HANDLER_PATH = '/home/ionlipca7/ecom_governed_runtime/storage/runtime_bridge/candidates/MENU18_RU_COPY_POLISH_V3_20260526T175451Z/menu18_route_handler_ru_copy_polish_v3.py'
    _ecom_ru_copy_v3_spec = _ecom_ru_copy_v3_importlib_util.spec_from_file_location("ecom_menu18_ru_copy_polish_v3", _ECOM_MENU18_RU_COPY_V3_HANDLER_PATH)
    _ecom_ru_copy_v3_module = _ecom_ru_copy_v3_importlib_util.module_from_spec(_ecom_ru_copy_v3_spec)
    _ecom_ru_copy_v3_spec.loader.exec_module(_ecom_ru_copy_v3_module)
    _ecom_menu18_ru_copy_polish_v3 = _ecom_ru_copy_v3_module.ecom_menu18_route_handler_ru_copy_polish_v3
except Exception:
    _ecom_menu18_ru_copy_polish_v3 = None
# === ECOM_MENU18_RU_COPY_POLISH_V3_END ===

def telegram_active_router_v1(update):
    try:
        if _ecom_menu18_ru_copy_polish_v3 is not None:
            if _ecom_menu18_ru_copy_polish_v3(update, ecom_cockpit_v2_send_message):
                return
    except Exception:
        pass
    try:
        if _ecom_menu18_ru_cards_v2 is not None:
            if _ecom_menu18_ru_cards_v2(update, ecom_cockpit_v2_send_message):
                return
    except Exception:
        pass
    try:
        if _ecom_menu18_route_handler_agent_wake_v1 is not None:
            if _ecom_menu18_route_handler_agent_wake_v1(update, ecom_cockpit_v2_send_message):
                return
    except Exception:
        pass
    try:
        if _ecom_digest_raw_router_v2e_process_update is not None:
            _ecom_digest_raw_router_v2e_process_update(update, ecom_cockpit_v2_send_message)
    except Exception:
        pass
    """Single active Telegram router shell. Returns True if update is handled before legacy fallback."""
    try:
        msg = update.get('message') or update.get('edited_message') or {}
        chat_id = ((msg.get('chat') or {}).get('id'))
        raw_text = str(msg.get('text') or '').strip()
        low = raw_text.lower()
        if chat_id and low in ('/cockpit', 'cockpit', 'пульт', '/menu', 'menu', '☰ главное меню', '🏠 главное меню', 'главное меню', 'меню'):
            ecom_cockpit_v2_send_message(chat_id, ecom_cockpit_v2_menu_text(), ecom_cockpit_main_inline_keyboard())
            return True
        if ecom_cockpit_v2_try_handle_update(update):
            return True
        return False
    except Exception as _e:
        try:
            from pathlib import Path as _Path
            _Path('/home/ionlipca7/runtime_eco_v1/storage/state_control/telegram_active_router_exception_v1.json').write_text(__import__('json').dumps({'exception': repr(_e), 'update_keys': list(update.keys()) if isinstance(update, dict) else []}, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
        return False
# TELEGRAM_ACTIVE_ROUTER_BOUNDARY_SHELL_V1_END




ROOT = Path(__file__).resolve().parent
INBOX = ROOT / "storage" / "telegram_inbox"
DRAFT = ROOT / "storage" / "drafts" / "telegram_package_v1.json"

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN","").strip()
if not TOKEN:
    raise SystemExit("NO TELEGRAM TOKEN")

BASE = f"https://api.telegram.org/bot{TOKEN}"

def api(method, params=None):
    url = BASE + "/" + method
    if params:
        url += "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode())

def send(chat_id, text):
    data = urllib.parse.urlencode({"chat_id":chat_id,"text":text}).encode()
    urllib.request.urlopen(BASE+"/sendMessage", data=data)

def session(chat_id):
    p = INBOX / str(chat_id)
    p.mkdir(parents=True, exist_ok=True)
    return p

def save_text(chat_id, text):
    # REVIEW_TEXT_INPUT_PATCH_V1_START
    try:
        import sys as _sys
        _helper_dir = ROOT / "storage" / "tools" / "telegram"
        if str(_helper_dir) not in _sys.path:
            _sys.path.insert(0, str(_helper_dir))
        from review_text_input_helper_v1 import consume_text_if_pending
        _res = consume_text_if_pending("/home/ionlipca7/ecom_governed_runtime", text, chat_id=chat_id)
        if _res.get("handled"):
            if _res.get("ok"):
                send(chat_id, "✅ Цена принята: " + str(_res.get("price_eur")) + " EUR\n\nLive закрыт. Черновик обновлён.")
            else:
                send(chat_id, "⚠️ " + str(_res.get("message", "Цена не распознана. Пример: 14,99")))
            return False
    except Exception as _price_ex:
        try:
            send(chat_id, "⚠️ Проверка цены дала ошибку, текст сохраню обычным способом: " + str(type(_price_ex).__name__))
        except Exception:
            pass
    # REVIEW_TEXT_INPUT_PATCH_V1_END

    f = session(chat_id) / "texts.txt"
    with open(f,"a",encoding="utf-8") as x:
        x.write(text+"\n")
    return True

def save_photo(file_id, chat_id, msg_id):
    info = api("getFile", {"file_id":file_id})
    file_path = info["result"]["file_path"]
    url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    out = session(chat_id) / f"{msg_id}.jpg"
    urllib.request.urlretrieve(url, out)
    return str(out)

def build_package(chat_id):
    base = session(chat_id)

    text_file = base / "texts.txt"
    texts = text_file.read_text(encoding="utf-8", errors="ignore") if text_file.exists() else ""

    photos = [str(p) for p in base.glob("*.jpg")]

    pkg = {
        "status":"READY_FOR_DRAFT",
        "publish_allowed":False,
        "raw_text":texts,
        "photos":photos,
        "image_count":len(photos),
        "timestamp":datetime.datetime.utcnow().isoformat()
    }

    DRAFT.parent.mkdir(parents=True, exist_ok=True)
    DRAFT.write_text(json.dumps(pkg, indent=2, ensure_ascii=False), encoding="utf-8")

    return pkg

offset = 0

print("TELEGRAM CONTROL+INTAKE FINAL RUNNING", flush=True)



# REVIEW_BUTTON_PATCH_V1_START
def save_review_action_v1(chat_id, action, source="telegram_button"):
    """Save operator review action only. No live action, no eBay mutation."""
    from pathlib import Path as _Path
    import json as _json
    import time as _time

    _root = _Path("/home/ionlipca7/ecom_governed_runtime")
    _runtime_root = _Path("/home/ionlipca7/runtime_eco_v1")
    _product_key = None
    _product_key_source = None
    _candidate_files = [
        _runtime_root / "storage/state_control/telegram_control_ru_dry_draft_request_v1.json",
        _runtime_root / "storage/control_room/CURRENT_POINTER.json",
        _root / "storage/state_control/telegram_listing_draft_packet_v1.json",
        _root / "storage/state_control/telegram_listing_draft_review_v1.json"
    ]
    for _candidate in _candidate_files:
        try:
            if _candidate.exists():
                _j = _json.loads(_candidate.read_text(encoding="utf-8", errors="replace"))
                _maybe = _j.get("canonical_key") or _j.get("product_key") or _j.get("active_product_key")
                if _maybe:
                    _product_key = str(_maybe)
                    _product_key_source = str(_candidate)
                    break
        except Exception:
            pass
    if not _product_key:
        _product_key = "UNKNOWN_PRODUCT_KEY_STOP_SAFE"
        _product_key_source = "missing_current_product_state"
    _out_dir = _root / "storage/review_actions" / _product_key
    _out_dir.mkdir(parents=True, exist_ok=True)
    _out = _out_dir / "review_action_v1.json"

    _allowed = {
        "APPROVE_DRY": "ОДОБРИТЬ DRY",
        "REDO_TITLE": "TITLE ПЕРЕДЕЛАТЬ",
        "CHECK_CATEGORY": "КАТЕГОРИЮ ПРОВЕРИТЬ",
        "REDO_SPECS": "ХАРАКТЕРИСТИКИ ПЕРЕДЕЛАТЬ",
        "REDO_HTML": "HTML ПЕРЕДЕЛАТЬ",
        "REDO_PRICE": "ЦЕНУ ПОМЕНЯТЬ",
        "CHECK_POLICIES": "ДОСТАВКУ/ОПЛАТУ ПРОВЕРИТЬ",
        "REDO_PHOTO_ORDER": "ФОТО ПОРЯДОК ПЕРЕДЕЛАТЬ",
        "CANCEL_PRODUCT": "ОТМЕНИТЬ ТОВАР",
        "ACCEPT_HTML_V2": "ПРИНЯТЬ HTML V2",
        "OPERATOR_OWN_PRICE": "СВОЯ ЦЕНА"
    }

    if action not in _allowed:
        _data = {
            "status": "BLOCKED_UNKNOWN_REVIEW_ACTION",
            "product_key": _product_key,
            "chat_id": str(chat_id),
            "action": str(action),
            "source": source,
            "timestamp_utc": _time.strftime("%Y%m%dT%H%M%SZ", _time.gmtime()),
            "live_allowed": False
        }
    else:
        _data = {
            "status": "REVIEW_ACTION_RECEIVED",
            "product_key": _product_key,
            "chat_id": str(chat_id),
            "action": action,
            "action_ru": _allowed[action],
            "source": source,
            "timestamp_utc": _time.strftime("%Y%m%dT%H%M%SZ", _time.gmtime()),
            "live_allowed": False,
            "next_allowed_action": "PROCESS_REVIEW_ACTION_DRY_ONLY"
        }

    # REVIEW_TEXT_INPUT_PENDING_PATCH_V1_START
    if action == "OPERATOR_OWN_PRICE":
        _pending = _out_dir / "pending_input_v1.json"
        _pending_data = {
            "status": "WAITING_FOR_TEXT",
            "input_type": "operator_price",
            "product_key": _product_key,
            "chat_id": str(chat_id),
            "source": source,
            "created_utc": _time.strftime("%Y%m%dT%H%M%SZ", _time.gmtime()),
            "allowed_example": "14,99",
            "live_gate": "CLOSED",
            "message_ru": "Введите свою цену. Пример: 14,99"
        }
        _pending.write_text(_json.dumps(_pending_data, ensure_ascii=False, indent=2), encoding="utf-8")
        _data["pending_input_created"] = True
        _data["pending_input_path"] = str(_pending)
        _data["operator_message_ru"] = "Введите свою цену. Пример: 14,99"
    # REVIEW_TEXT_INPUT_PENDING_PATCH_V1_END

    _out.write_text(_json.dumps(_data, ensure_ascii=False, indent=2), encoding="utf-8")
    return _data


def handle_review_callback_v1(update):
    """Handle Telegram inline button callback. Returns True if handled."""
    try:
        cb = update.get("callback_query")
        if not cb:
            return False

        action = cb.get("data", "")
        msg = cb.get("message", {})
        chat = msg.get("chat", {})
        chat_id = chat.get("id")

        if not chat_id:
            return True

        res = save_review_action_v1(chat_id, action, source="telegram_button")

        try:
            api("answerCallbackQuery", {
                "callback_query_id": cb.get("id"),
                "text": "Принято: " + str(res.get("action_ru", action)),
                "show_alert": False
            })
        except Exception:
            pass

        try:
            # REVIEW_BUTTON_ACTION_PROCESSOR_RU_V1_START
            import sys as _sys
            _helper_dir = ROOT / "storage" / "tools" / "telegram"
            if str(_helper_dir) not in _sys.path:
                _sys.path.insert(0, str(_helper_dir))
            from review_button_action_processor_ru_v1 import process_review_button_action_ru
            _msg_ru = process_review_button_action_ru(
                "/home/ionlipca7/runtime_eco_v1",
                "/home/ionlipca7/ecom_governed_runtime",
                action,
                res
            )
            send(chat_id, _msg_ru)
            # REVIEW_BUTTON_ACTION_PROCESSOR_RU_V1_END
        except Exception as _btn_ex:
            try:
                send(chat_id,
                    "✅ Решение принято\n\n"
                    "Действие: " + str(res.get("action_ru", action)) + "\n\n"
                    "Но обработчик кнопки дал ошибку: " + str(type(_btn_ex).__name__) + "\n"
                    "Live закрыт."
                )
            except Exception:
                pass

        return True
    except Exception as e:
        try:
            cb = update.get("callback_query", {})
            msg = cb.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            if chat_id:
                send(chat_id, "⚠️ Кнопка принята, но обработчик дал ошибку: " + str(type(e).__name__))
        except Exception:
            pass
        return True
# REVIEW_BUTTON_PATCH_V1_END


while True:
    try:
        updates = api("getUpdates", {"offset":offset,"timeout":25})

        for u in updates.get("result",[]):
            # TELEGRAM_ACTIVE_ROUTER_BOUNDARY_SHELL_V1_CALL_START
            try:
                if telegram_active_router_v1(u):
                    offset = u["update_id"] + 1
                    continue
            except Exception:
                pass
            # TELEGRAM_ACTIVE_ROUTER_BOUNDARY_SHELL_V1_CALL_END
            offset = u["update_id"] + 1
            # REVIEW_BUTTON_PATCH_V1_CALLBACK_CALL
            if handle_review_callback_v1(u):
                continue
            msg = u.get("message")
            if not msg:
                continue

            chat_id = msg["chat"]["id"]
            _raw_text = (msg.get("text") or msg.get("caption") or "")
            text = _raw_text.lower()
            # ECOM_SOURCES_COMMAND_PATCH_V1_START
            if text in ("/ecom_sources", "ecom_sources"):
                try:
                    import subprocess as _subprocess
                    import sys as _sys

                    _helper = ROOT / "storage" / "tools" / "ecom_os_v3" / "server" / "telegram_field_sources_report_v1.py"
                    _preview = ROOT / "storage" / "state_control" / "TELEGRAM_FIELD_SOURCES_REPORT_PREVIEW_V1.txt"

                    if not _helper.exists():
                        send(chat_id, "⚠️ /ecom_sources: helper не найден. Live закрыт.")
                        continue

                    _run = _subprocess.run(
                        [_sys.executable, str(_helper), "--action", "render"],
                        cwd=str(ROOT),
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                        timeout=25
                    )

                    if _run.returncode != 0:
                        send(chat_id, "⚠️ /ecom_sources: helper error code " + str(_run.returncode) + ". Live закрыт.")
                        continue

                    if _preview.exists():
                        _report = _preview.read_text(encoding="utf-8", errors="replace")
                    else:
                        _report = (_run.stdout or "").strip()

                    if not _report:
                        _report = "⚠️ /ecom_sources: отчёт пуст. Live закрыт."

                    if len(_report) > 3900:
                        _report = _report[:3900] + "\n\n…отчёт сокращён. Полный файл: storage/state_control/TELEGRAM_FIELD_SOURCES_REPORT_PREVIEW_V1.txt"

                    send(chat_id, _report)
                except Exception as _ex:
                    send(chat_id, "⚠️ /ecom_sources: ошибка " + str(type(_ex).__name__) + ". Live закрыт.")
                continue
            # ECOM_SOURCES_COMMAND_PATCH_V1_END


            READ_ONLY_COMMANDS = {
                "/ping": "PONG_RUNTIME_OK",

                "/status":
                    "СЕРВЕР АКТИВЕН | РЕЖИМ: ТОЛЬКО ЧТЕНИЕ | TELEGRAM OK",

                "/runtime":
                    "ACTIVE_RUNTIME=/home/ionlipca7/runtime_eco_v1",

                "/health":
                    "HEALTH OK | TMUX OK | TELEGRAM OK",

                "/bridge":
                    "BRIDGE CONNECTED | SERVER AUTHORITY ACTIVE"
            }

            if text == "/ecom_os_v3_preview":
                try:
                    import subprocess as _ecom_os_v3_subprocess
                    import json as _ecom_os_v3_json
                    _bridge = ROOT / "storage" / "tools" / "ecom_os_v3" / "server" / "telegram_ecom_os_v3_preview_bridge_v1.py"
                    _result_file = ROOT / "storage" / "state_control" / "telegram_ecom_os_v3_preview_bridge_result_v1.json"
                    _run = _ecom_os_v3_subprocess.run(
                        ["python3", str(_bridge)],
                        cwd=str(ROOT),
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if _result_file.exists():
                        _payload = _ecom_os_v3_json.loads(_result_file.read_text(encoding="utf-8"))
                        send(chat_id, _payload.get("preview_text", "ECOM OS V3 preview готов, но текст пустой."))
                    else:
                        send(chat_id, "ECOM OS V3 preview не создан: result file missing.")
                except Exception as _ecom_os_v3_error:
                    send(chat_id, "ECOM OS V3 preview error: " + str(_ecom_os_v3_error)[:300])
                continue

            if text in READ_ONLY_COMMANDS:
                send(chat_id, READ_ONLY_COMMANDS[text])
                continue

            if text in ["/ecom_os_v3_draft", "ecom_os_v3_draft"]:
                _ecom_draft_bridge = subprocess.run(
                    ["python3", "-B", "storage/tools/ecom_os_v3/server/telegram_ecom_os_v3_draft_route_bridge_v1.py"],
                    cwd=str(ROOT),
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=180
                )
                _ecom_draft_preview_path = ROOT / "storage" / "state_control" / "telegram_ecom_os_v3_draft_route_preview_text_v1.txt"
                if _ecom_draft_preview_path.exists():
                    _ecom_draft_preview = _ecom_draft_preview_path.read_text(encoding="utf-8", errors="replace")
                else:
                    _ecom_draft_preview = "ECOM OS V3 draft route executed, but preview file was not found."
                send(chat_id, _ecom_draft_preview[:3500])
                continue

            if text in ["/start","start"]:
                send(chat_id,"Готов. Отправь фото + описание. Потом /done")
                continue

            if text in ["/done","done"]:
                pkg = build_package(chat_id)
                send(chat_id,f"Собрано: {pkg['image_count']} фото. Готово к draft.")
                continue

            if "photo" in msg:
                ph = msg["photo"][-1]
                save_photo(ph["file_id"], chat_id, msg["message_id"])
                # ECOM_PHOTO_PRODUCT_ROUTER_V6_5_HOOK_START
                try:
                    _ecom_saved_photo_path = session(chat_id) / f"{msg['message_id']}.jpg"
                    ecom_photo_router_v6_5_route(
                        _ecom_saved_photo_path,
                        chat_id=chat_id,
                        msg_id=msg["message_id"],
                        file_id=ph["file_id"],
                        caption=msg.get("caption", "")
                    )
                except Exception:
                    pass
                # ECOM_PHOTO_PRODUCT_ROUTER_V6_5_HOOK_END
                # ECOM_SMART_ALBUM_ROUTER_V2_HOOK_START
                try:
                    _ecom_saved_photo_path_v2 = session(chat_id) / f"{msg['message_id']}.jpg"
                    ecom_smart_album_router_v2_register(
                        _ecom_saved_photo_path_v2,
                        media_group_id=msg.get('media_group_id'),
                        chat_id=chat_id,
                        msg_id=msg['message_id'],
                        file_id=ph['file_id'],
                        caption=msg.get('caption', '')
                    )
                except Exception:
                    pass
                # ECOM_SMART_ALBUM_ROUTER_V2_HOOK_END

                # ===== ECOM_REAL_PRODUCT_PHOTO_RECEIPT_INTAKE_V1 START =====
                try:
                    import json as _ecom_json_photo
                    import shutil as _ecom_shutil_photo
                    import datetime as _ecom_dt_photo
                    import re as _ecom_re_photo

                    def _ecom_photo_load_pointer_v2():
                        _pointer_file = ROOT / "storage/control_room/CURRENT_POINTER.json"
                        _pointer = _ecom_json_photo.loads(_pointer_file.read_text(encoding="utf-8"))
                        _pointer_text = _ecom_json_photo.dumps(_pointer, ensure_ascii=False)

                        def _walk(_x):
                            if isinstance(_x, dict):
                                yield _x
                                for _v in _x.values():
                                    yield from _walk(_v)
                            elif isinstance(_x, list):
                                for _v in _x:
                                    yield from _walk(_v)

                        for _d in _walk(_pointer):
                            for _k in ("active_canonical_key", "canonical_key", "current_canonical_key", "product_key"):
                                _val = _d.get(_k)
                                if isinstance(_val, str) and ":" in _val:
                                    _platform, _product_id = _val.split(":", 1)
                                    return {
                                        "canonical_key": _val,
                                        "platform": _d.get("platform") or _platform,
                                        "product_id": str(_d.get("product_id") or _product_id),
                                        "url": _d.get("url") or _d.get("product_url") or "",
                                    }

                        _m = _ecom_re_photo.search(r"\balibaba:(\d{8,})\b", _pointer_text)
                        if _m:
                            return {
                                "canonical_key": "alibaba:" + _m.group(1),
                                "platform": "alibaba",
                                "product_id": _m.group(1),
                                "url": "",
                            }
                        raise RuntimeError("ACTIVE_PRODUCT_NOT_FOUND_IN_CURRENT_POINTER")

                    def _ecom_photo_slug_v2(_canonical_key):
                        return _ecom_re_photo.sub(r"[^A-Za-z0-9]+", "_", str(_canonical_key)).strip("_")

                    def _ecom_photo_mode_file_v2():
                        _d = ROOT / "storage/state_control/telegram_upload_modes"
                        _d.mkdir(parents=True, exist_ok=True)
                        return _d / (str(chat_id) + ".json")

                    def _ecom_photo_read_mode_v2():
                        _p = _ecom_photo_mode_file_v2()
                        if not _p.exists():
                            return None
                        try:
                            _j = _ecom_json_photo.loads(_p.read_text(encoding="utf-8"))
                            return _j.get("next_upload_kind")
                        except Exception:
                            return None

                    def _ecom_photo_clear_mode_v2():
                        try:
                            _ecom_photo_mode_file_v2().write_text(_ecom_json_photo.dumps({"next_upload_kind": None, "cleared_at_utc": _ecom_dt_photo.datetime.now(_ecom_dt_photo.timezone.utc).isoformat()}, ensure_ascii=False, indent=2), encoding="utf-8")
                        except Exception:
                            pass

                    def _ecom_photo_infer_kind_v2(_msg):
                        _mode = _ecom_photo_read_mode_v2()
                        if _mode in ("receipts", "photos"):
                            return _mode
                        _probe = " ".join(str(_msg.get(_k, "")) for _k in ("caption", "text", "message", "file_name")).lower()
                        _receipt_markers = ["чек", "receipt", "rechnung", "invoice", "beleg", "закуп", "purchase", "cost", "kosten", "zahlung", "paid", "order summary", "bestellung"]
                        return "receipts" if any(_marker in _probe for _marker in _receipt_markers) else "photos"

                    _active_product = _ecom_photo_load_pointer_v2()
                    _canonical_key = _active_product["canonical_key"]
                    _slug = _ecom_photo_slug_v2(_canonical_key)
                    _src = session(chat_id) / f"{msg['message_id']}.jpg"
                    _kind = _ecom_photo_infer_kind_v2(msg)
                    _evidence_root = ROOT / "storage/evidence/real_products" / _slug
                    _dest_dir = _evidence_root / _kind
                    _dest_dir.mkdir(parents=True, exist_ok=True)

                    _suffix = _src.suffix if _src.suffix else ".jpg"
                    _dest = _dest_dir / f"telegram_{msg['message_id']}{_suffix}"
                    if _src.exists():
                        _ecom_shutil_photo.copy2(_src, _dest)
                    else:
                        raise FileNotFoundError(str(_src))

                    _meta_path = _evidence_root / "evidence_meta.json"
                    if _meta_path.exists():
                        try:
                            _meta = _ecom_json_photo.loads(_meta_path.read_text(encoding="utf-8"))
                        except Exception:
                            _meta = {}
                    else:
                        _meta = {}

                    _meta.update({
                        "status": "EVIDENCE_META_CREATED",
                        "layer": "ECOM_REAL_PRODUCT_PHOTO_RECEIPT_INTAKE_V2_DYNAMIC_POINTER",
                        "canonical_key": _canonical_key,
                        "platform": _active_product.get("platform"),
                        "product_id": _active_product.get("product_id"),
                        "url": _active_product.get("url"),
                        "last_saved_kind": _kind,
                        "last_saved_file": str(_dest),
                        "updated_at_utc": _ecom_dt_photo.datetime.now(_ecom_dt_photo.timezone.utc).isoformat(),
                        "no_ebay_api_call": True,
                        "no_live_ebay_write": True,
                        "no_delete": True,
                    })

                    _meta["photos_count"] = len([_p for _p in (_evidence_root / "photos").iterdir() if _p.is_file() and not _p.name.endswith(".json")]) if (_evidence_root / "photos").exists() else 0
                    _meta["receipts_count"] = len([_p for _p in (_evidence_root / "receipts").iterdir() if _p.is_file() and not _p.name.endswith(".json")]) if (_evidence_root / "receipts").exists() else 0
                    _meta_path.write_text(_ecom_json_photo.dumps(_meta, ensure_ascii=False, indent=2), encoding="utf-8")
                    _ecom_photo_clear_mode_v2()

                    if _kind == "receipts":
                        send(chat_id, "Чек/закупочный документ сохранён ✅\nПубликация на eBay не запускается.")
                    else:
                        send(chat_id, "Фото товара сохранено ✅\nПубликация на eBay не запускается.")
                except Exception as _ecom_photo_ex:
                    send(chat_id, "Фото принято, но evidence-копирование не подтверждено: " + repr(_ecom_photo_ex)[:300])
                # ===== ECOM_REAL_PRODUCT_PHOTO_RECEIPT_INTAKE_V1 END =====
                continue
            # ===== ECOM_RECEIPT_DOCUMENT_HANDLER_V2 START =====
            if "document" in msg:
                try:
                    import json as _ecom_doc_json_v2
                    import datetime as _ecom_doc_dt_v2
                    import re as _ecom_doc_re_v2
                    import urllib.request as _ecom_doc_urllib_v2

                    def _ecom_doc_find_product_v2():
                        _pointer = _ecom_doc_json_v2.loads((ROOT / "storage/control_room/CURRENT_POINTER.json").read_text(encoding="utf-8"))
                        def _walk(_x):
                            if isinstance(_x, dict):
                                yield _x
                                for _v in _x.values():
                                    yield from _walk(_v)
                            elif isinstance(_x, list):
                                for _v in _x:
                                    yield from _walk(_v)
                        for _d in _walk(_pointer):
                            for _k in ("active_canonical_key", "canonical_key", "current_canonical_key", "product_key"):
                                _val = _d.get(_k)
                                if isinstance(_val, str) and ":" in _val:
                                    _platform, _product_id = _val.split(":", 1)
                                    return {"canonical_key": _val, "platform": _d.get("platform") or _platform, "product_id": str(_d.get("product_id") or _product_id), "url": _d.get("url") or _d.get("product_url") or ""}
                        raise RuntimeError("ACTIVE_PRODUCT_NOT_FOUND_IN_CURRENT_POINTER")

                    _doc = msg["document"]
                    _info = api("getFile", {"file_id": _doc["file_id"]})
                    _file_path = _info["result"]["file_path"]
                    _url = "https://api.telegram.org/file/bot" + TOKEN + "/" + _file_path
                    _product = _ecom_doc_find_product_v2()
                    _slug = _ecom_doc_re_v2.sub(r"[^A-Za-z0-9]+", "_", _product["canonical_key"]).strip("_")
                    _root = ROOT / "storage/evidence/real_products" / _slug
                    _dest_dir = _root / "receipts"
                    _dest_dir.mkdir(parents=True, exist_ok=True)
                    _name = _doc.get("file_name") or ("telegram_document_" + str(msg["message_id"]))
                    _safe = _ecom_doc_re_v2.sub(r"[^A-Za-z0-9._-]+", "_", _name).strip("_")
                    _dest = _dest_dir / ("telegram_doc_" + str(msg["message_id"]) + "_" + _safe)
                    with _ecom_doc_urllib_v2.urlopen(_url, timeout=40) as _r:
                        _dest.write_bytes(_r.read())
                    _meta_path = _root / "evidence_meta.json"
                    try:
                        _meta = _ecom_doc_json_v2.loads(_meta_path.read_text(encoding="utf-8")) if _meta_path.exists() else {}
                    except Exception:
                        _meta = {}
                    _meta.update({"status": "EVIDENCE_META_CREATED", "layer": "ECOM_RECEIPT_DOCUMENT_HANDLER_V2", "canonical_key": _product["canonical_key"], "platform": _product.get("platform"), "product_id": _product.get("product_id"), "url": _product.get("url"), "last_saved_kind": "receipts", "last_saved_file": str(_dest), "last_saved_document_name": _name, "updated_at_utc": _ecom_doc_dt_v2.datetime.now(_ecom_doc_dt_v2.timezone.utc).isoformat(), "no_ebay_api_call": True, "no_live_ebay_write": True, "no_delete": True})
                    _meta["photos_count"] = len([_p for _p in (_root / "photos").iterdir() if _p.is_file() and not _p.name.endswith(".json")]) if (_root / "photos").exists() else 0
                    _meta["receipts_count"] = len([_p for _p in (_root / "receipts").iterdir() if _p.is_file() and not _p.name.endswith(".json")]) if (_root / "receipts").exists() else 0
                    _meta_path.write_text(_ecom_doc_json_v2.dumps(_meta, ensure_ascii=False, indent=2), encoding="utf-8")
                    send(chat_id, "Чек/закупочный документ сохранён ✅\nПубликация на eBay не запускается.")
                except Exception as _ecom_doc_ex_v2:
                    send(chat_id, "Документ принят, но receipt-сохранение не подтверждено: " + repr(_ecom_doc_ex_v2)[:300])
                continue
            # ===== ECOM_RECEIPT_DOCUMENT_HANDLER_V2 END =====



            # ===== ECOM_REAL_LOOP_SOURCE_BUILD_REVIEW_V1 START =====
            _ecom_resp = None
            try:
                import subprocess as _ecom_subprocess, json as _ecom_json, re as _ecom_re
                _cmd_text = (_raw_text or "").strip()
                # ===== ECOM_RECEIPT_UPLOAD_MODE_COMMANDS_V2 START =====
                import json as _ecom_receipt_json_v2
                import datetime as _ecom_receipt_dt_v2
                _ecom_receipt_cmd_v2 = _cmd_text.strip().lower()
                if _ecom_receipt_cmd_v2 in ["/ecom_receipt", "/receipt", "receipt", "чек", "режим чек", "режим чека"]:
                    _ecom_receipt_mode_dir_v2 = ROOT / "storage/state_control/telegram_upload_modes"
                    _ecom_receipt_mode_dir_v2.mkdir(parents=True, exist_ok=True)
                    (_ecom_receipt_mode_dir_v2 / (str(chat_id) + ".json")).write_text(_ecom_receipt_json_v2.dumps({"next_upload_kind": "receipts", "set_at_utc": _ecom_receipt_dt_v2.datetime.now(_ecom_receipt_dt_v2.timezone.utc).isoformat()}, ensure_ascii=False, indent=2), encoding="utf-8")
                    send(chat_id, "Режим чека включён ✅\nСледующее фото или PDF будет сохранено как чек/закупочный документ.\nПубликация на eBay не запускается.")
                    continue
                if _ecom_receipt_cmd_v2 in ["/ecom_photo", "/photo", "photo", "фото", "режим фото"]:
                    _ecom_receipt_mode_dir_v2 = ROOT / "storage/state_control/telegram_upload_modes"
                    _ecom_receipt_mode_dir_v2.mkdir(parents=True, exist_ok=True)
                    (_ecom_receipt_mode_dir_v2 / (str(chat_id) + ".json")).write_text(_ecom_receipt_json_v2.dumps({"next_upload_kind": "photos", "set_at_utc": _ecom_receipt_dt_v2.datetime.now(_ecom_receipt_dt_v2.timezone.utc).isoformat()}, ensure_ascii=False, indent=2), encoding="utf-8")
                    send(chat_id, "Режим фото включён ✅\nСледующее фото будет сохранено как фото товара.\nПубликация на eBay не запускается.")
                    continue
                # ===== ECOM_RECEIPT_UPLOAD_MODE_COMMANDS_V2 END =====
                _cmd_upper = _cmd_text.upper()
                if "REVIEW LISTING DRAFT V1" in _cmd_upper:
                    _p = _ecom_subprocess.run(
                        ["python3","/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_review_listing_draft_agent_v1.py"],
                        text=True, capture_output=True, timeout=60
                    )
                    _data = _ecom_json.loads((_p.stdout or "{}").splitlines()[-1])
                    _r = _data.get("review") or {}
                    _agents = _data.get("agents") or {}
                    _gaps = _r.get("blocking_gaps") or []
                    _ecom_resp = "\n".join([
                        "✅ REVIEW LISTING DRAFT V1",
                        "",
                        "📌 Статус: " + str(_data.get("status")),
                        "🛒 Товар: " + str(_r.get("title")),
                        "🏷 Категория: " + str(_r.get("category")),
                        "💶 Цена: " + str(_r.get("price_logic")),
                        "📦 Количество: " + str(_r.get("quantity")),
                        "🖼 Фото найдено: " + str(_r.get("photo_count")),
                        "⭐ Оценка качества: " + str(_r.get("quality_score")) + "/100",
                        "",
                        "🧠 Проверка агентов:",
                        "- SEO critic: " + str(_agents.get("seo_critic")),
                        "- Photo critic: " + str(_agents.get("photo_critic")),
                        "- Price critic: " + str(_agents.get("price_critic")),
                        "- Category critic: " + str(_agents.get("category_critic")),
                        "- Policy guard: " + str(_agents.get("policy_guard")),
                        "",
                        "⚠️ Что проверить:",
                        ("- " + "\n- ".join(_gaps)) if _gaps else "- критических проблем нет",
                        "",
                        "📄 Файл:",
                        "/home/ionlipca7/ecom_governed_runtime/storage/state_control/telegram_listing_draft_review_v1.json",
                        "",
                        "➡️ Следующий шаг:",
                        "Сначала подтвердить цену/категорию. Live eBay пока НЕ трогаем."
                    ])
                # ===== ECOM_OS_V3_TELEGRAM_CONTROL_RU_V1 START =====
                # ===== ECOM_NEW_PRODUCT_SESSION_RESET_V1 START =====

                # ===== ECOM_DRY_APPROVAL_CARD_V1 START =====
                elif _cmd_text.strip().lower().startswith("/ecom_dry_card"):
                    try:
                        _packet_path = ROOT / "storage/state_control/b8_dry_approval_packet_example_no_live_no_patch_v1.json"
                        _renderer_path = ROOT / "storage/tools/ecom_os_v3/server/telegram_approval_card_renderer_dry_v1.py"
                        _out_path = ROOT / "storage/review/TELEGRAM_DRY_APPROVAL_CARD_RENDERED_FROM_BOT_DRY_V1.txt"

                        if not _packet_path.exists():
                            send(chat_id, "STOP_SAFE: dry approval packet not found. Run B8 first.")
                            continue
                        elif not _renderer_path.exists():
                            send(chat_id, "STOP_SAFE: dry approval renderer not found. Run B9 first.")
                            continue
                        else:
                            import importlib.util as _ecom_importlib_util
                            import json as _ecom_json

                            _spec = _ecom_importlib_util.spec_from_file_location("telegram_approval_card_renderer_dry_v1", str(_renderer_path))
                            _mod = _ecom_importlib_util.module_from_spec(_spec)
                            _spec.loader.exec_module(_mod)

                            _packet = _ecom_json.loads(_packet_path.read_text(encoding="utf-8"))
                            _packet["next_allowed_action"] = "DRY_CARD_RENDERED_FROM_TELEGRAM_COMMAND_NO_LIVE"
                            _card = _mod.render_telegram_approval_card(_packet)
                            _out_path.write_text(_card, encoding="utf-8")
                            send(chat_id, _card)
                            continue
                    except Exception as e:
                        send(chat_id, "STOP_SAFE: dry card render failed: " + str(e)[:500])
                        continue
                # ===== ECOM_DRY_APPROVAL_CARD_V1 END =====
                elif _cmd_text.strip().lower().startswith("/ecom_new") or _cmd_text.strip().lower().startswith("новый товар") or _cmd_text.strip().lower().startswith("новый продукт"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_new_product_session_reset_bridge_v1.py", "--action", "new", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or _p.stderr or "ECOM OS V3 — новый товар: нет ответа от bridge.").strip()
                # ===== ECOM_NEW_PRODUCT_SESSION_RESET_V1 END =====
                elif _cmd_text.strip().lower().startswith("/ecom_help"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_control_ru_bridge_v1.py", "--action", "help", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка bridge.").strip()

                elif _cmd_text.strip().lower().startswith("/ecom_status"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_control_ru_bridge_v1.py", "--action", "status", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка bridge.").strip()

                elif _cmd_text.strip().lower().startswith("/ecom_preview"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_control_ru_bridge_v1.py", "--action", "preview", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка bridge.").strip()

                elif _cmd_text.strip().lower().startswith("/ecom_review"):
                    _current_state = ROOT / "storage/state_control/telegram_control_ru_dry_draft_request_v1.json"
                    _review_result = ROOT / "storage/state_control/real_product_dry_draft_runner_v1_result.json"
                    try:
                        import pathlib as _review_pathlib
                        import json as _review_json
                        _current_key = None
                        if _current_state.exists():
                            _current_data = _review_json.loads(_current_state.read_text(encoding="utf-8", errors="replace"))
                            _current_key = _current_data.get("canonical_key") or _current_data.get("product_key")
                        if not _current_key:
                            _ecom_resp = "STOP_SAFE_ECOM_REVIEW_NO_CURRENT_PRODUCT\n\nТекущий товар не найден. Сначала отправь /ecom_files.\nLive закрыт."
                        elif not _review_result.exists():
                            _ecom_resp = "\n".join([
                                "STOP_SAFE_ECOM_REVIEW_NO_CURRENT_DRY_RESULT",
                                "",
                                "Для текущего товара ещё нет актуального dry review.",
                                "Текущий товар: " + str(_current_key),
                                "",
                                "Нужно сначала выполнить dry draft rebuild.",
                                "Публикация на eBay не запускается."
                            ])
                        else:
                            _review_data = _review_json.loads(_review_result.read_text(encoding="utf-8", errors="replace"))
                            _result_key = _review_data.get("canonical_key") or _review_data.get("product_key")
                            _preview_path = _review_data.get("preview_txt")
                            if _result_key != _current_key:
                                _ecom_resp = "\n".join([
                                    "STOP_SAFE_ECOM_REVIEW_RESULT_PRODUCT_MISMATCH",
                                    "",
                                    "Dry-result относится не к текущему товару.",
                                    "Текущий товар: " + str(_current_key),
                                    "Dry-result товар: " + str(_result_key),
                                    "",
                                    "Публикация на eBay не запускается."
                                ])
                            elif not _preview_path or not _review_pathlib.Path(_preview_path).exists():
                                _ecom_resp = "STOP_SAFE_ECOM_REVIEW_PREVIEW_FILE_MISSING\n\nPreview file отсутствует. Live закрыт."
                            else:
                                _preview_text = _review_pathlib.Path(_preview_path).read_text(encoding="utf-8", errors="replace")
                                if _current_key not in _preview_text:
                                    _ecom_resp = "\n".join([
                                        "STOP_SAFE_ECOM_REVIEW_STALE_PRODUCT",
                                        "",
                                        "Review-карточка относится не к текущему товару.",
                                        "Текущий товар: " + str(_current_key),
                                        "Preview-файл: " + str(_preview_path),
                                        "",
                                        "Нужно пересобрать review/draft для текущего товара.",
                                        "Публикация на eBay не запускается."
                                    ])
                                else:
                                    _ecom_resp = _preview_text[:3500]
                    except Exception as _review_ex:
                        _ecom_resp = "ECOM OS V3 — review error: " + repr(_review_ex)[:300]

                elif _cmd_text.strip().lower().startswith("/ecom_draft"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_control_ru_bridge_v1.py", "--action", "draft", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка bridge.").strip()

                elif _cmd_text.strip().lower().startswith("/ecom_files"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_real_product_evidence_bridge_v1.py", "--action", "status", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка evidence bridge.").strip()

                elif any(_cmd_text.strip().lower().startswith(_prefix) for _prefix in ["количество:", "закупочная цена:", "закупка:", "желаемая цена:", "цена продажи:", "заметка:", "note:", "qty:", "cost:", "purchase price:", "target price:", "sale price:"]):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_real_product_evidence_bridge_v1.py", "--action", "text", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка evidence bridge.").strip()

                elif _cmd_text.strip().lower().startswith("/ecom_cancel"):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_control_ru_bridge_v1.py", "--action", "cancel", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — ошибка bridge.").strip()

                elif _cmd_text.strip().startswith("/"):
                    continue

                elif _ecom_re.findall(r"https?://\S+", _cmd_text) and (
                    any(_cmd_text.lower().split("?")[0].endswith(_ext) for _ext in [".jpg", ".jpeg", ".png", ".webp"])
                    or "alicdn.com" in _cmd_text.lower()
                ):
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/telegram_direct_image_url_evidence_bridge_v1.py", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or "ECOM OS V3 — image URL bridge error.").strip()

                elif _ecom_re.findall(r"https?://\S+", _cmd_text) and any(_x in _cmd_text.lower() for _x in ["alibaba.com", "aliexpress.", "temu.", "ebay.", "amazon."]):
                    # CLEAN_URL_INTAKE_FACADE_V3_MARKER: marketplace product URLs go only through clean facade
                    _p = _ecom_subprocess.run(
                        ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/clean_new_product_intake_facade_v1.py", "--action", "stage-url", "--text", _cmd_text],
                        text=True, capture_output=True, timeout=60
                    )
                    _ecom_resp = (_p.stdout or _p.stderr or "ECOM OS V3 — clean intake facade: нет ответа.").strip()
                    if _p.returncode == 0 and "clean URL принят" in _ecom_resp:
                        _q = _ecom_subprocess.run(
                            ["python3", "/home/ionlipca7/runtime_eco_v1/storage/tools/ecom_os_v3/server/operator_missing_fields_questions_v1.py"],
                            text=True, capture_output=True, timeout=30
                        )
                        _q_text = (_q.stdout or _q.stderr or "").strip()
                        if _q.returncode == 0 and _q_text:
                            _ecom_resp = _ecom_resp + "\n\n" + _q_text
                # ===== ECOM_OS_V3_TELEGRAM_CONTROL_RU_V1 END =====

                elif "BUILD LISTING DRAFT V1" in _cmd_upper:
                    _p = _ecom_subprocess.run(
                        ["python3","/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_build_listing_draft_agent_v1.py"],
                        text=True, capture_output=True, timeout=60
                    )
                    _data = _ecom_json.loads((_p.stdout or "{}").splitlines()[-1])
                    _d = _data.get("draft") or {}
                    _ecom_resp = "\n".join([
                        "✅ BUILD LISTING DRAFT V1",
                        "",
                        "📌 Статус: " + str(_data.get("status")),
                        "🛒 Заголовок: " + str(_d.get("title")),
                        "🏷 Категория: " + str(_d.get("category")),
                        "💶 Цена: " + str(_d.get("price_logic")),
                        "🖼 Фото найдено: " + str(_data.get("image_candidates_downloaded")),
                        "",
                        "📄 Файл:",
                        "/home/ionlipca7/ecom_governed_runtime/storage/state_control/telegram_listing_draft_packet_v1.json",
                        "",
                        "➡️ Следующий шаг:",
                        "REVIEW LISTING DRAFT V1"
                    ])
                elif _ecom_re.findall(r"https?://\S+", _cmd_text):
                    _url = _ecom_re.findall(r"https?://\S+", _cmd_text)[0]
                    _p = _ecom_subprocess.run(
                        ["python3","/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_source_link_intake_agent_v1.py", _url],
                        text=True, capture_output=True, timeout=90
                    )
                    _data = _ecom_json.loads((_p.stdout or "{}").splitlines()[-1])
                    _ecom_resp = "\n".join([
                        "✅ ССЫЛКА ПРИНЯТА",
                        "",
                        "📌 Статус обработки:",
                        str(_data.get("status")),
                        "🖼 Скачано фото: " + str(_data.get("downloaded_count")),
                        "",
                        "📄 Файл проверки:",
                        "/home/ionlipca7/ecom_governed_runtime/storage/state_control/telegram_source_link_intake_agent_v1_last.json",
                        "",
                        "➡️ Следующий шаг:",
                        "BUILD LISTING DRAFT V1"
                    ])
            except Exception as _ecom_ex:
                _ecom_resp = "STOP_SAFE_TELEGRAM_COMMAND_ERROR: " + repr(_ecom_ex)
            # ===== ECOM_REAL_LOOP_SOURCE_BUILD_REVIEW_V1 END =====

            if text:
                if save_text(chat_id,text):
                    send(chat_id,(_ecom_resp or "Текст сохранён. Если это ссылка товара — я подготовлю обработку для листинга."))

    except Exception as e:
        print("ERROR:", e, flush=True)
        time.sleep(3)


# ===== ECOM_SOURCE_LINK_INTAKE_V1 START =====
def ecom_source_link_intake_v1(text):
    import re, subprocess, json
    urls = re.findall(r'https?://\S+', text or "")
    if not urls:
        return None
    allowed = ["aliexpress.", "alibaba.", "1688.", "amazon.", "ebay.", "kaufland.", "temu."]
    if not any(a in urls[0].lower() for a in allowed):
        return None
    p = subprocess.run(
        ["python3", "/home/ionlipca7/ecom_governed_runtime/storage/tools/telegram_source_link_intake_agent_v1.py", urls[0]],
        text=True,
        capture_output=True,
        timeout=90
    )
    out = (p.stdout or "").strip()
    try:
        data = json.loads(out.splitlines()[-1]) if out else {}
    except Exception:
        data = {"status": "STOP_SAFE_SOURCE_LINK_PARSE_FAILED"}
    return "ССЫЛКА ПРИНЯТА ✅\nСтатус обработки: {}\nСкачано фото: {}\nФайл проверки: /home/ionlipca7/ecom_governed_runtime/storage/state_control/telegram_source_link_intake_agent_v1_last.json\nСледующий шаг: отправь BUILD LISTING DRAFT V1".format(
        data.get("status", "UNKNOWN"),
        data.get("downloaded_count", 0)
    )
# ===== ECOM_SOURCE_LINK_INTAKE_V1 END =====


# === ECOM OS V6.5 ADAPTER CANDIDATE HOOK - NO ACTIVE WRITE ===
def ecom_v6_5_adapter_preview_text():
    """
    Candidate-only helper.
    Does not start bot.
    Does not call external APIs.
    Does not read secrets.
    """
    return (
        "ECOM OS V6.5\\n"
        "Status: adapter candidate ready\\n"
        "Root: /home/ionlipca7/ecom_governed_runtime\\n"
        "Action: preview only, no restart"
    )
# === END ECOM OS V6.5 ADAPTER CANDIDATE HOOK ===


# === ECOM OS V6.5 DECISION INBOX PREVIEW HOOK - NO ACTIVE WRITE ===
def ecom_v6_5_decision_inbox_preview_text():
    """
    Candidate-only helper.
    Reads dry preview text from clean root.
    Does not send Telegram messages.
    Does not call external APIs.
    Does not read secrets.
    """
    from pathlib import Path
    root = Path("/home/ionlipca7/ecom_governed_runtime")
    previews = sorted((root / "storage/state_control").glob("TELEGRAM_DECISION_INBOX_PREVIEW_RU_*.txt"))
    if not previews:
        return "ECOM OS V6.5 — Decision Inbox\nPreview not found."
    return previews[-1].read_text(encoding="utf-8", errors="replace")[:3500]
# === END ECOM OS V6.5 DECISION INBOX PREVIEW HOOK ===


# === ECOM OS V6.5 SCHEDULED BRIEFING PREVIEW HOOK - NO ACTIVE WRITE ===
def ecom_v6_5_scheduled_briefing_preview_text():
    """
    Candidate-only helper.
    Reads dry briefing preview from clean root.
    Does not send Telegram messages.
    Does not call external APIs.
    Does not read secrets.
    """
    from pathlib import Path
    root = Path("/home/ionlipca7/ecom_governed_runtime")
    previews = sorted((root / "storage/state_control").glob("SCHEDULED_BRIEFING_PREVIEW_RU_*.txt"))
    if not previews:
        return "ECOM OS V6.5 — Scheduled Briefing\nPreview not found."
    return previews[-1].read_text(encoding="utf-8", errors="replace")[:3500]
# === END ECOM OS V6.5 SCHEDULED BRIEFING PREVIEW HOOK ===




