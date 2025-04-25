from celery import shared_task
import random

@shared_task
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x,y):
    total=x*(y* random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total