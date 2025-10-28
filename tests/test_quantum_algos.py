"""Unit tests for the quantum algorithm implementations."""

import importlib.util
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

    def test_grover_locates_marked_element(self) -> None:
        """Grover's algorithm should find the marked index for two qubits."""
        marked_index = 3
        self.assertEqual(qa.run_grover(2, marked_index), marked_index)

    def test_phase_oracle_sign_flip(self) -> None:
        """The phase oracle must invert the amplitude of the marked state."""
        oracle = qa.phase_oracle(2, 1)
        self.assertTrue(is_close_complex(oracle[1][1], -1.0))
        self.assertTrue(is_close_complex(oracle[0][0], 1.0))

    def test_diffusion_operator_unitary(self) -> None:
        """The diffusion operator should be unitary."""
        diffusion = qa.diffusion_operator(2)
        conjugate_transpose = qa.transpose_conjugate(diffusion)
        product = qa.matrix_multiply(diffusion, conjugate_transpose)
        self.assertTrue(matrices_allclose(product, qa.identity_matrix(4)))


if __name__ == "__main__":
    unittest.main()
