import AVLTreeMap_fix

"""
opens the file for reading reads through the file and gets rid of unwanted characters
from there we split the string so that each word is a element in array
"""


class WebPageIndex:
    def __init__(self, file):
        self.file = file
        self.path = "data/" + file
        w_file = open(file, "r")
        text1 = w_file.read().lower()
        character = text1
        for element in text1:
            if element == '.' or element == ',' or element == '(' or element == ')' or element == ':' or element == '/' \
                    or element == '-':
                character = character.replace(element, " ")
        self.new_list = character.split()

    """
    Counts the number of occurences of a specific word in the desired 
    file 
    """
    def getCount(self, s):
        counter = 0
        for i in range(0, len(self.new_list)):
            if s == self.new_list[i]:
                counter += 1
        return counter



"""
This is supposed be responsible for determining the priority of each "URL"
"""


class WebpagePriorityQueue:
    """
    this function takes the URLS and the queries
    and appends the number of occurences to array from which
    we can build a heap
    """
    def __init__(self, file2, WebPage):
        self.priority = []
        count = 0
        for i in file2:
            for j in WebPage:
                if " " in file2:
                    #for j in WebPage:
                    self.priority.append(j.getCount(i))
                else:
                    #for j in WebPage:
                    self.priority.append(j.getCount(i))
            count += 1
        WebpagePriorityQueue.buildHeap(self.priority, len(self.priority))
        WebpagePriorityQueue.printHeap(self.priority, len(self.priority))

    """
    Returns the highest priority URL or the first element in the 
    max heap.
    """
    def peek(self, web_ind):
        return web_ind[self.priority.index(self.priority[0])].file

    """
    Creates the heap
    """
    def heap(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            WebpagePriorityQueue.heap(arr, n, largest)

    """
    Pops the first index of the heap off and returns it 
    """
    def poll(self, web_ind):
        web_ind.pop(self.priority.index(self.priority[0]))
        return web_ind[self.priority.index(self.priority[0])].file

    """
    Re adds the popped element back to the heap
    """
    def re_heap(self, file3, WebPage):
        WebpagePriorityQueue.__init__(self, file3, WebPage)

    """
    builds heap and then uses print heap to display it
    """
    def buildHeap(arr, n):
        start_idx = n // 1
        for i in range(start_idx, -1, -1):
            WebpagePriorityQueue.heap(arr, n, i)

    def printHeap(arr, n):
        print("Heap:")

        for i in range(n):
            print(arr[i], end=" ")
        print()

    


if __name__ == "__main__":
    """
    Testing for the functions 
    """
    t1 = WebPageIndex("doc1-arraylist.txt")
    t2 = WebPageIndex("doc2-graph.txt")
    t3 = WebPageIndex("doc3-binarysearchtree.txt")
    t4 = WebPageIndex("doc4-stack.txt")
    t5 = WebPageIndex("doc5-queue.txt")
    t6 = WebPageIndex("doc6-AVLtree.txt")
    t7 = WebPageIndex("doc7-redblacktree.txt")
    t8 = WebPageIndex("doc8-heap.txt")
    t9 = WebPageIndex("doc9-hashtable.txt")

    print("Test for getCount:")
    print(t1.getCount("array"))
    print()
    print("test for the heap:")
    print()
    d1 = WebPageIndex("doc3-binarysearchtree.txt")
    file = open("queries (1).txt", "r")
    text = file.read().lower()
    c3 = WebpagePriorityQueue(text, [t1, t2, t3, t4, t5, t6, t7, t8, t9])
    print(c3.peek([t1, t2, t3, t4, t5, t6, t7, t8, t9]))
    print(c3.poll([t1, t2, t3, t4, t5, t6, t7, t8, t9]))
    print(c3.re_heap("array", [t1, t2, t3, t4, t5, t6, t7, t8, t9]))
    print(c3.peek([t1, t2, t3, t4, t5, t6, t7, t8, t9]))
