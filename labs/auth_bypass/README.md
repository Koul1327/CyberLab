## Подготовка и запуск

Все команды выполняются из корня репозитория CyberLab.

Перед первым запуском:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask pytest
```

При следующих запусках достаточно активировать окружение:

```bash
source .venv/bin/activate
```

### Уязвимая версия

```bash
python -m flask --app labs.auth_bypass.vulnerable.app run --host 127.0.0.1 --port 5000
```

Страница входа: http://127.0.0.1:5000/login

Админка: http://127.0.0.1:5000/admin

Для воспроизведения войди под `admin` с произвольным
неверным паролем, затем открой `/admin`.

### Исправленная версия

В другом терминале из корня проекта активируй окружение и запусти:

```bash
source .venv/bin/activate
python -m flask --app labs.auth_bypass.fixed.app run --host 127.0.0.1 --port 5001
```

Страница входа: http://127.0.0.1:5001/login

Админка: http://127.0.0.1:5001/admin

### Учебные аккаунты исправленной версии

| Пользователь | Пароль | Роль |
|---|---|---|
| Alex | alex-lab-password | user |
| admin | admin-lab-password | admin |

Неверный пароль отклоняется. Alex может войти, но не может открыть `/admin` а Admin с правильным паролем получает доступ.

### Запуск тестов

```bash
python -m pytest labs/auth_bypass/tests/ -q
```

Ожидаем: 6 passed.

Для остановки сервера нажми Ctrl+C в терминале
