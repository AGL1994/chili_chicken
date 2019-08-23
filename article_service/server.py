from sanic import Sanic

from article_service import views

app = Sanic()
app.blueprint(views.article.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
