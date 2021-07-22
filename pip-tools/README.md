# Instalar e utilizar pip-tools

### Criar ambiente virtual dentro do diretório do projeto
```python -m venv .venv```

### Instalar o pip-tools (Instalação Global)
``` pip install pip-tools```

### Criar os arquivos .in
criar arquivo de texto ```requirements.in``` e ```requirements-dev.in```

### No arquivo _requirements-dev.in_ adicionar como primeira linha:
```-r requirements.txt```

### Compilar os arquivos .in para .txt
```pip-compile --generate-hashes requirements.in -o requirements.txt```

```pip-compile --generate-hashes requirements-dev.in -o requirements-dev.txt```