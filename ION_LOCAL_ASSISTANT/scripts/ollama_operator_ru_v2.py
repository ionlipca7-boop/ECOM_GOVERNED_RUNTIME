import json
import urllib.request
from datetime import datetime
from pathlib import Path

MODEL = "ion-assistant"

SYSTEM = """
Ты ION LOCAL ASSISTANT.
Ты локальный оператор-помощник Ion на Windows.
Отвечай только на русском языке.
Отвечай коротко, спокойно и по делу.
Не спорь с пользователем.
Не называй себя Microsoft.
Не вставляй system-токены.

Главная задача:
помочь оператору подготовить текст, отчёт или команду, чтобы оператор мог отправить это в ChatGPT или проверить сам.

Ты НЕ выполняешь опасные действия сам.
Ты НЕ удаляешь файлы.
Ты НЕ публикуешь eBay.
Ты НЕ отправляешь email.
Ты НЕ трогаешь server/secrets.

Формат ответа всегда:
Кратко:
Риск:
Черновик для отправки в ChatGPT:
Что дальше:
""".strip()


def ask_ollama(user_text):
    prompt = SYSTEM + "\n\nЗадача оператора:\n" + user_text
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 260,
            "num_ctx": 2048,
            "repeat_penalty": 1.2
        }
    }

    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=300) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
        return data.get("response", "").strip()


def save_history(question, answer):
    base = Path(__file__).resolve().parent.parent
    memory_dir = base / "storage" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)
    history_file = memory_dir / "ollama_operator_ru_v2_history.json"

    history = []
    if history_file.exists():
        try:
            history = json.loads(history_file.read_text(encoding="utf-8"))
        except Exception:
            history = []

    history.append({
        "time": datetime.now().isoformat(),
        "model": MODEL,
        "question": question,
        "answer": answer
    })

    history_file.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")


def main():
    print("ION LOCAL ASSISTANT + OLLAMA V2")
    print("Модель:", MODEL)
    print("Для выхода: exit")
    print()

    while True:
        q = input("ION V2 > ").strip()
        if q.lower() in {"exit", "выход", "/bye"}:
            print("ВЫХОД")
            break

        if not q:
            continue

        try:
            answer = ask_ollama(q)
        except Exception as e:
            answer = "ОШИБКА OLLAMA: " + str(e)

        print()
        print(answer)
        print()
        save_history(q, answer)


if __name__ == "__main__":
    main()
