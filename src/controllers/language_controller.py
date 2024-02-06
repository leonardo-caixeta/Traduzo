from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from src.models.history_model import HistoryModel

from src.models.language_model import LanguageModel

language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET", "POST"])
def translate():
    all_languages = LanguageModel.list_dicts()
    if request.method == "POST":
        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")
        HistoryModel({
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }).save()
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)
        return render_template(
            "index.html",
            languages=all_languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )
    return render_template(
        "index.html",
        languages=all_languages,
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?",
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    all_languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)
    return render_template(
        "index.html",
        languages=all_languages,
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
