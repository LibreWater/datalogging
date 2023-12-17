#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install fasd -y
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
find . -type f -name "requirements.txt" -exec python3 -m pip install -r {} \;
