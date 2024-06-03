# Quantum Fourier Transform (QFT)

# Explanation:
# The Quantum Fourier Transform (QFT) is the quantum analog of the discrete Fourier transform (DFT).
# It transforms a quantum state into a superposition of phases, which is a key component in many quantum algorithms,
# such as Shor's algorithm and the quantum phase estimation algorithm.

# Qiskit Usage:
# The QFT can be implemented using a sequence of Hadamard gates and controlled phase rotation gates.

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

# Applications:
# 1. Phase Estimation: Estimating the phase of eigenvalues of a unitary operator.
# 2. Period Finding: Identifying the period of a periodic function, which is a key component of Shor's algorithm.
# 3. Signal Processing: Transforming time-domain signals into frequency-domain signals in quantum signal processing.
# 4. Cryptographic Analysis: Analyzing cryptographic protocols that rely on periodicity.
# 5. Quantum Simulations: Simulating the dynamics of quantum systems by transforming states into frequency domains.
