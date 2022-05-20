import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentimental_ru",
    page_icon="🤗",
)

classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

text = st.text_area(
            "Введите ваш текст здесь (максимум 500 слов)",
            height=510,
        )
MAX_WORDS = 500
import re

res = len(re.findall(r"\w+", text))
if res > MAX_WORDS:
    st.warning(
        "⚠️ Ваш текст содержит "
        + str(res)
        + " слов."
        + " толькое первые 500 слов будут проанализированы. Следите за новостями, скоро лимит будет увеличен! 😊"
    )

    text = text[:MAX_WORDS]

classifier(text)
