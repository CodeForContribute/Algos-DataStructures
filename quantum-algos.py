"""quantum-algos.py

This module implements simple quantum algorithms without external dependencies.
Every line contains a descriptive inline comment to explain the underlying logic.
"""

from __future__ import annotations  # Enables forward references in type annotations.

import math  # Supplies square root and pi constants for amplitude calculations.
from typing import List  # Provides type hints for readability.

Vector = List[complex]  # Alias for one-dimensional quantum states.
Matrix = List[List[complex]]  # Alias for square matrices representing gates.

EPSILON: float = 1e-9  # Small threshold used for floating point comparisons.


def create_basis_state(num_qubits: int, index: int) -> Vector:
    """Create a computational basis state with a single amplitude set to one."""
    dimension: int = 2 ** num_qubits  # Determine how many amplitudes are needed.
    state: Vector = [0j] * dimension  # Allocate the vector in one step for improved locality.
    state[index] = 1 + 0j  # Activate the requested basis state by setting its amplitude to one.
    return state  # Return the fully constructed state vector.


def hadamard() -> Matrix:
    """Return the single-qubit Hadamard gate as a 2x2 matrix."""
    coefficient: float = 1 / math.sqrt(2)  # Calculate the normalization constant.
    return [  # Build the matrix explicitly.
        [coefficient + 0j, coefficient + 0j],  # First row of the Hadamard gate.
        [coefficient + 0j, -coefficient + 0j],  # Second row accounts for the phase inversion.
    ]


def kronecker_product(a: Matrix, b: Matrix) -> Matrix:
    """Compute the Kronecker product between two matrices."""
    return [  # Build the result row by row using nested comprehensions to avoid append overhead.
        [value_a * value_b for value_a in row_a for value_b in row_b]  # Multiply each pair of entries to form the block row.
        for row_a in a  # Iterate over every row of the first matrix.
        for row_b in b  # For each row in the second matrix, expand the block structure.
    ]


def tensor_power(matrix: Matrix, count: int) -> Matrix:
    """Repeatedly apply the Kronecker product to build an n-qubit operator."""
    result: Matrix = matrix  # Start from the original matrix.
    for _ in range(1, count):  # Repeat count-1 times to reach the desired power.
        result = kronecker_product(result, matrix)  # Expand the operator at each step.
    return result  # Return the final tensor power.


HADAMARD_CACHE: dict[int, Matrix] = {}  # Cache to avoid rebuilding identical transforms.


def hadamard_n(num_qubits: int) -> Matrix:
    """Return the tensor product of num_qubits Hadamard gates."""
    if num_qubits not in HADAMARD_CACHE:  # Check whether the value was already computed.
        HADAMARD_CACHE[num_qubits] = tensor_power(hadamard(), num_qubits)  # Store the freshly built matrix.
    return HADAMARD_CACHE[num_qubits]  # Reuse the cached matrix when possible.


def apply_gate(state: Vector, gate: Matrix) -> Vector:
    """Apply a gate matrix to a state vector using matrix-vector multiplication."""
    return [  # Build the resulting vector using a comprehension for tighter loops.
        sum(value * basis_amplitude for value, basis_amplitude in zip(row, state))  # Perform the dot product for each row.
        for row in gate  # Iterate over every row of the gate matrix.
    ]  # Return the evolved quantum state.


def measure_probabilities(state: Vector) -> List[float]:
    """Compute the measurement probability for every basis state."""
    return [abs(amplitude) ** 2 for amplitude in state]  # Square magnitudes to obtain probabilities.


def identity_matrix(size: int) -> Matrix:
    """Create an identity matrix of arbitrary size."""
    return [  # Construct the matrix using a nested comprehension to minimize Python overhead.
        [1 + 0j if row_index == column_index else 0j for column_index in range(size)]  # Place ones on the diagonal.
        for row_index in range(size)  # Iterate over every row index.
    ]  # Return the identity matrix.


def deutsch_jozsa(oracle: Matrix) -> bool:
    """Run the Deutsch-Jozsa algorithm and decide whether the oracle is constant.

    Reference: https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
    """
    state: Vector = create_basis_state(2, 1)  # Prepare the |0⟩|1⟩ input state.
    hadamard_two: Matrix = kronecker_product(hadamard(), hadamard())  # Build the two-qubit Hadamard transform.
    state = apply_gate(state, hadamard_two)  # Apply Hadamards to create a superposition on both qubits.
    state = apply_gate(state, oracle)  # Query the oracle exactly once.
    first_qubit_hadamard: Matrix = kronecker_product(hadamard(), identity_matrix(2))  # Apply Hadamard to the first qubit only.
    state = apply_gate(state, first_qubit_hadamard)  # Finish the algorithm by transforming the first qubit again.
    probabilities: List[float] = measure_probabilities(state)  # Determine measurement probabilities for each basis state.
    half: int = len(probabilities) // 2  # Compute the number of states where the first qubit equals zero.
    return sum(probabilities[:half]) > 1 - EPSILON  # Constant functions yield the first qubit as |0⟩ with near certainty.


def balanced_oracle() -> Matrix:
    """Construct an oracle for the balanced function f(x) = x.

    Reference: https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
    """
    oracle: Matrix = identity_matrix(4)  # Start from the 4x4 identity matrix.
    oracle[2][2] = 0j  # Clear the entry for |10⟩ to prepare for the target flip.
    oracle[3][3] = 0j  # Clear the entry for |11⟩ for the same reason.
    oracle[2][3] = 1 + 0j  # Map |10⟩ to |11⟩ by flipping the second qubit.
    oracle[3][2] = 1 + 0j  # Map |11⟩ to |10⟩, completing the controlled-NOT behavior.
    return oracle  # Return the completed balanced oracle.


