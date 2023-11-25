def mergeSort(data):
    """
    Performs merge sort with
        O(n*log(n)) time complexity
        O(n) space complexity
    """
    size = len(data)
    middle = size // 2
    if middle == 0:
        return data
    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])

    result = [None] * size
    lsize = len(left)
    rsize = size - lsize
    
    rc = i = 0
    for lc in range(lsize):
        while rc < rsize and left[lc] > right[rc]:
            result[i] = right[rc]
            rc += 1
            i += 1
        result[i] = left[lc]
        i += 1
    for k in range(rc, rsize):
        result[i] = right[k]
        i += 1
    return result


def fastSort(data):
    """
    Runs fast sort at
        O(n*log(n)) time complexity
        O(log(n)) space complexity
    """
    size = len(data)
    if size//2 == 0:
        return data
    pivot = data[size//2]
    result = [None] * size
    left, right = [None] * size, [None] * size
    lc = rc = mc = 0
    for i in range(size):
        if data[i] < pivot:
            left[lc] = data[i]
            lc += 1
        elif data[i] > pivot:
            right[rc] = data[i]
            rc += 1
        else:
            mc += 1
    left = fastSort(left[:lc])
    right = fastSort(right[:rc])
    middle = [pivot] * mc
    return left + middle + right


def _makeHeap(data, size, k):
    largest = k
    lc, rc = 2*k+1, 2*k+2
    if lc < size and data[lc] > data[largest]:
        largest = lc
    if rc < size and data[rc] > data[largest]:
        largest = rc
    if largest != k:
        data[largest], data[k] = data[k], data[largest]
        _makeHeap(data, size, largest)

def heapSort(data):
    """
    Heap sorts data with
        O(n*log(n)) time complexity
        O(1) space complexity
    """
    size = len(data)
    for i in range(size, -1, -1):
        _makeHeap(data, size, i)

    for i in range(size-1, 0, -1):
        data[i], data[0] = data[0], data[i]
        _makeHeap(data, i, 0)
    return data
