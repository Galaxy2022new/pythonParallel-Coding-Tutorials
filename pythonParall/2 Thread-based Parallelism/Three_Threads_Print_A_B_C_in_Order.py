from threading import Thread, Condition

condition = Condition()
current = "A"
count = 0


class ThreadA(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "A":
                    condition.wait()
                print("A\t", end="")
                current = "B"
                condition.notify_all()


class ThreadB(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "B":
                    condition.wait()
                print("B\t", end="")
                current = "C"
                condition.notify_all()


class ThreadC(Thread):
    def run(self):
        global current, count
        for _ in range(10):
            with condition:
                while current != "C":
                    condition.wait()
                print("C")
                count += 1
                print("team {} is finish".format(count))
                current = "A"
                condition.notify_all()


a = ThreadA()
b = ThreadB()
c = ThreadC()

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()
