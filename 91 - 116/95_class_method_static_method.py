class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def utility_message():
        print("This is a utility message.")

Counter.increment()
Counter.utility_message()
print("Count:", Counter.count)