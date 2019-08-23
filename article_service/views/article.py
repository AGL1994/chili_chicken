from sanic import Blueprint
from sanic.response import json

from article_service import interface
from chili.gateway import get, post

bp = Blueprint(__name__)
article_interface = interface.ArticleClient()


@bp.route('/article')
async def test(request):
    params = {'f': 'ff'}
    result = await article_interface.get_blogger_list(json=params)
    print(result)
    return json({'data': result['result']})
