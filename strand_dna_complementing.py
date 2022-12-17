import pandas as pd
import numpy as np
import yaml
from Bio import SeqIO
from Bio.Seq import Seq
from rich import print as rprint


def main():
   with open('./config.yaml', 'r') as config_file:
      config = yaml.safe_load(config_file)
   
   n_threads = config['performance']['threads']
   
   if n_threads <= 1:
      pass
   else:
      pass
   
   file_path = 'sequences/GCF_000006945.2_ASM694v2_genomic.fna'
   sequences = SeqIO.parse(file_path, 'fasta')

   for seq in sequences:
      rna_m = seq.seq
      proteome = rna_m.translate()
      proteome_array = proteome.split('*')
      
      np.array(proteome_array)
      
      # for protein in proteome_array:
      #    print(protein)
      break
   
main()