def constant_oracle() -> Matrix:
    """Construct an oracle representing the constant zero function.

    Reference: https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html
    """
    return identity_matrix(4)  # The identity matrix leaves the target qubit unchanged.


def phase_oracle(num_qubits: int, marked_index: int) -> Matrix:
    """Create a phase oracle that negates the amplitude of the marked basis state.

    Reference: https://qiskit.org/textbook/ch-algorithms/grover.html
    """
    size: int = 2 ** num_qubits  # Determine the dimension of the search space.
    oracle: Matrix = identity_matrix(size)  # Start with the identity operator.
    oracle[marked_index][marked_index] = -1 + 0j  # Place a -1 on the marked state's diagonal entry.
    return oracle  # Provide the oracle matrix.


def outer_product(vector: Vector) -> Matrix:
    """Compute the outer product |v⟩⟨v| for the provided vector."""
    return [  # Build the matrix row by row using comprehensions for cache-friendly iteration.
        [amplitude_row * amplitude_column.conjugate() for amplitude_column in vector]  # Multiply by the conjugate for Hermitian symmetry.
        for amplitude_row in vector  # Iterate over every amplitude for the rows.
    ]  # Return the projector matrix.


def subtract_matrices(a: Matrix, b: Matrix) -> Matrix:
    """Subtract two matrices element-wise."""
    return [  # Construct the difference using comprehensions to reduce Python-level bookkeeping.
        [value_a - value_b for value_a, value_b in zip(row_a, row_b)]  # Subtract the entries component-wise.
        for row_a, row_b in zip(a, b)  # Pair up each row from both matrices.
    ]  # Return the resulting matrix.


def scale_matrix(matrix: Matrix, scalar: complex) -> Matrix:
    """Multiply every element of a matrix by a scalar."""
    return [[scalar * value for value in row] for row in matrix]  # Apply the scalar to each entry.


def diffusion_operator(num_qubits: int) -> Matrix:
    """Construct Grover's diffusion operator for the given number of qubits.

    Reference: https://qiskit.org/textbook/ch-algorithms/grover.html
    """
    size: int = 2 ** num_qubits  # Determine the dimension of the search space.
    uniform_weight: complex = (2 / size) + 0j  # Each entry in 2|s⟩⟨s| equals 2 divided by the number of states.
    return [  # Build the diffusion matrix directly without intermediate multiplications.
        [  # Construct each row explicitly.
            (uniform_weight - 1 + 0j) if row_index == column_index else uniform_weight  # Diagonal entries subtract one, off-diagonals share the uniform weight.
            for column_index in range(size)  # Iterate over every column index.
        ]
        for row_index in range(size)  # Iterate over every row index.
    ]  # Return the diffusion operator.


def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two square matrices."""
    columns_b: List[tuple[complex, ...]] = [tuple(column) for column in zip(*b)]  # Cache the columns of matrix B for reuse.
    return [  # Build the resulting matrix row by row.
        [sum(value_a * value_b for value_a, value_b in zip(row_a, column_b)) for column_b in columns_b]  # Compute each dot product using zipped pairs.
        for row_a in a  # Iterate over every row of matrix A.
    ]  # Return the matrix product.


def transpose_conjugate(matrix: Matrix) -> Matrix:
    """Compute the conjugate transpose (Hermitian adjoint) of a matrix."""
    return [  # Build the transposed matrix using zip for cache-friendly access.
        [value.conjugate() for value in column]  # Take the complex conjugate while iterating over each column.
        for column in zip(*matrix)  # Transpose by zipping the rows of the original matrix.
    ]  # Return the conjugate transpose.


def grover_iteration(num_qubits: int, oracle: Matrix, iterations: int) -> Vector:
    """Run Grover's search algorithm for a fixed number of iterations.

    Reference: https://qiskit.org/textbook/ch-algorithms/grover.html
    """
    state: Vector = create_basis_state(num_qubits, 0)  # Begin with the |0...0⟩ state.
    hadamard_full: Matrix = hadamard_n(num_qubits)  # Build the full Hadamard transform.
    state = apply_gate(state, hadamard_full)  # Place the state into an equal superposition.
    diffusion: Matrix = diffusion_operator(num_qubits)  # Pre-compute the diffusion operator.
    for _ in range(iterations):  # Repeat the Grover steps as requested.
        state = apply_gate(state, oracle)  # Apply the oracle to mark the solution.
        state = apply_gate(state, diffusion)  # Reflect about the mean amplitude.
    return state  # Return the final state vector.


def most_probable_state(state: Vector) -> int:
    """Identify the basis index with the highest measurement probability."""
    probabilities: List[float] = measure_probabilities(state)  # Compute measurement probabilities.
    return max(range(len(probabilities)), key=probabilities.__getitem__)  # Let Python's optimized max locate the best index.


def run_grover(num_qubits: int, marked_index: int) -> int:
    """Execute Grover's algorithm with the recommended number of iterations.

    Reference: https://qiskit.org/textbook/ch-algorithms/grover.html
    """
    size: int = 2 ** num_qubits  # Determine how many elements are being searched.
    iterations: int = max(1, int(math.floor((math.pi / 4) * math.sqrt(size))))  # Use the standard floor-based heuristic.
    oracle: Matrix = phase_oracle(num_qubits, marked_index)  # Build the oracle that marks the desired state.
    final_state: Vector = grover_iteration(num_qubits, oracle, iterations)  # Run Grover's algorithm.
    return most_probable_state(final_state)  # Report the most probable measurement outcome.
