# Number Theory and Cryptography
This Repository has all the assignments and the mini-project of the Network and Cryptography course

## Coding Assignment 1

Question: Implement the Eucildean Algorithm to find GCD of 2 numbers. 

Contributors:

1. Samyak Jain - 16CO254
2. Adwaith Gautham - 16CO203

Approach: 

**1**. Naive GCD: 

* In this approach we select min of 2 numbers then we traverse from smaller number to 0 to find the number which divides both of them.
* If we find such a number, it is the GCD. Else, GCD = 1.

**2**. Slow GCD:

* Subtract smaller number from bigger number and iterate till one of them becomes 0 the other number is GCD.

**3**. Fast GCD :

* Instead of subtraction use division and get the remainder and set the bigger number as the remainder. Iterate till one of them becomes 0 other is GCD.

**4**. Extended Euclid :
* use fast euclid algorithm to find GCD and then apply it in reverse(recursion) to find value of x and y in equation ax+by=g.

This is graph which shows the comparision of the 4 algorithms implemented: 

[Graph](./NTC-Assignment/GCD_16_24.jpg)
