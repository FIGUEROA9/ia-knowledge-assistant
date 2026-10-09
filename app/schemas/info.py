cat > app/schemas/info.py << 'EOF'
from pydantic import BaseModel


class InfoResponse(BaseModel):
    name: str
    version: str
    environment: str
    llm_enabled: bool
EOF
