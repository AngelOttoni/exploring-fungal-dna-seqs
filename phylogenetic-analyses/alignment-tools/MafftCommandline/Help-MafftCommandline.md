Help on class MafftCommandline in module Bio.Align.Applications._Mafft:

class MafftCommandline(Bio.Application.AbstractCommandline)
 |  MafftCommandline(cmd='mafft', **kwargs)
 |  
 |  Command line wrapper for the multiple alignment program MAFFT.
 |  
 |  http://align.bmr.kyushu-u.ac.jp/mafft/software/
 |  
 |  Notes
 |  -----
 |  Last checked against version: MAFFT v6.717b (2009/12/03)
 |  
 |  References
 |  ----------
 |  Katoh, Toh (BMC Bioinformatics 9:212, 2008) Improved accuracy of
 |  multiple ncRNA alignment by incorporating structural information into
 |  a MAFFT-based framework (describes RNA structural alignment methods)
 |  
 |  Katoh, Toh (Briefings in Bioinformatics 9:286-298, 2008) Recent
 |  developments in the MAFFT multiple sequence alignment program
 |  (outlines version 6)
 |  
 |  Katoh, Toh (Bioinformatics 23:372-374, 2007)  Errata PartTree: an
 |  algorithm to build an approximate tree from a large number of
 |  unaligned sequences (describes the PartTree algorithm)
 |  
 |  Katoh, Kuma, Toh, Miyata (Nucleic Acids Res. 33:511-518, 2005) MAFFT
 |  version 5: improvement in accuracy of multiple sequence alignment
 |  (describes [ancestral versions of] the G-INS-i, L-INS-i and E-INS-i
 |  strategies)
 |  
 |  Katoh, Misawa, Kuma, Miyata (Nucleic Acids Res. 30:3059-3066, 2002)
 |  
 |  Examples
 |  --------
 |  >>> from Bio.Align.Applications import MafftCommandline
 |  >>> mafft_exe = "/opt/local/mafft"
 |  >>> in_file = "../Doc/examples/opuntia.fasta"
 |  >>> mafft_cline = MafftCommandline(mafft_exe, input=in_file)
 |  >>> print(mafft_cline)
 |  /opt/local/mafft ../Doc/examples/opuntia.fasta
 |  
 |  If the mafft binary is on the path (typically the case on a Unix style
 |  operating system) then you don't need to supply the executable location:
 |  
 |  >>> from Bio.Align.Applications import MafftCommandline
 |  >>> in_file = "../Doc/examples/opuntia.fasta"
 |  >>> mafft_cline = MafftCommandline(input=in_file)
 |  >>> print(mafft_cline)
 |  mafft ../Doc/examples/opuntia.fasta
 |  
 |  You would typically run the command line with mafft_cline() or via
 |  the Python subprocess module, as described in the Biopython tutorial.
 |  
 |  Note that MAFFT will write the alignment to stdout, which you may
 |  want to save to a file and then parse, e.g.::
 |  
 |      stdout, stderr = mafft_cline()
 |      with open("aligned.fasta", "w") as handle:
 |          handle.write(stdout)
 |      from Bio import AlignIO
 |      align = AlignIO.read("aligned.fasta", "fasta")
 |  
 |  Alternatively, to parse the output with AlignIO directly you can
 |  use StringIO to turn the string into a handle::
 |  
 |      stdout, stderr = mafft_cline()
 |      from io import StringIO
 |      from Bio import AlignIO
 |      align = AlignIO.read(StringIO(stdout), "fasta")
 |  
 |  Method resolution order:
 |      MafftCommandline
 |      Bio.Application.AbstractCommandline
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, cmd='mafft', **kwargs)
 |      Initialize the class.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  LEXP
 |      Gap extension penalty to skip the alignment. Default: 0.00
 |      
 |      This controls the addition of the --LEXP parameter and its associated value.  Set this property to the argument value required.
 |  
 |  LOP
 |      Gap opening penalty to skip the alignment. Default: -6.00
 |      
 |      This controls the addition of the --LOP parameter and its associated value.  Set this property to the argument value required.
 |  
 |  aamatrix
 |      Use a user-defined AA scoring matrix. Default: BLOSUM62
 |      
 |      This controls the addition of the --aamatrix parameter and its associated value.  Set this property to the argument value required.
 |  
 |  adjustdirection
 |      Adjust direction according to the first sequence. Default off.
 |      
 |      This property controls the addition of the --adjustdirection switch, treat this property as a boolean.
 |  
 |  adjustdirectionaccurately
 |      Adjust direction according to the first sequence,for highly diverged data; very slowDefault off.
 |      
 |      This property controls the addition of the --adjustdirectionaccurately switch, treat this property as a boolean.
 |  
 |  amino
 |      Assume the sequences are amino acid (True/False). Default: auto
 |      
 |      This property controls the addition of the --amino switch, treat this property as a boolean.
 |  
 |  auto
 |      Automatically select strategy. Default off.
 |      
 |      This property controls the addition of the --auto switch, treat this property as a boolean.
 |  
 |  bl
 |      BLOSUM number matrix is used. Default: 62
 |      
 |      This controls the addition of the --bl parameter and its associated value.  Set this property to the argument value required.
 |  
 |  clustalout
 |      Output format: clustal (True) or fasta (False, default)
 |      
 |      This property controls the addition of the --clustalout switch, treat this property as a boolean.
 |  
 |  dpparttree
 |      The PartTree algorithm is used with distances based on DP. Default: off
 |      
 |      This property controls the addition of the --dpparttree switch, treat this property as a boolean.
 |  
 |  ep
 |      Offset value, which works like gap extension penalty, for group-to- group alignment. Default: 0.123
 |      
 |      This controls the addition of the --ep parameter and its associated value.  Set this property to the argument value required.
 |  
 |  fastapair
 |      All pairwise alignments are computed with FASTA (Pearson and Lipman 1988). Default: off
 |      
 |      This property controls the addition of the --fastapair switch, treat this property as a boolean.
 |  
 |  fastaparttree
 |      The PartTree algorithm is used with distances based on FASTA. Default: off
 |      
 |      This property controls the addition of the --fastaparttree switch, treat this property as a boolean.
 |  
 |  fft
 |      Use FFT approximation in group-to-group alignment. Default: on
 |      
 |      This property controls the addition of the --fft switch, treat this property as a boolean.
 |  
 |  fmodel
 |      Incorporate the AA/nuc composition information into the scoring matrix (True) or not (False, default)
 |      
 |      This property controls the addition of the --fmodel switch, treat this property as a boolean.
 |  
 |  genafpair
 |      All pairwise alignments are computed with a local algorithm with the generalized affine gap cost (Altschul 1998). Default: off
 |      
 |      This property controls the addition of the --genafpair switch, treat this property as a boolean.
 |  
 |  globalpair
 |      All pairwise alignments are computed with the Needleman-Wunsch algorithm. Default: off
 |      
 |      This property controls the addition of the --globalpair switch, treat this property as a boolean.
 |  
 |  groupsize
 |      Do not make alignment larger than number sequences. Default: the number of input sequences
 |      
 |      This property controls the addition of the --groupsize switch, treat this property as a boolean.
 |  
 |  input
 |      Input file name
 |      
 |      This controls the addition of the input parameter and its associated value.  Set this property to the argument value required.
 |  
 |  input1
 |      Second input file name for the mafft-profile command
 |      
 |      This controls the addition of the input1 parameter and its associated value.  Set this property to the argument value required.
 |  
 |  inputorder
 |      Output order: same as input (True, default) or alignment based (False)
 |      
 |      This property controls the addition of the --inputorder switch, treat this property as a boolean.
 |  
 |  jtt
 |      JTT PAM number (Jones et al. 1992) matrix is used. number>0. Default: BLOSUM62
 |      
 |      This controls the addition of the --jtt parameter and its associated value.  Set this property to the argument value required.
 |  
 |  lep
 |      Offset value at local pairwise alignment. Default: 0.1
 |      
 |      This controls the addition of the --lep parameter and its associated value.  Set this property to the argument value required.
 |  
 |  lexp
 |      Gap extension penalty at local pairwise alignment. Default: -0.1
 |      
 |      This controls the addition of the --lexp parameter and its associated value.  Set this property to the argument value required.
 |  
 |  localpair
 |      All pairwise alignments are computed with the Smith-Waterman algorithm. Default: off
 |      
 |      This property controls the addition of the --localpair switch, treat this property as a boolean.
 |  
 |  lop
 |      Gap opening penalty at local pairwise alignment. Default: 0.123
 |      
 |      This controls the addition of the --lop parameter and its associated value.  Set this property to the argument value required.
 |  
 |  maxiterate
 |      Number cycles of iterative refinement are performed. Default: 0
 |      
 |      This controls the addition of the --maxiterate parameter and its associated value.  Set this property to the argument value required.
 |  
 |  memsave
 |      Use the Myers-Miller (1988) algorithm. Default: automatically turned on when the alignment length exceeds 10,000 (aa/nt).
 |      
 |      This property controls the addition of the --memsave switch, treat this property as a boolean.
 |  
 |  namelength
 |      Name length in CLUSTAL and PHYLIP output.
 |      
 |                          MAFFT v6.847 (2011) added --namelength for use with
 |                          the --clustalout option for CLUSTAL output.
 |      
 |                          MAFFT v7.024 (2013) added support for this with the
 |                          --phylipout option for PHYLIP output (default 10).
 |                          
 |      
 |      This controls the addition of the --namelength parameter and its associated value.  Set this property to the argument value required.
 |  
 |  nofft
 |      Do not use FFT approximation in group-to-group alignment. Default: off
 |      
 |      This property controls the addition of the --nofft switch, treat this property as a boolean.
 |  
 |  noscore
 |      Alignment score is not checked in the iterative refinement stage. Default: off (score is checked)
 |      
 |      This property controls the addition of the --noscore switch, treat this property as a boolean.
 |  
 |  nuc
 |      Assume the sequences are nucleotide (True/False). Default: auto
 |      
 |      This property controls the addition of the --nuc switch, treat this property as a boolean.
 |  
 |  op
 |      Gap opening penalty at group-to-group alignment. Default: 1.53
 |      
 |      This controls the addition of the --op parameter and its associated value.  Set this property to the argument value required.
 |  
 |  partsize
 |      The number of partitions in the PartTree algorithm. Default: 50
 |      
 |      This controls the addition of the --partsize parameter and its associated value.  Set this property to the argument value required.
 |  
 |  parttree
 |      Use a fast tree-building method with the 6mer distance. Default: off
 |      
 |      This property controls the addition of the --parttree switch, treat this property as a boolean.
 |  
 |  phylipout
 |      Output format: phylip (True), or fasta (False, default)
 |      
 |      This property controls the addition of the --phylipout switch, treat this property as a boolean.
 |  
 |  quiet
 |      Do not report progress (True) or not (False, default).
 |      
 |      This property controls the addition of the --quiet switch, treat this property as a boolean.
 |  
 |  reorder
 |      Output order: aligned (True) or in input order (False, default)
 |      
 |      This property controls the addition of the --reorder switch, treat this property as a boolean.
 |  
 |  retree
 |      Guide tree is built number times in the progressive stage. Valid with 6mer distance. Default: 2
 |      
 |      This controls the addition of the --retree parameter and its associated value.  Set this property to the argument value required.
 |  
 |  seed
 |      Seed alignments given in alignment_n (fasta format) are aligned with sequences in input.
 |      
 |      This controls the addition of the --seed parameter and its associated value.  Set this property to the argument value required.
 |  
 |  sixmerpair
 |      Distance is calculated based on the number of shared 6mers. Default: on
 |      
 |      This property controls the addition of the --6merpair switch, treat this property as a boolean.
 |  
 |  thread
 |      Number of threads to use. Default: 1
 |      
 |      This controls the addition of the --thread parameter and its associated value.  Set this property to the argument value required.
 |  
 |  tm
 |      Transmembrane PAM number (Jones et al. 1994) matrix is used. number>0. Default: BLOSUM62
 |      
 |      This controls the addition of the --tm parameter and its associated value.  Set this property to the argument value required.
 |  
 |  treeout
 |      Guide tree is output to the input.tree file (True) or not (False, default)
 |      
 |      This property controls the addition of the --treeout switch, treat this property as a boolean.
 |  
 |  weighti
 |      Weighting factor for the consistency term calculated from pairwise alignments. Default: 2.7
 |      
 |      This controls the addition of the --weighti parameter and its associated value.  Set this property to the argument value required.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Bio.Application.AbstractCommandline:
 |  
 |  __call__(self, stdin=None, stdout=True, stderr=True, cwd=None, env=None)
 |      Execute command, wait for it to finish, return (stdout, stderr).
 |      
 |      Runs the command line tool and waits for it to finish. If it returns
 |      a non-zero error level, an exception is raised. Otherwise two strings
 |      are returned containing stdout and stderr.
 |      
 |      The optional stdin argument should be a string of data which will be
 |      passed to the tool as standard input.
 |      
 |      The optional stdout and stderr argument may be filenames (string),
 |      but otherwise are treated as a booleans, and control if the output
 |      should be captured as strings (True, default), or ignored by sending
 |      it to /dev/null to avoid wasting memory (False). If sent to a file
 |      or ignored, then empty string(s) are returned.
 |      
 |      The optional cwd argument is a string giving the working directory
 |      to run the command from. See Python's subprocess module documentation
 |      for more details.
 |      
 |      The optional env argument is a dictionary setting the environment
 |      variables to be used in the new process. By default the current
 |      process' environment variables are used. See Python's subprocess
 |      module documentation for more details.
 |      
 |      Default example usage::
 |      
 |          from Bio.Emboss.Applications import WaterCommandline
 |          water_cmd = WaterCommandline(gapopen=10, gapextend=0.5,
 |                                       stdout=True, auto=True,
 |                                       asequence="a.fasta", bsequence="b.fasta")
 |          print("About to run: %s" % water_cmd)
 |          std_output, err_output = water_cmd()
 |      
 |      This functionality is similar to subprocess.check_output(). In general
 |      if you require more control over running the command, use subprocess
 |      directly.
 |      
 |      When the program called returns a non-zero error level, a custom
 |      ApplicationError exception is raised. This includes any stdout and
 |      stderr strings captured as attributes of the exception object, since
 |      they may be useful for diagnosing what went wrong.
 |  
 |  __repr__(self)
 |      Return a representation of the command line object for debugging.
 |      
 |      e.g.
 |      
 |      >>> from Bio.Emboss.Applications import WaterCommandline
 |      >>> cline = WaterCommandline(gapopen=10, gapextend=0.5)
 |      >>> cline.asequence = "asis:ACCCGGGCGCGGT"
 |      >>> cline.bsequence = "asis:ACCCGAGCGCGGT"
 |      >>> cline.outfile = "temp_water.txt"
 |      >>> print(cline)
 |      water -outfile=temp_water.txt -asequence=asis:ACCCGGGCGCGGT -bsequence=asis:ACCCGAGCGCGGT -gapopen=10 -gapextend=0.5
 |      >>> cline
 |      WaterCommandline(cmd='water', outfile='temp_water.txt', asequence='asis:ACCCGGGCGCGGT', bsequence='asis:ACCCGAGCGCGGT', gapopen=10, gapextend=0.5)
 |  
 |  __setattr__(self, name, value)
 |      Set attribute name to value (PRIVATE).
 |      
 |      This code implements a workaround for a user interface issue.
 |      Without this __setattr__ attribute-based assignment of parameters
 |      will silently accept invalid parameters, leading to known instances
 |      of the user assuming that parameters for the application are set,
 |      when they are not.
 |      
 |      >>> from Bio.Emboss.Applications import WaterCommandline
 |      >>> cline = WaterCommandline(gapopen=10, gapextend=0.5, stdout=True)
 |      >>> cline.asequence = "a.fasta"
 |      >>> cline.bsequence = "b.fasta"
 |      >>> cline.csequence = "c.fasta"
 |      Traceback (most recent call last):
 |      ...
 |      ValueError: Option name csequence was not found.
 |      >>> print(cline)
 |      water -stdout -asequence=a.fasta -bsequence=b.fasta -gapopen=10 -gapextend=0.5
 |      
 |      This workaround uses a whitelist of object attributes, and sets the
 |      object attribute list as normal, for these.  Other attributes are
 |      assumed to be parameters, and passed to the self.set_parameter method
 |      for validation and assignment.
 |  
 |  __str__(self)
 |      Make the commandline string with the currently set options.
 |      
 |      e.g.
 |      
 |      >>> from Bio.Emboss.Applications import WaterCommandline
 |      >>> cline = WaterCommandline(gapopen=10, gapextend=0.5)
 |      >>> cline.asequence = "asis:ACCCGGGCGCGGT"
 |      >>> cline.bsequence = "asis:ACCCGAGCGCGGT"
 |      >>> cline.outfile = "temp_water.txt"
 |      >>> print(cline)
 |      water -outfile=temp_water.txt -asequence=asis:ACCCGGGCGCGGT -bsequence=asis:ACCCGAGCGCGGT -gapopen=10 -gapextend=0.5
 |      >>> str(cline)
 |      'water -outfile=temp_water.txt -asequence=asis:ACCCGGGCGCGGT -bsequence=asis:ACCCGAGCGCGGT -gapopen=10 -gapextend=0.5'
 |  
 |  set_parameter(self, name, value=None)
 |      Set a commandline option for a program (OBSOLETE).
 |      
 |      Every parameter is available via a property and as a named
 |      keyword when creating the instance. Using either of these is
 |      preferred to this legacy set_parameter method which is now
 |      OBSOLETE, and likely to be DEPRECATED and later REMOVED in
 |      future releases.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Bio.Application.AbstractCommandline:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Bio.Application.AbstractCommandline:
 |  
 |  parameters = None

