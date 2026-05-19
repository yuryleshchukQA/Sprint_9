# Sprint 9 — UI-тесты Foodgram

Автотесты Selenium + Page Object для [Foodgram](https://foodgram-frontend-1.foodgram.education-services.ru/signin).

## Структура проекта

| Путь | Назначение |
|------|------------|
| `locators/` | Локаторы элементов |
| `pages/` | Page Object (отдельный класс на страницу) |
| `tests/` | Тесты по функциональности (отдельный модуль и класс) |
| `data.py` | Тестовые данные |
| `resources/` | Фото для теста создания рецепта |
| `allure-report/` | Сгенерированный Allure-отчёт (в репозиторий) |
| `docs/` | Скриншот успешного CI-пайплайна |

## Сценарии

1. **Создание аккаунта** — регистрация → редирект на `/signin`, форма входа видна.
2. **Авторизация** — вход → главная `/recipes`, ссылка «Выход».
3. **Создание рецепта** — форма + ингредиент из списка + фото → карточка с названием.

## Локальный запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Allure

```bash
pytest -v
allure generate allure-results -o allure-report --clean
open allure-report/index.html
```

Папка `allure-results/` в git не попадает (см. `.gitignore`).

## Docker + Selenoid

```bash
docker compose up --build --abort-on-container-exit
```

Selenoid UI: http://localhost:8080

## CI/CD

GitHub Actions: `.github/workflows/ci.yml` (ветки `main`, `master`, `develop`).

Скриншот успешного пайплайна: `docs/ci_pipeline_success.png`
