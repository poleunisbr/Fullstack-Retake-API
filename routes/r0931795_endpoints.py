from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from database import execute_sql_query
from queries.r0931795_queries import (
    GET_ALL_PRODUCE_QUERY,
    GET_PRODUCE_BY_ID_QUERY,
    INSERT_PRODUCE_QUERY,
    GET_ALL_FARMING_PRACTICES_QUERY,
    GET_ALL_COMMUNITY_EVENTS_QUERY
)
from models.r0931795_models import Produce, FarmingPractice, CommunityEvent

router = APIRouter()

# Endpoint to get all produce
@router.get("/produce/", response_model=List[Produce])
async def get_all_produce():
    try:
        produce_list = execute_sql_query(GET_ALL_PRODUCE_QUERY)
        if not produce_list:
            raise HTTPException(status_code=404, detail="No produce found")
        return produce_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get produce by ID
@router.get("/produce/{produce_id}", response_model=Produce)
async def get_produce_by_id(produce_id: int):
    try:
        produce = execute_sql_query(GET_PRODUCE_BY_ID_QUERY, (produce_id,))
        if not produce:
            raise HTTPException(status_code=404, detail="Produce not found")
        return produce[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to create new produce
@router.post("/produce/", response_model=Produce)
async def create_produce(produce: Produce):
    try:
        execute_sql_query(INSERT_PRODUCE_QUERY, (produce.name, produce.description, produce.price, produce.season))
        return {"message": "Produce created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all farming practices
@router.get("/farming-practices/", response_model=List[FarmingPractice])
async def get_all_farming_practices():
    try:
        practices = execute_sql_query(GET_ALL_FARMING_PRACTICES_QUERY)
        if not practices:
            raise HTTPException(status_code=404, detail="No farming practices found")
        return practices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all community events
@router.get("/community-events/", response_model=List[CommunityEvent])
async def get_all_community_events():
    try:
        events = execute_sql_query(GET_ALL_COMMUNITY_EVENTS_QUERY)
        if not events:
            raise HTTPException(status_code=404, detail="No community events found")
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
