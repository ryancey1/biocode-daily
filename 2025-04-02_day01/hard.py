#! /usr/bin/env python3

import unittest

"""
1b. mRNA to Protein Translator

Concept: Translating mRNA into Protein
In cells, genetic information encoded in DNA is transcribed into messenger RNA (mRNA) and then translated into a chain of amino acids — a protein. This translation process involves reading the mRNA in sets of three bases called codons:

- Translation begins at the first occurrence of the start codon AUG, which codes for Methionine (Met)
- The ribosome reads codons one at a time, moving forward in triplets
- Translation ends at the first stop codon encountered: UAA, UAG, or UGA

Only codons that appear after the start and before the stop are translated.

---

Example
Input mRNA sequence: CCGAUGGCUUAA

The first start codon AUG appears at index 3
The codons read after that are: AUG, GCU, UAA
Translation proceeds: Met, Ala → STOP

Output: ["Met", "Ala"]

---

Your Task
Write a function that: 1. Searches the mRNA sequence for the first AUG codon 2. Translates each subsequent codon using the provided codon table 3. Stops translation when a stop codon is encountered or the sequence ends

If no start codon is found, return an empty list.
"""


CODON_TABLE = {
    "AUG": "Met",
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr",
    "UGU": "Cys", "UGC": "Cys",
    "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser",
    "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
}


class Solution(unittest.TestCase):
    def test_correct_output_regular(self):
        """Test for regular mRNA string"""
        self.assertEqual(translate_mrna('CCGAUGGCUUAA'),
                         ['Met', 'Ala'])

    def test_correct_output_no_stop_codon(self):
        """Test for mRNA string without 'STOP'"""
        self.assertEqual(translate_mrna('CCGAUGGCUGGG'),
                         ['Met', 'Ala', 'Gly'])

    def test_correct_output_no_start_codon(self):
        """Test for mRNA string without 'Met'"""
        self.assertEqual(translate_mrna('CCGAGGGCUUAA'),
                         [])


def translate_mrna(mrna: str) -> list[str]:
    # local copy of CODON_TABLE
    codon_table = CODON_TABLE
    mrna = mrna.upper()
    protein = []
    # find index of the start codon (if present)
    codon_ix = mrna.find('AUG')
    if codon_ix == -1:
        # return empty list if no start codon
        return protein
    else:
        protein.append(codon_table['AUG'])
        codon_ix += 3
    for i in range(codon_ix, len(mrna), 3):
        codon = mrna[i:i + 3]
        amino_acid = codon_table[codon]
        if amino_acid == "STOP":
            break
        else:
            protein.append(amino_acid)
    return protein
