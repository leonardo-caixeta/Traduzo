import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    histories = json.loads(HistoryModel.list_as_json())
    history = histories[0]

    assert history["text_to_translate"] == "Hello, I like videogame"
    assert history["translate_from"] == "en"
    assert history["translate_to"] == "pt"
