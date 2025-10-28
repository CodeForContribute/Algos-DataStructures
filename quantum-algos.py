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
    state: Vector = [0j for _ in range(dimension)]  # Start with all-zero complex amplitudes.
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
    result: Matrix = []  # Prepare a container for the expanded matrix.
    for row_a in a:  # Iterate over each row of the first matrix.
        for row_b in b:  # Iterate over each row of the second matrix.
            new_row: List[complex] = []  # Assemble the resulting row entry by entry.
            for value_a in row_a:  # Process each value from the current row of matrix A.
                for value_b in row_b:  # Multiply with each value from the current row of matrix B.
                    new_row.append(value_a * value_b)  # Append the product to build the Kronecker row.
            result.append(new_row)  # Store the completed row.
    return result  # Provide the Kronecker product matrix.


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
    new_state: Vector = []  # Prepare the container for the resulting state.
    for row in gate:  # Iterate over each row of the gate matrix.
        amplitude: complex = 0j  # Start the dot product at zero.
        for value, basis_amplitude in zip(row, state):  # Pair each matrix entry with the state amplitude.
            amplitude += value * basis_amplitude  # Accumulate the contribution to the new amplitude.
        new_state.append(amplitude)  # Append the finished amplitude to the result vector.
    return new_state  # Return the evolved quantum state.


def measure_probabilities(state: Vector) -> List[float]:
    """Compute the measurement probability for every basis state."""
    return [abs(amplitude) ** 2 for amplitude in state]  # Square magnitudes to obtain probabilities.


def identity_matrix(size: int) -> Matrix:
    """Create an identity matrix of arbitrary size."""
    matrix: Matrix = []  # Prepare the outer list of rows.
    for row_index in range(size):  # Iterate through each row index.
        row: List[complex] = []  # Create a fresh row container.
        for column_index in range(size):  # Iterate through each column index.
            value: complex = (1 + 0j) if row_index == column_index else 0j  # Place ones on the diagonal and zeros elsewhere.
            row.append(value)  # Store the computed value in the row.
        matrix.append(row)  # Append the completed row to the matrix.
    return matrix  # Return the identity matrix.


def deutsch_jozsa(oracle: Matrix) -> bool:
    """Run the Deutsch-Jozsa algorithm and decide whether the oracle is constant."""
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
    """Construct an oracle for the balanced function f(x) = x."""
    oracle: Matrix = identity_matrix(4)  # Start from the 4x4 identity matrix.
    oracle[2][2] = 0j  # Clear the entry for |10⟩ to prepare for the target flip.
    oracle[3][3] = 0j  # Clear the entry for |11⟩ for the same reason.
    oracle[2][3] = 1 + 0j  # Map |10⟩ to |11⟩ by flipping the second qubit.
    oracle[3][2] = 1 + 0j  # Map |11⟩ to |10⟩, completing the controlled-NOT behaviour.
    return oracle  # Return the completed balanced oracle.


def constant_oracle() -> Matrix:
    """Construct an oracle representing the constant zero function."""
    return identity_matrix(4)  # The identity matrix leaves the target qubit unchanged.


def phase_oracle(num_qubits: int, marked_index: int) -> Matrix:
    """Create a phase oracle that negates the amplitude of the marked basis state."""
    size: int = 2 ** num_qubits  # Determine the dimension of the search space.
    oracle: Matrix = identity_matrix(size)  # Start with the identity operator.
    oracle[marked_index][marked_index] = -1 + 0j  # Place a -1 on the marked state's diagonal entry.
    return oracle  # Provide the oracle matrix.


def outer_product(vector: Vector) -> Matrix:
    """Compute the outer product |v⟩⟨v| for the provided vector."""
    matrix: Matrix = []  # Prepare the resulting matrix.
    for amplitude_row in vector:  # Iterate over each amplitude for the rows.
        row: List[complex] = []  # Create the row container.
        for amplitude_column in vector:  # Iterate over each amplitude for the columns.
            row.append(amplitude_row * amplitude_column.conjugate())  # Multiply with the complex conjugate for Hermitian symmetry.
        matrix.append(row)  # Append the completed row to the outer product matrix.
    return matrix  # Return the projector matrix.


