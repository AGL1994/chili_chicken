from sanic import Sanic

from config_center import views

app = Sanic(__name__)
app.blueprint(views.service_config.bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
    # app.run(host='0.0.0.0', port=8001, workers=4, debug=False, access_log=False)
