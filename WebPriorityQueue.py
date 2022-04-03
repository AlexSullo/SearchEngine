import WebPageIndex


class WebpagePriorityQueue:
    def __init__(self, file):
        counter = 0
        n_file = open(file, "r")
        text = n_file.read().lower()
        character = text
        for element in text:
            if element == '.' or element == ',' or element == '(' or element == ')' or element == ':' or element == '/' \
                    or element == '-':
                character = character.replace(element, " ")
        self.end_list = character.split()
        for i in range(0, len(self.end_list)):
            for j in range(0, len(WebPageIndex.d1)):
                counter += 1