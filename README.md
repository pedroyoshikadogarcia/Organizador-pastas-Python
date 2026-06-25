#  Organizador de Pastas Automatizado

Uma ferramenta em linha de comando (CLI) desenvolvida em Python para automatizar a organização de arquivos em diretórios específicos com base em suas extensões. Ideal para limpar pastas de "Downloads" ou "Área de Trabalho" bagunçadas de forma rápida e segura.

---

##  Funcionalidades

* **Organização Dinâmica:** Identifica a extensão do arquivo e o move para a pasta correspondente (ex: `.pdf` vai para `Documentos`, `.png` vai para `Imagens`).
* **Criação Automática de Diretórios:** Se a pasta de destino não existir, o script a cria em tempo real.
* **Categoria "Outros":** Arquivos com extensões não mapeadas são movidos para uma pasta genérica, garantindo que nada fique solto.
* **Segurança:** O script ignora subpastas já existentes, evitando loops ou movimentações indevidas.

##  Tecnologias Utilizadas

* **Python 3.x**
* **Biblioteca `os`** (Manipulação de caminhos e sistema de arquivos)
* **Biblioteca `shutil`** (Movimentação de arquivos de alta escala)

##  Como Executar o Projeto

### Pré-requisitos
* Ter o Python instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/organizador-pastas-python.git](https://github.com/seu-usuario/organizador-pastas-python.git)
   cd organizador-pastas-python
    ```
2. **Configuração do caminho:**
Abra o arquivo organizador.py e altere a variável CAMINHO_PASTA com o caminho absoluto do diretório que você deseja organizar:
   ```bash
   CAMINHO_PASTA = r"C:\Seu\Caminho\Aqui"
   ```

3. **Execute o arquivo**
   ```bash
   python organizador.py
   ```

## Estrutura do Código
O projeto foi estruturado seguindo boas práticas de desenvolvimento em Python, utilizando funções (def) para modularização e o bloco if __name__ == "__main__": para controle de escopo de execução.

Desenvolvido por Pedro Yoshikado Garcia 
