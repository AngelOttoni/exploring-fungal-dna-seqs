---

# MAFFT Sequence Alignment Script

This Python script is designed to perform sequence alignment using the MAFFT software and manage the output and error logs. It is particularly useful when you want to align biological sequences in a batch process.

## Requirements

- Python (3.x recommended)
- MAFFT software installed on your system

## Usage

1. Set the paths to the MAFFT executable, input sequence file, output file, error log file, and alignment process log file in the script.

```python
mafft_exe = "/lib/mafft/bin/mafft"
input_file = "./seqs_its.fasta"
output_file = "./its_alignment.fasta"
error_file = "./mafft_error.log"
alignment_log_file = "./mafft_log.log"
```

2. Run the script. It will execute MAFFT with the specified input file and redirect the standard output to the output file and the standard error to the alignment process log file.

```shell
python mafft_alignment.py
```

3. If the alignment is successful, the aligned sequences will be saved in the `aligned_its_sequences.fasta` file. If there is an error during the alignment process, details will be saved in the `mafft_error.log` file.

## Notes

- This script uses the `subprocess` module in Python to execute the MAFFT command and manage the output and errors.
- It also handles the redirection of the MAFFT progress log to the `mafft_log.log` file to capture detailed information about the alignment process.

Feel free to customize the script according to your needs and file paths. For more information about MAFFT and its options, refer to the [MAFFT documentation](https://mafft.cbrc.jp/alignment/software/).

---
