import collections
import itertools
import operator
from operator import itemgetter

class Permutation:
  def __init__(self, data_set):
    self.data_set = data_set

  def get_permutation(self, 
                      length, 
                      sort_column_number = 0,
                      sort_order = "ASC",
                      ignore_different_order = True
  ):
    """Generate all the possible permutation.
    
    Arguments:
    length -- the size of each permutation
      -- Given [([A, B, C])]
        -- if length = 1 then 
        --- you will get a permutation of a single A, B, and C
        -- if length = 2 then 
        --- you will get a permutation of a pair: AB / AC / BC
        -- if length = 3 then  
        --- you will get a permutation of a triplet: ABC
    sort_column_number -- sort by specific column number
      -- Given result ('John', 'Foo'): 235, ('Steve', 'Bone'): 123
        -- if sort_column_number = 0 then (it sorts by the pair name)
        --- first: ('John', 'Foo'): 235 then ('Steve', 'Bone'): 123
        -- if sort_column_number = 1 then (it sorts by the integer)
        --- first: ('Steve', 'Bone'): 123 then ('John', 'Foo'): 235
    sort_order -- sort order; either "ASC" (ascending) or "DESC" (descending)
    ignore_different_order -- whether the order in which letter appears in matters
      -- Given a record of A,B,C
      --- You will only get a permutation of ABC, because ABC/ACB/BCA/ets or any other "order" is ignored
    """

    # Instanitate an instance of the collections int dictionary
    # https://docs.python.org/2/library/collections.html#collections.defaultdict
    new_collections = collections.defaultdict(int)
    for row in self.data_set:
      # Check if we want to ignore_different_order
      if ignore_different_order == True:
        row.sort()

      # The for loop is broken down into 2 parts
      # - #1) `itertools.combinations(row, length)`
      # -- Creates a permutation, given row, create permutation of length sizes
      # - #2) `for permutation in`
      # -- For each of the permutation created in (#1)
      # --- If the permutation is not there, add it there and set it to 1
      # --- If its there, find that permutation and increment it by 1
      for permutation in itertools.combinations(row, length):
        new_collections[permutation] = new_collections[permutation] + 1

    # Set the sorting direction DESC / ASC
    if sort_order == "DESC":
      is_reverse = True
    else:
      is_reverse = False

    # Set the column number that you want to sort by
    #   -If the column number is not specify then you do not need to sort
    if sort_column_number != None:
      new_collections = sorted(new_collections.iteritems(), key=operator.itemgetter(sort_column_number), reverse=is_reverse)
    
    return new_collections

  def get_permutation_by_pair_order_by_occurance_descending(self):
    """
      This is basically doing get_permutation(2, 1, "DESC", True)

      But the performance is better, due to
      - Don't have to hit the if-condition in 
      -- 1) `if ignore_different_order == True:`
      -- 2) `if sort_order == "DESC":`
      -- 3) `if sort_column_number != None:`

      However, the drawback is having to maintain 2 separate code
    """

    new_collections = collections.defaultdict(int)
    for row in self.data_set:
      row.sort()
      for permutation in itertools.combinations(row, 2):
        new_collections[permutation] = new_collections[permutation] + 1

    new_collections = sorted(new_collections.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    return new_collections


