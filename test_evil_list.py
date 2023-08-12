import time
from evil_list import EvilList


class TestEvilList:
    @staticmethod
    def compare_with_builtin_list(size):
        # Testing with EvilList
        evil_list = EvilList()
        start_time = time.time()
        for i in range(size):
            evil_list.put(i)
        el_time = time.time() - start_time

        # Testing with built-in list
        built_in_list = []
        start_time = time.perf_counter()
        for i in range(size):
            built_in_list.append(i)
        bl_time = time.perf_counter() - start_time

        print(f"EvilList time: {el_time:.5f} seconds")
        print(f"Built-in list time: {bl_time:.5f} seconds")


if __name__ == "__main__":
    TestEvilList.compare_with_builtin_list(1000)
