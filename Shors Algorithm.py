# Detailed Explanation of Shor's Algorithm

# Introduction:
# Shor's Algorithm is a quantum algorithm for integer factorization, formulated by Peter Shor in 1994.
# It efficiently solves the problem of finding the prime factors of a given integer N.
# This algorithm is significant because it runs in polynomial time, exponentially faster than the best-known
# classical factoring algorithms. Shor's algorithm forms the basis for quantum computing's potential impact
# on cryptography, particularly RSA encryption.

# Problem Statement:
# Given an integer N, the goal is to find its prime factors. The classical problem is hard to solve efficiently
# for large N, which is why it forms the basis for cryptographic systems.

# Steps of Shor's Algorithm

# 1. Classical Part:
#    - Step 1: Check if N is even. If N is even, return 2.
#    - Step 2: Check if N is a perfect power. If N = a^b, for some integers a > 1 and b > 1, return a.
#    - Step 3: Choose a random integer a such that 1 < a < N. Compute gcd(a, N). If gcd(a, N) != 1, return gcd(a, N)
#      as it is a non-trivial factor of N.

# 2. Quantum Part:
#    - Step 4: Use quantum period-finding subroutine to find the period r of the function f(x) = a^x mod N.
#      1. Initialization:
#         - Prepare two quantum registers:
#           - One register in an equal superposition of states |0⟩ to |q-1⟩, where q is the smallest power of 2
#             such that q ≥ N^2.
#           - The second register initialized to the state |1⟩.
#      2. Modular Exponentiation:
#         - Apply the unitary transformation Uf which maps |x⟩|1⟩ → |x⟩|a^x mod N⟩.
#      3. Quantum Fourier Transform (QFT):
#         - Apply QFT to the first register.
#      4. Measurement:
#         - Measure the first register to obtain a result c.
#      5. Classical Post-processing:
#         - Use continued fractions to determine the period r from the measurement result c.



# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT
from math import gcd
import numpy as np

# Define a function for the classical part of Shor's algorithm
def shors_classical_part(N):
    # Step 1: Check if N is even
    if N % 2 == 0:
        return 2

    # Step 2: Check if N is a perfect power
    for a in range(2, int(np.sqrt(N)) + 1):
        b = 2
        while a ** b <= N:
            if a ** b == N:
                return a
            b += 1

    # Step 3: Choose a random integer a such that 1 < a < N
    a = np.random.randint(2, N)
    d = gcd(a, N)
    if d != 1:
        return d
    return a

# Function to apply the inverse QFT on a quantum circuit
def inverse_qft(qc, n):
    """Apply inverse QFT on the first n qubits in the quantum circuit qc"""
    qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))

# Function to perform the quantum part of Shor's algorithm
def shors_quantum_part(a, N, n_count):
    # Create a quantum circuit with n_count qubits for phase estimation and 1 qubit for the eigenvector
    qc = QuantumCircuit(n_count + 1, n_count)
    
    # Initialize the eigenvector to |1⟩
    qc.x(n_count)
    
    # Apply Hadamard gate to the first n_count qubits
    qc.h(range(n_count))
    
    # Apply controlled unitary operations
    for i in range(n_count):
        qc.cp(2 * np.pi * a ** (2 ** i) % N / N, i, n_count)
    
    # Apply inverse QFT
    inverse_qft(qc, n_count)
    
    # Measure the first n_count qubits
    qc.measure(range(n_count), range(n_count))
    
    # Use the Aer simulator to execute the circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()
    
    # Get the measurement results
    counts = result.get_counts()
    
    # Get the most frequent measurement result
    measured_value = max(counts, key=counts.get)
    
    # Convert the measured value to an integer
    phase = int(measured_value, 2) / (2 ** n_count)
    
    # Estimate the period r
    r = 1 / phase
    
    return int(r)

# Example with N=15 and a=2
N = 15
a = shors_classical_part(N)
if a in [2, 3, 5, 7, 11, 13]:  # Simple factorization cases
    print(f"Found factor: {a}")
