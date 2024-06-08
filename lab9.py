import csv
import streamlit as st
import matplotlib.pyplot as plt

def load_data(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Age']:
                try:
                    row['Age'] = float(row['Age'])
                    data.append(row)
                except ValueError:
                    pass
    return data

def filter_by_age_category(data, category):
    age_ranges = {
        'Молодой до 30 лет': (0, 30),
        'Среднего возраста от 30 до 60': (30, 60),
        'Старый старше 60': (60, float('inf'))
    }
    min_age, max_age = age_ranges[category]
    filtered_data = [row for row in data if min_age <= row['Age'] < max_age]
    return filtered_data

def calculate_survival_rates(data):
    total = len(data)
    survived = sum(1 for row in data if row['Survived'] == '1')
    deceased = total - survived
    survived_rate = survived / total if total > 0 else 0
    deceased_rate = deceased / total if total > 0 else 0
    return survived_rate, deceased_rate

def main():
    st.image('titanik.jpg')
    st.title('Анализ погибших и спасенных пассажиров Титаника разных возрастных категорий')

    file_path = 'data.csv'
    data = load_data(file_path)

    age_category = st.selectbox('Выберите возрастную категорию:',
                                ('Молодой до 30 лет', 'Среднего возраста от 30 до 60', 'Старый старше 60'))

    if st.button('Показать результаты'):
        filtered_data = filter_by_age_category(data, age_category)
        survived_rate, deceased_rate = calculate_survival_rates(filtered_data)

        st.write(f"Доля спасенных пассажиров ({age_category}): {survived_rate:.2%}")
        st.write(f"Доля погибших пассажиров ({age_category}): {deceased_rate:.2%}")

        labels = ['Спасенные', 'Погибшие']
        sizes = [survived_rate, deceased_rate]
        colors = ['#4CAF50', '#FF5733']
        explode = (0.1, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.axis('equal')

        st.pyplot(fig)

if __name__ == "__main__":
    main()