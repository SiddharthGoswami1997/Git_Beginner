# def mygen(n):
#     for i in range(n):
#         yield i

# print(mygen(5))
# a = mygen(5)
# print(a)
# for i in a:
#     print(i)
# b = mygen(6)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
#
#
# def mycoroutine():
#     received = yield
#     print(f"i have recieved {received}")
#     received = yield
#     print(f"i have recieved {received}")
#
#
# a = mycoroutine()
# next(a)
# a.send("Tanisha")
# a.send("Nisha")

# import time
#
# def func():
#     time.sleep(2)
#     return "Happy"
#
# print(func())

# import asyncio
# async def func():
#     await asyncio.sleep(2)
#     return "Very Happy"
#
# async def main():
#     result = await func()
#     print(result)
#
# asyncio.run(main())

# import asyncio
#
# async def greet():
#     await asyncio.sleep(2)  # Doesn't block other tasks
#     print("Hello!")
#
# async def main():
#     await greet()
#     print("Done")
#
# asyncio.run(main())

# import asyncio
#
# async def greet(name, delay):
#     await asyncio.sleep(delay)
#     print(f"Hello {name} after {delay} seconds")
#
# async def main():
#     await asyncio.gather(
#         greet("Alice", 2),
#         greet("Bob", 1),
#         greet("Charlie", 3)
#     )
#
# asyncio.run(main())

# with open("file3.txt", "w") as f:
#     f.write("Hello, woiuytresdfgnorld!")
#     f.flush()  # Forces the data to be written to disk immediately

class Mydescripter:
    def __get__(self, instance, owner):
        return instance._name.upper()
    def __set__(self, instance, value):
        instance._name = value

class Person:
    name = Mydescripter()
    def __init__(self, name):
        self.name = name

P = Person("tnaisha")
print(P.name)