from .responses import response
from flask import Blueprint

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")




@api_v1.route('/tasks', methods=["GET"])
def get_tasks():
    return response({
        "mensaje" : "nuevo mensaje"
    })


@api_v1.route('/tasks/<int:id>', methods=["GET"])
def get_task():
    pass


@api_v1.route('/tasks', methods=["POST"])
def create_task():
    pass


@api_v1.route('/tasks/<int:id>', methods=["PUT"])
def update_task():
    pass


@api_v1.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task():
    pass




