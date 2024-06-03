# Bernstein-Vazirani Algorithm

# Explanation:
# The Bernstein-Vazirani Algorithm is a quantum algorithm that determines a hidden string s of bits with a single query to the oracle,
# whereas a classical algorithm would require multiple queries.

# Qiskit Usage:
# The Bernstein-Vazirani algorithm uses Hadamard gates and an oracle to determine the hidden string.

# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with n+1 qubits and n classical bits
n = 4
qc = QuantumCircuit(n + 1, n)

# Initialize last qubit in state |1⟩
qc.x(n)

# Apply Hadamard gate to all qubits
qc.h(range(n + 1))

# Apply the oracle Uf for s = 1101 (hidden string)
# The oracle flips the phase of the output qubit based on the input qubits
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

# Applications:
# 1. Hidden Pattern Detection: Identifying hidden patterns in binary strings.
# 2. Cryptography: Testing cryptographic protocols involving hidden strings.
# 3. Quantum Circuit Validation: Validating the correctness of quantum circuits.
# 4. Algorithm Efficiency Testing: Comparing quantum and classical algorithm efficiencies.
# 5. Quantum Education: Teaching principles of quantum algorithms and hidden pattern detection.
