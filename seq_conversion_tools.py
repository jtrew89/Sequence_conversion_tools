# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:14:29 2023

@author: Jahcub Trew
"""

##A set of tools, that can be used to convert sequences to all different sequencing
##format types. Also convert DNA to RNA and both to amino acids

##import libraries used in script
import os
from Bio import AlignIO
#from Bio import SeqIO
import argparse
import subprocess

##set up arguments
parser = argparse.ArgumentParser(description=(
                                'Sequence conversion script. Specify formats in lower case. Formats accepted: fasta, clustal, emboss, nexus, phylip, phylip-sequential and phylip-relaxed'
                                ))
parser.add_argument('-d', '--working_directory', dest='directory', help='directory input file(s) are kept in', required=True)
parser.add_argument('-i', '--input', dest='in_filename', help='name of input file, including extension', required=True)
parser.add_argument('-t', '--input_type', dest='in_type', help= "alignment format of input file ('fasta', 'pylip', 'nexus')", required=True)
parser.add_argument('-o', '--output', dest='out_filename', help='name of output file, including extension', required=True)
parser.add_argument('-ot', '--output_type', dest='out_type', help="alignment format of input file ('fasta', 'pylip', 'nexus')", required=True)
parser.add_argument('-od', '--output_directory', dest='out_directory', help='specify directory for output file if different')
 

args = parser.parse_args()

##set working directory 
os.chdir(args.directory)

##load fasta sequence (AlignIO.parse returns a MSA as an interator, to get
#access to seperate sequences it has to be saved into a list)
if args.out_directory:
    os.chdir(args.out_directory)
    with open(args.in_filename, 'r') as input_handle:
        with open(args.out_filename, 'w') as output_handle:
            ##convert and write out sequence file
            alignment = AlignIO.parse(input_handle, args.in_type)
            seq_out = AlignIO.write(alignment, output_handle, args.out_type)
            ##some alignment stats output automatically
#           print('Alignment length is %i' % alignment.get_alignment_length())
#           print(subprocess.call(['grep', '-c', '>', 'test_fasta.fasta']) 'sequences in this alignment')

else:
    with open(args.in_filename, 'r') as input_handle:
        with open(args.out_filename, 'w') as output_handle:
            ##convert and write out sequence file
            alignment = AlignIO.parse(input_handle, args.in_type)
            seq_out = AlignIO.write(alignment, output_handle, args.out_type)
            ##some alignment stats output automatically
#           print('Alignment length is %i' % alignment.get_alignment_length())
#           print(subprocess.call(['grep', '-c', '>', 'test_fasta.fasta']) 'sequences in this alignment')

#if args.fastq: