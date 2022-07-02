# -*- coding: utf-8 -*-
"""
# Author      : Camey
# DateTime    : 2022/6/28 5:48 下午
# Description : 
"""
import sys
sys.path.append("./PARIETAL")
from brain_extraction import BrainExtraction

b = BrainExtraction()
input_scan = './images/monkey.nii'
output_scan = './result/monkey_brain_s2.nii'

# The result is stored both in disk at output_scan path and returned
# as np.array
brainmask = b.run(input_scan, output_scan)