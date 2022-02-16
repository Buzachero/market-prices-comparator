import time


def get_now_time():
    tuple_time = time.localtime()
    return time.strftime("%d-%m-%Y_%H-%M-%S", tuple_time)