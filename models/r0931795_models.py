from pydantic import BaseModel

class Produce(BaseModel):
    id: int
    name: str
    description: str
    price: float
    season: str

class FarmingPractice(BaseModel):
    id: int
    practice_name: str
    description: str

class CommunityEvent(BaseModel):
    id: int
    event_name: str
    event_date: str  # Date can be handled as a string or datetime
    description: str

