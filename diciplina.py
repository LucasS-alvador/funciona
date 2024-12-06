from cor import cor

class Disciplina:
    def __init__(self, identificador: int, 
                 descricao: str, 
                 segmento: list, 
                 professor: list, 
                 status=1):
        self.__identificador = identificador
        self.__descricao = descricao
        
        if isinstance(segmento, list):
            self.__segmento = segmento  # EM ou Superior
        else:
            self.__segmento = [segmento]

        if isinstance(professor, list):
            self.__professor = professor
        else:
            self.__professor = [professor]

        self.__status = status

    # Getters
    def get_identificador(self):
        return self.__identificador

    def get_descricao(self):
        return self.__descricao

    def get_segmento(self):
        total = ""
        for i in self.__segmento:
            total += i + ", "
        return total

    def get_professor(self):
        total = ""
        for i in self.__professor:
            total += i + ", "
        return total
    
    def get_status(self):
        return self.__status

    # Setters
    def set_identificador(self, novo_identificador: int):
        if not self.__status:
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(novo_identificador, int) and novo_identificador > 0:
            self.__identificador = novo_identificador
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}O identificador deve ser um número inteiro positivo.{cor['final']}")

    def set_descricao(self, nova_descricao: str):
        if not self.__status:
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(nova_descricao, str) and nova_descricao.strip():
            self.__descricao = nova_descricao
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}A descrição deve ser uma string não vazia.{cor['vermelho']}")

    def set_segmento(self, novos_segmentos: list):
        if not self.__status:
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if all(i in ["EM", "Superior"] for i in novos_segmentos):
            self.__segmento = novos_segmentos
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}Segmentos inválidos. Devem ser 'EM' ou 'Superior'.{cor['vermelho']}")

    def set_professor(self, novo_professor: list):
        if not self.__status:
            raise Exception(f"{cor['vermelho']}Entidade desativada, valores não podem ser modificados{cor['final']}")
        if isinstance(novo_professor, list):
            self.__professor = novo_professor
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
        else:
            raise ValueError(f"{cor['vermelho']}Os professores devem ser fornecidos como uma lista.{cor['vermelho']}")
        
    def set_status(self, novo_status):
        if novo_status in [0,1]:
            self.__status = novo_status
            print(f"{cor['verde']}Editado com sucesso!{cor['final']}")
