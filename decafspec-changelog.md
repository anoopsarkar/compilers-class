Changelog for the Decaf spec
============================

2021-11-24
----------

- Clarify what happens when `main` has type `bool` and has no `return` statement.
- `%` should be implemented using the `srem` instruction in LLVM, as mentioned in the DecafLLVM lecture. The old spec described behaviour that was not consistent with the use of `srem`.
- main can return bool. There were two testcases that had bool returns and expected actual output instead of a semantic error. The default return value for bools is `ret i1 1`. 
- To simplify the contest, main must still return `int` for all contest submissions.
- Array bounds checking produces undefined behaviour. Compile-time errors, runtime errors, and segfaults are all acceptable outcomes.
