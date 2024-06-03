# Detailed Explanation of the Deutsch-Jozsa Algorithm

# Introduction:
# The Deutsch-Jozsa Algorithm is an extension of the original Deutsch Algorithm.
# It is one of the first examples demonstrating a quantum algorithm that solves a problem
# exponentially faster than any classical algorithm. The problem involves determining whether 
# a given function f: {0,1}^n -> {0,1} is constant (same output for all inputs) or balanced 
# (outputs 0 for half of the inputs and 1 for the other half).

# Problem Statement:
# Given a function f that maps {0,1}^n to {0,1}, determine if f is constant or balanced.
# Classically, this requires checking at least half of the possible inputs, but the 
# Deutsch-Jozsa algorithm can solve this with a single evaluation.

# Steps of the Deutsch-Jozsa Algorithm:
# 1. Initialization:
#    - Start with n+1 qubits in the state |0⟩^⊗n ⊗ |1⟩.
# 2. Apply Hadamard Gates:
#    - Apply a Hadamard gate to each of the n+1 qubits. The first n qubits transform into 
#      an equal superposition of all possible n-bit strings. The last qubit transforms to 
#      (|0⟩ - |1⟩)/√2.
# 3. Oracle Application:
#    - Apply the oracle Uf which encodes the function f into the quantum state. The oracle 
#      maps |x⟩|y⟩ -> |x⟩|y ⊕ f(x)⟩.
# 4. Apply Hadamard Gates to the First n Qubits:
#    - Apply a Hadamard gate to each of the first n qubits.
# 5. Measurement:
#    - Measure the first n qubits. If the result is the all-zero state |0⟩^⊗n, f is constant. 
#      Otherwise, f is balanced.

# Quantum Circuit:
# The circuit for the Deutsch-Jozsa algorithm is as follows:
# 1. Initialize n+1 qubits: |0⟩^⊗n ⊗ |1⟩.
# 2. Apply Hadamard gates to all n+1 qubits.
# 3. Apply the oracle Uf.
# 4. Apply Hadamard gates to the first n qubits.
# 5. Measure the first n qubits.

# Simple Example Using Qiskit

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Number of qubits for the input (n)
n = 2

# Create a quantum circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for a constant function (e.g., f(x) = 0)
# For a constant function, the oracle does nothing
# Example: no gate is needed for a constant zero function

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

# More Complex Example Using Qiskit

# In this example, we'll consider an oracle for a balanced function.

# Number of qubits for the input (n)
n = 2

# Create a quantum circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for a balanced function (e.g., f(x) = x1 XOR x2)
# This function flips the last qubit when the number of 1s in the input is odd
qc.cx(0, n)
qc.cx(1, n)

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

# Explanation of Each Line in the Code

# Simple Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.visualization import plot_histogram`: Import the function to visualize the results.
# 3. `n = 2`: Define the number of input qubits.
# 4. `qc = QuantumCircuit(n + 1, n)`: Create a quantum circuit with n+1 qubits and n classical bits.
# 5. `qc.x(n)`: Initialize the last qubit in the state |1⟩.
# 6. `qc.h(range(n + 1))`: Apply a Hadamard gate to all n+1 qubits to create superposition.
# 7. Apply the oracle Uf for a constant function. In this example, no gate is needed as the function is constant.
# 8. `qc.h(range(n))`: Apply a Hadamard gate to the first n qubits.
# 9. `qc.measure(range(n), range(n))`: Measure the first n qubits.
# 10. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 11. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 12. `counts = result.get_counts()`: Get the measurement results.
# 13. `plot_histogram(counts)`: Plot the measurement results.

# Complex Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.visualization import plot_histogram`: Import the function to visualize the results.
# 3. `n = 2`: Define the number of input qubits.
# 4. `qc = QuantumCircuit(n + 1, n)`: Create a quantum circuit with n+1 qubits and n classical bits.
# 5. `qc.x(n)`: Initialize the last qubit in the state |1⟩.
# 6. `qc.h(range(n + 1))`: Apply a Hadamard gate to all n+1 qubits to create superposition.
# 7. `qc.cx(0, n)`: Apply a CNOT gate with the first qubit as control and the last qubit as target.
# 8. `qc.cx(1, n)`: Apply another CNOT gate with the second qubit as control and the last qubit as target.
# 9. `qc.h(range(n))`: Apply a Hadamard gate to the first n qubits.
# 10. `qc.measure(range(n), range(n))`: Measure the first n qubits.
# 11. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 12. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 13. `counts = result.get_counts()`: Get the measurement results.
# 14. `plot_histogram(counts)`: Plot the measurement results.

# Conclusion
# The Deutsch-Jozsa Algorithm leverages quantum parallelism to determine if a function is constant or balanced 
# with a single query to the oracle. The simple and complex examples provided demonstrate how to implement this 
# algorithm using Qiskit, with detailed explanations for each step in the code. This understanding lays the 
# foundation for more advanced quantum algorithms.
