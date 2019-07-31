from sanic import Blueprint
from sanic.response import json
from sanic.views import HTTPMethodView

from db import objects, models_to_dict
from models import ArticleType

bp = Blueprint('article_type_bp')


class ArticleTypeViews(HTTPMethodView):
    """ 文章类型 """
    @staticmethod
    async def get(request):
        article_types = await objects.execute(
            ArticleType.select()
        )
        return json(models_to_dict(article_types))

    @staticmethod
    async def post(request):
        params = request.json
        await objects.create(ArticleType, **params)
        return json({'status': 'success'})


class ArticleViews(HTTPMethodView):
    """ 文章 """
    async def get(self, request):
        pass


bp.add_route(ArticleTypeViews.as_view(), "/article-type")

