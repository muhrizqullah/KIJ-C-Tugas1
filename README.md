# KIJ-C-Tugas1

## How to run
1. Install [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/index.html)
2. Run `python3 server.py`
3. Run `python3 client.py`

## Running the automated test
1. Make sure you have [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/index.html) installed and `server.py` run.
2. Open `run-test.sh` to configure the test. The test has 4 parameters:
    - `encryptionMethods`. Change this variable to choose what encryption you want to test. You can choose "aes", "des", "rc4", "diy_aes", or "diy_des".
    - `files`. Choose what files that will be used to test the encryption.
    - `count`. Choos how many times the test will be conducted on each encryptions and each files.
    - `csv`. The test result output file name.
3. Run `run-test.sh`
