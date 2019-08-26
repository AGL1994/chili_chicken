from sanic import Sanic

from blogger_service import views, SERVICE_NAME

app = Sanic(SERVICE_NAME)
print(views.blogger.bp.routes)
app.blueprint(views.blogger.bp)
print(app.router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
    # app.run(host='0.0.0.0', port=8002, workers=4, debug=False, access_log=False)
