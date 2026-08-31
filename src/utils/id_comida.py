from pydantic import BaseModel, Field

class IdInput(BaseModel):
    # Valida entero estrictamente mayor o igual a 1
    id_comida: int = Field(..., gt=0)