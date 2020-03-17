import time
import timeit
import logging
import getpass
from functools import wraps
from random import randint


def congif_logger():
    logger = logging.getLogger("decorator.log")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("machine.log", mode="w")
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)


# Creating my logger
congif_logger()


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("decorator.log")

        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        end_time = timeit.default_timer()

        exec_time = end_time - start_time
        if exec_time > 1.0:
            exec_str = f"{exec_time:.3f} s "
        else:
            exec_str = f"{exec_time * 1000:.3f} ms"

        logger.info(f"({getpass.getuser()})Running: {func.__name__.replace('_', ' ').title():19s} [ exec-time = {exec_str} ]")
        return value

    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
