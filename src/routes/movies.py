from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db, MovieModel
from schemas import MovieListResponseSchema

router = APIRouter()

@router.get(
    "/movies",
    response_model=MovieListResponseSchema
)
async def get_movies(
        movie_id: int,
        db: AsyncSession = Depends(get_db)
) -> MovieModel:
    movie = await db.get(MovieModel, movie_id)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie with the given ID was not found.",
        )
    return movie
