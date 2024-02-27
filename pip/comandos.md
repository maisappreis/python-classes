
## Comandos no terminal:

> pip --version
> python -m pip --version

Ps.: o parâmetro -m permite rodar um módulo como script, ou seja o módulo terá o
__name__ como __main__. Este módulo será procurado na path de bibliotecas do Python.

> pip --help
> pip search <nome-pacote>
    (procura pacotes no PyPI, executa uma busca no https://pypi.org (Python Package Index))

> pip install <pacote>==<versao>

> pip3 list
    (lista pacotes instalados)

> pip3 freeze
    (cria o arquivo/manifesto 'requirements.txt' com a lista dos pacotes instalados)
    (ignora os pacotes 'pip' e 'setuptools', pois são os 2 pacotes padrão após criação do ambiente isolado)

> pip3 install -r requirements.txt
    (instala tudo que está dentro do arquivo/manifesto 'requirements.txt', -r igual a --requirement.)

> pip3 install --upgrade setuptools

> pip3 list --outdated
    (lista pacotes desatualizados)

> pip install --user --upgrade pip
    (atualiza o pip)

> python -m pip --version
    (caso o shell guardou no cache o caminho do pip anterior, e o pip --version não funcionou)

> pip install --user -r requirements.txt
    (usar --user em casos de falta de permissão, instala um pacote no home do usuário)


### Parâmetros do interpretador Python:
-m
    Rodar um módulo como script;
-c
    Rodar um script Python passado como string;