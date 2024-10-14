import random
import concurrent.futures


# 顺序合并排序实现
def sequential_mergesort(arr):
    print(f"正在顺序合并排序：{arr}" if len(arr) <= 10 else f"正在顺序合并排序，数组长度：{len(arr)}")
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = sequential_mergesort(arr[:mid])
        right = sequential_mergesort(arr[mid:])
        return merge(left, right)


# 合并两个已排序的数组
def merge(left, right):
    print(f"正在合并：左侧数组 {left}，右侧数组 {right}" if len(left) + len(
        right) <= 20 else f"正在合并，左侧数组长度：{len(left)}，右侧数组长度：{len(right)}")
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# 并行合并排序实现
def parallel_mergesort(arr):
    print(f"开始并行合并排序，数组长度：{len(arr)}")
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # 异步提交排序任务，但这里不打印Future对象，因为它不是数组本身
            left_future = executor.submit(sequential_mergesort, arr[:mid])
            right_future = executor.submit(sequential_mergesort, arr[mid:])

            # 等待排序完成并打印结果
            left = left_future.result()
            right = right_future.result()
            print(f"并行排序得到的左半部分：{left}，右半部分：{right}")

        return merge(left, right)


# 主程序入口
if __name__ == '__main__':
    random.seed(0)
    arr = [random.randint(0, 100) for _ in range(1000)]
    sorted_arr = parallel_mergesort(arr)
    print(f"排序完成，结果的前10个元素：{sorted_arr[:10]}")
