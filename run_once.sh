#!/usr/bin/env bash

if [ -e ~/.bash_profile ]; then
  echo "export PATH=\"\$PATH:`pwd`\"" >> ~/.bash_profile
  echo "alias selfrun=\"selfrun.py\""
elif [-e ~/.bashrc]; then
  echo "export PATH=\"\$PATH:`pwd`\"" >> ~/.bashrc
  echo "alias selfrun=\"selfrun.py\""
else
  echo "please add these lines to your system's equivilent of ~/.bashrc or ~/.bash_profile:"
  echo "export PATH=\"\$PATH:`pwd`\""\
  echo "alias selfrun=\"selfrun.py\""
fi
