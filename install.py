#!/usr/bin/env python

import os
import subprocess
import sys
import os.path as p
import glob

def Main():
  script_dir = p.dirname( p.realpath( __file__ ) )
  build_file = p.join( script_dir, 'third_party', 'ycmd', 'build.py' )

  if not p.isfile(build_file):
    sys.exit( 'File ' + build_file + ' does not exist; you probably forgot '
              'to run:\n\tgit submodule update --init --recursive\n\n' )

  python_binary = sys.executable
  args = ' '.join( sys.argv[1:] )
  subprocess.call( ' '.join( [ python_binary, build_file, args ] ) )

  # Remove old YCM libs if present so that YCM can start.
  old_libs = glob.glob( p.join(script_dir, 'python', '*ycm_core.*') 
    ) + glob.glob( p.join(script_dir, 'python', '*ycm_client_support.*') 
    ) + glob.glob( p.join(script_dir, 'python', '*clang*.*') )
  for lib in old_libs:
    os.remove(lib)

if __name__ == "__main__":
  Main()
