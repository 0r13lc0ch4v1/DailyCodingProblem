"""Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""

import time


class Scheduler:
    def __init__(self):
        self._tasks_queue = []

    def add_task(self, task, params, delay):
        self._tasks_queue.append((task, params, time.time() + delay))

    def execute_tasks(self):
        self._tasks_queue = sorted(self._tasks_queue, key=lambda x: x[2])
        while self._tasks_queue:
            task, args, exe_time = self._tasks_queue.pop(0)
            try:
                time.sleep(exe_time - time.time())
            except ValueError:
                pass
            task(*args)


def print_time(sec, start_time):
    print('{} Started at {}'.format(sec, time.asctime(time.localtime(start_time))))
    print('{} Finished at {}'.format(sec, time.asctime(time.localtime(time.time()))))


scheduler = Scheduler()
scheduler.add_task(print_time, ('5 sec', time.time()), 5)
scheduler.add_task(print_time, ('2 sec', time.time()), 2)
scheduler.add_task(print_time, ('1 sec', time.time()), 1)
scheduler.execute_tasks()
