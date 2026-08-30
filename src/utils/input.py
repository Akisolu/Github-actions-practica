from pydantic import BaseModel, Field

class OpcionInput(BaseModel):
    # Valida entero estrictamente en el rango 1 a 4
    opcion: int = Field(..., ge=1, le=4)