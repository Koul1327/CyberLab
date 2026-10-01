# CyberLab

Моя маленькая учебная лаборатория веб-безопасности на Flask для резюме)))

Каждый модуль содержит уязвимую реализацию, исправленную версию, тесты и объяснение проблемы

## Лаборатории

В планах 10 модулей с привязкой к категориям OWASP

## Подготовка

Вам потребуется Python 3.12. Команды выполняются из корня проекта

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask pytest
```

## Запуск первого модуля

Уязвимая версия:

```bash
python -m flask --app labs.auth_bypass.vulnerable.app run --host 127.0.0.1 --port 5000
```

Исправленная версия, в другом терминале с активным окружением:

```bash
python -m flask --app labs.auth_bypass.fixed.app run --host 127.0.0.1 --port 5001
```

Страница входа: `/login`. Административная страница: `/admin`.

Учебные аккаунты исправленной версии:

Пользователь:Пароль:Роль
Alex:alex-lab-password:user
admin:admin-lab-password:admin

## Проверка

```bash
python -m pytest labs/auth_bypass/tests/ -q
```

Тесты подтверждают обход входа в уязвимой версии, отказ при неверном пароле в исправленной версии и проверку рута
