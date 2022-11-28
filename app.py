from flask import Flask
from flask_cors import CORS
from waitress import serve
from decouple import config
from Routes import ClienteRoutes, MesaRoutes, SolicitudRoutes, ReservaRoutes

app = Flask(__name__)
cors = CORS(app)

def pageNotFound(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    print("Server running: "+"http://"+config('URL_BACKEND')+":"+config('PORT'))
    app.register_blueprint(ClienteRoutes.main, url_prefix='/api/clientes')
    app.register_blueprint(MesaRoutes.main, url_prefix='/api/mesas')
    app.register_blueprint(SolicitudRoutes.main, url_prefix='/api/solicitudes')
    app.register_blueprint(ReservaRoutes.main, url_prefix='/api/reservas')
    app.register_error_handler(404, pageNotFound)
    serve(app, host = config('URL_BACKEND'), port = config('PORT'))