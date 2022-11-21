"""
This is a custom module for using basic list functions
"""

# Importing important libraries
from _collections_abc import Iterable
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

    # Defining the append function as myappend
    def append(self, x):
        """
        Add an item to the end of the list.
        """
        try: 
            self.l = self.l + [x]
            logging.info("Append function succeeded.")
        except Exception as e:
            logging.exception(f"Append function failed. Error Code: {e}")
            raise e

    def extend(self, x):
        """
        Extend the list by appending all the items from the iterable. 
        Equivalent to a[len(a):] = iterable.    
        """
        try:
            if isinstance(x, Iterable):
                for i in x:
                    self.l = self.l + [i]
                    logging.info(f"Extend function succeeded. Appended {i}")
            elif type(x) == dict:
                for i in x.keys():
                    self.l = self.l + [i]
                    logging.info(f"Extend function succeeded. Appended {i}")
        except Exception as e:
            logging.exception(f"Extend function failed. Error Code: {e}")
            raise e

    def insert(self, i, x):
        """
        Insert an item at a given position. 
        The first argument is the index of the element before which to insert, 
        so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).    
        """
        i = int(i)

        try:
            if i == 0:
                self.l = [x] + self.l
                logging.info(f"{x} inserted at Index 0")
            elif i >= len(self.l) - 1:
                self.l = self.l + [x]
                logging.info(f"{x} inserted at Index {len(self.l) - 1}")
            
            # Required to add code for negative indices
            
            # elif i < 0:
            #     j = i
            #     i = len(self.l) - i
            #     self.l = self.l[:i] + [x] + self.l[i:]
            #     logging.info(f"{x} inserted at Index {j}")
            else:    
                self.l = self.l[:i] + [x] + self.l[i:]
                logging.info(f"{x} inserted at Index {i}")
        except Exception as e:
            logging.exception(f"Exception encountered. Exception: {e}")
            raise e

    def remove(self, x):
        """
        Remove the first item from the list whose value is equal to x. 
        It raises a ValueError if there is no such item.    
        """
        try:
            for i in range(len(self.l)):
                if self.l[i] == x:
                    self.l = self.l[:i] + self.l[i+1:]
                    logging.info(f"Successfully removed {x}")
                    break
        except ValueError:
            raise (f"ValueError: {x} not found in list")
            logging.error(f"{x} not found in list")
        except Exception as e:
            raise e
            logging.exception(f"Encountered Exception: {e}")

    def pop(self, i):
        """
        Remove the item at the given position in the list, and return it. 
        If no index is specified, a.pop() removes and returns the last item in the list.   
        """
        try:
            x = self.l[i]
            self.l = self.l[:i] + self.l[i+1:]
            logging.info(f"Successfully popped element at {i}th position")
            print(x)
            return x                
        except IndexError:
            raise f"IndexError: {i} out of index"
            logging.error(f"{i} greater than length of self")
        except Exception as e:
            raise e
            logging.exception(f"Encountered Exception: {e}")
                
    def clear(self):
        """
        Remove all items from the list. Equivalent to del a[:].
        """
        try:
            self.l = list()
            logging.info(f"Successfully cleared the list")
        except Exception as e:
            logging.exception(f"Encountered Exception as {e}")
            raise e

    def index(self, x):
        """
        Return zero-based index in the list of the first item whose value is equal to x. 
        Raises a ValueError if there is no such item.
        """
        try:
            if x in self.l:
                for i in len(range(self.l)):
                    if self.l[i] == x:
                        logging.info(f"Found {x} in list at index {i}")
                        return i
            else:
                logging.error(f"Value Error: {x} not found in list")
                raise ValueError (f"{x} not found in list")
        except Exception as e:
            logging.exception(f"Encountered error as {e}")

    def count(self, x):
        """
        Return the number of times x appears in the list.    
        """
        
        try: 
            if x in self.l:
                logging.info(f"{x} found in accessed list")
                i = 0
                for ele in self.l:
                    if ele == x:
                        i += 1
                logging.info(f"Found {i} instances of {x} in accessed list")
                return i            
            else:
                logging.error(f"{x} not present in accessed list")
                raise ValueError (f"{x} not in accessed list")
        except Exception as e:
            logging.exception (f"Encountered error as {e}")

    def sort(self, reverse=False):
        """
        Sort the items of the list in place.
        """
        # Check if type of all elements is either float or int
        # if yes, then go ahead and compare and sort
        # if not, then check if all elements are of type  str
        # if yes, then go ahead and compare and sort
        # if not, then raise typerror as cannot compare between numeric and non-numeric types
              
        flag = True
        if type(self.l[0]) in [int, float]:
            for element in self.l:
                if type(element) not in [float, int]:
                    flag = False
                    break
        elif type(self.l[0]) == str:
            for element in self.l:
                if type(element) != str:
                    flag = False
                    break
        else:
            flag = False
        
        if flag == False:
            logging.info("Elements of non-comparable type encountered.")
            raise TypeError
        else:
            try:
                for i in range(len(self.l)):
                    for j in range(i+1, len(self.l)):
                        if self.l[j] < self.l[i]:
                            temp = self.l[i]
                            self.l[i] = self.l[j]
                            self.l[j] = temp                            
                logging.info("List sorted in ascending order.")
            except Exception as e:
                logging.exception(f"Exception encountered: {e}")
                raise Exception

        # If reverse = True then reverse the current list

        if reverse == True:
            self.l[::-1]

    def reverse(self):
        """
        Reverse the elements of the list in place.
        """
        self.l = self.l[::-1]
    
    def copy(self):
        """
        Return a shallow copy of the list. Equivalent to a[:].    
        """
        return self.l[:]
        
        
