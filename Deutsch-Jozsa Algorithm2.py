# Deutsch-Jozsa Algorithm

# Explanation:
# The Deutsch-Jozsa Algorithm is a quantum algorithm that determines whether a given function f: {0,1}^n -> {0,1}
# is constant (same output for all inputs) or balanced (outputs 0 for half of the inputs and 1 for the other half) with a single query.

# Qiskit Usage:
# The Deutsch-Jozsa algorithm uses Hadamard gates and an oracle to determine the nature of the function.

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with n+1 qubits and n classical bits
n = 3
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for a balanced function (e.g., f(x) = x1 XOR x2 XOR x3)
# This function flips the last qubit when the number of 1s in the input is odd
qc.cx(0, n)
qc.cx(1, n)
qc.cx(2, n)

# Apply Hadamard gate to the first n qubits
qc.h(range(n))

# Measure the first n qubits
qc.measure(range(n), range(n))

# Use the Aer simulator to execute the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()

# Get the measurement results
counts = result.get_counts()

# Plot the results
plot_histogram(counts)

# Applications:
# 1. Algorithm Verification: Testing other quantum algorithms.
# 2. Circuit Optimization: Optimizing quantum circuits by verifying constant or balanced functions.
# 3. Pattern Recognition: Determining patterns in binary functions.
# 4. Quantum Computing Education: Teaching the principles of quantum computing.
# 5. Quantum Algorithm Benchmarking: Comparing the efficiency of different quantum algorithms.
