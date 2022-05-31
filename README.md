# executor-cases

Summarize all Executor patterns for Hubble

## Repo Structure

- `success` folder summarizes (all) successful cases;
- `error` folder summarizes (all) failure cases.

## A Valid Executor Source Package

- On the presences of the files:
    - 💠 Must have, Hubble requires it
    - 🔸 Optional, Hubble can use it
    - 🔹 Free to have, e.g. user files

- On the name of the files:
    - ⭕ Must follow the file name Hubble defined
    - 🟢 Arbitrary file name

- On the number of files:
    - 1️⃣ Only one
    - 🔢 Can be multiple

```text
- foobar.git/  🔸🟢1️⃣
    |- hubble.yml  🔸⭕1️⃣
    |- foo/  💠🟢️🔢
        |
        |- bar.py  💠🟢1️⃣
        |- helper(s).py  🔹🟢🔢
        |- Dockerfile  🔸⭕1️⃣
        |- README.md  🔸⭕1️⃣
        |- requirements.txt  🔸⭕1️⃣
        |- config.yml  🔸⭕1️⃣
        |- manifest.yml  🔸⭕1️⃣
    |
    |- foo2/...
```

[`case9` showcases the **"maximum"** form of the **"minimum unit"** package.](success/case9)


### Fixed filenames and their Purposes

| ⭕ Fixed file name | Purpose |
| --- | --- |
| `Dockerfile` | the Dockerfile that Hubble will build on |
| `README.md` | the usage of the Executor |
| `requirements.txt` | `pip install -r` required packages |
| `config.yml` | the Executor YAML config file |
| `manifest.yml` | an annotation contains meta information of the Executor to get better appealing on Jina Hub |
| `hubble.yml` | the build config file for Hubble |

### Fields of `manifest.yml`

`manifest.yml` is optional.

`manifest.yml` annotates your image so that it can be managed by Hubble. To get better appealing on Jina Hub, you should
carefully set `manifest.yml` to the correct values.

| Key | Description | Default |
| --- | --- | --- |
| `manifest_version` | The version of the manifest protocol | `1` |
| `name` | Human-readable title of the Executor | None |
| `description` | Human-readable description of the Executor | None |
| `url` | URL to find more information on the Executor, normally it should be the GitHub repo URL | None |
| `keywords` | A list of strings help user to filter and locate your package  | None | 

### Fields of `hubble.yml`

TBA by @mapleeit

## Success cases

Hubble v1 support planning

- Built and run 💜
- Built but can't run 🚧

Hubble support | Folder | Executors in single Python file | `config.yml` |  Internal module dependencies | External package dependencies | `requirements.txt` with `jina` | `requirements.txt` | `Dockerfile` | `manifest.yml` | `README.md` |
| --- | --- | --- | --- | --- | --- | --- | --- |--- |--- |--- |
| 💜 | [`case1`](success/case1) | ✅ |
| 💜 | [`case2`](success/case2) | ✅ | ✅ |
| 💜 | [`case3`](success/case3) | ✅ | ✅ |✅ |
| 🚧 | [`case4`](success/case4) | ✅ | ✅ |✅ |✅ |
| 💜 | [`case5`](success/case5) | ✅ | ✅ |✅ |✅ |✅ |
| 💜 | [`case6`](success/case6) | ✅ | ✅ |✅ |✅ |✅ |✅ |
| 💜 | [`case7`](success/case7) | ✅ | ✅ |✅ |✅ |✅ |✅ |✅ |
| 💜 | [`case8`](success/case8) | ✅ | ✅ |✅ |✅ |✅ |✅ |✅ |✅ |
| 💜 | [`case9`](success/case9) | ✅ | ✅ |✅ |✅ |✅ |✅ |✅ |✅ |✅ |

`case9` is the complete form.

### Defining multiple Executors in one repository

**Not yet decided - up for discussion!**

We might want to combine multiple Executors into one repository for easier maintainability.
Suggestion (see `multi1`):

1. include `setup.py` which install all executors with the prefix `jinahub.`
2. hubble first build the python package from the repository
3. afterwards hubble build the docker images
    - `py_modules` gets empowered by being able to import from a given module import path.
    - every executor needs the top-level package inside `requirements.txt`

Beauty of this approach:

1. Building the python package and building the docker image is decoupled.
**Is this good or bad?**
2. We can have a full hub again, which is independant of core.


## Executor Package Normalizer in Hubble

Package normalizer completes `case1-8` to `case9`.
