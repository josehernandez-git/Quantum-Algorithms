# Detailed Explanation of the Bernstein-Vazirani Algorithm

# Introduction:
# The Bernstein-Vazirani algorithm is a quantum algorithm that can determine a hidden string s 
# of bits with a single query to the oracle, whereas a classical algorithm would require 
# multiple queries. This algorithm illustrates how quantum computing can achieve exponential 
# speedups over classical approaches.

# Problem Statement:
# Given a function f: {0,1}^n -> {0,1} defined as f(x) = s · x (where s · x is the bitwise 
# inner product modulo 2), determine the hidden string s. The hidden string s is an n-bit string, 
# and x is an n-bit input.

# Steps of the Bernstein-Vazirani Algorithm:
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
#    - Measure the first n qubits. The result will be the hidden string s.

# Quantum Circuit:
# The circuit for the Bernstein-Vazirani algorithm is as follows:
# 1. Initialize n+1 qubits: |0⟩^⊗n ⊗ |1⟩.
# 2. Apply Hadamard gates to all n+1 qubits.
# 3. Apply the oracle Uf.
# 4. Apply Hadamard gates to the first n qubits.
# 5. Measure the first n qubits to get the string s.

# Simple Example Using Qiskit

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Number of qubits for the input (n)
n = 3

# Create a quantum circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for s = 101 (hidden string)
# The oracle flips the phase of the output qubit based on the input qubits
# In this case, Uf applies a CNOT gate for each 1 in the hidden string s
qc.cx(0, n)
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

# More Complex Example Using Qiskit

# In this example, we'll consider an oracle for a different hidden string.

# Number of qubits for the input (n)
n = 4

# Create a quantum circuit with n+1 qubits and n classical bits
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for s = 1101 (hidden string)
# The oracle flips the phase of the output qubit based on the input qubits
# In this case, Uf applies a CNOT gate for each 1 in the hidden string s
qc.cx(0, n)
qc.cx(1, n)
qc.cx(3, n)

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
# 3. `n = 3`: Define the number of input qubits.
# 4. `qc = QuantumCircuit(n + 1, n)`: Create a quantum circuit with n+1 qubits and n classical bits.
# 5. `qc.x(n)`: Initialize the last qubit in the state |1⟩.
# 6. `qc.h(range(n + 1))`: Apply a Hadamard gate to all n+1 qubits to create superposition.
# 7. Apply the oracle Uf for the hidden string s = 101. In this case, the oracle applies CNOT gates for each 1 in the hidden string s.
# 8. `qc.cx(0, n)`: Apply a CNOT gate with the first qubit as control and the last qubit as target.
# 9. `qc.cx(2, n)`: Apply a CNOT gate with the third qubit as control and the last qubit as target.
# 10. `qc.h(range(n))`: Apply a Hadamard gate to the first n qubits.
# 11. `qc.measure(range(n), range(n))`: Measure the first n qubits.
# 12. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 13. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 14. `counts = result.get_counts()`: Get the measurement results.
# 15. `plot_histogram(counts)`: Plot the measurement results.

# Complex Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.visualization import plot_histogram`: Import the function to visualize the results.
# 3. `n = 4`: Define the number of input qubits.
# 4. `qc = QuantumCircuit(n + 1, n)`: Create a quantum circuit with n+1 qubits and n classical bits.
# 5. `qc.x(n)`: Initialize the last qubit in the state |1⟩.
# 6. `qc.h(range(n + 1))`: Apply a Hadamard gate to all n+1 qubits to create superposition.
# 7. Apply the oracle Uf for the hidden string s = 1101. In this case, the oracle applies CNOT gates for each 1 in the hidden string s.
# 8. `qc.cx(0, n)`: Apply a CNOT gate with the first qubit as control and the last qubit as target.
# 9. `qc.cx(1, n)`: Apply a CNOT gate with the second qubit as control and the last qubit as target.
# 10. `qc.cx(3, n)`: Apply a CNOT gate with the fourth qubit as control and the last qubit as target.
# 11. `qc.h(range(n))`: Apply a Hadamard gate to the first n qubits.
# 12. `qc.measure(range(n), range(n))`: Measure the first n qubits.
# 13. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 14. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 15. `counts = result.get_counts()`: Get the measurement results.
# 16. `plot_histogram(counts)`: Plot the measurement results.

# Conclusion
# The Bernstein-Vazirani Algorithm leverages quantum parallelism to determine a hidden string with a single 
# query to the oracle. The simple and complex examples provided demonstrate how to implement this algorithm 
# using Qiskit, with detailed explanations for each step in the code. This understanding lays the foundation 
# for more advanced quantum algorithms.
