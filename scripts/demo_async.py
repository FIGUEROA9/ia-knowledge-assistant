import asyncio
import time

import httpx

from app.main import app

QUESTIONS = [
    "Que es FastAPI?",
    "Que es Pydantic?",
    "Que es AsyncIO?",
    "Hola mundo",
]


async def ask(client: httpx.AsyncClient, question: str) -> tuple[str, int, dict]:
    response = await client.post("/api/v1/chat", json={"question": question})
    return question, response.status_code, response.json()


async def main() -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://demo") as client:
        start = time.perf_counter()
        results = await asyncio.gather(*(ask(client, q) for q in QUESTIONS))
        elapsed = time.perf_counter() - start

    for question, status, body in results:
        print(f"[{status}] {question} -> {body['provider']}")
    print(f"{len(results)} peticiones concurrentes en {elapsed:.3f}s")


if __name__ == "__main__":
    asyncio.run(main())
