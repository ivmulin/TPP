class Sortirovka:
    def Insertion(array):
        if len(array) < 2:
            return array
        for i in range(0, len(array)):
            a = array[i]
            j = i-1
            while j >= 0 and array[j] > a:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = a
        return array

    def Selection(array):
        if len(array) < 2:
            return array
        L = len(array)
        for i in range(0, L-1):
            m = array[i]
            mi = i
            for j in range(i+1, L):
                if array[j] < m:
                    m = array[j]
                    mi = j
            _ = array[i]
            array[i] = array[mi]
            array[mi] = _
        return array

    def Bubble(array):
        if len(array) < 2:
            return array
        L = len(array)
        for i in range(L-1):
            for j in range(0, L-i-1):
                if array[j] > array[j+1]:
                    _ = array[j]
                    array[j] = array[j+1]
                    array[j+1] = _
        return array
