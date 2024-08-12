from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.r0931795_models import Contact
from typing import List, Optional
from database import execute_sql_query
from queries.r0931795_queries import (
    GET_ALL_PRODUCE_QUERY,
    GET_PRODUCE_BY_ID_QUERY,
    INSERT_CONTACT_QUERY,
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
    # Fetch data from the database
    events = execute_sql_query(GET_ALL_COMMUNITY_EVENTS_QUERY)

    # Convert event_date to string
    for event in events:
        event['event_date'] = event['event_date'].strftime('%Y-%m-%d')

    return events

# Endpoint to submit contact form
@router.post("/contact/")
async def create_contact(contact: Contact):
    try:
        execute_sql_query(INSERT_CONTACT_QUERY, (contact.name, contact.email, contact.message))
        return {"message": "Contact form submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

