from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit import BasicAer


def get0or1():
    # initialize a quantum register with a single bit
    q = QuantumRegister(1)

    # initialize a classical register with a single bit
    c = ClassicalRegister(1)

    # initialize the quantum circuit
    circuit = QuantumCircuit(q, c)

    # Put the bit into superposition
    circuit.h(q[0])

    # measure the bit
    circuit.measure(q, c)

    # submit job to qasm simulator
    job = execute(circuit, BasicAer.get_backend('qasm_simulator'), shots=1024)

    # determine output
    counts = job.result().get_counts()
    if counts['1'] > counts['0']:
        return 1

    else:
        return 0
