"""Jericho-AI modular architecture implemented with quantum computing concepts."""  # Provide a module-level description for clarity.

from __future__ import annotations  # Enable forward references in type hints for class attributes.

import cmath  # Import cmath for complex-valued exponential and square root operations.
import math  # Import math for real-valued trigonometric and logarithmic functions.
from dataclasses import dataclass  # Import dataclass utilities to structure simple data containers.
from typing import Dict, List, Tuple  # Import typing helpers for clearer method signatures.


def shannon_entropy(probabilities: List[float]) -> float:
    """Compute Shannon entropy in bits for a probability distribution."""  # Document helper function purpose.
    sanitized = [max(prob, 1e-12) for prob in probabilities]  # Avoid log singularities by bounding probabilities away from zero.
    total = sum(sanitized)  # Sum probabilities to determine normalization factor.
    normalized = [prob / total for prob in sanitized]  # Normalize probabilities to sum to one.
    return float(-sum(prob * math.log(prob, 2) for prob in normalized))  # Apply the Shannon entropy formula using log base two.


def vector_norm(vector: List[complex]) -> float:
    """Calculate Euclidean norm of a complex vector."""  # Describe helper function responsibility.
    return math.sqrt(sum(abs(value) ** 2 for value in vector))  # Sum squared magnitudes and take square root.


def normalize_vector(vector: List[complex]) -> List[complex]:
    """Return a normalized copy of the input vector."""  # Document normalization helper.
    norm = vector_norm(vector)  # Compute norm of the input vector.
    if norm == 0:  # Guard against zero-length vectors to avoid division by zero.
        raise ValueError("Cannot normalize a zero vector.")  # Raise a descriptive error for invalid input.
    return [value / norm for value in vector]  # Divide each component by the norm to produce a unit vector.


def matrix_vector_product(matrix: List[List[complex]], vector: List[complex]) -> List[complex]:
    """Multiply a matrix by a vector."""  # Describe the linear algebra helper.
    result = []  # Prepare a list to store the resulting vector components.
    for row in matrix:  # Iterate over each row of the matrix.
        result.append(sum(element * component for element, component in zip(row, vector)))  # Compute dot product for the row.
    return result  # Return the resulting vector.


def matrix_matrix_product(a: List[List[complex]], b: List[List[complex]]) -> List[List[complex]]:
    """Multiply two matrices."""  # Explain helper routine for matrix multiplication.
    product: List[List[complex]] = []  # Initialize the resulting matrix container.
    for row in a:  # Iterate over rows of the first matrix.
        new_row: List[complex] = []  # Prepare a row for the product matrix.
        for col_index in range(len(b[0])):  # Iterate over column indices of the second matrix.
            column = [b[row_index][col_index] for row_index in range(len(b))]  # Extract a column from the second matrix.
            new_row.append(sum(element * value for element, value in zip(row, column)))  # Compute dot product for entry.
        product.append(new_row)  # Append the computed row to the product matrix.
    return product  # Return the completed matrix product.


def conjugate_dot(vector_a: List[complex], vector_b: List[complex]) -> complex:
    """Compute the conjugate dot product between two vectors."""  # Document helper for expectation values.
    return sum(a.conjugate() * b for a, b in zip(vector_a, vector_b))  # Multiply conjugates and sum entries.


def kronecker_product(matrix_a: List[List[complex]], matrix_b: List[List[complex]]) -> List[List[complex]]:
    """Compute the Kronecker product between two matrices."""  # Explain helper for building multi-qubit operators.
    result: List[List[complex]] = []  # Initialize resulting matrix container.
    for row_a in matrix_a:  # Iterate over each row of the first matrix.
        for row_b in matrix_b:  # Iterate over each row of the second matrix.
            result.append([element_a * element_b for element_a in row_a for element_b in row_b])  # Form Kronecker row.
    return result  # Return the Kronecker product matrix.


