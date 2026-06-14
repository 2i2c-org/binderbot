# About the project

Clinder is currently maintained by [2i2c](https://2i2c.org) and developed at [2i2c-org/clinder](https://github.com/2i2c-org/clinder).
It bundles a fork of [`@jupyterhub/binderhub-client`](https://github.com/jupyterhub/binderhub) extended to run in Node.js.
Our plan is to upstream that Node.js support (see [jupyterhub/binderhub#2044](https://github.com/jupyterhub/binderhub/pull/2044)) and move Clinder into the JupyterHub community so it lives alongside the tools it builds on.
See [how to contribute](./contributing.md) to get involved.

## History

Inspiration for `clinder` comes from the [Pangeo binderbot](https://github.com/pangeo-gallery/binderbot), which was inspired by Ryan Abernathey's [Statement of Need: integrating JupyterBook and JupyterHubs via CI](https://discourse.pangeo.io/t/statement-of-need-integrating-jupyterbook-and-jupyterhubs-via-ci/2705) and related to [JupyterHub/BinderHub + Jupyter Book as a publishing platform](https://discourse.jupyter.org/t/feature-idea-jupyterhub-binderhub-jupyter-book-as-a-publishing-platform/8359).

Clinder re-implements much of the same functionality to be more modular and stable, better-integrated with Jupyter Book, and in a state that we can upstream into `JupyterHub`. This work on `Clinder` was funded by Project Pythia (see below).

## Acknowledgements

Most of Clinder's development has been funded by [Project Pythia](https://projectpythia.org), supported by the U.S. National Science Foundation through EarthCube award [#2026863](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026863).
