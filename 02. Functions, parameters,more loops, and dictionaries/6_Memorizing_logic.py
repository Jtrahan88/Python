print('''
The Truth Terms
In python we have the following terms (characters and phrases) for determining if something is "True" or "False".
Logic on a computer is all about seeing if some combination of these characters and some variables is True at that
point in the program.

Examples:
and
or
not
!= (not equal)
== (equal)
>= (greater-than-equal)
<= (less-than-equal)
True
False


The phrases (and, or, not) actually work the way you expect them to, just like in English.

The Truth Tables to memorize:

NOT	| True?
---------------------
not False | True
not True  | False
---------------------

OR | True?
---------------------
True or False  | True
True or True   | True
False or True  | True
False or False | False
---------------------

AND | True?
---------------------
True and False  | False
True and True   | True
False and True  | False
False and False | False
---------------------

NOT OR | True?
---------------------
not (True or False)  | False
not (True or True)   | False
not (False or True)  | False
not (False or False) | True
---------------------

NOT AND	| True?
---------------------
not (True and False)  | True
not (True and True)   | False
not (False and True)  | True
not (False and False) | True
---------------------

!= | True?
---------------------
1 != 0 | True
1 != 1 | False
0 != 1 | True
0 != 0 | False
---------------------

== | True?
---------------------
1 == 0 | False
1 == 1 | True
0 == 1 | False
0 == 0 | True








''')