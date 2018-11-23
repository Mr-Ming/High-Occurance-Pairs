import unittest


from classes.permutation import Permutation

class PermutationTest(unittest.TestCase):
  """
  Run unit test for classes/permutation.py
  """
  def test_get_permutation_success_when_length_is_single(self):
    permutation = Permutation([(["A", "B", "C"])])
    result = permutation.get_permutation(1);
    self.assertEqual([(('A', ),1), (('B', ),1), (('C', ),1)], result);
    
  def test_get_permutation_success_when_length_is_pair(self):
    permutation = Permutation([(["A", "B", "C"])])
    result = permutation.get_permutation(2);
    self.assertEqual([(('A', 'B'),1), (('A', 'C'),1), (('B', 'C'),1)], result)

  def test_get_permutation_success_when_length_is_triple(self):
    permutation = Permutation([(["A", "B", "C"])])
    result = permutation.get_permutation(3);
    self.assertEqual([(('A', 'B', 'C'),1)], result)

  def test_get_permutation_success_when_sorting_by_pair_name_ascending(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "C"])])
    result = permutation.get_permutation(2);
    self.assertEqual([(('A', 'B'), 1), (('A', 'C'), 2), (('B', 'C'), 1)], result)

  def test_get_permutation_success_when_sorting_by_pair_name_descending(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "C"])])
    result = permutation.get_permutation(2, 0, "DESC");
    self.assertEqual([(('B', 'C'), 1), (('A', 'C'), 2), (('A', 'B'), 1)], result)

  def test_get_permutation_success_when_sorting_by_occurance_name_ascending(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "C"])])
    result = permutation.get_permutation(2, 1, "ASC");
    self.assertEqual([(('B', 'C'), 1), (('A', 'B'), 1), (('A', 'C'), 2)], result)

  def test_get_permutation_success_when_sorting_by_occurance_name_descending(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "C"])])
    result = permutation.get_permutation(2, 1, "DESC");
    self.assertEqual([(('A', 'C'), 2), (('B', 'C'), 1), (('A', 'B'), 1)], result)

  def test_get_permutation_success_when_sorting_by_occurance_name_descending_not_ignoring_different_order(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "B", "C"]), (["C", "A", "B"])])
    result = permutation.get_permutation(2, 1, "DESC", False);

    expected = [(('A', 'B'),3), (('B', 'C'),2), (('A', 'C'),2), (('C', 'A'),1), (('C', 'B'),1)]
    self.assertEqual(expected, result)

  def test_get_permutation_success_when_sorting_by_occurance_name_descending_ignoring_different_order(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "B", "C"]), (["C", "A", "B"])])
    result = permutation.get_permutation(2, 1, "DESC", True);

    self.assertEqual([(('B', 'C'), 3), (('A', 'B'), 3), (('A', 'C'), 3)], result)

  def test_get_permutation_by_pair_order_by_occurance_descending(self):
    permutation = Permutation([(["A", "B", "C"]), (["A", "B", "C"]), (["C", "A", "B"])])
    result = permutation.get_permutation_by_pair_order_by_occurance_descending();

    self.assertEqual([(('B', 'C'), 3), (('A', 'B'), 3), (('A', 'C'), 3)], result)

if __name__ == '__main__':
    unittest.main()