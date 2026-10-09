from app.services import chat_service


async def test_generate_answer_known_question():
    answer = await chat_service.generate_answer("¿Qué es FastAPI?")
    assert "framework web" in answer
