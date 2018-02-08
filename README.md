# PSAPP

* Not optimized for speed. But only consumes O(N) memory.
* Bails out as soon as first customer constraint can't be satisfied.
* Data input is continously processed and status updated.
* Feels like I am missing something (Efficiency gains by using "at most one like will be matte" etc.)
* Would be cool to simulate an input file to check how well this does with larger inputs.

## Quickstart

### Run example

* Requires Python 3.6
```bash
cd src/trivial
python runner.py < ../../test_inputs/test1.txt
```

### Run unit tests
* Requires Nose: http://nose.readthedocs.io/en/latest/

```bash
pip install -r requirements.txt
cd src/trivial
nosetests
```

### Run through Docker container:

* Note: Haven't tested this with macOS or Windows, only on Linux. Not sure if stdin redirection works on Mac / Windows.

Run this from the projects main directory `psapp/`.

```bash
# From project main directory.
docker build -t bwv988/psapp .
./psapp.sh < test_inputs/test1.txt
```

## Solution Overview and Highlights

The solution consists of three Python classes:

* `Runner`
* `Case`
* `Batch`

### `Runner` class

The `Runner` class is the main class. It reads a test case from standard input and processes it line by line.

Processing of a case is stopped **immediately** once we encounter the first customer for whom we cannot produce any paint they like.

Output is produced depending on the outcome, i.e. either the paint batches to produce, or "IMPOSSIBLE".

### `Case` class

The `Case` class maintains and continously updates **one** production batch -- using the `Batch` class -- for the current case.

For each customer, their paint preferences are assessed individually.

Also, `Case` provides a utility method `print_final_batch()` to output a final production batch string, provided a possible batch was found.

### `Batch` class

This class holds the production batch and the updater method `set_col()` for **one** case.

## Notes on Runtime and Memory Complexity

Here is a very rough analysis of runtime and memory complexity. The key datastructure is a an integer array of size N.

Further, the core algorithm can be summarized as follows:

```
1: Read C 
2: Iterate at most C times:
3:    Read N
4:    Read M
5:    Create batch_list(N)
6:
7:    Iterate at most M times:
8:       Read T pairs X, Y:
9:          Update batch_list T times
10:         Sum # of successful updates
11:      Test if at least one successful update
12: Produce final batch output
```

### Results

* Read / write access to array has constant time: O(1).
* Step 5: Creating the array is O(1).
* Steps 7-11: For one case, producing a result costs O(M*T).
* Step 10: Summing integers is O(1).
* Step 11: Test boolean results is O(1).
* The memory complexity is O(N).

 
## Caveats

* No error checking -- assuming constraints are as in the input description.
* Definitely not optimal solution. Sounded vaguely like a SAT (satisfiability) problem but didn't look further into it.
