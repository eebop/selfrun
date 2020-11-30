#!/usr/bin/env bash

if [ -e ~/.bash_profile ]; then
  echo "export PATH=\"\$PATH:`pwd`\"" >> ~/.bash_profile
else
  echo "export PATH=\"\$PATH:`pwd`\"" >> ~/.bashrc
fi
