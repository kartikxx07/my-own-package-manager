# 🐍 Own Package Manager (OPM)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)

A lightweight, educational Python package manager built from scratch — designed to understand how tools like `pip`, `uv`, and `poetry` actually work under the hood.
## 🚀 Features

✅ Fetches metadata for any Python package from **PyPI**  
✅ Downloads `.whl` or `.tar.gz` distribution files  
✅ Computes and verifies **SHA256 hashes** for file integrity  
✅ Supports dependency resolution through recursive metadata parsing  
✅ Modular structure with separate components for fetching, verification, and installation  

---

## 🧩 Project Structure

``` bash
own-package-manager/
│
├── fetcher.py # Fetches metadata and downloads package files
├── utils.py # Hash computation and verification logic
├── installer.py # Verifies and installs validated packages
├── resolver.py # Resolves dependencies recursively
├── downloads/ # Stores downloaded files
└── README.md # Project documentation
```

## 🧠 How It Works

### 1. **Fetch Metadata**
```python
from fetcher import fetch_metadata
```
metadata = fetch_metadata("requests")
print(metadata)
Fetches the latest release info from PyPI, including:
- download URL
- version
- supported Python versions
- SHA256 checksum

### 2. **Download Package**
``` python
from fetcher import download_package

file_path = download_package(metadata["url"])
```
### 3. Verify Integrity
``` python
from utils import verify_hash

is_valid = verify_hash(file_path, metadata["sha256"])
if is_valid:
    print("File integrity verified!")
else:
    print("Hash mismatch! Possible tampering detected.")
```

### 4. Install Packages
``` python
from installer import install_package

install_package(file_path)
```

### 5. Resolve Dependencies
``` python
from resolver import resolve_dependencies
resolve_dependencies("requests")
```

## Requirements
- Python 3.9+
- requests
- (optional) packaging for semantic version comparison
``` bash
pip install requests packaging
```
## Next Features(Roadmap)
- Handle version constraints (>=, <=, ==)
- Detect and report dependency conflicts
- Parallel dependency resolution
- Lockfile generation (opm.lock)
- Offline / cached installation mode
- Dependency tree visualization
- Semantic version update notifications

## Example Usage(Future)
``` bash
$ opm install requests
Resolving dependencies...
Downloading packages...
Verifying hashes...
Installing to environment...
✅ requests 2.31.0 installed successfully!
```
## Goal of this Project
This project is meant as a learning tool, not a production-ready installer.
It demonstrates how package managers like pip, uv, and poetry work behind the scenes:
- Fetching metadata from PyPI
- Handling dependency graphs
- Verifying hashes
- Installing packages into environments




