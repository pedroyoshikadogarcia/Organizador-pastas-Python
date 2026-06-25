import os
import shutil

# Configuração constante
CAMINHO_PASTA = r"D:\Projetos\Organizador\Teste"

MAPA_EXTENSOES = {
    '.txt': 'Documentos',
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.png': 'Imagens',
    '.zip': 'Compactados',
    '.rar': 'Compactados',
}


def obter_pasta_destino(extensao):
    """Retorna o nome da pasta com base na extensão do arquivo."""
    return MAPA_EXTENSOES.get(extensao.lower(), 'Outros')


def organizar_diretorio(caminho):
    """Função principal que varre e organiza a pasta."""
    if not os.path.exists(caminho):
        print(f"Erro: O caminho '{caminho}' não existe.")
        return

    arquivos = os.listdir(caminho)
    print(f"Iniciando a varredura em: {caminho}\n")

    contador_movidos = 0

    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho, arquivo)

        # Ignora se for pasta
        if os.path.isdir(caminho_completo):
            continue

        # Pega a extensão
        _, extensao = os.path.splitext(arquivo)

        nome_pasta_destino = obter_pasta_destino(extensao)
        caminho_pasta_destino = os.path.join(caminho, nome_pasta_destino)

        # Cria a pasta se não existir
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            print(f"Pasta criada: [{nome_pasta_destino}]")

        # Move o arquivo
        novo_caminho_arquivo = os.path.join(caminho_pasta_destino, arquivo)
        shutil.move(caminho_completo, novo_caminho_arquivo)
        print(f"  ↳ Movido: {arquivo} -> {nome_pasta_destino}/")

        contador_movidos += 1

    print(f"\nPronto! {contador_movidos} arquivo(s) foram organizados com sucesso.")


# Só roda se o arquivo for executado direto
if __name__ == "__main__":
    organizar_diretorio(CAMINHO_PASTA)