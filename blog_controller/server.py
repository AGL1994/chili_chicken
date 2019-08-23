from sanic import Sanic

from views.article import bp as article_bp

app = Sanic()
app.blueprint(article_bp)
# app.blueprint(news_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
