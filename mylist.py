"""
This is a custom module for using basic list functions
"""

# Importing important libraries
import logging
logging.basicConfig(filename="list.log", level=logging.DEBUG, \
                    format='%(asctime)s %(levelname)s %(message)s')

class listfunctions:

    def __init__(self, l: list):
        try:
            if type(l) == list:
                self.l = l
                logging.info("Initialization succeeded.")
            else:
                logging.error(f"""Incorrect input type. Expected input is a list.
                                 Input received is of type {type(l)}""")
        except Exception as e:
            logging.error("Error Code: ", e)
            raise e

    def __str__(self):
        return self.l

    # Defining the append function as myappend
    def myappend(self, x):
        """
        Add an item to the end of the list.
        """
        try: 
            self.l = self.l + [x]
            logging.info("Append function succeeded.")
        except Exception as e:
            logging.exception(f"Append function failed. Error Code: {e}")
            raise e
        return self.l

        # Unable to get the list as a result. Producing class as an output.

    def myextend(self, x: list):
        """
        Extend the list by appending all the items from the iterable. 
        Equivalent to a[len(a):] = iterable.    
        """
        try:
            self.l = self.l + x
            logging.info("Extend function succeeded.")
        except Exception as e:
            logging.exception(f"Extend function failed. Error Code: {e}")
            raise e
        return self.l

    def myinsert(i, x):
        """
        Insert an item at a given position. 
        The first argument is the index of the element before which to insert, 
        so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).    
        """
        try:
            if x == 0:
                self.l = [i] + self.l
                logging.info(f"{i} inserted at Index 0")
            elif x >= len(self.l):
                self.l = self.l + [i]
                logging.info(f"{i} inserted at Index {len(self.l) - 1}")
            else:    
                self.l = self.l[:i] + [i] + self.l[i+1:]
                logging.info(f"{i} inserted at Index {x}")
        except Exception as e:
            logging.exception(f"Exception encountered. Exception: {e}")
            raise e
        return self.l

    def myremove(x):
        """
        Remove the first item from the list whose value is equal to x. 
        It raises a ValueError if there is no such item.    
        """
        return 1

    def mypop(i):
        """
        Remove the item at the given position in the list, and return it. 
        If no index is specified, a.pop() removes and returns the last item in the list.   
        """
        return 1

    def myclear():
        """
        Remove all items from the list. Equivalent to del a[:].
        """
        return 1

    def myindex(x):
        """
        Return zero-based index in the list of the first item whose value is equal to x. 
        Raises a ValueError if there is no such item.
        """
        return 1

    def mycount(x):
        """
        Return the number of times x appears in the list.    
        """
        return 1

    def mysort(*, key=None, reverse=False):
        """
        Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
        """
        return 1

    def myreverse():
        """
        Reverse the elements of the list in place.
        """
        return 1

    def mycopy():
        """
        Return a shallow copy of the list. Equivalent to a[:].    
        """
        return 1
