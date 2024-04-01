from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aprendiz_model import AprendizModel
from schemas.aprendiz_schema import AprendizSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AprendizSchema)
async def post_aprendiz(aprendiz: AprendizSchema, db: AsyncSession = Depends(get_session)):
    novo_aprendiz = AprendizModel(nome=aprendiz.nome, idade=aprendiz.idade, turma=aprendiz.turma)
    db.add(novo_aprendiz)
    await db.commit()

    return novo_aprendiz

@router.get("/", response_model=List[AprendizSchema])
async def get_aprendizes(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AprendizModel)
        result = await session.execute(query)
        aprendizes: List[AprendizModel] = result.scalars().all()

        return aprendizes
    
@router.put("/{aprendiz_id}", response_model=AprendizModel, status_code=status.HTTP_202_ACCEPTED)
async def put_aprendiz(aprendiz_id: int, aprendiz: AprendizSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AprendizModel).filter(AprendizModel.id == aprendiz_id)
        result = await session.execute(query)
        aprendiz_up = result.scalar_one_or_none()

        if aprendiz_up:
            aprendiz_up.nome = aprendiz.nome
            aprendiz_up.idade = aprendiz.idade
            aprendiz_up.turma = aprendiz.turma

            await session.commit()
            return aprendiz_up

        else:
            raise HTTPException(detail="Aprendiz não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{aprendiz_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aprendiz(aprendiz_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AprendizModel).filter(AprendizModel.id == aprendiz_id)
        result = await session.execute(query)
        aprendiz_del = result.scalar_one_or_none()

        if aprendiz_del:
            await session.delete(aprendiz_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Aprendiz não encontrado", status_code=status.HTTP_404_NOT_FOUND)