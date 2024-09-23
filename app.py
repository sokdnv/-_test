import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency
from funcs import histplots

file = st.file_uploader(label='Закинь сюда файл для обработки', type='csv')


def my_test(first: pd.Series, second: pd.Series) -> None:
    """Функция для проведения теста"""
    cross_table = pd.crosstab(first, second)
    _, p, _, _ = chi2_contingency(cross_table)

    if p < 0.05:
        st.write('H1 взлетела')
    else:
        st.write('H1 не взлетела')


if file:
    df = pd.read_csv(file, encoding='windows-1251')

    if df is not None:
        st.write('Распределение признаков')
        st.pyplot(histplots(df))

        with st.form(key='params'):
            days = st.number_input(label='Day input', min_value=0,
                                   max_value=df['Количество больничных дней'].max(), value=2)
            age = st.number_input(label='Age input', min_value=df['Возраст'].min(),
                                  max_value=df['Возраст'].max(), value=35)
            button = st.form_submit_button(label='Запустить тест')

        if button:
            cols = st.columns(2)

            with cols[0]:
                st.subheader('Гипотеза 1')
                df['Прогульщики'] = df['Количество больничных дней'] > days
                my_test(first=df['Пол'], second=df['Прогульщики'])

            with cols[1]:
                st.subheader('Гипотеза 2')
                df['старше_возраста'] = df['Возраст'] > age
                my_test(first=df['старше_возраста'], second=df['Прогульщики'])
