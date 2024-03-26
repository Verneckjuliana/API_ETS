from typing import Optional
from pydantic import BaseModel as SCBaseModel

class AprendizSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str 
    idade: str 
    turma: str 

    class Config:
        orm_mode = True