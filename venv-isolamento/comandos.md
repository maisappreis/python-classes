
## Comandos para usar o Ambiente Vitual

1. Criação do ambiente virtual:
> python -m venv .venv
    1. O '.venv' seria o nome da pasta que ele irá criar
    2. Cria uma estrutura para manter o site-packages, totalmente isolado do seu sistema


Mostrar 'sys.path':
> python -m site


2. Habilitar o ambiente virtual:
> Windows:
    cmd.exe C:\> <venv>\Scripts\activate.bat
    PowerShell PS C:\> <venv>\Scripts\Activate.ps1
> Posix:
    bash/zsh $ source <venv>/bin/activate
    fish $ . <venv>/bin/activate.fish
    csh/tcsh $ source <venv>/bin/activate.csh


3. Desabilitar:
> deactivate


Variável de ambiente:
> echo $VIRTUAL_ENV


Onde ele procura os pacotes, endereços:
> python -c 'import sys; print("\n".join(sys.path))'