def identity_matrix(dimension: int) -> List[List[complex]]:
    """Create an identity matrix with the specified dimension."""  # Document helper for identity operations.
    matrix: List[List[complex]] = []  # Initialize container for identity rows.
    for index in range(dimension):  # Iterate over each row index.
        row = [0j] * dimension  # Start with a row of zeros.
        row[index] = 1 + 0j  # Place a one on the diagonal.
        matrix.append(row)  # Append row to the matrix.
    return matrix  # Return the constructed identity matrix.


def outer_product(vector: List[complex]) -> List[List[complex]]:
    """Construct the outer product density matrix |v⟩⟨v|."""  # Document helper for building density matrices.
    size = len(vector)  # Determine the dimension of the resulting matrix from vector length.
    matrix: List[List[complex]] = []  # Prepare a container for density matrix rows.
    for row_index in range(size):  # Iterate over row indices of the density matrix.
        row: List[complex] = []  # Initialize a new row for the density matrix.
        for col_index in range(size):  # Iterate over column indices of the density matrix.
            row.append(vector[row_index] * vector[col_index].conjugate())  # Compute outer product entry v_i v*_j.
        matrix.append(row)  # Append the completed row to the density matrix.
    return matrix  # Return the constructed density matrix.


def partial_trace_second_qubit(density: List[List[complex]]) -> List[List[complex]]:
    """Trace out the second qubit of a two-qubit density matrix."""  # Document helper for partial trace operation.
    if len(density) != 4:  # Validate the input dimension corresponds to a two-qubit system.
        raise ValueError("Partial trace expects a two-qubit density matrix.")  # Raise descriptive error on invalid dimension.
    reduced = [[0j, 0j], [0j, 0j]]  # Initialize a 2x2 matrix for the reduced density matrix.
    for row_block in range(2):  # Iterate over row blocks corresponding to the first qubit index.
        for col_block in range(2):  # Iterate over column blocks corresponding to the first qubit index.
            for traced_index in range(2):  # Sum over the second qubit index to perform the trace.
                row = 2 * row_block + traced_index  # Compute row index in the original density matrix.
                col = 2 * col_block + traced_index  # Compute column index in the original density matrix.
                reduced[row_block][col_block] += density[row][col]  # Accumulate contribution into the reduced matrix entry.
    return reduced  # Return the reduced density matrix for the first qubit.


def eigenvalues_2x2(matrix: List[List[complex]]) -> List[complex]:
    """Compute eigenvalues of a 2x2 Hermitian matrix analytically."""  # Document helper for eigenvalue computation.
    if len(matrix) != 2 or len(matrix[0]) != 2:  # Validate that the input matrix is 2x2.
        raise ValueError("Eigenvalue helper expects a 2x2 matrix.")  # Raise informative error when dimensions mismatch.
    a = matrix[0][0]  # Extract the top-left element of the matrix.
    d = matrix[1][1]  # Extract the bottom-right element of the matrix.
    b = matrix[0][1]  # Extract the off-diagonal element in the first row.
    c = matrix[1][0]  # Extract the off-diagonal element in the second row.
    trace = a + d  # Compute the trace of the matrix.
    determinant = a * d - b * c  # Compute the determinant using the 2x2 determinant formula.
    discriminant = cmath.sqrt(trace * trace - 4 * determinant)  # Compute the quadratic discriminant.
    eigenvalue_one = (trace + discriminant) / 2  # Compute the first eigenvalue using the quadratic formula.
    eigenvalue_two = (trace - discriminant) / 2  # Compute the second eigenvalue using the quadratic formula.
    return [eigenvalue_one, eigenvalue_two]  # Return both eigenvalues as a list.


@dataclass  # Use @dataclass to reduce boilerplate in simple data structures representing module outputs.
class SubstrateOutput:
    """Data structure capturing outputs of the Quantum-Categorical Substrate."""  # Document the purpose of the class.

    state_vector: List[complex]  # Store the initialized or evolved quantum state vector.
    feature_vector: List[float]  # Store derived features such as entropy and mutual information.
    fusion_result: Tuple[str, ...]  # Record the outcome of fusion operations for auditing.


