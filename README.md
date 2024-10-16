# Accelerate Python with Parallelism

[Link to slides](https://thomasjpfan.github.io/2024-accelerate-python-with-parallelism/)

Python is essential in many data science, machine learning, and computationally intensive tasks. However, its Global Interpreter Lock (GIL) traditionally limits parallelism, hindering performance for CPU-bound operations. This presentation explores how numerical libraries such as NumPy, Scikit-learn, Polars, and PyTorch bypass the GIL's limitations through vectorization, multi-threading, and compilation. We explore benchmarking techniques to identify performance bottlenecks and show practical methods to accelerate your code. We also address common pitfalls of parallel programming in Python, including over-subscription and combining different parallelism paradigms. Finally, we review the impact of recent advancements, like free-threading and sub-interpreters, on the future of parallel computing in Python.

## License

This repo is under the [MIT License](LICENSE).
