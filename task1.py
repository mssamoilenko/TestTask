import logging

logging.basicConfig(
    filename='pythagoras.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8')

def main(numbers):
    try:
        numb_list = [int(x) for x in numbers.split()]
        if len(numb_list) != 3:
            raise ValueError("You must enter exactly 3 numbers!")

        numb_list.sort()
        a, b, c = numb_list
        result = a ** 2 + b ** 2 == c ** 2

        logging.info(f"Numbers: {numb_list}, Result: {result}")
        return result

    except ValueError as e:
        logging.error(f"Error: {e}, Entered data: '{numbers}'")
        return False
    except Exception as e:
        logging.error(f"Unknown error: {e}, Entered data: '{numbers}'")
        return False

test_cases = [
    "3 4 5",  # True
    "5 12 13",  # True
    "1 2 3",  # False
    "3 4",    # Помилка
    "a b c",  # Помилка
]

for test in test_cases:
    main(test)