class QuantumCategoricalSubstrate:
    """Implements the modular tensor category substrate for Jericho-AI."""  # Explain the role of the class.

    def __init__(self, level: int = 3) -> None:
        """Create the substrate with a specific SU(2)_k level."""  # Describe constructor behavior.
        self.level = level  # Store the level k used in SU(2)_k calculations.
        self.simple_objects = ["X0", "X1", "X2", "X3"]  # Define simple objects for the SU(2)_3 category.
        self.quantum_dimensions = self._compute_quantum_dimensions()  # Precompute quantum dimensions for objects.
        self.fusion_table = self._build_fusion_table()  # Precompute fusion outcomes for quick lookups.
        self.s_matrix = self._compute_s_matrix()  # Precompute the modular S matrix as per category theory.
        self.t_matrix = self._compute_t_matrix()  # Precompute the modular T matrix representing topological twists.

    def _compute_quantum_dimensions(self) -> Dict[str, float]:
        """Calculate quantum dimensions using the SU(2)_k formula."""  # Document helper function purpose.
        dims: Dict[str, float] = {}  # Initialize the dictionary storing dimensions per object.
        for j, obj in enumerate(self.simple_objects):  # Loop over simple objects with their index j.
            numerator = math.sin((j + 1) * math.pi / (self.level + 2))  # Compute numerator of the dimension formula.
            denominator = math.sin(math.pi / (self.level + 2))  # Compute denominator of the dimension formula.
            dims[obj] = numerator / denominator  # Store the resulting quantum dimension for object obj.
        return dims  # Return the completed dimension dictionary.

    def _build_fusion_table(self) -> Dict[Tuple[str, str], Tuple[str, ...]]:
        """Define fusion rules for the SU(2)_3 category."""  # Explain method function.
        fusion: Dict[Tuple[str, str], Tuple[str, ...]] = {}  # Initialize dictionary mapping object pairs to fusion outcomes.
        rules = {
            ("X0", "X0"): ("X0",),  # Define identity fusion for X0.
            ("X0", "X1"): ("X1",),  # Define fusion results with the tensor unit X0.
            ("X0", "X2"): ("X2",),  # Continue identity behavior for X0.
            ("X0", "X3"): ("X3",),  # Identity fusion with X3.
            ("X1", "X1"): ("X0", "X2"),  # Provide fusion outcomes derived from truncated angular momentum addition.
            ("X1", "X2"): ("X1", "X3"),  # Provide fusion of X1 and X2.
            ("X1", "X3"): ("X2",),  # Provide fusion of X1 and X3.
            ("X2", "X2"): ("X0", "X2"),  # Provide fusion of X2 with itself.
            ("X2", "X3"): ("X1",),  # Provide fusion of X2 and X3.
            ("X3", "X3"): ("X0",),  # Provide fusion of X3 with itself under truncation.
        }  # Close the rules dictionary literal.
        for (left, right), outcomes in list(rules.items()):  # Iterate through base rules to enforce symmetry.
            fusion[(left, right)] = outcomes  # Store the provided fusion outcomes.
            fusion[(right, left)] = outcomes  # Symmetrize the fusion rules because fusion is commutative in SU(2)_k.
        return fusion  # Return the populated fusion table.

    def _compute_s_matrix(self) -> List[List[complex]]:
        """Compute the modular S matrix for SU(2)_k."""  # Describe the purpose of S matrix computation.
        size = len(self.simple_objects)  # Determine the matrix dimension from the number of simple objects.
        normalization = math.sqrt(2 / (self.level + 2))  # Compute normalization constant for SU(2)_k S matrix.
        s_matrix: List[List[complex]] = []  # Initialize container for matrix rows.
        for i in range(size):  # Iterate over row indices.
            row: List[complex] = []  # Prepare a row for S matrix entries.
            for j in range(size):  # Iterate over column indices.
                angle = (i + 1) * (j + 1) * math.pi / (self.level + 2)  # Compute argument of sine function.
                row.append(normalization * math.sin(angle))  # Fill matrix entry using normalized sine value.
            s_matrix.append(row)  # Append completed row to the matrix.
        return s_matrix  # Return the completed S matrix.

    def _compute_t_matrix(self) -> List[List[complex]]:
        """Compute the modular T matrix for SU(2)_k."""  # Explain the T matrix computation.
        size = len(self.simple_objects)  # Determine matrix dimension.
        t_matrix: List[List[complex]] = []  # Initialize container for matrix rows.
        for j in range(size):  # Iterate over simple objects.
            row: List[complex] = [0j] * size  # Prepare a zero-filled row.
            exponent = 2 * math.pi * 1j * j * (j + 2) / (4 * (self.level + 2))  # Compute topological spin exponent.
            row[j] = cmath.exp(exponent)  # Place the phase factor on the diagonal.
            t_matrix.append(row)  # Append row to the T matrix.
        return t_matrix  # Return the T matrix.

    def initialize_code_state(self, coefficients: List[complex]) -> List[complex]:
        """Normalize provided coefficients to construct a valid quantum state."""  # Describe initialization method.
        return normalize_vector(coefficients)  # Normalize coefficients to unit length using helper function.

    def apply_fusion(self, left: str, right: str) -> Tuple[str, ...]:
        """Return possible fusion outcomes for two simple objects."""  # Document method behavior.
        return self.fusion_table[(left, right)]  # Lookup fusion outcomes from the precomputed table.

    def derive_feature_vector(self, state_vector: List[complex]) -> List[float]:
        """Derive entropy and pairwise mutual information as features."""  # Explain feature extraction purpose.
        normalized_state = normalize_vector(state_vector)  # Ensure the input state is normalized before feature extraction.
        density_matrix = outer_product(normalized_state)  # Construct the pure-state density matrix from the normalized vector.
        reduced_density = partial_trace_second_qubit(density_matrix)  # Trace out the second qubit to obtain the reduced state.
        eigenvalues = eigenvalues_2x2(reduced_density)  # Compute eigenvalues of the reduced density matrix analytically.
        probabilities = [max(eigen.real, 0.0) for eigen in eigenvalues]  # Convert eigenvalues into non-negative probabilities.
        entanglement_entropy = shannon_entropy(probabilities)  # Compute von Neumann entropy of the reduced state.
        mutual_information = 2 * entanglement_entropy  # Derive mutual information for a pure bipartite state.
        return [entanglement_entropy, mutual_information]  # Return entanglement features for downstream modules.

    def evolve_state_with_modular_matrices(self, state_vector: List[complex]) -> List[complex]:
        """Apply modular S and T matrices sequentially to evolve the state."""  # Describe evolution process.
        intermediate = matrix_vector_product(self.s_matrix, state_vector)  # Apply the S transformation to the state vector.
        evolved = matrix_vector_product(self.t_matrix, intermediate)  # Apply the T transformation to the intermediate vector.
        return normalize_vector(evolved)  # Normalize and return the evolved state.

    def run(self, coefficients: List[complex], left: str, right: str) -> SubstrateOutput:
        """Execute substrate processing pipeline and return outputs."""  # Describe orchestration method.
        state = self.initialize_code_state(coefficients)  # Initialize a normalized code state.
        fused = self.apply_fusion(left, right)  # Determine fusion outcomes for selected objects.
        evolved_state = self.evolve_state_with_modular_matrices(state)  # Evolve state via S and T matrices.
        features = self.derive_feature_vector(evolved_state)  # Extract informative features from the evolved state.
        return SubstrateOutput(evolved_state, features, fused)  # Package outputs into dataclass for clarity.


