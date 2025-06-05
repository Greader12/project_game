from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        # Если ошибка известная (HTTPException) — возьмем код ошибки
        code = 500
        if isinstance(e, HTTPException):
            code = e.code

        response = {
            "error": str(e),
            "status_code": code
        }
        return jsonify(response), code
