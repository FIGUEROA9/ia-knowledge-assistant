from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    question: str = Field(
        ...,
        min_length=3,
        max_length=2000,
        description="Pregunta del usuario (3 a 2000 caracteres).",
        examples=["¿Qué es FastAPI?"],
    )


class ChatResponse(BaseModel):
    answer: str
    provider: str
