import random
class NumList(object):
    def __init__(self, list_length=None):
        # type: (int) -> None
        self._len = 0      # type: int
        self._nums = []    # type: List[int]
        self._odds = []    # type: List[int]
        self._evens = []   # type: List[int]
        if not (list_length is None):
            try:
                if list_length < 0:
                    raise ValueError('The length of the number list must be greater than zero')
                i = 0              # type: int
                n = 0              # type: int
                for i in range(list_length):
                    n = random.randint(1,99)
                    self._nums.append(n)
                    if n % 2:
                        self._odds.append(n)
                    else:
                        self._evens.append(n)
                self._len = len(self._nums)
            except:
                print('Something went wrong when initialising your number list')
    def __str__(self):
        # type: (None) -> str
        return (f'The number list is:\n    {self._nums}\n\n'
                f'Which contains odd numbers:\n    {self._odds}\n\n'
                f'...and even numbers:\n    {self._evens}')
    @property
    def length(self):
        # type: (None) -> int
        return self._len 
    @property
    def number_list(self):
        # type: (None) -> List[int]
        return self._nums
    @number_list.setter
    def number_list(self, new_num_list):
        # type: (List[int] -> None)
        n = 0                       # type: int
        nums_backup = self._nums    # type: List[int]
        len_backup = self._len      # type: int
        odds_backup = self._odds    # type: List[int]
        evens_backup = self._evens  # type: List[int]
        try:
            for n in new_num_list:
                if not (1 <= n <= 99):
                    raise ValueError('Integer value in number list is not in range 1 to 99')
            self._nums = new_num_list
            self._len = len(self._nums)
            self._odds = []
            self._evens = []
            for n in self._nums:
                if n % 2:
                    self._evens.append(n)
                else:
                    self._odds.append(n)
        except:
            self._nums  = nums_backup
            self._len   = len_backup
            self._odds  = odds_backup
            self._evens = evens_backup
            print('We didn\'t like your number list so we did nothing!')
    @property
    def odds_list(self):
        # type: (None) -> int
        return self._odds
    @property
    def evens_list(self):
        # type: (None) -> int
        return self._evens
if __name__ == '__main__':
    # Instantiate a new NumList object
    # Specify optional argument list_length will cause
    # object to be initialised with a list of random
    # integers with the number of integers in the list
    # being list_length
    # If list_length is omitted, then the new object
    # will just initialise with an empty list
    print('Random list of length 10...\n')
    nums = NumList(10)
    print(nums)
    # The number_list property can be assigned
    # a new list overwriting whatever was
    # there before
    print('--------------------------------------------------\nAssigned list of numbers 1 to 5...\n')
    nums.number_list = [1,2,3,4,5]
    print(nums)
    # Errors are handled
    print('--------------------------------------------------\nThe list contains a non-integer!...\n')
    nums.number_list = ['a string should not be here']
    print(nums)