# Developer guide

This covers the technical design and some common tasks for `binderbot`.
For broader contributing documentation, see [Contributing](./contributing.md).

## Developer documentation

### Architecture

The repository is an npm monorepo with three packages:

`packages/binderbot`
: The `binderbot` CLI, published to npm.

`packages/binderbot-action`
: The GitHub Action that spins up and tears down a BinderHub session.

`binderhub-client-next`
: A fork of `@jupyterhub/binderhub-client` (vendored as the `binderhub/` git submodule) that supports running in Node.js. It is private and bundled into the other two packages with `esbuild`.

The packages are authored as ESM, but several dependencies are CommonJS-only, so `esbuild` bundles and transpiles everything to CJS.

### Vendored `binderhub-client`

`@jupyterhub/binderhub-client` is browser-only, so it cannot run in the Node.js environments the CLI and Action target.
We therefore vendor a Node.js-compatible fork as the `binderhub/` git submodule, which tracks [`agoose77/binderhub@feat-node-support`](https://github.com/agoose77/binderhub/tree/feat-node-support).
The fix swaps the browser-only `@microsoft/fetch-event-source` dependency for the cross-runtime [`eventsource`](https://www.npmjs.com/package/eventsource) package.

Our plan is to upstream this change into BinderHub, see https://github.com/jupyterhub/binderhub/pull/2044 for the tracking PR.

### Development setup

```bash
git clone --recurse-submodules https://github.com/2i2c-org/binderbot
cd binderbot
npm ci
npm run build --workspaces
```

### Documentation

The documentation is a [MyST](https://mystmd.org) site in `docs/`, built with [nox](https://nox.thea.codes):

```bash
nox -s docs       # build static HTML in docs/_build/html
nox -s docs-live  # serve locally with live reload
```

The published docs are hosted on GitHub Pages (built from `main` by [`docs.yml`](https://github.com/2i2c-org/binderbot/blob/main/.github/workflows/docs.yml)).
The `netlify.toml` config only serves as a demo of per-PR deploy previews (it exists at <https://2i2c-binderbot.netlify.app> though the URL of each PR demo is unique).

### Releases

Releasing the CLI
: Merge the new version in `packages/binderbot/package.json` to `main`, then create a GitHub release with tag `cli-vX.X.X`. CI publishes to npm.

Releasing the action
: Merge a branch containing the built action (`npm run build -w packages/binderbot-action`) to `main`, then create a GitHub release with tag `action-vX`.

### Testing

The packages don't yet have unit tests, because the intention is to rely on the upstream `@jupyterhub/binderhub-client` package once it supports Node.js.

The action is tested in CI on every push: [`test.yml`](https://github.com/2i2c-org/binderbot/blob/main/.github/workflows/test.yml) launches `binder-examples/requirements` on mybinder.org with the action, then builds the small MyST project in [`test/`](https://github.com/2i2c-org/binderbot/tree/main/test) with `myst build --site --strict --execute`.
The test page contains a single code cell:

```python
import os

assert "CI" not in os.environ
```

GitHub Actions runners always set `CI=true`, so the build passes only if the code ran on the Binder pod rather than on the runner.
Watch real runs at [Test Build on BinderHub](https://github.com/2i2c-org/binderbot/actions/workflows/test.yml).
