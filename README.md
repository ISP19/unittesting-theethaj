## Unit Testing Assignment

by Tetach Rattanavikran (6110545554).


## Test Cases for unique

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| empty list                               |  empty list                           |
| 1 item                                   |  1 list with 1 item                   |
| 1 list                                   |  1 list with 1 list                   |
| 2 items, many times, many orders         |  2 items list, items in same order    |
| 3 items, many times, many orders         |  3 items list, items in same order    |
| 5 items, once per item	           |  5 items list, items in same order    |
| 2 items, 1 list, many times, many orders |  2 items, 1 list, items in same order |
| 3 items, 1 list, many times, many orders |  3 items, 1 list, items in same order |
| 3 items, 2 list, many times, many orders |  3 items, 2 list, items in same order |


## Test Cases for Fraction

Test Cases for init method

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| numerator and denominator (common factor) | lowest-term fraction |
| both numerator and denominator is positive | positive lowest-term fraction |
| both numerator and denominator is negative | positive lowest-term fraction |
| positive numerator and negative denominator | negative lowest-term fraction |
| negative numerator and positive denominator | negative lowest-term fraction |
| positive numerator | positive numerator and denominator is 1 |
| negative numerator | negative numerator and denominator is 1 |
| numerator is 0 | 0 |
| positive numerator and denominator is 0 | 1/0 |
| negative numerator and denominator is 0 | - 1/0 |
| both numerator and denominator is 0 | 0/0 |
| arguments aren't an integer | raise ValueError |

Test Cases for string method

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| both numerator and denominator is positive | numerator/denominator |
| both numerator and denominator is negative | numerator/denominator |
| positive numerator and negative denominator | - numerator/denominator |
| negative numerator and positive denominator | - numerator/denominator |
| positive numerator and denominator is 1 | numerator |
| positive numerator and denominator is -1 | - numerator |
| numerator is 0 | 0 |
| positive numerator and denominator is 0 | 1/0 |
| negative numerator and denominator is 0 | - 1/0 |
| both numerator and denominator is 0 | 0/0 |

Test Cases for addition method

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| positive fraction plus positive fraction | positive fraction |
| negative fraction plus negative fraction | negative fraction |
| any fraction plus zero | default fraction |
| any fraction (less than infinity) plus positive infinity (1/0) | positive infinity (1/0) |
| any fraction (less than infinity) plus negative infinity (-1/0) | negative infinity (-1/0) |
| positive infinity (1/0) plus positive infinity (1/0) | positive infinity (1/0) |
| negative infinity (-1/0) plus negative infinity (-1/0) | negative infinity (-1/0) |
| positive infinity (1/0) plus negative infinity (-1/0) | fraction 0/0 |
| fraction 0/0 plus any fraction (less than infinity) | fraction 0/0 |
| fraction 0/0 plus infinity | fraction 0/0 |

Test Cases for multiplication method

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| infinity multiply zero | fraction 0/0 |
| fraction 0/0 multiply anything | fraction 0/0 |
| infinity multiply infinity | infinity |
| zero multiply anything | 0 |
| infinity multiply any fraction (less than infinity) | infinity |

Test Cases for equality method

| Test case                                |  Expected Result                      |
|------------------------------------------|---------------------------------------|
| positive fraction equals negative fraction | False |
| any fraction (less than infinity) equals lowest-term fraction | True |
| positive infinity equals negative infinity | False |
| fraction 0/0 equals any fraction (less than infinity) | False |
| fraction 0/0 equals infinity | False |

### Status
[![Build Status](https://travis-ci.com/theethaj/unittesting-theethaj.svg?branch=master)](https://travis-ci.com/theethaj/unittesting-theethaj)