import unittest
from unittest.mock import patch

import matplotlib

matplotlib.use("Agg")

from dogukangundemir_diffusion2d import diffusion2d


class Diffusion2DTests(unittest.TestCase):
    def test_solve_rejects_non_positive_parameters(self):
        for parameters in ((0, 0.1, 4), (0.1, -0.1, 4), (0.1, 0.1, 0)):
            with self.subTest(parameters=parameters):
                with self.assertRaises(ValueError):
                    diffusion2d.solve(*parameters)

    def test_solve_rejects_grid_without_interior_points(self):
        with self.assertRaises(ValueError):
            diffusion2d.solve(dx=5.0, dy=0.1)

    @patch("dogukangundemir_diffusion2d.diffusion2d.output_plots")
    @patch("dogukangundemir_diffusion2d.diffusion2d.create_plot")
    def test_solve_creates_four_snapshots(self, create_plot, output_plots):
        diffusion2d.solve(dx=1.0, dy=1.0, D=4.0)

        self.assertEqual(create_plot.call_count, 4)
        output_plots.assert_called_once()


if __name__ == "__main__":
    unittest.main()
