from pydantic import BaseModel
from typing import Literal

from doco.io._graph import options
# ===== SUPERVIOR =====
class routeResponse(BaseModel):
    # next: Literal[*options]
    next: Literal["FINISH", "Summarizer", "ContentCreator"]
