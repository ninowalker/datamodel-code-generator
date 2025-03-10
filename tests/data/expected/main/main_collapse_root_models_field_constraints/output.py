# generated by datamodel-codegen:
#   filename:  not_real_string.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Tweet(BaseModel):
    author_id: Optional[str] = None


class FileRequest(BaseModel):
    file_hash: str = Field(..., max_length=32, min_length=32, regex='^[a-fA-F\\d]{32}$')
