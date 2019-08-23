
from sanic import Blueprint
from sanic.response import json

from blogger_service.db import objects, models_to_dict
from blogger_service import models

bp = Blueprint(__name__)


@bp.post('/blogger')
async def get_blogger(request):
    print({"parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string, 'json': request.json})
    blogger = await objects.execute(
        models.User.select()
    )
    return json(models_to_dict(blogger))
