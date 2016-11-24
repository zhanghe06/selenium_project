
https://docs.python.org/2.7/library/unittest.html

- the most commonly used methods

Method | Checks that
--- | ---
assertEqual(a, b) | a == b
assertNotEqual(a, b) | a != b
assertTrue(x) | bool(x) is True
assertFalse(x) | bool(x) is False
assertIs(a, b) | a is b
assertIsNot(a, b) | a is not b
assertIsNone(x) | x is None 
assertIsNotNone(x) | x is not None 
assertIn(a, b) | a in b
assertNotIn(a, b) | a not in b
assertIsInstance(a, b) | isinstance(a, b)
assertNotIsInstance(a, b) | not isinstance(a, b)


- It is also possible to check that exceptions and warnings are raised using the following methods:

Method | Checks that	New in
--- | ---
assertRaises(exc, fun, *args, **kwds) | fun(*args, **kwds) raises exc
assertRaisesRegexp(exc, r, fun, *args, **kwds) | fun(*args, **kwds) raises exc and the message matches regex r


- There are also other methods used to perform more specific checks, such as:

Method | Checks that
--- | ---
assertAlmostEqual(a, b) | round(a-b, 7) == 0
assertNotAlmostEqual(a, b) | round(a-b, 7) != 0
assertGreater(a, b) | a > b
assertGreaterEqual(a, b) | a >= b
assertLess(a, b) | a < b
assertLessEqual(a, b) | a <= b
assertRegexpMatches(s, r) | r.search(s)
assertNotRegexpMatches(s, r) | not r.search(s)
assertItemsEqual(a, b) | sorted(a) == sorted(b) and works with unhashable objs
assertDictContainsSubset(a, b) | all the key/value pairs in a exist in b


Method | Used to compare
--- | ---
assertMultiLineEqual(a, b) | strings
assertSequenceEqual(a, b) | sequences
assertListEqual(a, b) | lists
assertTupleEqual(a, b) | tuples
assertSetEqual(a, b) | sets or frozensets
assertDictEqual(a, b) | dicts


注意区别：

```
# 测试类内部的每一个测试方法都会执行
setUp()
tearDown()
```
与
```
# 测试类内部只执行一次
setUpClass()
tearDownClass()
```


```
@classmethod
def setUpClass(cls):
    ...

@classmethod
def tearDownClass(cls):
    ...
```


测试方法

https://docs.python.org/2/library/unittest.html#test-discovery

```
cd project_directory
python -m unittest discover
```

```
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
```


## 异常的断言
```
with self.assertRaises(SomeException):
    do_something()
```

```
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)
```


## 基本概念

测试驱动开发（TDD：Test-Driven Development）


## 测试单个测试用例
```
✗ cd src
✗ python -m unittest tests.test_bar.BarTest.test_a
```


## 测试全部测试用例
```
✗ cd src
✗ python -m unittest discover -s 'tests' -p 'test_bar.py'
✗ python -m unittest discover -s 'tests' -p 'test_*.py'
```