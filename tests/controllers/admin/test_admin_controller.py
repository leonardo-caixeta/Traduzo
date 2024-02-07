import json

from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    languages = [
        {"name": "Peter", "level": "admin", "token": "token_secreto123"},
        {"name": "Vini", "level": "admin", "token": "soeusei"},
    ]
    UserModel.drop()
    for language in languages:
        UserModel(language).save()

    history = json.loads(HistoryModel.list_as_json())
    id1 = history[0]["_id"]
    id2 = history[1]["_id"]
    app_test.delete(
        f"/admin/history/{id1}",
        headers={
            "Authorization": "token_secreto123",
            "User": "Peter",
        },
    )
    app_test.delete(
        f"/admin/history/{id2}",
        headers={
            "Authorization": "soeusei",
            "User": "Vini",
        },
    )

    assert json.loads(HistoryModel.list_as_json()) == []
