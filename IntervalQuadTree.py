from City import City
from Button import Button

class IntervalQuadTree:
    def __init__(self):
        self.root = None

    def add_interval(self, button: Button):
        interval = Interval(button.x-button.width/2, button.x+button.width/2, button.y-button.width/2, button.y+button.width/2)
        if self.root==None:
            self.root = Node(button, interval)
        else:
            currentNode = self.root
            while currentNode!=None:
                #x interval
                if interval.start_x>currentNode.interval.start_x and interval.start_y>currentNode.interval.start_y:
                    if currentNode.left==None:
                        currentNode.left = Node(button, interval)
                        break
                    currentNode = currentNode.left
                elif interval.start_x<currentNode.interval.start_x and interval.start_y<currentNode.interval.start_y:
                    if currentNode.right==None:
                        currentNode.right = Node(button, interval)
                        break
                    currentNode = currentNode.right
                elif interval.start_x>currentNode.interval.start_x and interval.start_y<currentNode.interval.start_y:
                    if currentNode.left_middle==None:
                        currentNode.left_middle = Node(button, interval)
                        break
                    currentNode = currentNode.left_middle
                elif interval.start_x<currentNode.interval.start_x and interval.start_y>currentNode.interval.start_y:
                    if currentNode.right_middle==None:
                        currentNode.right_middle = Node(button, interval)
                        break
                    currentNode = currentNode.right_middle

                    
    def search_interval(self, x, y):
        if self.root==None:
            raise Exception("Empty quad tree. Please add a node before querying")
        else:
            currentNode = self.root
            while currentNode!=None:
                if currentNode.interval.start_x<=x<=currentNode.interval.end_x  and currentNode.interval.start_y<=y<=currentNode.interval.end_y:
                    return currentNode.button
                elif x>currentNode.interval.end_x and y>currentNode.interval.end_y:
                    currentNode = currentNode.left
                elif x>currentNode.interval.end_x and y<currentNode.interval.end_y:
                    currentNode = currentNode.left_middle
                elif x<currentNode.interval.end_x and y>currentNode.interval.end_y:
                    currentNode = currentNode.right_middle
                elif x<currentNode.interval.end_x and y<currentNode.interval.end_y:
                    currentNode = currentNode.right
            return -1

class Interval:
    def __init__(self, start_x, end_x, start_y, end_y):
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

        
class Node:
    def __init__(self, button, interval):
        self.left = None
        self.left_middle = None
        self.right_middle = None
        self.right = None
        self.button = button
        self.interval = interval