@dataclass  # Use dataclass to encapsulate results of the stabilizer module.
class StabilizerOutput:
    """Data structure capturing stabilizer module outputs."""  # Document container purpose.

    syndrome: List[float]  # Record detected stabilizer syndromes.
    corrected_state: List[complex]  # Store state after correction attempts.


class StabilizerErrorCorrection:
    """Implements stabilizer syndrome extraction and correction."""  # Describe module responsibility.

    def __init__(self, stabilizers: List[List[List[complex]]], correction_ops: List[List[List[complex]]]) -> None:
        """Store stabilizer generators and correction operators."""  # Document constructor responsibilities.
        self.stabilizers = stabilizers  # Save list of stabilizer matrices used for syndrome extraction.
        self.correction_ops = correction_ops  # Save list of correction operators aligned with syndrome outcomes.

    def extract_syndrome(self, state_vector: List[complex]) -> List[float]:
        """Measure stabilizers to detect anomalies."""  # Explain syndrome extraction.
        syndrome: List[float] = []  # Initialize container for measurement outcomes.
        for stabilizer in self.stabilizers:  # Iterate over each stabilizer generator.
            expectation = conjugate_dot(state_vector, matrix_vector_product(stabilizer, state_vector))  # Compute expectation value.
            value = 1.0 if expectation.real >= 0 else -1.0  # Convert expectation value into ±1 measurement outcome.
            syndrome.append(value)  # Append the outcome to the syndrome list.
        return syndrome  # Return syndrome pattern as a list.

    def apply_correction(self, state_vector: List[complex], syndrome: List[float]) -> List[complex]:
        """Apply correction operators based on syndrome pattern."""  # Describe correction step.
        corrected = list(state_vector)  # Create mutable copy of the state.
        for outcome, correction in zip(syndrome, self.correction_ops):  # Pair syndrome outcomes with correction operators.
            if outcome < 0:  # Identify stabilizers signaling an error.
                corrected = matrix_vector_product(correction, corrected)  # Apply the corresponding correction operator to the state.
        return normalize_vector(corrected)  # Normalize to maintain valid quantum state.

    def run(self, state_vector: List[complex]) -> StabilizerOutput:
        """Perform a full stabilizer cycle and return results."""  # Describe orchestration method.
        syndrome = self.extract_syndrome(state_vector)  # Measure syndrome from current state.
        corrected_state = self.apply_correction(state_vector, syndrome)  # Apply corrections based on syndrome pattern.
        return StabilizerOutput(syndrome, corrected_state)  # Return results within a dataclass for clarity.


