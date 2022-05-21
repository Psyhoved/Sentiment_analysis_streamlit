import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Sentimental_ru",
    page_icon="😎",
)
with st.spinner('Загрузка модели анализа тональности текстов на русском языке...'):
    classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")


def get_output(text):
    label = classifier(text)[0]['label']
    score = classifier(text)[0]['score']

    if label == 'POSITIVE':
        return st.write(
            f"Данный текст имеет **положительную** эмоциональную окраску с вероятностью {round(100 * score, 2)}%")
    elif label == 'NEGATIVE':
        return st.write(
            f"Данный текст имеет **негативную** эмоциональную окраску с вероятностью {round(100 * score, 2)}%")
    else:
        return st.write(
            f"Данный текст имеет **нейтральную** эмоциональную окраску с вероятностью {round(100 * score, 2)}%")


with st.form(key="my_form"):
    text = st.text_area(
        "Введите ваш текст здесь (максимум 500 слов)",
        height=300,
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
    submit_button = st.form_submit_button(label="✨ Получить результат")
    if submit_button:
        with st.spinner('Идёт анализ текста...'):
            get_output(text)
        st.success('Готово!')

if not submit_button:
    st.stop()
