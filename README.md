# tap-klass

`tap-klass` is a Singer tap for Statistics Norway's Klass API for codes and classifications.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.



## Installation

Install from GitHub:

```bash
pipx install git+https://github.com/radbrt/tap-klass.git
```

## Configuration

### Accepted Config Options

#### Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

#### Settings

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| classifications     | False    | None    | List of classifications with options            |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |
| batch_config        | False    | None    |             |


The `classifications` setting list items contains the following elements:

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| name                | False    | True    | User-defined name of the classification           |
| id                  | False    | True    | The classification ID, found in the URL. ex "131" for municipalities |
| valid_at            | False    | None    | Date string for retreiving codes valid at given date |
| valid_from          | False    | None    | Date string for retrieving codes valid on or after given date |
| valid_to            | False    | None    | The max depth to flatten schemas. |
| language            | False    | nb      | The language to be returned. Either nb (Norwegian Bokmål), nn (Norwegian Nynorsk) or en (English) |


A full list of supported settings and capabilities is available by running: `tap-klass --about`

#### Supported Python Versions

* 3.8
* 3.9
* 3.10
* 3.11

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-klass --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

This API does not require authentication.

## Usage

You can easily run `tap-klass` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-klass --version
tap-klass --help
tap-klass --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-klass` CLI interface directly using `poetry run`:

```bash
poetry run tap-klass --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-klass
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-klass --version
# OR run a test `elt` pipeline:
meltano elt tap-klass target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
