from pydantic import BaseModel, ConfigDict

# Shared base field
class NoteBase(BaseModel):
    title: str
    content: str 

# for creation 
class NoteCreate(NoteBase):
    pass

# for full update(PUT) 
class NoteUpdate(NoteBase):
    pass

# for partial update(PATCH)
class NotePatch(BaseModel):
    title: str | None = None
    content: str | None = None

# for the response serialization
class NoteOut(NoteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)