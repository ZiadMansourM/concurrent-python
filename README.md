#  Python `concurrent.futures` 
Python's concurrent.futures module simplifies concurrent programming by providing a high-level interface for asynchronously executing callable (functions/methods). ThreadPoolExecutor and ProcessPoolExecutor are two popular classes within this module that enable you to easily execute tasks concurrently, using threads or processes, respectively.

## When to consider which
When deciding between ThreadPoolExecutor and ProcessPoolExecutor, consider the following analogy:
- ThreadPoolExecutor is like having multiple chefs in a shared kitchen.
- ProcessPoolExecutor is like having multiple chefs, each with their own kitchen.

ThreadPoolExecutor is ideal for `I/O-bound` tasks, where tasks often wait for external resources, such as reading files or downloading data. In these cases, sharing resources is acceptable and efficient. On the other hand, ProcessPoolExecutor is better suited for `CPU-bound` tasks, where heavy computations are performed, and sharing resources could lead to performance bottlenecks.

## executor.map()
Executes tasks concurrently and returns results in the `order they were submitted`.

> `executor.map()` method ensures that the results are `ordered according to the input sequence`, even though the tasks `finished at different times`.

## executor.submit() and executor.as_completed()
Executes tasks concurrently but allows you to process results `as they become` available.
