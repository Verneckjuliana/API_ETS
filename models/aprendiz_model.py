from core.configs import settings
from sqlalchemy import Column, Integer, String

class AprendizModel(settings.DBBaseModel):
    __tablename__ = 'aprendiz'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    idade: str = Column(String(6))
    turma: str = Column(String(4))