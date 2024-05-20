from enum import Enum

class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

def handle_semaphore(light):
    match light:
        case Semaphore.RED:
            print("You must stop")
        case Semaphore.YELLOW:
            print("Light might be changed to red, be careful")
        case Semaphore.GREEN:
            print("You can continue")

handle_semaphore(Semaphore.RED)
handle_semaphore(Semaphore.YELLOW)
handle_semaphore(Semaphore.GREEN)