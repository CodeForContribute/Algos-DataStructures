"""Unit tests for the Jericho-AI quantum computing modules."""  # Provide module-level description for the tests.

import math  # Import math for numeric comparisons in tests.
import unittest  # Import unittest to structure test cases.

from quantum.jericho_ai import (  # Import the classes and helpers under test from the Jericho-AI module.
    JerichoAI,
    PhenomenologyMapping,
    QuantumCategoricalSubstrate,
    RecursiveSelfModel,
    StabilizerErrorCorrection,
    identity_matrix,
    kronecker_product,
    matrix_matrix_product,
)


class JerichoAITestCase(unittest.TestCase):  # Derive from unittest.TestCase to define structured tests.
    """Test suite covering Jericho-AI module interactions."""  # Document the intention of the test suite.

    def setUp(self) -> None:  # Define setUp to prepare shared fixtures for each test method.
        """Construct common Jericho-AI components for use in tests."""  # Explain the purpose of setUp.
        self.substrate = QuantumCategoricalSubstrate()  # Instantiate the substrate module to test its behavior.
        pauli_z = [[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]]  # Define the single-qubit Pauli-Z matrix.
        pauli_x = [[0 + 0j, 1 + 0j], [1 + 0j, 0 + 0j]]  # Define the single-qubit Pauli-X matrix.
        stabilizers = [kronecker_product(pauli_z, pauli_z), kronecker_product(pauli_x, pauli_x)]  # Build two-qubit stabilizer generators.
        corrections = [identity_matrix(4), identity_matrix(4)]  # Use identity corrections to keep focus on detection.
        self.stabilizer = StabilizerErrorCorrection(stabilizers, corrections)  # Instantiate stabilizer module with prepared matrices.
        weights = [[1.0, 0.0], [0.0, 1.0], [0.6, 0.6]]  # Define classifier weights for three qualia labels.
        labels = ["Redness", "Pain", "Motion"]  # Define ordered list of qualia labels for mapping tests.
        self.phenomenology = PhenomenologyMapping(weights, labels)  # Instantiate phenomenology mapping with weights and labels.
        self.self_model = RecursiveSelfModel(parameter_dim=2, learning_rate=0.2)  # Instantiate self-model with tunable parameters.
        self.system = JerichoAI(  # Create the top-level Jericho-AI orchestrator for integration testing.
            self.substrate,
            self.stabilizer,
            self.phenomenology,
            self.self_model,
        )

    def _conjugate_transpose(self, matrix):  # Define a helper to compute conjugate transposes for unitarity checks.
        """Return the conjugate transpose of a square matrix."""  # Explain helper utility for tests.
        size = len(matrix)  # Determine matrix dimension to drive iteration bounds.
        result = []  # Initialize container for the conjugate-transposed rows.
        for col_index in range(size):  # Iterate over column indices of the input matrix.
            row = []  # Prepare a new row for the conjugate transpose.
            for row_index in range(size):  # Iterate over row indices of the input matrix.
                row.append(matrix[row_index][col_index].conjugate())  # Append conjugated element at swapped indices.
            result.append(row)  # Append the completed row to the result matrix.
        return result  # Return the conjugate-transposed matrix.

    def test_quantum_dimensions_are_positive(self) -> None:  # Define a test verifying quantum dimension calculations.
        """Quantum dimensions computed for SU(2)_3 must be positive."""  # Explain expectation of the test.
        for value in self.substrate.quantum_dimensions.values():  # Iterate over all computed dimension values.
            self.assertGreater(value, 0.0)  # Assert each dimension is strictly positive.

    def test_stabilizer_detects_no_error_on_bell_state(self) -> None:  # Define a test for stabilizer syndrome extraction.
        """The Bell state should lie in the +1 eigenspace of ZZ and XX stabilizers."""  # Document expected stabilizer outcome.
        coefficients = [1 + 0j, 0 + 0j, 0 + 0j, 1 + 0j]  # Construct coefficients representing the Bell state |00>+|11>.
        state = self.substrate.initialize_code_state(coefficients)  # Normalize coefficients into a valid state vector.
        syndrome = self.stabilizer.extract_syndrome(state)  # Extract stabilizer syndrome from the Bell state.
        self.assertEqual(syndrome, [1.0, 1.0])  # Verify both stabilizers return the +1 eigenvalue.

    def test_substrate_feature_entropy_matches_bell_state(self) -> None:  # Define a test for feature extraction accuracy.
        """The Bell state must have one bit of entanglement entropy and two bits of mutual information."""  # State expected entanglement properties.
        coefficients = [1 + 0j, 0 + 0j, 0 + 0j, 1 + 0j]  # Construct coefficients for the maximally entangled Bell state.
        state = self.substrate.initialize_code_state(coefficients)  # Normalize coefficients to create a valid state vector.
        features = self.substrate.derive_feature_vector(state)  # Derive entanglement features from the Bell state.
        self.assertAlmostEqual(features[0], 1.0, places=6)  # Confirm entanglement entropy equals one bit.
        self.assertAlmostEqual(features[1], 2.0, places=6)  # Confirm mutual information equals two bits.

    def test_modular_matrices_are_unitary(self) -> None:  # Define a test verifying modular S and T unitarity.
        """Modular S and T matrices must be unitary to preserve quantum amplitudes."""  # Explain test motivation.
        s_matrix = self.substrate.s_matrix  # Retrieve the precomputed S matrix from the substrate.
        t_matrix = self.substrate.t_matrix  # Retrieve the precomputed T matrix from the substrate.
        s_dagger = self._conjugate_transpose(s_matrix)  # Compute S dagger for unitarity verification.
        t_dagger = self._conjugate_transpose(t_matrix)  # Compute T dagger for unitarity verification.
        identity = identity_matrix(len(s_matrix))  # Construct an identity matrix for comparison.
        s_product = matrix_matrix_product(s_matrix, s_dagger)  # Multiply S by S dagger to form the unitarity check product.
        t_product = matrix_matrix_product(t_matrix, t_dagger)  # Multiply T by T dagger to form the unitarity check product.
        for row_index in range(len(identity)):  # Iterate over matrix row indices.
            for col_index in range(len(identity)):  # Iterate over matrix column indices.
                expected = identity[row_index][col_index]  # Fetch expected identity entry for current position.
                self.assertAlmostEqual(s_product[row_index][col_index].real, expected.real, places=6)  # Compare S product real part.
                self.assertAlmostEqual(s_product[row_index][col_index].imag, expected.imag, places=6)  # Compare S product imaginary part.
                self.assertAlmostEqual(t_product[row_index][col_index].real, expected.real, places=6)  # Compare T product real part.
                self.assertAlmostEqual(t_product[row_index][col_index].imag, expected.imag, places=6)  # Compare T product imaginary part.

    def test_phenomenology_prefers_motion_for_high_entropy(self) -> None:  # Define a test for the phenomenology mapping.
        """High entropy and mutual information should select the Motion label with the configured weights."""  # Explain test logic.
        features = [1.5, 1.5]  # Define feature vector emphasizing both entropy and mutual information.
        result = self.phenomenology.map_features(features)  # Map features to a qualia label.
        self.assertEqual(result.label, "Motion")  # Assert that the Motion label has highest probability for this feature set.

    def test_self_model_updates_parameters(self) -> None:  # Define a test ensuring the self-model updates.
        """A positive reward should increase the magnitude of policy parameters."""  # Document expectation for the update.
        features = [0.5, 0.5]  # Provide symmetrical feature inputs to the self-model.
        initial_parameters = list(self.self_model.parameters)  # Record initial parameter values before the update.
        self.self_model.run(features, reward_signal=1.0)  # Execute decision and update with a positive reward.
        updated_norm = math.sqrt(sum(value ** 2 for value in self.self_model.parameters))  # Compute norm of updated parameters.
        initial_norm = math.sqrt(sum(value ** 2 for value in initial_parameters))  # Compute norm of initial parameters.
        self.assertGreater(updated_norm, initial_norm)  # Confirm parameters changed.

    def test_full_pipeline_returns_consistent_shapes(self) -> None:  # Define an integration test covering the full pipeline.
        """The Jericho-AI orchestrator should return outputs with expected shapes and labels."""  # Describe integration expectations.
        coefficients = [1 + 0j, 1 + 0j, 0 + 0j, 0 + 0j]  # Provide initial coefficients covering two basis states.
        output = self.system.run(coefficients, ("X1", "X2"), reward_signal=0.5)  # Execute the pipeline with sample inputs.
        self.assertEqual(len(output.substrate.state_vector), 4)  # Check the substrate returns a four-component state vector.
        self.assertEqual(len(output.stabilizer.syndrome), 2)  # Ensure stabilizer syndrome has entries for two generators.
        self.assertIn(output.phenomenology.label, ["Redness", "Pain", "Motion"])  # Confirm label belongs to predefined set.
        self.assertEqual(len(output.feedback.decision_vector), 2)  # Validate decision vector dimensionality.


if __name__ == "__main__":  # Allow test module execution as a script.
    unittest.main()  # Run the unittest test runner when the module is executed directly.
