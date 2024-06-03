# Detailed Explanation of the Quantum Fourier Transform (QFT) Algorithm

# Introduction:
# The Quantum Fourier Transform (QFT) is the quantum analog of the classical discrete Fourier transform (DFT).
# It is a linear transformation on quantum bits and is widely used in various quantum algorithms, such as Shor's
# algorithm for factoring large numbers and the quantum phase estimation algorithm.

# Definition:
# Given an n-qubit quantum state |x⟩, where x is an integer in binary representation, the QFT transforms |x⟩
# into another quantum state as follows:
# QFT(|x⟩) = (1/√2^n) Σ_k=0^2^n-1 e^(2πi xk / 2^n) |k⟩

# Steps of the QFT Algorithm:
# 1. Initialization:
#    - Start with n qubits in the state |x⟩.
# 2. Apply Hadamard Gate:
#    - Apply a Hadamard gate to the first qubit.
# 3. Apply Controlled Phase Rotation Gates:
#    - For each subsequent qubit, apply controlled phase rotation gates R_k where R_k applies a phase shift of
#      2π/2^k when the control qubit is |1⟩.
# 4. Repeat:
#    - Repeat the above steps for each qubit.
# 5. Swap Qubits:
#    - Swap the k-th qubit with the (n-k-1)-th qubit to reverse the order of the qubits.

# Quantum Circuit:
# The QFT circuit consists of Hadamard gates and controlled phase rotation gates, followed by a series of qubit swaps.
# The circuit depth is O(n^2).

# Simple Example Using Qiskit

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import numpy as np

# Function to apply QFT on a quantum circuit
def qft(qc, n):
    """Apply QFT on the first n qubits in the quantum circuit qc"""
    for i in range(n):
        qc.h(i)
        for j in range(i + 1, n):
            qc.cp(np.pi / 2 ** (j - i), j, i)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)

# Create a quantum circuit with 3 qubits
qc = QuantumCircuit(3)

# Initialize the quantum state |x⟩ = |5⟩ = |101⟩
qc.x(0)
qc.x(2)

# Apply QFT
qft(qc, 3)

# Use the Aer simulator to get the statevector
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()

# Plot the Bloch sphere representation of the statevector
plot_bloch_multivector(statevector)

# More Complex Example Using Qiskit

# Function to apply QFT on a quantum circuit
def qft(qc, n):
    """Apply QFT on the first n qubits in the quantum circuit qc"""
    for i in range(n):
        qc.h(i)
        for j in range(i + 1, n):
            qc.cp(np.pi / 2 ** (j - i), j, i)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4)

# Initialize the quantum state |x⟩ = |9⟩ = |1001⟩
qc.x(0)
qc.x(3)

# Apply QFT
qft(qc, 4)

# Use the Aer simulator to get the statevector
simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()
statevector = result.get_statevector()

# Plot the Bloch sphere representation of the statevector
plot_bloch_multivector(statevector)

# Explanation of Each Line in the Code

# Simple Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.visualization import plot_histogram, plot_bloch_multivector`: Import functions for visualization.
# 3. `import numpy as np`: Import NumPy for numerical operations.
# 4. `def qft(qc, n)`: Define a function to apply QFT on the first n qubits in the quantum circuit qc.
# 5. `for i in range(n)`: Loop over each qubit.
# 6. `qc.h(i)`: Apply a Hadamard gate to the i-th qubit.
# 7. `for j in range(i + 1, n)`: Loop over each subsequent qubit.
# 8. `qc.cp(np.pi / 2 ** (j - i), j, i)`: Apply a controlled phase rotation gate.
# 9. `for i in range(n // 2)`: Loop over half of the qubits.
# 10. `qc.swap(i, n - i - 1)`: Swap the i-th qubit with the (n-i-1)-th qubit.
# 11. `qc = QuantumCircuit(3)`: Create a quantum circuit with 3 qubits.
# 12. `qc.x(0)`: Initialize the first qubit in the state |1⟩.
# 13. `qc.x(2)`: Initialize the third qubit in the state |1⟩.
# 14. `qft(qc, 3)`: Apply QFT on the 3 qubits.
# 15. `simulator = Aer.get_backend('statevector_simulator')`: Use the Aer simulator to get the statevector.
# 16. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 17. `statevector = result.get_statevector()`: Get the statevector.
# 18. `plot_bloch_multivector(statevector)`: Plot the Bloch sphere representation of the statevector.

# Complex Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.visualization import plot_histogram, plot_bloch_multivector`: Import functions for visualization.
# 3. `import numpy as np`: Import NumPy for numerical operations.
# 4. `def qft(qc, n)`: Define a function to apply QFT on the first n qubits in the quantum circuit qc.
# 5. `for i in range(n)`: Loop over each qubit.
# 6. `qc.h(i)`: Apply a Hadamard gate to the i-th qubit.
# 7. `for j in range(i + 1, n)`: Loop over each subsequent qubit.
# 8. `qc.cp(np.pi / 2 ** (j - i), j, i)`: Apply a controlled phase rotation gate.
# 9. `for i in range(n // 2)`: Loop over half of the qubits.
# 10. `qc.swap(i, n - i - 1)`: Swap the i-th qubit with the (n-i-1)-th qubit.
# 11. `qc = QuantumCircuit(4)`: Create a quantum circuit with 4 qubits.
# 12. `qc.x(0)`: Initialize the first qubit in the state |1⟩.
# 13. `qc.x(3)`: Initialize the fourth qubit in the state |1⟩.
# 14. `qft(qc, 4)`: Apply QFT on the 4 qubits.
# 15. `simulator = Aer.get_backend('statevector_simulator')`: Use the Aer simulator to get the statevector.
# 16. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 17. `statevector = result.get_statevector()`: Get the statevector.
# 18. `plot_bloch_multivector(statevector)`: Plot the Bloch sphere representation of the statevector.

# Conclusion
# The Quantum Fourier Transform (QFT) is a fundamental operation in quantum computing, enabling exponential
# speedups in various quantum algorithms. The provided examples, along with detailed explanations, demonstrate
# how to implement QFT using Qiskit, making it easier to understand each step in the code. This understanding
# is crucial for developing more advanced quantum algorithms.
