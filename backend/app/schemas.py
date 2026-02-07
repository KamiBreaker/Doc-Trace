from pydantic import BaseModel
from typing import List

class DiffItem(BaseModel):
    type: str
    old: str | None = None
    new: str | None = None
    similarity: float | None = None

class DiffResponse(BaseModel):
    diffs: List[DiffItem]
