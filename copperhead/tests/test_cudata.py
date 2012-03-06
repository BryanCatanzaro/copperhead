#
#   Copyright 2012      NVIDIA Corporation
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# 
#

import numpy as np
from copperhead import *
import unittest
import collections
import itertools
import operator

def recursive_equal(a, b):
    if isinstance(a, collections.Iterable):
        return all(itertools.imap(recursive_equal, a, b))
    else:
        return a == b

    
class CudataTest(unittest.TestCase):
    def testNumpyFlat(self):
        a = np.array([1,2,3,4,5])
        b = cuarray(a)
        self.assertTrue(recursive_equal(a, b))
    def testPythonFlat(self):
        a = [2.78, 3.14, 1.62]
        b = cuarray(a)
        self.assertTrue(recursive_equal(a, b))
    def testNumpyNested(self):
        a = [[np.array([1,2]), np.array([3,4,5])],
        [np.array([6,7,8,9]), np.array([10,11,12,13,14]),
         np.array([15,16,17,18,19,20])]]
        b = cuarray(a)
        self.assertTrue(recursive_equal(a, b))
    def testPythonNested(self):
        a = [[[1,2], [3,4,5]],
        [[6,7,8,9], [10,11,12,13,14],
         [15,16,17,18,19,20]]]
        b = cuarray(a)
        self.assertTrue(recursive_equal(a, b))
    def deref_type_check(self, np_type):
        a = np.array([1], dtype=np_type)
        b = cuarray(a)
        self.assertTrue(type(a[0]) == type(b[0]))
        self.assertTrue(a[0] == b[0])
    def testInt32(self):
        self.deref_type_check(np.int32)
    def testInt64(self):
        self.deref_type_check(np.int64)
    def testFloat32(self):
        self.deref_type_check(np.float32)
    def testFloat64(self):
        self.deref_type_check(np.float64)
    def testBool(self):
        self.deref_type_check(np.bool)
    def testStr(self):
        a = [[[1,2], [3,4,5]],
        [[6,7,8,9], [10,11,12,13,14],
         [15,16,17,18,19,20]]]
        b = cuarray(a)
        self.assertEqual(str(a), str(b))

if __name__ == '__main__':
    unittest.main()
