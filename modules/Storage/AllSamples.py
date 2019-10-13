#!/usr/bin/env python

from . import Sample
from . import Chr


class AllSamples:
    """
    This Class will contain all information about samples in VCF files
    Beside that It will contain info about chromosomes
    """
    def __init__(self):
        self.sample_list = {}
        self.chr_list = {}

    def add_new_sample(self, sample_name):
        if sample_name in self.sample_list.keys():
            pass
        else:
            sample = Sample.Sample()
            self.sample_list[sample_name] = sample

<<<<<<< HEAD
    def add_new_chr(self, chr_name, position, variant, gap=1):
=======
    def add_new_chr(self, chr_name, position, variant, gap=10000):
>>>>>>> 95d134afb3e6dd4c60cfa6247285c5e19e5dc903
        if chr_name in self.chr_list.keys():
            self.chr_list[chr_name].update_position(position, gap)
            self.chr_list[chr_name].add_variant(variant)
        else:
            chr_obj = Chr.Chr(chr_name, position)
            self.chr_list[chr_name] = chr_obj
            self.chr_list[chr_name].add_variant(variant)
