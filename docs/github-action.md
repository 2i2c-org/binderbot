# Use the GitHub Action

The `2i2c-org/clinder` action provisions a BinderHub session and exposes the Jupyter server information to the rest of the job.
The action:

- Creates a Binder session for the repository you configure.
- Exports the `JUPYTER_BASE_URL` and `JUPYTER_TOKEN` environment variables for subsequent steps.
- Shuts down the BinderHub server when the job completes.

It is meant to be used with **Jupyter Book** or the **MyST Document Engine**, which automatically detect these environment variables in executing notebooks.

## Example

Build a MyST site whose code is executed on mybinder.org rather than on the CI runner:

```{code-block} yaml
:emphasize-lines: 11-14,20-21
:linenos:
name: Build on BinderHub

on:
  push:
jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      # Sets the JUPYTER_BASE_URL and JUPYTER_TOKEN env vars
      - uses: 2i2c-org/clinder@action-v1
        with:
          hub-url: https://mybinder.org/
      - uses: actions/setup-node@v4
        with:
          node-version: 20.x
      - name: Install MyST Markdown
        run: npm install -g mystmd
      - name: Build MyST Project
        run: myst build --html --execute
```

Because `JUPYTER_BASE_URL` and `JUPYTER_TOKEN` are in the environment, `myst build --execute` runs the project's code on the Binder session.

## Inputs

`hub-url` (required)
: The URL of the BinderHub, e.g. `https://mybinder.org/`.

`repo`
: The `ORG/REPO` identifying a GitHub repository to build. Defaults to the repository running the workflow.

`ref`
: The Git reference (e.g. branch name) to build. Defaults to the ref that triggered the workflow.

`build-token`
: A BinderHub build token, if your hub requires one.

## Outputs

`url`
: The URL of the started Jupyter server.

`token`
: The token of the started Jupyter server.

Both values are also exported as the `JUPYTER_BASE_URL` and `JUPYTER_TOKEN` environment variables, and the token is registered as a secret so it is masked in logs.
