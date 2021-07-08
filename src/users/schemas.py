from typing import List, Optional
from ninja import Schema
from datetime import datetime, date


class RoleIn(Schema):
    description: str


class RoleOut(Schema):
    id: int
    description: str

    
class UserIn(Schema):
    name: str
    email: str
    role_id: int=None
    password: str=None


class UserOut(Schema):
    id: int=None
    name: str=None
    email: str=None
    role_id: int=None
    role__description: str=None
    created_at: datetime=None
    updated_at: datetime=None
    is_deleted: bool=None
    


class ClaimIn(Schema):
    description: str
    is_active: bool=None


class ClaimOut(Schema):
    id: int
    description: str
    is_active: bool


class UserClaimIn(Schema):
    user_id: int
    claim_id: int


class UserClaimOut(Schema):
    users: Optional[UserOut]=None
    claims: Optional[ClaimOut]=None
