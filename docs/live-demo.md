---
kernelspec:
  name: python3
  display_name: Python 3
---

# Live demo: this page was computed on Binder

The outputs on this page were computed when the documentation was built, on a Binder session that the [GitHub Action](./github-action.md) started for the build.

Where did this code run?

```{code-cell} python3
import platform

print(f"This code ran on: {platform.node()}")
```

A hostname starting with `jupyter-binder-` means the code ran on a [mybinder.org](https://mybinder.org) pod.

This documentation is built with the following `binderbot` GitHub action configuration, which specifies the repository to use on Binder:

```{literalinclude} ../.github/workflows/docs.yml
:start-at: 2i2c-org/binderbot@HEAD
:end-before: name: Build docs
```

We can then import any package installed in that Binder image, such as NumPy:

```{code-cell} python3
import numpy as np

x = np.linspace(0, np.pi, 5)
np.round(np.sin(x), 3)
```
