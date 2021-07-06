# PraticasExerciciosAmigosDevPro

## Configurações inicias
```
git clone git@github.com:marcospsviana/PraticasExerciciosAmigosDevPro.git

python -m venv .venv

source .venv/bin/activate

pip install pip-tools


pip-compile requirements.in

pip-compile requirements-dev.in

git checkout -b nodedeumabranch

#Instale o pyenv  guia de instalação no Ubuntu

$ sudo apt update

$ sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

$ curl https://pyenv.run | bash

## Configurar o ambiente
# Copie e cole o conteúdo abaixo no final do arquivo .bashrc caso esteja usando zsh .zshrc

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

#bash
source .bashrc 

#zsh
source .zshrc

# Instale o python 3.9.5 com pyenv

pyenv install 3.9.5

#set o python 3.9.5 como global

pyenv global 3.9.5

```