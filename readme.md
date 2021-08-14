# Lights Out Puzzle Solver

A python program that finds solution to any *m x n* Lights Out Puzzle for prime *p* number of colors using Gauss-Jordan Elimination.

## Source File

```
matrix_p_class.py
```
-> A class containing methods that perform operations on a matrix in field of *p* colors where *p* is prime. The class takes the field and the matrix as an input at the point of instantiation


```
activation_matrix.py 
```
-> Returns an *m x n* activation matrix of an *m x n* lights out puzzle where "*m*" is the puzzle row number, and "*n*" is the puzzle column number.

```
build_matrix_for_rref.py
```
-> Takes inputs of m-number of rows and n-number of columns and returns a matrix for computing the Gauss-Jordan elimination of a lights out puzzle whose lights start all off and to be all switched on. It returns the matrix as a list of columns with an element of the solution vector at the end.

```
row_echelon_form.py
```
-> A function that computes the row echelon form of an *m x n* matrix.
Take an input matrix from build_matrix_for_rref and returns the row echelon form of that *m x n* matrix

```
row_reduced_echelon_form.py
```
-> A function that computes the row-reduced echelon form of an *m x n* matrix.
Take an input matrix from build_matrix_for_rref and returns the row echelon form of that *m x n* matrix


```
solution_noSolution.py
```
-> Returns the sollution space if there is a solution and 
"NO SOLUTION" if there is not.

```
nullity.py
```
 -> Returns the nullity of *m x n* lights out puzzle.

```
puzzle_solver.py
``` 
-> Asks for an following input from an user: number of rows, number of columns and number of colors. Returns the solution (if it exists) for that particular lights out puzzle as a lists of list.

# Running the program on terminal

```
python puzzle_solver.py
```

# Dependencies

Just Python 3 and you are good to go!

-------

# Lights Out Puzzle Web Interface

## Source File



### *In collaboration with Dr. Igor Minevich and Wisdom Boinde at Earlham College.*









