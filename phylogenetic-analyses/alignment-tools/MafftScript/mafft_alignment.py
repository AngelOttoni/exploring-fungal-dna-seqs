import subprocess

# Path to the MAFFT executable and input file
mafft_exe = "/lib/mafft/bin/mafft"
input_file = "./seqs_its.fasta"

# Path to the output file of the alignment
output_file = "./aligned_its_sequences.fasta"

# Path to the error log file
error_file = "./mafft_error.log"

# Path to the alignment process log file
alignment_log_file = "./mafft_log.log"

# Command line to run MAFFT and redirect output, errors, and the log
mafft_cmd = f"{mafft_exe} --thread 1 {input_file} > {output_file} 2> {alignment_log_file}"

try:
    subprocess.run(mafft_cmd, shell=True, check=True)
    print(f"The alignment was completed successfully and saved to {output_file}.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred during the alignment. Details in the error file: {error_file}")
