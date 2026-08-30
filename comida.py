from typing import Optional
from pydantic import BaseModel, Field

class Comida(BaseModel):
    # strict=True evita que True/False pasen como 1/0
    id: Optional[int] = Field(default=None, gt=0, strict=True)
    nombre: str = Field(..., min_length=1)
    precio: float = Field(..., gt=0, strict=True)