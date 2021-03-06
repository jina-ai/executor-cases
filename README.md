# executor-cases

Summarize all Executor patterns for Hubble

## Repo Structure

- `success` folder summarizes (all) successful cases;
- `error` folder summarizes (all) failure cases.

## A Valid Executor Source Package

- On the presences of the files:
    - π  Must have, Hubble requires it
    - πΈ Optional, Hubble can use it
    - πΉ Free to have, e.g. user files

- On the name of the files:
    - β­ Must follow the file name Hubble defined
    - π’ Arbitrary file name

- On the number of files:
    - 1οΈβ£ Only one
    - π’ Can be multiple

```text
- foobar.git/  πΈπ’1οΈβ£
    |- hubble.yml  πΈβ­1οΈβ£
    |- foo/  π π’οΈπ’
        |
        |- bar.py  π π’1οΈβ£
        |- helper(s).py  πΉπ’π’
        |- Dockerfile  πΈβ­1οΈβ£
        |- README.md  πΈβ­1οΈβ£
        |- requirements.txt  πΈβ­1οΈβ£
        |- config.yml  πΈβ­1οΈβ£
        |- manifest.yml  πΈβ­1οΈβ£
    |
    |- foo2/...
```

[`case9` showcases the **"maximum"** form of the **"minimum unit"** package.](success/case9)


### Fixed filenames and their Purposes

| β­ Fixed file name | Purpose |
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

- Built and run π
- Built but can't run π§

Hubble support | Folder | Executors in single Python file | `config.yml` |  Internal module dependencies | External package dependencies | `requirements.txt` with `jina` | `requirements.txt` | `Dockerfile` | `manifest.yml` | `README.md` |
| --- | --- | --- | --- | --- | --- | --- | --- |--- |--- |--- |
| π | [`case1`](success/case1) | β |
| π | [`case2`](success/case2) | β | β |
| π | [`case3`](success/case3) | β | β |β |
| π§ | [`case4`](success/case4) | β | β |β |β |
| π | [`case5`](success/case5) | β | β |β |β |β |
| π | [`case6`](success/case6) | β | β |β |β |β |β |
| π | [`case7`](success/case7) | β | β |β |β |β |β |β |
| π | [`case8`](success/case8) | β | β |β |β |β |β |β |β |
| π | [`case9`](success/case9) | β | β |β |β |β |β |β |β |β |

`case9` is the complete form.

## Executor Package Normalizer in Hubble

Package normalizer completes `case1-8` to `case9`.
