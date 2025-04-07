#! /usr/bin/env python3

import unittest

'''
1a. GC Content Classifier

Concept: Understanding GC Content
DNA consists of four nucleotide bases: Adenine (A), Thymine (T), Guanine (G), and Cytosine (C). The GC content of a sequence refers to the percentage of bases that are either G or C. A sequence can be considered "GC-rich" when it at least 60% of it's nucleotides are Guanine (G) or Cytosine (C). This metric has biological significance:

GC-rich regions are more thermally stable due to triple hydrogen bonding.
Different organisms and genomic regions exhibit varying GC content.
GC content is commonly used to: - Compare genome structures across species - Predict melting temperatures of DNA segments - Identify gene-dense regions in eukaryotic genomes

---

Example
Given the DNA sequence: ATGCGC - G/C bases: G, C, G, C → 4 out of 6 total bases - GC content = 4 / 6 ≈ 66.67% - Since this is 60% or greater, the sequence is classified as GC-rich

---

Your Task
Implement a function that takes a DNA string as input and returns either: - "GC-rich" if at least 60% of the sequence consists of G or C bases - "AT-rich" otherwise

You may assume the input string contains only valid DNA characters (A, T, G, C), and that the comparison should be case-insensitive.
'''


class Solution(unittest.TestCase):

    def test_case_gc_rich(self):
        """Test GC-rich solution"""
        self.assertEqual(classify_gc_content("GCGCGC"), 'GC-rich')
        self.assertEqual(classify_gc_content("GCGCGCAAT"), 'GC-rich')

    def test_case_at_rich(self):
        """Test AT-rich solution"""
        self.assertEqual(classify_gc_content("AATTAA"), 'AT-rich')
        self.assertEqual(classify_gc_content("ATGCAT"), 'AT-rich')

    def test_case_case_sensitivity(self):
        """Test case with mixture of uppercase and lowercase bases"""
        self.assertEqual(classify_gc_content("GCgcGCgC"), 'GC-rich')
        self.assertEqual(classify_gc_content("ATtagcgcgcGCgC"), 'GC-rich')
        self.assertEqual(classify_gc_content("ATtatataatGCgC"), 'AT-rich')


def classify_gc_content(dna: str) -> str:
    # ensure comparison is case-insensitive
    dna = dna.upper()
    # get GC count in DNA
    gc_count = dna.count('C') + dna.count('G')
    # return classification based on GC content
    return 'GC-rich' if (gc_count / len(dna)) >= 0.6 else 'AT-rich'