def subtract_matrices(a: Matrix, b: Matrix) -> Matrix:
    """Subtract two matrices element-wise."""
    result: Matrix = []  # Prepare a container for the difference.
    for row_a, row_b in zip(a, b):  # Pair rows from both matrices.
        row: List[complex] = []  # Create a row for the result.
        for value_a, value_b in zip(row_a, row_b):  # Iterate over corresponding entries.
            row.append(value_a - value_b)  # Subtract values component-wise.
        result.append(row)  # Append the row to the result matrix.
    return result  # Return the resulting matrix.


def scale_matrix(matrix: Matrix, scalar: complex) -> Matrix:
    """Multiply every element of a matrix by a scalar."""
    return [[scalar * value for value in row] for row in matrix]  # Apply the scalar to each entry.


def diffusion_operator(num_qubits: int) -> Matrix:
    """Construct Grover's diffusion operator for the given number of qubits."""
    hadamard_full: Matrix = hadamard_n(num_qubits)  # Build the full Hadamard transform.
    zero_state: Vector = create_basis_state(num_qubits, 0)  # Prepare the |0...0⟩ state vector.
    projector: Matrix = outer_product(zero_state)  # Compute the projector onto |0...0⟩.
    identity: Matrix = identity_matrix(len(projector))  # Build an identity matrix of matching size.
    reflection: Matrix = subtract_matrices(scale_matrix(projector, 2 + 0j), identity)  # Compute 2|0⟩⟨0| - I.
    temp: Matrix = matrix_multiply(hadamard_full, reflection)  # Multiply Hadamard by the reflection.
    diffusion: Matrix = matrix_multiply(temp, hadamard_full)  # Apply the second Hadamard to complete the operator.
    return diffusion  # Return the diffusion operator.


def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two square matrices."""
    result: Matrix = []  # Prepare the container for the product matrix.
    size: int = len(a)  # Determine the dimension of the matrices.
    for row_index in range(size):  # Iterate over each row index of the first matrix.
        row: List[complex] = []  # Create a new row for the result.
        for column_index in range(size):  # Iterate over each column index of the second matrix.
            value: complex = 0j  # Initialize the accumulator for the dot product.
            for k in range(size):  # Walk over the shared dimension.
                value += a[row_index][k] * b[k][column_index]  # Accumulate the product of corresponding entries.
            row.append(value)  # Store the finished entry in the row.
        result.append(row)  # Append the row to the result matrix.
    return result  # Return the matrix product.


def transpose_conjugate(matrix: Matrix) -> Matrix:
    """Compute the conjugate transpose (Hermitian adjoint) of a matrix."""
    size: int = len(matrix)  # Determine the dimension of the matrix.
    result: Matrix = []  # Prepare the container for the transposed matrix.
    for column_index in range(size):  # Iterate over each column index of the original matrix.
        row: List[complex] = []  # Build a row for the conjugate transpose.
        for row_index in range(size):  # Iterate over each row index of the original matrix.
            row.append(matrix[row_index][column_index].conjugate())  # Take the complex conjugate while swapping indices.
        result.append(row)  # Append the completed row to the result matrix.
    return result  # Return the conjugate transpose.


def grover_iteration(num_qubits: int, oracle: Matrix, iterations: int) -> Vector:
    """Run Grover's search algorithm for a fixed number of iterations."""
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
    best_index: int = 0  # Track the current best index.
    best_probability: float = -1.0  # Track the highest probability encountered so far.
    for index, probability in enumerate(probabilities):  # Iterate through all probabilities.
        if probability > best_probability:  # Check whether the current probability is larger than the best.
            best_probability = probability  # Update the best probability.
            best_index = index  # Update the best index to the current position.
    return best_index  # Return the index associated with the highest probability.


def run_grover(num_qubits: int, marked_index: int) -> int:
    """Execute Grover's algorithm with the recommended number of iterations."""
    size: int = 2 ** num_qubits  # Determine how many elements are being searched.
    iterations: int = max(1, int(math.floor((math.pi / 4) * math.sqrt(size))))  # Use the standard floor-based heuristic.
    oracle: Matrix = phase_oracle(num_qubits, marked_index)  # Build the oracle that marks the desired state.
    final_state: Vector = grover_iteration(num_qubits, oracle, iterations)  # Run Grover's algorithm.
    return most_probable_state(final_state)  # Report the most probable measurement outcome.