else:
    n_count = 3  # Number of qubits for phase estimation
    r = shors_quantum_part(a, N, n_count)
    print(f"Estimated period: {r}")
    
    # Use the estimated period to find the factors of N
    if r % 2 == 0:
        factor1 = gcd(a ** (r // 2) - 1, N)
        factor2 = gcd(a ** (r // 2) + 1, N)
        print(f"Factors of {N} are {factor1} and {factor2}")

# More Complex Example Using Qiskit

# Function to perform the quantum part of Shor's algorithm
def shors_quantum_part_complex(a, N, n_count):
    # Create a quantum circuit with n_count qubits for phase estimation and 1 qubit for the eigenvector
    qc = QuantumCircuit(n_count + 1, n_count)
    
    # Initialize the eigenvector to |1⟩
    qc.x(n_count)
    
    # Apply Hadamard gate to the first n_count qubits
    qc.h(range(n_count))
    
    # Apply controlled unitary operations
    for i in range(n_count):
        qc.cp(2 * np.pi * a ** (2 ** i) % N / N, i, n_count)
    
    # Apply inverse QFT
    inverse_qft(qc, n_count)
    
    # Measure the first n_count qubits
    qc.measure(range(n_count), range(n_count))
    
    # Use the Aer simulator to execute the circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator).result()
    
    # Get the measurement results
    counts = result.get_counts()
    
    # Get the most frequent measurement result
    measured_value = max(counts, key=counts.get)
    
    # Convert the measured value to an integer
    phase = int(measured_value, 2) / (2 ** n_count)
    
    # Estimate the period r
    r = 1 / phase
    
    return int(r)

# Example with N=21 and a=4
N = 21
a = shors_classical_part(N)
if a in [2, 3, 5, 7, 11, 13, 17, 19]:  # Simple factorization cases
    print(f"Found factor: {a}")
else:
    n_count = 4  # Number of qubits for phase estimation
    r = shors_quantum_part_complex(a, N, n_count)
    print(f"Estimated period: {r}")
    
    # Use the estimated period to find the factors of N
    if r % 2 == 0:
        factor1 = gcd(a ** (r // 2) - 1, N)
        factor2 = gcd(a ** (r // 2) + 1, N)
        print(f"Factors of {N} are {factor1} and {factor2}")

# Explanation of Each Line in the Code

# Simple Example
# 1. `from qiskit import QuantumCircuit, Aer, execute`: Import necessary classes from Qiskit.
# 2. `from qiskit.circuit.library import QFT`: Import the Quantum Fourier Transform class.
# 3. `from math import gcd`: Import the greatest common divisor function from the math library.
# 4. `import numpy as np`: Import NumPy for numerical operations.
# 5. `def shors_classical_part(N)`: Define a function for the classical part of Shor's algorithm.
# 6. `if N % 2 == 0`: Check if \( N \) is even.
# 7. `for a in range(2, int(np.sqrt(N)) + 1)`: Check if \( N \) is a perfect power.
# 8. `b = 2`: Initialize \( b \) for checking perfect powers.
# 9. `while a ** b <= N`: Loop to check if \( N \) is a perfect power.
# 10. `if a ** b == N`: If \( N \) is a perfect power, return \( a \).
# 11. `a = np.random.randint(2, N)`: Choose a random integer \( a \) such that \( 1 < a < N \).
# 12. `d = gcd(a, N)`: Compute the greatest common divisor of \( a \) and \( N \).
# 13. `if d != 1`: If \( \gcd(a, N) \neq 1 \), return \( d \) as a non-trivial factor of \( N \).
# 14. `return a`: Return \( a \) for the quantum part if no factor is found.
# 15. `def inverse_qft(qc, n)`: Define a function to apply the inverse QFT on the first \( n \) qubits in the quantum circuit `qc`.
# 16. `qc.append(QFT(num_qubits=n, inverse=True, do_swaps=False), range(n))`: Apply the inverse QFT to the first \( n \) qubits.
# 17. `def shors_quantum_part(a, N, n_count)`: Define a function to perform the quantum part of Shor's algorithm.
# 18. `qc = QuantumCircuit(n_count + 1, n_count)`: Create a quantum circuit with \( n \) qubits for phase estimation and 1 qubit for the eigenvector.
# 19. `qc.x(n_count)`: Initialize the eigenvector to \(|1\rangle\).
# 20. `qc.h(range(n_count))`: Apply a Hadamard gate to the first \( n \) qubits to create superposition.
# 21. `for i in range(n_count)`: Loop to apply controlled unitary operations.
# 22. `qc.cp(2 * np.pi * a ** (2 ** i) % N / N, i, n_count)`: Apply the controlled unitary operation.
# 23. `inverse_qft(qc, n_count)`: Apply the inverse QFT to the first \( n \) qubits.
# 24. `qc.measure(range(n_count), range(n_count))`: Measure the first \( n \) qubits.
# 25. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 26. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 27. `counts = result.get_counts()`: Get the measurement results.
# 28. `measured_value = max(counts, key=counts.get)`: Get the most frequent measurement result.
# 29. `phase = int(measured_value, 2) / (2 ** n_count)`: Convert the measured value to an integer and calculate the phase.
# 30. `r = 1 / phase`: Estimate the period \( r \).
# 31. `N = 15`: Example with \( N = 15 \) and \( a = 2 \).
# 32. `a = shors_classical_part(N)`: Run the classical part of Shor's algorithm.
# 33. `if a in [2, 3, 5, 7, 11, 13]`: Check if \( a \) is a simple factor.
# 34. `print(f"Found factor: {a}")`: Print the found factor.
# 35. `else`: If no simple factor is found, proceed with the quantum part.
# 36. `n_count = 3`: Number of qubits for phase estimation.
# 37. `r = shors_quantum_part(a, N, n_count)`: Run the quantum part of Shor's algorithm.
# 38. `print(f"Estimated period: {r}")`: Print the estimated period.
# 39. `if r % 2 == 0`: Check if the period \( r \) is even.
# 40. `factor1 = gcd(a ** (r // 2) - 1, N)`: Calculate the first factor.
# 41. `factor2 = gcd(a ** (r // 2) + 1, N)`: Calculate the second factor.
# 42. `print(f"Factors of {N} are {factor1} and {factor2}")`: Print the factors of \( N \).

# Complex Example
# 1. `def shors_quantum_part_complex(a, N, n_count)`: Define a function to perform the quantum part of Shor's algorithm.
# 2. `qc = QuantumCircuit(n_count + 1, n_count)`: Create a quantum circuit with \( n \) qubits for phase estimation and 1 qubit for the eigenvector.
# 3. `qc.x(n_count)`: Initialize the eigenvector to \(|1\rangle\).
# 4. `qc.h(range(n_count))`: Apply a Hadamard gate to the first \( n \) qubits to create superposition.
# 5. `for i in range(n_count)`: Loop to apply controlled unitary operations.
# 6. `qc.cp(2 * np.pi * a ** (2 ** i) % N / N, i, n_count)`: Apply the controlled unitary operation.
# 7. `inverse_qft(qc, n_count)`: Apply the inverse QFT to the first \( n \) qubits.
# 8. `qc.measure(range(n_count), range(n_count))`: Measure the first \( n \) qubits.
# 9. `simulator = Aer.get_backend('qasm_simulator')`: Use the Aer simulator to execute the circuit.
# 10. `result = execute(qc, simulator).result()`: Execute the circuit on the simulator.
# 11. `counts = result.get_counts()`: Get the measurement results.
# 12. `measured_value = max(counts, key=counts.get)`: Get the most frequent measurement result.
# 13. `phase = int(measured_value, 2) / (2 ** n_count)`: Convert the measured value to an integer and calculate the phase.
# 14. `r = 1 / phase`: Estimate the period \( r \).
# 15. `N = 21`: Example with \( N = 21 \) and \( a = 4 \).
# 16. `a = shors_classical_part(N)`: Run the classical part of Shor's algorithm.
# 17. `if a in [2, 3, 5, 7, 11, 13, 17, 19]`: Check if \( a \) is a simple factor.
# 18. `print(f"Found factor: {a}")`: Print the found factor.
# 19. `else`: If no simple factor is found, proceed with the quantum part.
# 20. `n_count = 4`: Number of qubits for phase estimation.
# 21. `r = shors_quantum_part_complex(a, N, n_count)`: Run the quantum part of Shor's algorithm.
# 22. `print(f"Estimated period: {r}")`: Print the estimated period.
# 23. `if r % 2 == 0`: Check if the period \( r \) is even.
# 24. `factor1 = gcd(a ** (r // 2) - 1, N)`: Calculate the first factor.
# 25. `factor2 = gcd(a ** (r // 2) + 1, N)`: Calculate the second factor.
# 26. `print(f"Factors of {N} are {factor1} and {factor2}")`: Print the factors of \( N \).

# Conclusion
# Shor's Algorithm efficiently solves the problem of finding the prime factors of a given integer \( N \).
# The provided examples, along with detailed explanations, demonstrate how to implement Shor's Algorithm using Qiskit,
# making it easier to understand each step in the code. This understanding is crucial for developing more advanced quantum algorithms.
