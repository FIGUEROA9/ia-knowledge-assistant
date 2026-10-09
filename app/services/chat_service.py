import unicodedata

PROVIDER_NAME = "bootstrap-local"

_KNOWN_ANSWERS: dict[str, str] = {
    "que es fastapi": (
        "FastAPI es un framework web de Python para construir APIs "
        "con tipado, validacion y documentacion OpenAPI automatica."
    ),
    "que es pydantic": (
        "Pydantic es una libreria de Python que valida y modela datos "
        "usando anotaciones de tipo."
    ),
}

_DEFAULT_ANSWER = (
    "Respuesta de bootstrap local: todavia no hay un modelo de lenguaje conectado."
)


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text.lower())
    without_accents = "".join(c for c in decomposed if unicodedata.category(c) != "Mn")
    return without_accents.strip(" ¿?¡!.")


async def generate_answer(question: str) -> str:
    """Genera la respuesta local de bootstrap (sin LLM)."""
    return _KNOWN_ANSWERS.get(_normalize(question), _DEFAULT_ANSWER)
