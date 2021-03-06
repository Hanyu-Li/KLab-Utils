from __future__ import print_function, division
import os
import glob
import numpy as np
import argparse
import shutil
import sys
import cv2
import re
from tqdm import tqdm

class EM_preprocessor(object):
  def __init__(self, input_dir, output):
    self.input_dir = input_dir
    # self.output_dir = output_dir
    # if self.output_dir == None:
    #     try:
    #         os.makedirs(os.path.join(self.input_dir, 'output'))
    #     except:
    #         pass
    #     self.output_dir = os.path.join(self.input_dir, 'output')
    self.output = output
    output_dir = os.path.dirname(self.output)
    os.makedirs(output_dir, exist_ok=True)
    self.flist = None

    self.MAX_ROW = 0
    self.MAX_COL = 0
    self.TILE_ROW = 0
    self.TILE_COL = 0
    self.TILE_MIN = 0
    self.TILE_MAX = 0
    self.DTYPE = 0

  def test_one_image(self):
    f_dummy = glob.glob(os.path.join(self.input_dir, '**/Tile_*.tif'), recursive=True)[0]
    dummy_data = cv2.imread(f_dummy, flags=cv2.IMREAD_GRAYSCALE)
    print(dummy_data.shape)
    self.TILE_ROW, self.TILE_COL = dummy_data.shape
    self.TILE_MIN, self.TILE_MAX = np.min(dummy_data[:]), np.max(dummy_data[:])
    print(self.TILE_ROW, self.TILE_COL, self.TILE_MIN,
          self.TILE_MAX, dummy_data.dtype)
    if dummy_data.dtype == np.uint8:
      print('8bit')
      self.DTYPE = 0
    elif dummy_data.dtype == np.uint16:
      print('16bit')
      self.DTYPE = 1

  def prepare_align_txt(self):
    with open(self.output, 'w') as f_out:
      for f in self.flist:
        res = re.search(r'Tile_r([0-9])-c([0-9])_S_([0-9]+)_*', f)
        tile_name = os.path.abspath(f)
        r = res.group(1)
        c = res.group(2)
        z = int(res.group(3))

        command = '{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7} \t {8} \n'.format(
            tile_name, c, r, z, self.TILE_COL, self.TILE_ROW, self.TILE_MIN, self.TILE_MAX, self.DTYPE)
        f_out.write(command)

  def run(self):
    print("Input:", self.input_dir)
    print("Output:", self.output)

    self.flist = glob.glob(os.path.join(self.input_dir, '**/Tile_*.tif*'), recursive=True)
    def get_index(f): return re.search(
        r'S_([0-9]+)_', os.path.basename(f)).group(1)

    self.flist.sort(key=get_index)

    self.test_one_image()
    self.prepare_align_txt()


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', type=str, help='Directory of a section_set/site')
  parser.add_argument('output', type=str,
                      default='./align.txt', help='Output .txt file')
  args = parser.parse_args()
  emp = EM_preprocessor(args.input, args.output)
  emp.run()


if __name__ == '__main__':
  main()