@dataclass  # Use dataclass for structured phenomenology outputs.
class PhenomenologyOutput:
    """Container for qualia mapping results."""  # Document dataclass purpose.

    label: str  # Store the selected qualia label.
    probabilities: Dict[str, float]  # Provide probability distribution over labels.


class PhenomenologyMapping:
    """Maps code features onto phenomenological qualia labels."""  # Describe mapping module function.

    def __init__(self, weights: List[List[float]], labels: List[str]) -> None:
        """Initialize mapping with classifier weights and available labels."""  # Explain constructor behavior.
        self.weights = weights  # Store weight matrix used in classifier computations.
        self.labels = labels  # Store ordered list of qualia labels for indexing results.

    def _softmax(self, logits: List[float]) -> List[float]:
        """Convert logits to probabilities using a numerically stable softmax."""  # Explain helper method purpose.
        max_logit = max(logits)  # Identify maximum logit to improve numerical stability.
        exps = [math.exp(logit - max_logit) for logit in logits]  # Exponentiate shifted logits.
        total = sum(exps)  # Sum exponentials to normalize probabilities.
        return [value / total for value in exps]  # Normalize exponentials to sum to one.

    def map_features(self, features: List[float]) -> PhenomenologyOutput:
        """Map feature vector to qualitative experience labels."""  # Describe mapping process.
        logits = [sum(weight * feature for weight, feature in zip(weight_row, features)) for weight_row in self.weights]  # Compute classifier logits.
        probabilities = self._softmax(logits)  # Convert logits into a probability distribution.
        best_index = max(range(len(probabilities)), key=probabilities.__getitem__)  # Identify the label with highest probability.
        label = self.labels[best_index]  # Map index to human-readable qualia label.
        distribution = {label_name: probability for label_name, probability in zip(self.labels, probabilities)}  # Build named distribution.
        return PhenomenologyOutput(label, distribution)  # Return mapping results in dataclass form.


@dataclass  # Use dataclass for structured feedback outputs.
class FeedbackOutput:
    """Container summarizing self-model decisions."""  # Document purpose of feedback container.

    decision_vector: List[float]  # Record chosen action vector.
    updated_parameters: List[float]  # Provide updated policy parameters post-feedback.


