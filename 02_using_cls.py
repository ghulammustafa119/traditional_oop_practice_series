# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.




class Counter:
    count = 0
    def __init__(self):
       Counter.count += 1
    @classmethod
    def display_count(cls):
        print("Total objects created: ", cls.count)
c1 = Counter()      
c2 = Counter()      
c3 = Counter()      
c4 = Counter()      
c5 = Counter()      
c6 = Counter()  
Counter.display_count()    