from typing import List
from django.db.models.query_utils import Q
from ninja import Router, Query
from ninja.errors import HttpError
from django.contrib.auth.hashers import make_password
import secrets
from .models import Claim, Role, User
from .schemas import (
    UserIn, UserOut,
    ClaimIn, ClaimOut,
    RoleIn, RoleOut,
    UserClaimIn, UserClaimOut
)

router = Router()



@router.post('/users')
def create_user(request, data: UserIn):
    """
    Insere um novo usuário
    """
    try:
        randompass = secrets.token_urlsafe()
        hashed_pass = make_password(data.password if data.password else randompass)
        role = Role.objects.get(id=data.role_id) if data.role_id else None
        user = User(name=data.name, email=data.email, password=hashed_pass, role=role)
        user.save()
        return {'ok': True, 'id': user.id}
    except:
        raise HttpError(400, 'Bad Request')


@router.get('/users', response=List[UserOut])
def read_users(request, id: int=None, name: str=None, email: str=None, role_id: int=None):
    """
    Retornar os dados de todos os usuarios cadastrados,
    ou utiliza o *query parameters* para realizar um filtro.
    """
    try:
        query = Q()
        query = Q(is_deleted=False)
        if id:
            query &= Q(id=id)
        if name:
            query &= Q(name=name)
        if email:
            query &= Q(name=email)
        if role_id:
            role = Role.objects.get(id=role_id)
            query &= Q(role=role)
        users = User.objects.filter(query).values(
            'id', 'name', 'email',
            'role_id', 'role__description',
            'created_at', 'updated_at',
            'is_deleted'
        )
        return users
    except:
        raise HttpError(404, 'Not Found')


@router.put('/users/{id}')
def update_user(request, id: int, data: UserIn):
    """
    Atualiza um desenvolvedor já cadastrado
    """
    try:
        return {'ok': True}
    except:
        raise HttpError(400, 'Bad Request')


@router.delete('/users/{id}')
def delete_user(request, id: int):
    """
    Realizar a **deleção lógica** de um usuário específico
    """
    try:
        user = User.objects.get(id=id)
        user.is_deleted = False
        user.save()
        return {'ok': True} 
    except:
        raise HttpError(400, 'Bad Request')


@router.post('/role')
def create_role(request, data: RoleIn):
    try:
        role = Role(description=data.description)
        role.save()
        return {'ok': True, 'id': role.id}
    except:
        raise HttpError(400, 'Bad Request')


@router.get('/role', response=List[RoleOut])
def read_role(request, id: int=None):
    try:
        query = Q()
        if id:
            query &= Q(id=id)
        role = Role.objects.filter(query).values()
        return role
    except:
        raise HttpError(404, 'Not Found')


@router.put('/role/{id}')
def update_role(request, id: int, data: RoleIn):
    try:
        role = Role.objects.get(id=id)
        if not data.description:
            raise Exception()
        role.description = data.description.strip()
        role.save()
        return {'ok': True}
    except:
        raise HttpError(400, 'Bad Request')


@router.delete('/role/{id}')
def delete_role(request, id: int):
    try:
        role = Role.objects.get(id=id)
        role.delete()
        return {'ok': True} 
    except:
        raise HttpError(400, 'Bad Request')


@router.post('/claim')
def create_claim(request, data: ClaimIn):
    try:
        claim = Claim(description=data.description, is_active=True)
        claim.save()
        return {'ok': True, 'id': claim.id}
    except:
        raise HttpError(400, 'Bad Request')


@router.get('/claim', response=List[ClaimOut])
def read_claim(request, id: int=None):
    try:
        query = Q()
        if id:
            query &= Q(id=id)
        claim = Claim.objects.filter(query).values()
        return claim
    except:
        raise HttpError(404, 'Not Found')


@router.put('/claim/{id}')
def update_claim(request, id: int, data: ClaimIn):
    try:
        claim = Claim.objects.get(id=id)
        if data.description:
            claim.description = data.description.strip()
        if data.is_active is not None:
            claim.is_active = data.is_active
        claim.save()
        return {'ok': True}
    except:
        raise HttpError(400, 'Bad Request')


@router.delete('/claim/{id}')
def delete_claim(request, id: int):
    try:
        claim = Claim.objects.get(id=id)
        claim.delete()
        return {'ok': True} 
    except:
        raise HttpError(400, 'Bad Request')


