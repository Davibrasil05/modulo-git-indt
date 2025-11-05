"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    return "Bem-Vindo ao Desafio de Git!"
    

def listar_comandos_git_basicos():
    return ["git init", "git add", "git commit", "git status", "git push"]

def criar_mensagem_commit(funcao_nome):
    return f"Implemente função {funcao_nome}"



def verificar_tag_valida(tag):

    if not tag.startswith("v"):
        return False

    numeros = tag[1:]

    partes = numeros.split(".")

    if len(partes) != 3:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False

    return True

    


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass
