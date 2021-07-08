from ninja import NinjaAPI
from users.api import router as users_router

VERSION = '0.0.1'
DESCRIPTION = 'Documentação das rotas'

api = NinjaAPI(title='API Luiz', version=VERSION, description=DESCRIPTION)
api.add_router('/', users_router, tags=['Users'])

