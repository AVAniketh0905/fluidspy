# fluidspy
# Arhan

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Gh Test](https://github.com/AVAniketh0905/fluidspy/actions/workflows/test_basic.yml/badge.svg)

`fluidspy` is a Python library for Computational Fluid Dynamics (CFD) simulations.

## Features

- Most famous cfd algorithms implemented in python.
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

### Setup

1. Fork this repository.
2. Clone the forked repository to your local machine.
   > `git clone {repo_name}`
3. Change the current working directory to the cloned repository.
4. Add the upstream reference. This will add the original repository as reference.
   > `git remote add upstream git@github.com:AVAniketh0905/fluidspy.git`
   - Note
     - Everytime you boot up/push please run the following command to stay up-to date with the original repo.
         > `git pull upstream main`
5. Create a virtual environment.
   > `python -m venv venv`
6. Activate the virtual environment.
   - Windows
     > `venv\Scripts\activate`
   - Linux
     > `source venv/bin/activate`
7. Install the dependencies.
   > `pip install -r requirements_dev.txt`
8. Make the changes.
9. Run the tests.
   > `pytest`
10. Commit the changes.
11. Push the changes to your forked repository.
12. Create a pull request.
13. Wait for the review!!!

## License

This project is licensed under the MIT License. See the *LICENSE* file for details.

## Contact

AVAniketh0905 (dekomori_sanae09)
Project Link: [fluidspy](https://github.com/AVAniketh0905/fluidspy)

## Acknowledgments

`Manim` has inspired me a lot!!!
