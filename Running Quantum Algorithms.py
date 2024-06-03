"""
Running Quantum Algorithms: Local Simulation vs. IBMQ

### Local Simulation

1. **Quantum Simulators**:
   - **Advantages**:
     - **Accessibility**: No need for an internet connection.
     - **Cost-Effective**: Free to use.
     - **Development**: Easier to debug and develop algorithms.
     - **Speed**: Faster execution for small-scale problems (since they run on classical computers).
   - **Limitations**:
     - **Scale**: Limited by the classical computing resources. Simulating large quantum systems (beyond 30-40 qubits) becomes impractical.
     - **Realism**: Simulators do not perfectly replicate all noise and imperfections present in actual quantum hardware.

2. **Popular Simulators**:
   - **Qiskit Aer**: Provided by IBM, it allows you to simulate quantum circuits on your local machine.
   - **Forest**: Provided by Rigetti, it includes a simulator called `quilc`.
   - **Cirq**: Provided by Google, includes a simulator for quantum circuits.

### Running on Actual Quantum Hardware (IBMQ)

1. **IBM Quantum Experience (IBMQ)**:
   - **Advantages**:
     - **Realism**: Provides access to real quantum processors, giving insight into how quantum algorithms perform on actual hardware.
     - **Scalability**: Can handle more qubits than classical simulators.
   - **Limitations**:
     - **Accessibility**: Requires an internet connection and an IBM Quantum account.
     - **Cost**: There might be costs associated with accessing larger quantum systems or more computing time.
     - **Queue Times**: Running on actual quantum hardware may involve waiting in a queue.
     - **Noise**: Real quantum computers have noise and error rates that can affect the results.

2. **How to Use IBMQ**:
   - **Qiskit**: A Python library provided by IBM that allows you to create, simulate, and run quantum circuits on IBM quantum computers.
   - **Steps**:
     - **Create an IBM Quantum Account**: Sign up on the IBM Quantum Experience website.
     - **Obtain API Token**: Use the token to access IBMQ services through Qiskit.
     - **Code Example**:
       ```python
       from qiskit import IBMQ, Aer, execute
       from qiskit import QuantumCircuit

       # Load your IBMQ account
       IBMQ.save_account('YOUR_API_TOKEN')
       IBMQ.load_account()

       provider = IBMQ.get_provider(hub='ibm-q')
       backend = provider.get_backend('ibmq_qasm_simulator')

       # Create a quantum circuit
       qc = QuantumCircuit(2, 2)
       qc.h(0)
       qc.cx(0, 1)
       qc.measure([0, 1], [0, 1])

       # Execute the circuit on the backend
       job = execute(qc, backend)
       result = job.result()

       print(result.get_counts())
       ```

### Conclusion

- **Local Simulation**: Ideal for development, testing, and small-scale quantum problems.
- **Running on IBMQ**: Essential for testing how algorithms perform on real quantum hardware, especially for larger problems that are impractical to simulate classically.

For best practices, develop and debug your quantum algorithms locally using simulators, and then run them on actual quantum hardware to validate their performance in real-world conditions. This hybrid approach leverages the strengths of both methods.
"""


from qiskit import IBMQ, Aer, execute
from qiskit import QuantumCircuit

# Load your IBMQ account
IBMQ.save_account('YOUR_API_TOKEN')
IBMQ.load_account()

provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')

# Create a quantum circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Execute the circuit on the backend
job = execute(qc, backend)
result = job.result()

print(result.get_counts())
