import streamlit as st
import joblib

# Функция для загрузки srt субтитров и вывода их уровня
def process_subtitles(subtitles):
    # Загрузка обученной модели
    model = joblib.load("linear_svc_model.joblib")

    # Обработка субтитров и предсказание уровня английского языка
    result = model.predict(subtitles)

    # Возвращаем результат
    return result

# Основной код Streamlit
def main():
    st.title("Распознавание уровня английского языка в субтитрах")

    # Загрузка файла с субтитрами
    uploaded_file = st.file_uploader("Выберите файл с субтитрами (.srt)", type="srt")

    if uploaded_file is not None:
        # Чтение содержимого файла
        content = uploaded_file.read()

        # Передача содержимого субтитров в функцию обработки
        result = process_subtitles(content)

        # Вывод результата
        st.header("Результат")
        st.write(result)
        
        # Кнопка для очистки результатов
        if st.button("Очистить"):
            result = None

# Запуск приложения
if __name__ == "__main__":
    main()
