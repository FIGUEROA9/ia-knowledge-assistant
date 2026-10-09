# AI Knowledge Assistant - Bootstrap API

Primer incremento funcional del proyecto AI Knowledge Assistant: una API asíncrona
con FastAPI, validada con Pydantic, probada con pytest y versionada con Git.

**Importante:** este incremento NO integra ningún LLM. La respuesta del chat es
generada por una implementación local de bootstrap (`provider: bootstrap-local`).

## Requisitos

- Python 3.12 o superior
- Git
- Una cuenta de GitHub (solo para clonar o publicar el repositorio)

## Instalación

```bash
git clone https://github.com/FIGUEROA9/ia-knowledge-assistant.git
cd ia-knowledge-assistant
python -m venv .venv
```

## Activación del entorno virtual

- Git Bash (Windows): `source .venv/Scripts/activate`
- PowerShell (Windows): `.venv\Scripts\Activate.ps1`
- CMD (Windows): `.venv\Scripts\activate.bat`
- Linux / macOS: `source .venv/bin/activate`

Cuando está activo, aparece `(.venv)` al inicio de la terminal.

## Instalar dependencias

```bash
pip install -e ".[dev]"
```

Las dependencias están declaradas en `pyproject.toml`.

## Ejecutar la API

```bash
uvicorn app.main:app --reload
```

- API: http://127.0.0.1:8000
- Documentación Swagger: http://127.0.0.1:8000/docs

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/health` | Estado del servicio |
| POST | `/api/v1/chat` | Recibe una pregunta y devuelve `answer` y `provider` |
| GET | `/api/v1/info` | Información básica del proyecto |

### Ejemplo de chat

```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "Que es FastAPI?"}'
```

La pregunta debe tener entre 3 y 2000 caracteres. Si no cumple, la API responde
HTTP 422 (validación de Pydantic).

## Ejecutar las pruebas

```bash
python -m pytest -q
```

## Estructura del proyecto

```
ai-knowledge-assistant/
├── app/
│   ├── main.py
│   ├── api/routes/      # capa HTTP (routers)
│   ├── schemas/         # modelos Pydantic
│   └── services/        # lógica del asistente
├── scripts/
├── tests/
│   ├── unit/
│   └── integration/
├── .gitignore
├── pyproject.toml
└── README.md
```

## Flujo de Git

- Rama principal: `main`
- Ramas de funcionalidad: `feat/bootstrap-api`, `feat/bootstrap-tests`
- Los cambios se integran a `main` mediante Pull Request.

## Preguntas de sustentación

1. ¿Qué responsabilidad tiene FastAPI en esta solución?
2. ¿Qué problema resuelve Pydantic y por qué un request inválido retorna 422?
3. ¿Qué diferencia existe entre def y async def en este contexto?
4. ¿Qué hace await y por qué es importante en aplicaciones que consumen servicios externos?
5. ¿Qué diferencia existe entre una prueba unitaria y una prueba de integración?
6. ¿Por qué el servicio del asistente está separado del router?
7. ¿Qué diferencia existe entre Git y GitHub?
8. ¿Qué cambiará en el próximo módulo cuando se conecte un LLM real y qué debería permanecer estable?
