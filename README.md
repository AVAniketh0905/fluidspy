# fluidspy

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Your `fluidspy` is a Python library for Computational Fluid Dynamics (CFD) simulations.

## Features

- Most famous algorithms implemented in python.
- Animations coming soon!

## Installation

You can install `fluidspy` using pip:

```bash
pip install fluidspy
```

## Usage

```python
import numpy as np
from fluidspy import taylor_methods

f = lambda x: x**2 / 4
x, h = 2.0, 0.1

taylor = taylor_methods("central", "first", "one")
print(taylor, f"{taylor(f, x, h):.3f}")

taylor = taylor_methods("central", "second", "one")
print(taylor, f"{taylor(f, x, h):.3f}")

## Outputs
# Calling from FirstOrder with central difference with a function of one dimension. 1.000
# Calling from FirstOrder with central difference with a function of one dimension. 0.500
```

## Contributing

If you want to contribute to this project, see `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

AVAniketh0905 (dekomori_sanae09) -> adimoolamaniketh@gmail.com
Project Link: [fluidspy](https://github.com/AVAniketh0905/fluidspy)

## Acknowledgments

`Manim` has inspired me a lot!
