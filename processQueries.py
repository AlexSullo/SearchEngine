import os
import WebPageIndex

"""returns a list of all the text files"""


def read_files(file):
    file_list = []
    for j in file:
        t1 = WebPageIndex.WebPageIndex(j)
        file_list.append(t1)
    return file_list


"""
creates a heap for every file in the directory
"""
if __name__ == "__main__":
    list = []
    path = os.getcwd()
    bruh = os.listdir(path)
    for file in bruh:
        if "doc" in file:
            list.append(file)
        elif "queries" in file:
            new_var = file
    quer = open(new_var, "r").read().split("\n")
    indices = read_files(list)
    for q in quer:
        WebPageIndex.WebpagePriorityQueue(q, indices)
