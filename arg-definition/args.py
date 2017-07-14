"""
"""

def get_parser():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--config', '-c', help='location of configuration yaml file', default='default-config.yaml')
  return parser