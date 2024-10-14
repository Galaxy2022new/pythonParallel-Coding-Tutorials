import celeryAddTask

if __name__ == "__main__":
    result = celeryAddTask.add.delay(5, 5)
