#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    def test_read_2 (self) : 
    
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        r.readline()
        r.readline()
        i, j = collatz_read(r)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)
    
    def test_read_3 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        r.readline()
        r.readline()
        r.readline()
        r.readline()
        
        self.assertEqual(len(collatz_read(r)), 0)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 189)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, collatz_eval(1, 10))
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
       w = StringIO()
       collatz_print(w, 100, 200, collatz_eval(100, 200))
       self.assertEqual(w.getvalue(), "100 200 125\n")
       
    def test_print_3 (self) :
       w = StringIO()
       collatz_print(w, 201, 210, collatz_eval(201, 210))
       self.assertEqual(w.getvalue(), "201 210 189\n")
       
    def test_print_4 (self) :
      w = StringIO()
      collatz_print(w, 900, 1000, collatz_eval(900, 1000))
      self.assertEqual(w.getvalue(), "900 1000 174\n")
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 189\n900 1000 174\n")
    
    def test_solve_2 (self) :
       r = StringIO("")
       w = StringIO()
       collatz_solve(r, w)
       self.assertEqual(w.getvalue(), '')
       
# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out.txt 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      32      1      0      0    97%   78
---------------------------------------------------------
TOTAL            50      1      6      0    98%
"""