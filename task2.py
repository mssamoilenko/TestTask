import logging

logging.basicConfig(
    filename='pythagoras2.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8')

logger = logging.getLogger(__name__)

def game(plant_input, zombi_input):

    try:
        logger.info("Початок обробки вхідних даних")

        if not plant_input or not zombi_input:
            raise ValueError("Вхідні дані не можуть бути пустими")

        plants = list(map(int, plant_input.split()))
        zombies = list(map(int, zombi_input.split()))

        logger.info(f"Початковий список рослин: {plants}")
        logger.info(f"Початковий список зомбі: {zombies}")

        plant_power = sum(plants)
        zombi_power = sum(zombies)

        plant_survivors = 0
        zombi_survivors = 0

        for i in range(max(len(plants), len(zombies))):
            plant = plants[i] if i < len(plants) else None
            zombi = zombies[i] if i < len(zombies) else None

            if plant is not None and zombi is not None:
                if plant > zombi:
                    plant_survivors += 1
                elif zombi > plant:
                    zombi_survivors += 1

            elif plant is not None:
                plant_survivors += 1
            elif zombi is not None:
                zombi_survivors += 1

        logger.info(f"Рослин вижило: {plant_survivors}")
        logger.info(f"Зомбі вижило: {zombi_survivors}")
        logger.info(f"Початкова сила рослин: {plant_power}")
        logger.info(f"Початкова сила зомбі: {zombi_power}")

        if plant_survivors > zombi_survivors:
            logger.info("Перемога рослин (більше вижило)")
            return True
        elif zombi_survivors > plant_survivors:
            logger.info("Перемога зомбі (більше вижило)")
            return False
        else:
            logger.info("Нічия - перевірка сили")
            return plant_power >= zombi_power

    except Exception as e:
        logger.error(f"Сталася помилка: {str(e)}")
        return False


test_cases = [
    ("2 4 6 8", "1 3 5 7", True),
    ("2 4", "1 3 5 7", False),
    ("2 4 0 8", "1 3 5 7", True),
    ("1 2 1 1", "2 1 1 1", True)
]

for i, (plants, zombies, expected) in enumerate(test_cases, 1):
    try:
        logger.info(f"\n=== Тест {i} ===")
        logger.info(f"Рослини: {plants}")
        logger.info(f"Зомбі: {zombies}")
        logger.info(f"Очікуваний результат: {expected}")

        result = game(plants, zombies)
        logger.info(f"Отриманий результат: {result}")

        if result == expected:
            logger.info("Тест пройдений")
        else:
            logger.error("Тест не пройдений")
    except Exception as e:
        logger.error(f"Помилка під час виконання тесту {i}: {str(e)}")