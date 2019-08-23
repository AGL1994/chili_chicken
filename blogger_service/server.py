from sanic import Sanic

from blogger_service import views, SERVICE_NAME

app = Sanic(SERVICE_NAME)
app.blueprint(views.blogger.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