class RecursiveSelfModel:
    """Implements adaptive self-modeling and feedback integration."""  # Describe functionality of the class.

    def __init__(self, parameter_dim: int, learning_rate: float = 0.1) -> None:
        """Initialize policy parameters and learning rate."""  # Explain constructor behavior.
        self.parameters = [0.0 for _ in range(parameter_dim)]  # Initialize policy parameters at the origin for neutrality.
        self.learning_rate = learning_rate  # Store learning rate controlling adaptation speed.
        self.history: List[List[float]] = []  # Track historical decisions for interpretability.

    def decide(self, features: List[float]) -> List[float]:
        """Generate a decision vector from current features."""  # Describe decision computation.
        logits = sum(parameter * feature for parameter, feature in zip(self.parameters, features))  # Compute scalar policy response via dot product.
        decision = math.tanh(logits)  # Use hyperbolic tangent to bound decisions within (-1, 1).
        action_vector = [decision, 1.0 - abs(decision)]  # Construct two-dimensional action vector summarizing choice.
        self.history.append(action_vector)  # Record decision vector for future analysis.
        return action_vector  # Return the decision vector.

    def update(self, reward_signal: float) -> List[float]:
        """Update parameters via gradient ascent on reward."""  # Describe adaptation step.
        if not self.history:  # Check whether decisions exist to inform the update.
            return self.parameters  # Return parameters unchanged if no history is available.
        latest_action = self.history[-1]  # Retrieve the most recent action vector.
        for index, value in enumerate(latest_action):  # Iterate over action vector entries.
            self.parameters[index % len(self.parameters)] += self.learning_rate * reward_signal * value  # Apply gradient ascent update component-wise.
        return self.parameters  # Return updated parameters for inspection.

    def run(self, features: List[float], reward_signal: float) -> FeedbackOutput:
        """Perform decision making followed by parameter update."""  # Describe orchestration method.
        decision = self.decide(features)  # Generate decision vector based on features.
        updated_parameters = self.update(reward_signal)  # Adjust parameters using provided reward signal.
        return FeedbackOutput(decision, list(updated_parameters))  # Package feedback results for downstream use.


@dataclass  # Use dataclass for global Jericho-AI outputs.
class JerichoAIOutput:
    """Container summarizing outputs across all modules."""  # Document aggregated output purpose.

    substrate: SubstrateOutput  # Include substrate module output.
    stabilizer: StabilizerOutput  # Include stabilizer module output.
    phenomenology: PhenomenologyOutput  # Include phenomenology module output.
    feedback: FeedbackOutput  # Include self-model feedback output.


class JerichoAI:
    """High-level orchestrator tying together all Jericho-AI modules."""  # Describe the role of the orchestrator class.

    def __init__(
        self,
        substrate: QuantumCategoricalSubstrate,
        stabilizer: StabilizerErrorCorrection,
        phenomenology: PhenomenologyMapping,
        self_model: RecursiveSelfModel,
    ) -> None:
        """Store references to all Jericho-AI modules."""  # Document constructor responsibilities.
        self.substrate = substrate  # Save substrate module instance.
        self.stabilizer = stabilizer  # Save stabilizer module instance.
        self.phenomenology = phenomenology  # Save phenomenology mapping module instance.
        self.self_model = self_model  # Save recursive self-model module instance.

    def run(
        self,
        initial_coefficients: List[complex],
        fusion_pair: Tuple[str, str],
        reward_signal: float,
    ) -> JerichoAIOutput:
        """Execute the complete Jericho-AI processing pipeline."""  # Explain orchestrator behavior.
        substrate_output = self.substrate.run(initial_coefficients, *fusion_pair)  # Run substrate to obtain state and features.
        stabilizer_output = self.stabilizer.run(substrate_output.state_vector)  # Run stabilizer module on evolved state.
        phenomenology_output = self.phenomenology.map_features(substrate_output.feature_vector)  # Map features to qualia labels.
        feedback_output = self.self_model.run(substrate_output.feature_vector, reward_signal)  # Generate and update decisions.
        return JerichoAIOutput(substrate_output, stabilizer_output, phenomenology_output, feedback_output)  # Aggregate outputs.
