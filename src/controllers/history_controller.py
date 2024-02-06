from flask import Blueprint, jsonify

from src.models.history_model import HistoryModel


history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def get_history():
    return jsonify(HistoryModel.list_as_json())
