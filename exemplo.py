class ContextoSimples:

    def __enter__(self):
        print("Iniciar Conexão...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando Conexão com Segurança!")


with ContextoSimples() as cs:
    print("Execuções em banco de dados!")
