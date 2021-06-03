# executor-cases
Summarize all Executor patterns for Hubble

## Repo Structure

- `success` folder summarizes (all) success cases;
- `fail` folder summarizes (all) success cases.

## A Valid Executor Source Package

On the presences of the files:
- 💠 Must have, Hubble requires it
- 🔸 Optional, Hubble can use it
- 🔹 Free to have, e.g. user files

On the name of the files:
- ⭕ Must follow the file name Hubble defined
- 🟢 Arbitrary file name

On the number of files:
- 1️⃣ Only one
- 🔢 Can be multiple files

```text
- foobar.git/  💠🟢1️⃣
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
```

### Success cases

Hubble v1 support planning 💜

Hubble support | Folder | Single Python file | `config.yml` |  Internal dependencies | External dependencies | `requirements.txt` with `jina` | `requirements.txt` | `Dockerfile` | `manifest.yml` | `README.md` |
| --- | --- | --- | --- | --- | --- | --- | --- |--- |--- |--- |
| 💜 | `case1` |  ✅ |
| 💜 | `case2` |  ✅ | ✅ |
| 💜 | `case3` |  ✅ | ✅ |✅ |
|   | `case4` |  ✅ | ✅ |✅ |✅ |
| 💜 | `case5` |  ✅ | ✅ |✅ |✅ |✅ |
| 💜 | `case6` |  ✅ | ✅ |✅ |✅ |✅ |✅ |
| 💜  | `case7` | ✅ | ✅ |✅ |✅ |✅ |✅ |✅ |
