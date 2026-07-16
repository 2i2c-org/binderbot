# BinderBot - a BinderHub CLI and GitHub Action

BinderBot starts and stops [BinderHub](https://binderhub.readthedocs.io) sessions from the command line or from a GitHub Actions workflow.
It gives you a running Jupyter server, built from any Binder-ready repository and running in the cloud, and the URL and token to execute code on it.

For example, the following command will start a Binder session and return the URL and Token so that you can execute code within it:

```bash
binderbot start https://mybinder.org/ --github-repo binder-examples/requirements
```

## The problem this solves

Many users execute notebooks in CI (e.g. GitHub Workflows) in order to deploy to public websites or Jupyter Books.
However, many notebooks require computational resources or access to data that is not accessible to the CI environments.
[BinderHub](https://binderhub.readthedocs.io) allows you to build and execute arbitrary computational environments in the cloud, but it cannot easily be controlled from the command line.
Users need a way to request and control computational resources in the cloud, and then use these resources as part of their CI build.

## What BinderBot does

BinderBot asks a BinderHub to build and launch a session, streams the build logs so you can inspect them, and reports two values when the server is ready: the URL of the running Jupyter server, and the token needed to execute code on it.

Tools like [MyST](https://mystmd.org) and [Jupyter Book](https://jupyterbook.org) read these values from two environment variables to decide where to execute code:

- `JUPYTER_BASE_URL`: the URL of the Jupyter server
- `JUPYTER_TOKEN`: the token for that server

The [GitHub Action](./github-action.md) exports both variables for the rest of the workflow automatically. The [BinderBot CLI](./cli.md) lets you export these variables yourself.
A documentation build in CI can therefore execute its notebooks on a BinderHub, with no environment setup in the workflow itself.

## Two ways to use it

- [GitHub Action](./github-action.md): Provision a BinderHub session inside a workflow, for example to execute a Jupyter Book or MyST site during a deploy.
- [Command-line tool](./cli.md): Start and stop BinderHub sessions from your own machine or scripts.

The [live demo](./live-demo.md) is a page in these docs whose outputs were computed on Binder.

## Get involved

BinderBot is currently maintained by [2i2c](https://2i2c.org), with support from [Project Pythia](https://2i2c.org/collaborators/pythia). Our intent is upstream this project and build a broader community around it.

See [how to engage](./contributing.md) to ask questions, report issues, or contribute, and [about the project](./about.md) for its history and direction.
