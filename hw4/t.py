import unittest
from GF2 import *
from hw3 import *
from matutil import *
from vecutil import *


class Hw3Test(unittest.TestCase):
  
  # -------------------------------------------------- 
  # problem 1 is hand answered - no programming required
  # --------------------------------------------------
  
  def test_problem_2(self):
    self.assert_size_matrix(M_swap_two_vector, 2, 2)
    
    self.helper_problem_2(M_swap_two_vector, 1, 2)
    self.helper_problem_2(M_swap_two_vector, 5, 7)
    self.helper_problem_2(M_swap_two_vector, 13, 3)
    self.helper_problem_2(M_swap_two_vector, 1681, 16361)
    self.helper_problem_2(M_swap_two_vector, .5, .5)
  
  def helper_problem_2(self, m, x, y):
    actual_first = m[0][0] * x + m[0][1] * y
    actual_second = m[1][0] * x + m[1][1] * y
    # for human debugging
    print("Problem 2")
    print(str(x) + " " + str(y))
    print(str(actual_first) + " " + str(actual_second))
    print()
    # automated verification
    self.assertEqual(y, actual_first, 'first position')
    self.assertEqual(x, actual_second, 'second position')
  
  def assert_size_matrix(self, m, expected_rows, expected_cols):
    self.assertEqual(expected_rows, len(m), "# rows")
    for i in range(len(m)):
      self.assertEqual(expected_cols, len(m[i]), "# columns in row " + str(i))
    
  # --------------------------------------------------
    
  def test_problem_3(self):
    self.assert_size_matrix(three_by_three_matrix, 3, 3)
    
    self.helper_problem_3(three_by_three_matrix, 1, 2, 3)
    self.helper_problem_3(three_by_three_matrix, 5, 7, 1)
    self.helper_problem_3(three_by_three_matrix, 13, 3, 18)
    self.helper_problem_3(three_by_three_matrix, 1681, 16361, 15554)
  
  def helper_problem_3(self, m, x, y, z):
    actual_first = m[0][0] * x + m[0][1] * y + m[0][2] * z
    actual_second = m[1][0] * x + m[1][1] *  y+ m[1][2] * z
    actual_third = m[2][0] * x + m[2][1] *  y+ m[2][2] * z  
    # for human debugging
    print("Problem 3")
    print(str(x) + " " + str(y) + " " + str(z))
    print(str(actual_first) + " " + str(actual_second) + " " + str(actual_third))
    print()
    # automated verification
    self.assertEqual(z+x, actual_first, 'first position')
    self.assertEqual(y, actual_second, 'second position')
    self.assertEqual(x, actual_third, 'third position')
   
  # --------------------------------------------------
    
  def test_problem_4(self):
    self.assert_size_matrix(multiplied_matrix, 3, 3)
    
    self.helper_problem_4(multiplied_matrix, 1, 2, 3)
    self.helper_problem_4(multiplied_matrix, 5, 7, 1)
    self.helper_problem_4(multiplied_matrix, 13, 3, 18)
    self.helper_problem_4(multiplied_matrix, 1681, 16361, 15554)
  
  def helper_problem_4(self, m, x, y, z):
    actual_first = m[0][0] * x + m[0][1] * y + m[0][2] * z
    actual_second = m[1][0] * x + m[1][1] *  y+ m[1][2] * z
    actual_third = m[2][0] * x + m[2][1] *  y+ m[2][2] * z  
    # for human debugging
    print(str(x) + " " + str(y) + " " + str(z))
    print(str(actual_first) + " " + str(actual_second) + " " + str(actual_third))
    print()
    # automated verification
    self.assertEqual(2*x, actual_first, 'first position')
    self.assertEqual(4*y, actual_second, 'second position')
    self.assertEqual(3*z, actual_third, 'third position')
 
  # -------------------------------------------------- 
  # problem 5 is hand answered - no programming required
  # --------------------------------------------------
  
  # -------------------------------------------------- 
  # problem 6 is hand answered (I think) - no programming required.  And even if it isn't, 
  # I can't think of a way to write the test without giving away too much of the answer
  # --------------------------------------------------
  
  # -------------------------------------------------- 
  # problem 7, 8, and 9 are hand answered - no programming required
  # --------------------------------------------------
  
  # -------------------------------------------------- 
  # problem 10 is hand answered (I think) - no programming required.  And even if it isn't, 
  # I can't think of a way to write the test without giving away too much of the answer
  # --------------------------------------------------
  
  def print_and_assertEqual(self, problemName, expected, actual):
    # for human debugging
    print(problemName)
    print(expected)
    print(actual)
    print()
    # automated verification
    self.assertEqual(expected, actual)
  
  def test_problem_11(self):
    matrix = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
    vector = list2vec([1, 2, 0])
    expected = list2vec([1, 5, 6])
    
    actual = lin_comb_mat_vec_mult(matrix, vector)
    self.print_and_assertEqual("Problem 11", expected, actual)
    
  def test_problem_11_smaller(self):
    matrix = listlist2mat([[8, 1, 2]])
    vector = list2vec([1, 2, 2])
    expected = list2vec([14])
   
    actual = lin_comb_mat_vec_mult(matrix, vector)
    self.print_and_assertEqual("Problem 11 - smaller", expected, actual)
    
  # --------------------------------------------------
    
  def test_problem_12(self):
    matrix = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
    vector = list2vec([4, 3, 2, 1])
    expected = list2vec([-40, 80])
    
    actual = lin_comb_vec_mat_mult(vector, matrix) 
    self.print_and_assertEqual("Problem 12", expected, actual)
    
  def test_problem_12_smaller(self):
    matrix = listlist2mat([[5], [8]])
    vector = list2vec([2, 1])
    expected = list2vec([18])
    
    actual = lin_comb_vec_mat_mult(vector, matrix) 
    self.print_and_assertEqual("Problem 12 - smaller", expected, actual)
    
  # --------------------------------------------------
  
  def test_problem_13(self):
    matrix = listlist2mat([[-1, 1, 2], [1, 2, 3], [2, 2, 1]])
    vector = list2vec([1, 2, 0])
    expected = list2vec([1, 5, 6])
    
    actual = dot_product_mat_vec_mult(matrix, vector)
    self.print_and_assertEqual("Problem 13", expected, actual)
    
  def test_problem_13_smaller(self):
    matrix = listlist2mat([[8, 1, 2]])
    vector = list2vec([1, 2, 2])
    expected = list2vec([14])
   
    actual = dot_product_mat_vec_mult(matrix, vector)
    self.print_and_assertEqual("Problem 13 - smaller", expected, actual)
    
  # --------------------------------------------------
  
  def test_problem_14(self):
    matrix = listlist2mat([[-5, 10], [-4, 8], [-3, 6], [-2, 4]])
    vector = list2vec([4, 3, 2, 1])
    expected = list2vec([-40, 80])
    
    actual = dot_product_vec_mat_mult(vector, matrix) 
    self.print_and_assertEqual("Problem 14", expected, actual)
    
  def test_problem_14_smaller(self):
    matrix = listlist2mat([[5], [8]])
    vector = list2vec([2, 1])
    expected = list2vec([18])
    
    actual = dot_product_vec_mat_mult(vector, matrix) 
    self.print_and_assertEqual("Problem 14 - smaller", expected, actual)
    
  # --------------------------------------------------
  
  def test_problem_15_symmetric(self):
    A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
    B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
    expected = Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
    actual = Mv_mat_mat_mult(A, B)
    self.print_and_assertEqual("Problem 15 - symmetric", expected, actual)
    
  def test_problem_15_asymmetric(self):
    C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
    D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
    expected = Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})
    actual = Mv_mat_mat_mult(C, D)
    self.print_and_assertEqual("Problem 15 - asymmetric", expected, actual)
    
  def test_problem_15_empty(self):
    M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
    N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
    expected = Mat(({0,1}, {(1,1), (2,2)}), {})
    actual = Mv_mat_mat_mult(M, N)
    self.print_and_assertEqual("Problem 15 - empty", expected, actual)
    self.assertEqual(expected, actual, 'confirm zeros not included')
    
  # --------------------------------------------------
  def test_problem_16_symmetric(self):
    A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
    B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
    expected = Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
    actual = Mv_mat_mat_mult(A, B)
    self.print_and_assertEqual("Problem 16 - symmetric", expected, actual)
    
  def test_problem_16_asymmetric(self):
    C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
    D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
    expected = Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})
    actual = Mv_mat_mat_mult(C, D)
    self.print_and_assertEqual("Problem 16 - asymmetric", expected, actual)
    
  def test_problem_16_empty(self):
    M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
    N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
    expected = Mat(({0,1}, {(1,1), (2,2)}), {})
    actual = Mv_mat_mat_mult(M, N)
    self.print_and_assertEqual("Problem 16 - empty", expected, actual)
    self.assertEqual(expected, actual, 'confirm zeros not included')
  # --------------------------------------------------
  def test_problem_17_symmetric(self):
    A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
    B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
    expected = Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
    actual = dot_prod_mat_mat_mult(A, B)
    self.print_and_assertEqual("Problem 17 - symmetric", expected, actual)
    
  def test_problem_17_asymmetric(self):
    C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2}) 
    D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
    expected = Mat(({0,1,2}, {'x','y'}), {(0,'y'):-5, (1,'x'):3, (1,'y'):-2, (2,'x'):-5})
    actual = dot_prod_mat_mat_mult(C, D)
    self.print_and_assertEqual("Problem 17 - asymmetric", expected, actual)
    
  def test_problem_17_empty(self):
    M = Mat(({0, 1}, {'a', 'c', 'b'}), {})
    N = Mat(({'a', 'c', 'b'}, {(1, 1), (2, 2)}), {})
    expected = Mat(({0,1}, {(1,1), (2,2)}), {})
    actual = dot_prod_mat_mat_mult(M, N)
    self.print_and_assertEqual("Problem 17 - empty", expected, actual)
    self.assertEqual(expected, actual, 'confirm zeros not included')
  
  # --------------------------------------------------
  def test_problem_18_x(self):
    vector = list2vec([solving_systems_x1, solving_systems_x2])
    expected = list2vec([1, 0])
    
    actual = lin_comb_mat_vec_mult(solving_systems_a, vector)
    self.print_and_assertEqual("Problem 18 - x", expected, actual)
    
  def test_problem_18_y(self):
    vector = list2vec([solving_systems_y1, solving_systems_y2])
    
    actual = lin_comb_mat_vec_mult(solving_systems_a, vector)
    
    # added "almost equals" because was getting double precision issue comparing to zero
    self.assertAlmostEqual(0, actual[0], msg='0')
    self.assertAlmostEqual(1, actual[1], msg='1')
    
  def test_problem_18_identity(self):
    actual = Mv_mat_mat_mult(solving_systems_m, solving_systems_a)
    
    # added "almost equals" because was getting double precision issue comparing to zero
    self.assertAlmostEqual(1, actual[(0,0)], msg='0,0')
    self.assertAlmostEqual(0, actual[(1,0)], msg='1,0')
    self.assertAlmostEqual(0, actual[(0,1)], msg='0,1')
    self.assertAlmostEqual(1, actual[(1,1)], msg='1,1')


    
  # the final parts of #18 can't be tested without giving away the answer
  
  # --------------------------------------------------
  
  # -------------------------------------------------- 
  # problem 19 is hand answered - no programming required
  # --------------------------------------------------
  
  # --------------------------------------------------
  
    
if __name__ == '__main__':
  unittest.main()
