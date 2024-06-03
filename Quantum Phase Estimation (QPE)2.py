# Quantum Phase Estimation (QPE)

# Explanation:
# Quantum Phase Estimation (QPE) estimates the phase (or eigenvalue) of an eigenvector of a unitary operator.
# It is a fundamental algorithm used in various applications, such as Shor's algorithm and quantum simulations.

# Qiskit Usage:
# QPE uses controlled unitary operations and the Quantum Fourier Transform (QFT) to estimate the phase.

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

# Applications:
# 1. Shor's Algorithm: Finding the period of a function for integer factorization.
# 2. Quantum Simulations: Estimating the eigenvalues of Hamiltonians in quantum chemistry.
# 3. Cryptographic Protocols: Analyzing protocols that rely on phase estimation.
# 4. Machine Learning: Implementing quantum algorithms for machine learning that involve phase estimation.
# 5. Quantum Metrology: Improving precision measurements in quantum sensing and metrology.
