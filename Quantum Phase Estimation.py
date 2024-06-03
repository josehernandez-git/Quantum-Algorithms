# Detailed Explanation of the Quantum Phase Estimation (QPE) Algorithm

# Introduction:
# The Quantum Phase Estimation (QPE) algorithm is a fundamental quantum algorithm that estimates the phase (or eigenvalue)
# of an eigenvector of a unitary operator. It is a crucial component in several important quantum algorithms, such as Shor's
# algorithm for factoring and the quantum algorithm for solving linear systems of equations.

# Problem Statement:
# Given a unitary operator U and an eigenvector |u⟩ such that U|u⟩ = e^(2πiθ)|u⟩ for some unknown phase θ (0 ≤ θ < 1),
# the goal of QPE is to estimate the value of θ.

# Steps of the QPE Algorithm:
# 1. Initialization:
#    - Start with two registers: 
#      - An n-qubit register initialized to |0⟩^⊗n.
#      - An m-qubit register initialized to the eigenvector |u⟩ of U.
# 2. Apply Hadamard Gates:
#    - Apply a Hadamard gate to each qubit in the first register, creating a superposition of all possible states.
# 3. Apply Controlled Unitary Operations:
#    - Apply controlled unitary operations U^(2^j) (where j ranges from 0 to n-1) to the second register, controlled by
#      the corresponding qubit in the first register.
# 4. Apply Inverse Quantum Fourier Transform (QFT):
#    - Apply the inverse QFT to the first register.
# 5. Measurement:
#    - Measure the first register to obtain an n-bit approximation of the phase θ.

# Quantum Circuit:
# The QPE circuit consists of Hadamard gates, controlled unitary operations, and the inverse QFT, followed by measurements.
# The circuit depth is O(n^2).

# Simple Example Using Qiskit

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
import numpy as np

# Function to apply the inverse QFT on a quantum circuit
def inverse_qft(qc, n):
    """Apply inverse QFT on the first n qubits in the quantum circuit qc"""
    qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))

# Create a quantum circuit with 3 qubits for phase estimation and 1 qubit for the eigenvector
qc = QuantumCircuit(4, 3)

# Initialize the eigenvector to |1⟩
qc.x(3)

# Apply Hadamard gate to the first 3 qubits
qc.h(range(3))

# Apply controlled unitary operations
# For a simple example, let's use a phase gate Rz(2π/8)
for i in range(3):
    qc.cp(2 * np.pi / 2**(i+1), i, 3)

# Apply inverse QFT
inverse_qft(qc, 3)

# Measure the first 3 qubits
qc.measure(range(3), range(3))

# Use the Aer simulator to execute the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()

# Get the measurement results
counts = result.get_counts()

# Plot the results
plot_histogram(counts)

# More Complex Example Using Qiskit

# Function to apply the inverse QFT on a quantum circuit
def inverse_qft(qc, n):
    """Apply inverse QFT on the first n qubits in the quantum circuit qc"""
    qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))

# Create a quantum circuit with 4 qubits for phase estimation and 1 qubit for the eigenvector
qc = QuantumCircuit(5, 4)

# Initialize the eigenvector to |1⟩
qc.x(4)

# Apply Hadamard gate to the first 4 qubits
qc.h(range(4))

# Apply controlled unitary operations
# For a more complex example, let's use a different unitary gate
for i in range(4):
    qc.cp(2 * np.pi / 2**(i+1), i, 4)

# Apply inverse QFT
inverse_qft(qc, 4)

# Measure the first 4 qubits
qc.measure(range(4), range(4))

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
# 2. `from qiskit.circuit.library import QFT`: Import the Quantum Fourier Transform class.
# 3. `from qiskit.visualization import plot_histogram`: Import the function to visualize the results.
# 4. `import numpy as np`: Import NumPy for numerical operations.
# 5. `def inverse_qft(qc, n)`: Define a function to apply the inverse QFT on the first n qubits in the quantum circuit qc.
# 6. `qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))`: Apply the inverse QFT to the first n qubits.
# 7. `qc = QuantumCircuit(4, 3)`: Create a quantum circuit with 4 qubits (3 for phase estimation and 1 for the eigenvector) and 3 classical bits for measurement.
# 8. `qc.x(3)`: Initialize the eigenvector to |1⟩.
# 9. `qc.h(range(3))`: Apply a Hadamard gate to the first 3 qubits to create superposition.
# 10. Apply controlled unitary operations: Use a phase gate Rz(2π/8) controlled by the first 3 qubits.
# 11. `inverse_qft(qc, 3)`: Apply the inverse QFT to the first 3 qubits.
# 12. `qc.measure(range(3), range(3))`: Measure the first 3 qubits.
# 13. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 14. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 15. `counts = result.get_counts()`: Get the measurement results.
# 16. `plot_histogram(counts)`: Plot the measurement results.

# Complex Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.circuit.library import QFT`: Import the Quantum Fourier Transform class.
# 3. `from qiskit.visualization import plot_histogram`: Import the function to visualize the results.
# 4. `import numpy as np`: Import NumPy for numerical operations.
# 5. `def inverse_qft(qc, n)`: Define a function to apply the inverse QFT on the first n qubits in the quantum circuit qc.
# 6. `qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))`: Apply the inverse QFT to the first n qubits.
# 7. `qc = QuantumCircuit(5, 4)`: Create a quantum circuit with 5 qubits (4 for phase estimation and 1 for the eigenvector) and 4 classical bits for measurement.
# 8. `qc.x(4)`: Initialize the eigenvector to |1⟩.
# 9. `qc.h(range(4))`: Apply a Hadamard gate to the first 4 qubits to create superposition.
# 10. Apply controlled unitary operations: Use a different unitary gate controlled by the first 4 qubits.
# 11. `inverse_qft(qc, 4)`: Apply the inverse QFT to the first 4 qubits.
# 12. `qc.measure(range(4), range(4))`: Measure the first 4 qubits.
# 13. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 14. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 15. `counts = result.get_counts()`: Get the measurement results.
# 16. `plot_histogram(counts)`: Plot the measurement results.

# Conclusion
# The Quantum Phase Estimation (QPE) algorithm is a fundamental quantum algorithm that estimates the phase of an
# eigenvector of a unitary operator. The provided examples, along with detailed explanations, demonstrate how to
# implement QPE using Qiskit, making it easier to understand each step in the code. This understanding is crucial
# for developing more advanced quantum algorithms.
