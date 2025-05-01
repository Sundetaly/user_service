# Calendar Weather - User Service

Handles user registration and Telegram ID storage.

## Local Dev

1. Create `.env` from `.env.example`
2. Run PostgreSQL locally (port 5432)
3. Run Alembic: `alembic upgrade head`
4. Start server: `uvicorn app.main:app --reload`


## Docker

`docker build -t user_service . docker run -p 8001:8001 --env-file .env user_service`


## API

- POST `/users/` → `{ telegram_id: "12345" }`

