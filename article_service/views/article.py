from sanic import Blueprint
from sanic.response import json

from article_service import interface

bp = Blueprint(__name__)
article_interface = interface.ArticleClient()


@bp.route('/article')
async def test(request):
    json_params = {'f': 'ff'}
    result = await article_interface.get_blogger_list(json=json_params)
    print(result)
    return json({'data': result['result']})

