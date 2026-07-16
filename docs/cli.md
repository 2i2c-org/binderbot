# Use the CLI

The `binderbot` command-line tool starts and stops BinderHub sessions from your own machine or scripts.
If you're using this as part of CI/CD in GitHub, see [](./github-action.md).

## Install

```bash
npm install -g binderbot
```

## Start a session

```bash
binderbot start https://mybinder.org/ --github-repo binder-examples/requirements
```

This streams the Binder build logs and, once the server is ready, prints its URL and token.

% TODO: Make this programmatically generated? Or we'll need to update each time
% we change the CLI docs.
```
Usage: binderbot start [options] <binderhub <url>>

Arguments:
  binderhub <url>       BinderHub URL

Options:
  --github-repo <repo>  GitHub repo
  --github-ref <ref>    GitHub ref (default: "HEAD")
  --json                Output JSON
  --build-token         BinderHub build token
  -h, --help            display help for command
```

## Save the environment variabels for re-use

Use `--json` to print `{"url": ..., "token": ...}` on `stdout` so you can save to disk (the build logs will then be sent to `stderr`):

```bash
binderbot start https://mybinder.org/ --github-repo binder-examples/requirements --json > session.json
```

Unlike the [GitHub Action](./github-action.md), the CLI does not set environment variables automaitcally, so export the connection info yourself for the examples below:

```bash
export JUPYTER_BASE_URL=$(jq -r .url session.json)
export JUPYTER_TOKEN=$(jq -r .token session.json)
```

## Open JupyterLab in the session

The session is a full Jupyter server, so the quickest demo is to open its JupyterLab in your browser:

```bash
open "${JUPYTER_BASE_URL}lab?token=${JUPYTER_TOKEN}"  # macOS; use xdg-open on Linux
```

## Execute a MyST or Jupyter Book project

[MyST](https://mystmd.org) and [Jupyter Book](https://jupyterbook.org) execute against the session whenever `JUPYTER_BASE_URL` and `JUPYTER_TOKEN` are set, with no extra configuration:

```bash
myst build --html --execute
```

The build log shows MyST connecting to the Binder kernel rather than starting a local one, and the page outputs are computed on the Binder pod.
The [live demo](./live-demo.md) uses this pattern in CI to build these docs.

### Execute on non-GitHub build platforms

To use `binderbot` on platforms other than GitHub Actions, you can follow the logic above with other CI/CD configuration. For example, you could host your website on **Netlify** to get **Pull Request previews** and use configuration like the following:
On Netlify, in `netlify.toml`:

```toml
[build]
  publish = "_build/html"
  command = """
  npm install -g mystmd binderbot && \
  binderbot start https://mybinder.org/ --github-repo org/repo --json > session.json && \
  export JUPYTER_BASE_URL=$(jq -r .url session.json) JUPYTER_TOKEN=$(jq -r .token session.json) && \
  myst build --html --execute && \
  binderbot stop "$JUPYTER_BASE_URL" "$JUPYTER_TOKEN"
  """
```

On Read the Docs, in `.readthedocs.yaml` (each command runs in a separate shell, so the session must start, build, and stop within one command):

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    nodejs: "22"
  commands:
    - npm install -g mystmd binderbot
    - >
      binderbot start https://mybinder.org/ --github-repo org/repo --json > session.json
      && export JUPYTER_BASE_URL=$(jq -r .url session.json) JUPYTER_TOKEN=$(jq -r .token session.json)
      && myst build --html --execute
      && binderbot stop "$JUPYTER_BASE_URL" "$JUPYTER_TOKEN"
    - mkdir -p $READTHEDOCS_OUTPUT && cp -r _build/html $READTHEDOCS_OUTPUT/html
```

If a build fails before reaching `binderbot stop`, the session is cleaned up by the BinderHub's inactivity timeout.

## Stop a session

Pass the URL and token printed by `binderbot start`:

```bash
binderbot stop <url> <token>
```

For example, reading them from the `session.json` written above:

```bash
binderbot stop "$(jq -r .url session.json)" "$(jq -r .token session.json)"
```

Binder sessions time out after a period of inactivity, but shutting them down explicitly frees resources for other users.
