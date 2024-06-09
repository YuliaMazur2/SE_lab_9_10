import pytest
from lab9 import filter_by_age_category, calculate_survival_rates

def test_filter_by_age_category():
    data = [
        {'Age': 25, 'Survived': '1'},
        {'Age': 35, 'Survived': '0'},
        {'Age': 65, 'Survived': '1'},
    ]
    yound = filter_by_age_category(data, 'Молодой до 30 лет')
    middle_aged = filter_by_age_category(data, 'Среднего возраста от 30 до 60')
    old = filter_by_age_category(data, 'Старый старше 60')

    assert len(yound) == 1
    assert len(middle_aged) == 1
    assert len(old) == 1
    assert yound[0]['Age'] == 25
    assert middle_aged[0]['Age'] == 35
    assert old[0]['Age'] == 65

def test_calculate_survival_rates():
    data = [
        {'Age': 25, 'Survived': '1'},
        {'Age': 35, 'Survived': '0'},
        {'Age': 25, 'Survived': '0'},
        {'Age': 35, 'Survived': '1'},
    ]
    survived_rate, deceased_rate = calculate_survival_rates(data)

    assert survived_rate == 0.5
    assert deceased_rate == 0.5

def test_emply_data():
    data = []
    survived_rate, deceased_rate = calculate_survival_rates(data)
    assert survived_rate == 0.0
    assert deceased_rate == 0.0

def test_no_passengers_in_category():
    data = [
        {'Age': 25, 'Survived': '1'},
        {'Age': 25, 'Survived': '0'},
        {'Age': 25, 'Survived': '1'},
    ]
    filtered_data = filter_by_age_category(data, 'Старый старше 60')
    assert len(filtered_data) == 0
    survived_rate, deceased_rate = calculate_survival_rates(filtered_data)
    assert survived_rate == 0.0
    assert deceased_rate == 0.0

if __name__ == '__main__':
    pytest.main()