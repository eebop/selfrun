#!/usr/bin/env bash

echo_all() {
  echo "export PATH=\"\$PATH:`pwd`\""
  echo "alias selfrun=\"selfrun.py\""
}

if [ -e ~/.bash_profile ]; then
  echo_all >> ~/.bash_profile
elif [-e ~/.bashrc]; then
  echo_all >> ~/.bashrc
else
  echo "please add these lines to your system's equivilent of ~/.bashrc or ~/.bash_profile:"
  echo_all
fi
