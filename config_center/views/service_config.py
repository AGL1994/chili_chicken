from sanic import Blueprint
from sanic.response import json

from config_center import config

bp = Blueprint('config-center', url_prefix='/config-center')


@bp.route('/<config_name:string>/<service:string>')
async def get_config(request, config_name, service):
    if hasattr(config, config_name):
        this = getattr(config, config_name)
        if service in this:
            return json(this.get(service))
    return json({})
