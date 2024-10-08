from pydantic import BaseModel
from typing import Literal


# ===== SUPERVIOR =====
class routeResponse(BaseModel):
    # next: Literal[*options]
    next: Literal["FINISH", "Summarizer", "ContentCreator"]
