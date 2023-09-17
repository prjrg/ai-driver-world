import jax
import jax.numpy as jnp
import jax.random as jr

import numpy as np

import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
import matplotlib_inline

matplotlib_inline.backend_inline.set_matplotlib_formats("svg", "pdf")
from matplotlib.colors import to_rgba

import seaborn as sns

sns.set()


def simple_graph(x):
    x = x + 2
    x = x**2
    x = x + 3
    return x.mean()


inp = jnp.arange(3, dtype=jnp.float32)
print(jax.make_jaxpr(simple_graph)(inp))

