# c-in-my-python (cimp)

> How to use your clibrary in Python with ctypes.

## Getting Started

To get started with this project locally, yourself you first need a few
prerequisites. This project was built for macOS and may need a few tweaks to
get started on Windows or Linux.

### Prerequisites

For this project you will need:
- Cmake
- C compiler
- Python3

This instructions show how to do this on macOS, for Linux or Windows please
check the specific installations.

1. Install homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install cmake, gcc and Python3

```bash
brew update
brew install cmake gcc pyenv
pyenv install 3.9.1
```

3. Download this repository and set a local Python version

```bash
git clone https://github.com/henriwoodcock/c-in-my-python.git
cd c-in-my-python
pyenv local 3.9.1
```

### Installation

To build the library we create a build directory, use cmake to build the
makefiles and finally build the application.

```bash
mkdir build
cd build
cmake ..
make -j8
cd ../
```

### Run the tests

Before running in Python, make sure the c application has build correctly:

```bash
./run_tests.sh
```

## Run the Python script

The c library will now be used in Python:

```bash
python main.py
```

You should see "ALL TESTS PASSED".
