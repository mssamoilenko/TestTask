import logging
from datetime import datetime, timedelta
from typing import List

logging.basicConfig(
    filename='work_schedule.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

logger = logging.getLogger(__name__)

def generate_schedule(days: int, work_days: int, rest_days: int, start_date: datetime):
    logger.info("Початок генерації розкладу")
    try:
        if days <= 0 or work_days <= 0 or rest_days < 0:
            raise ValueError("Некоректні параметри: days > 0, work_days > 0, rest_days >= 0")

        schedule = []
        current_date = start_date

        while len(schedule) < days:
            for _ in range(work_days):
                if len(schedule) < days:
                    schedule.append(current_date)
                    logger.info(f"Додано робочий день: {current_date}")
                current_date += timedelta(days=1)
            current_date += timedelta(days=rest_days)
            logger.info(f"Пропущено {rest_days} днів відпочинку")

        logger.info("Генерація завершена успішно")
        return schedule

    except Exception as e:
        logger.error(f"Помилка: {e}")
        return []

def test_schedule():
    logger.info("Початок тестування")

    days = 5
    work_days = 2
    rest_days = 1
    start_date = datetime(2020, 1, 30)

    expected = [
        datetime(2020, 1, 30, 0, 0),
        datetime(2020, 1, 31, 0, 0),
        datetime(2020, 2, 2, 0, 0),
        datetime(2020, 2, 3, 0, 0),
        datetime(2020, 2, 5, 0, 0)
    ]

    result = generate_schedule(days, work_days, rest_days, start_date)

    if result == expected:
        logger.info("Тест пройдений успішно: True")
        return True
    else:
        logger.error(f"Тест не пройдений: False")
        logger.error(f"Очікувано: {expected}")
        logger.error(f"Отримано: {result}")
        return False

if __name__ == "__main__":
    test_schedule()