## USACO Training

Below is answer to beads question:

```python
"""
ID: amolgur1
LANG: PYTHON3
TASK: beads
"""

with open("beads.in", "r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
s += s

max_total = 0

for i in range(n):
    window = s[i : i + n]
    left_r = 0
    for bead in window:
        if bead == "r" or bead == "w":
            left_r += 1
        else:
            break

    left_b = 0
    for bead in window:
        if bead == "b" or bead == "w":
            left_b += 1
        else:
            break

    right_r = 0
    for bead in reversed(window):
        if bead == "r" or bead == "w":
            right_r += 1
        else:
            break

    right_b = 0
    for bead in reversed(window):
        if bead == "b" or bead == "w":
            right_b += 1
        else:
            break

    left_max = max(left_r, left_b)
    right_max = max(right_r, right_b)
    total = left_max + right_max

    # Ensure total does not exceed n
    if total > n:
        total = n

    if total > max_total:
        max_total = total


with open("beads.out", "w") as fout:
    fout.write(f"{max_total}\n")
```

### Thought 1 - Using Dynamic Programming

Thoughts on dynamic programming

```python
if something>10:
    print("yes")
```

## DSA

## Scope of Variables

## **1. For Loops**

### **In C/Java/C++:**

- **Local Declaration:**  
  When you declare a loop variable in the loop header, it is local to that loop’s block. For example:

  ```java
  for (int i = 0; i < 10; i++) {
      // `i` is accessible only within this block.
      System.out.println(i);
  }

  ```

- **External Declaration:**  
  If you declare the variable before the loop, it remains accessible after the loop completes:

  ```java
  int i;  // declared in the outer scope (e.g., function scope)
  for (i = 0; i < 10; i++) {
      System.out.println(i);
  }
  System.out.println("After loop, i = " + i);  // i is still accessible.
  ```

### **In Python:**

Python does not create a new scope for for loops. This means the loop variable “leaks” into the surrounding function (or global) scope:

```python
for i in range(10):
    print(i)
print("Outside loop, i =", i)  # i is still accessible and has the last value (9)
```

---

## **2. While and Do‑While Loops**

### **In C/Java/C++:**

- **While Loop:**  
  Any variable declared inside the while’s block (i.e. within the curly braces) is local to that block:

  ```java
  while (someCondition) {
      int temp = 100; // local to this block
      // ...
  }
  // temp is not accessible here.
  ```

- **Do‑While Loop:**  
  The same principle applies. Variables declared inside the do‑while block are local to the block:

  ```java
  int j = 0;
  do {
      int k = j + 1;  // k is scoped to this block
      System.out.println(k);
      j++;
  } while (j < 10);
  // k is not accessible here.
  ```

### **In Python:**

Like for loops, Python does not impose a new block scope for while loops. If you create a variable inside a while loop, it will belong to the containing function’s scope:

```python
x = 5
while x > 0:
    y = x * 2  # y becomes part of the function/module scope
    x -= 1
print("Last computed y =", y)
```

---

## **3. With Statement**

### **In Python:**

- The `with` statement is used with context managers (such as opening files) to ensure proper resource management.
- **Scope Behavior:** The block inside a `with` does **not** create a new local scope. Any variable assigned inside is part of the surrounding (usually function) scope.

  ```python
  with open('file.txt') as f:
      data = f.read()
  # Both f and data are still available here:
  print(f)
  print(data)
  ```

### **In Other Languages (e.g., JavaScript):**

- JavaScript’s deprecated `with` statement works differently—it adds properties of an object to the scope chain temporarily, but it does not isolate new variable declarations to a separate block. (Note that using `with` is generally discouraged due to its confusing scope behavior.)

---

## **4. Try/Catch Blocks**

### **In C/Java/C++:**

- A `try` block creates its own block scope. Variables declared inside are **not accessible** outside of that block.
- In a `catch` block, the exception parameter is local to that block. If you need to use a variable after the try/catch, you must declare it in the surrounding scope.

  ```java
  int result;  // declare outside if you need its value later
  try {
      result = performComplexCalculation();
  } catch (Exception e) {
      System.out.println("An error occurred: " + e.getMessage());
      // result might not be assigned if an exception occurs.
  }
  // Here, result is accessible but should be used only if safely assigned.
  ```

  This behavior is designed to avoid accidental misuse of variables that may have never been initialized if an exception is thrown.

### **In Python:**

- Python’s `try/except` does not create a new scope at the level of a function; variables assigned in the try block remain in the function’s local namespace.
- However, if an exception occurs, some variables may not be assigned, so you must design carefully:

  ```python
  try:
      result = perform_complex_calculation()
  except Exception as e:
      print("Error:", e)
  else:
      print("Result is", result)
  # In Python, if result was assigned, it remains available after the try/except.
  ```

  One nuance is that the exception variable (commonly named `e`) in an except clause is cleaned up after the block in Python 3, minimizing potential side-effects.

---

## **Summary Table**

| **Construct**              | **Block-Level Scope in C/Java/C++**                                                                                                                        | **Behavior in Python**                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **For Loop**               | Loop variables declared in the header (e.g., `for (int i = …)`) are local to the loop.<br>Variables declared outside the loop remain accessible afterward. | The loop’s iteration variable remains in the enclosing function’s scope.                            |
| **While Loop**             | Variables declared inside the loop’s braces are local to that block.                                                                                       | No new scope is created; variables belong to the function scope.                                    |
| **Do‑While Loop**          | Same as while loops – variables declared within are local to that block.                                                                                   | Not applicable (Python does not have a native do‑while construct).                                  |
| **With Statement**         | (E.g., in C#’s `using` block) typically creates a block where variables are local to that block.                                                           | Does not create a new scope; variables assigned remain in the containing scope.                     |
| **Try/Catch (Try/Except)** | Variables declared in the `try` block are local to that block.<br>The catch/exception variable is local to its block.                                      | The try/except block is not a separate scope except for the exception variable cleanup in Python 3. |

---
