"""Unit tests for the quantum algorithm implementations."""

import importlib.util
import math
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "quantum-algos.py"
SPEC = importlib.util.spec_from_file_location("quantum_algos", MODULE_PATH)
qa = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader  # Satisfy type checkers when available.
SPEC.loader.exec_module(qa)  # type: ignore[arg-type]


def is_close_complex(a: complex, b: complex, tol: float = 1e-9) -> bool:
    """Helper function that compares two complex numbers within tolerance."""
    return abs(a - b) <= tol


def matrices_allclose(a: qa.Matrix, b: qa.Matrix, tol: float = 1e-9) -> bool:
    """Check whether two matrices are entry-wise close within a tolerance."""
    for row_a, row_b in zip(a, b):
        for value_a, value_b in zip(row_a, row_b):
            if not is_close_complex(value_a, value_b, tol):
                return False
    return True


class QuantumAlgosTestCase(unittest.TestCase):
    """Collection of correctness checks for the demonstration algorithms."""

    def test_deutsch_jozsa_constant_oracle(self) -> None:
        """Deutsch-Jozsa should detect a constant oracle."""
        self.assertTrue(qa.deutsch_jozsa(qa.constant_oracle()))

    def test_deutsch_jozsa_balanced_oracle(self) -> None:
        """Deutsch-Jozsa should reject a balanced oracle."""
        self.assertFalse(qa.deutsch_jozsa(qa.balanced_oracle()))

    def test_basis_state_has_single_amplitude(self) -> None:
        """create_basis_state should produce a vector with one unit amplitude."""
        state = qa.create_basis_state(3, 5)
        self.assertEqual(len(state), 8)
        for index, amplitude in enumerate(state):
            if index == 5:
                self.assertTrue(is_close_complex(amplitude, 1 + 0j))
            else:
                self.assertTrue(is_close_complex(amplitude, 0 + 0j))

    def test_hadamard_n_matches_tensor_power(self) -> None:
        """The cached Hadamard tensor power should match a manual computation."""
        reference = qa.tensor_power(qa.hadamard(), 3)
        cached = qa.hadamard_n(3)
        self.assertTrue(matrices_allclose(cached, reference))

    def test_tensor_power_dimensions(self) -> None:
        """tensor_power should expand the matrix size correctly."""
        matrix = qa.tensor_power([[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], 3)
        self.assertEqual(len(matrix), 8)
        for row in matrix:
            self.assertEqual(len(row), 8)

    def test_apply_gate_agrees_with_matrix_multiply(self) -> None:
        """apply_gate should produce the same result as matrix multiplication."""
        state = [1 + 0j, 0 + 0j]
        gate = qa.hadamard()
        via_apply = qa.apply_gate(state, gate)
        via_multiply = qa.matrix_multiply(gate, [[amplitude] for amplitude in state])
        self.assertTrue(
            all(
                is_close_complex(left, right[0])
                for left, right in zip(via_apply, via_multiply)
            )
        )

    def test_measure_probabilities_are_normalized(self) -> None:
        """Probabilities should add up to approximately one."""
        state = qa.apply_gate(qa.create_basis_state(1, 0), qa.hadamard())
        probabilities = qa.measure_probabilities(state)
        self.assertAlmostEqual(sum(probabilities), 1.0, places=9)

    def test_grover_locates_marked_element(self) -> None:
        """Grover's algorithm should find the marked index for two qubits."""
        marked_index = 3
        self.assertEqual(qa.run_grover(2, marked_index), marked_index)

    def test_grover_iteration_amplifies_marked_state(self) -> None:
        """The Grover iteration should increase the marked state's probability."""
        num_qubits = 3
        marked_index = 4
        oracle = qa.phase_oracle(num_qubits, marked_index)
        state = qa.grover_iteration(num_qubits, oracle, 1)
        probabilities = qa.measure_probabilities(state)
        average = sum(probabilities) / len(probabilities)
        self.assertGreater(probabilities[marked_index], average)

    def test_phase_oracle_sign_flip(self) -> None:
        """The phase oracle must invert the amplitude of the marked state."""
        oracle = qa.phase_oracle(2, 1)
        self.assertTrue(is_close_complex(oracle[1][1], -1.0))
        self.assertTrue(is_close_complex(oracle[0][0], 1.0))

    def test_phase_oracle_is_unitary(self) -> None:
        """The phase oracle should be unitary for any size."""
        oracle = qa.phase_oracle(3, 5)
        conjugate_transpose = qa.transpose_conjugate(oracle)
        product = qa.matrix_multiply(oracle, conjugate_transpose)
        self.assertTrue(matrices_allclose(product, qa.identity_matrix(8)))

    def test_diffusion_operator_unitary(self) -> None:
        """The diffusion operator should be unitary."""
        diffusion = qa.diffusion_operator(2)
        conjugate_transpose = qa.transpose_conjugate(diffusion)
        product = qa.matrix_multiply(diffusion, conjugate_transpose)
        self.assertTrue(matrices_allclose(product, qa.identity_matrix(4)))

    def test_diffusion_operator_preserves_uniform_state(self) -> None:
        """Applying the diffusion operator to the uniform state should leave it unchanged."""
        num_qubits = 2
        uniform_state = qa.apply_gate(qa.create_basis_state(num_qubits, 0), qa.hadamard_n(num_qubits))
        diffusion = qa.diffusion_operator(num_qubits)
        transformed = qa.apply_gate(uniform_state, diffusion)
        for original, updated in zip(uniform_state, transformed):
            self.assertTrue(is_close_complex(original, updated))

    def test_outer_product_constructs_projector(self) -> None:
        """outer_product should produce a projector matrix."""
        weight = 1 / math.sqrt(2)
        vector = [weight + 0j, weight + 0j]
        projector = qa.outer_product(vector)
        expected = [
            [0.5 + 0j, 0.5 + 0j],
            [0.5 + 0j, 0.5 + 0j],
        ]
        self.assertTrue(matrices_allclose(projector, expected))

    def test_matrix_multiply_associativity_small_case(self) -> None:
        """Matrix multiplication should respect associativity for compatible matrices."""
        a = qa.hadamard()
        b = qa.hadamard()
        c = qa.hadamard()
        left = qa.matrix_multiply(qa.matrix_multiply(a, b), c)
        right = qa.matrix_multiply(a, qa.matrix_multiply(b, c))
        self.assertTrue(matrices_allclose(left, right))

    def test_most_probable_state_returns_expected_index(self) -> None:
        """most_probable_state should return the index with the largest probability."""
        state = [0.1 + 0j, 0.9 + 0j, 0.2 + 0j, 0.3 + 0j]
        self.assertEqual(qa.most_probable_state(state), 1)


if __name__ == "__main__":
    unittest.main()
