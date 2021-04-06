#!usr/bin/env python3


class Banco: #classe
    def novo_cliente(self):  #Método para criar cliente
        nome = input("Nome: ")  # Inserção Nome do cliente
        cpf = input("CPF: ")  #Inserção Cpf do cliente
        conta = input("Tipo de conta:\n 1- Salário\n 2- Comum\n 3- Plus\n")  #Inserção tipo de conta á criar
        valor = float(input("---Utilize (.) para separações decimais---\nValor inicial da conta: "))  #Inserção valor inicial á adicionar na contar
        senha = input("Senha: \n")  #Inserção senha do cliente
        arquivo = open("%s.txt" % cpf, "w")  #Cria arquivo com a varíavel do cpf
        if conta == "1": #Caso conta seja salário
            lista_salario = [str(nome), str(cpf), "Salário", str(valor), str(senha)]
            for ele in lista_salario: # para cada elemento da lista, escreve no arquivo
                arquivo.write(ele+'\n')  #Registra no arquivo o tipo de conta "Salário"
        elif conta == "2": #Caso conta seja comum
            lista_comum = [str(nome), str(cpf), "Comum", str(valor), str(senha)]
            for ele in lista_comum: # para cada elemento da lista, escreve no arquivo
                arquivo.write(ele+'\n')  #Registra no arquivo o tipo de conta "Comum"
        elif conta == "3": #Caso conta seja plus
            lista_plus = [str(nome), str(cpf), "Plus", str(valor), str(senha)]
            for ele in lista_plus: # para cada elemento da lista, escreve no arquivo
                arquivo.write(ele+'\n')  #Registra no arquivo o tipo de conta "Plus"
        else: #Nenhuma das opções
            print("Comando inválido")  #Se a inserção do tipo de conta não for válida, o arquivo do cliente não será gerado
        arquivo.close()  #Fechamento de edição do arquivo

    def apaga_cliente(self):  #Função para apagar conta de cliente já cadastrado
        import os  #Importa biblioteca para leitura dos dados
        cpf = input("CPF do cliente á apagar: ")  #Inserção CPF do cliente á apagar
        if os.path.exists("%s.txt" % cpf):  #Condição de existência do arquivo do cliente
            while True:  #Loop
                pergunta = int(input("Deseja apagar cliente?\n1 - Sim\n2 - Não\n"))  #Confirmação da ação
                if pergunta == 1:  #Condição para resposta "1"
                    try: #Tenta
                        os.remove("%s.txt" % cpf)  #Remoção do arquivo com cpf do cliente
                        os.remove("%s_extrato.txt" % cpf) #Remove o extrato
                        print("Cliente apagado") #Printa o resultado
                        break  #Fim do loop após condição
                    except Exception: #Caso não exista algum dos arquivos
                        break    #Fim do loop
                elif pergunta == 1:  #Condição para resposta "2"
                    break  #Fim do loop
                else: #Caso nenhum comando seja valido
                    continue  #O loop se reinicia
        else:  #Caso não exista o arquivo do cliente
            print("O cliente não está cadastrado") #Printa que não existe cliente
    
    def debita(self): #Método para debitar
        resultado = 0 #Define a variável resultado
        cpf = input("CPF: ") #armazena o CPF
        import os #Módulo OS 
        if os.path.exists("%s.txt" % cpf): #Confirma se o arquivo do CPF existe
            arquivo = open("%s.txt" % cpf, "r") #Abre o arquivo 
            linhas_arquivo = arquivo.readlines() #lê as linhas do arquivo e armazena em uma variável
            arquivo.close()  #fecha o arquivo
            if linhas_arquivo[2] == "Salário\n": #Se a conta for salário procede
                while True:       #loop   
                    senha = input("Senha: ") #pergunta a senha
                    senha = senha + "\n" #senha + \n para verificar o arquivo
                    if senha == linhas_arquivo[4]: # se a senha for correta
                        valor = float(input("---Utilize (.) para separações decimais---\nValor: ")) # Solicita o valor a ser debitado
                        valor = round(valor,2) # arrendonda o valor para 2 casa decimais
                        taxa = round((valor*0.05), 2) # arrendonda o valor com taxas para 2 casa decimais
                        resultado = round(float(linhas_arquivo[-2]) - float(valor) - taxa, 2) #Armazena o resultado da subtração do saldo - valor a ser debitado
                        if resultado >= 0: # se o resultado for maior que 0
                            linhas_arquivo[-2] = str(round(resultado, 2)) + '\n' # Atualiza o saldo
                            arquivo = open("%s.txt" % cpf, "w") #Abre o arquivo
                            arquivo.writelines(linhas_arquivo) #Escreve o saldo
                            arquivo.close() # fecha o arquivo
                            print("\nDébito realizado\n") # Printa que o resultado
                            operador = "   -   " # define o operador (débito = negativo)
                            resultado_total = operador + str(valor) #define o resultado total com o operador
                            self.armazenar_extrato(cpf, resultado_total) # armazena no extrato
                            break #fim do loop
                        else: # Se não
                            print("\nLimite de débito excedido\n") #Printa que o resutaldo
                            break # fim do loop
                    else: # Se a senha for errada
                        print("Senha incorreta") #printa o resultado

            if linhas_arquivo[2] == "Comum\n": # se a conta for comum
                while True:       #loop   
                    senha = input("Senha: ") #pede a senha
                    senha = senha + "\n" #coloca \n na senha para verificar
                    if senha == linhas_arquivo[4]: #verifica a senha
                        valor = float(input("---Utilize (.) para separações decimais---\nValor: ")) #pergunta o valor a ser debitado
                        valor = round(valor,2) # arrendonda o valor para 2 casa decimais
                        taxa = round((valor*0.03), 2) # arrendonda o valor com taxas para 2 casa decimais
                        resultado = round(float(linhas_arquivo[-2]) - float(valor) - taxa, 2) # armazena o resultado
                        if resultado >= -500: #se o resultaod for maior que -500
                            linhas_arquivo[-2] = str(round(resultado,2 )) + "\n" #atualiza o saldo
                            arquivo = open("%s.txt" % cpf, "w") #abre o arquivo
                            arquivo.writelines(linhas_arquivo) #escreve o saldo
                            arquivo.close() #fecha o arquivo
                            print("\nDébito realizado\n") #printa o resultado
                            operador = "   -   " #armazena o operador
                            resultado_total = operador + str(valor) #armazena o operador + o valor
                            self.armazenar_extrato(cpf, resultado_total) #armazena tudo no extrato
                            break #fim do loop
                        else: #se não
                            print("\nLimite de débito excedido\n") #printa o resultado
                            break # fim do loop
                    else: # se não
                        print("Senha incorreta") #printa o resultado
                    
            if linhas_arquivo[2] == "Plus\n": #se a conta for Plus
                while True: #loop
                    senha = input("Senha: ") #pede a senha
                    senha = senha + "\n" #coloca \n na senha para confirmar
                    if senha == linhas_arquivo[-1]: #confirma a senha
                        valor = float(input('---Utilize (.) para separações decimais---\nValor: ')) #armazena o valor a ser debitado
                        valor = round(valor, 2) #arredonda o valor para 2 casas decimais
                        taxa = round((valor*0.01), 2) #arredonda o valor com taxas para 2 casas decimais
                        resultado = round(float(linhas_arquivo[-2]) - float(valor) - taxa, 2) # armazena o resultado
                        if resultado >= -5000: #se o resultado for maior que -500
                            linhas_arquivo[-2] = str(round(resultado, 2)) + "\n" #atualiza o saldo
                            arquivo = open("%s.txt" % cpf, "w") #abre o arquivo
                            arquivo.writelines(linhas_arquivo) #escreve o saldo
                            arquivo.close() #fecha o arquivo 
                            print("\nDébito realizado\n") #printa o resultado
                            operador = "   -   " #armazena o operador
                            resultado_total = operador + str(valor) #armazena o resultado
                            self.armazenar_extrato(cpf, resultado_total) #armazena no extrado com o operador
                            break #fim do loop
                        else: #se não
                            print("\nLimite de débito excedido\n") #printa o resultado
                            break #fim do loop
                    else: #se não
                        print("Senha incorreta") #printa o resultado
        else: #se não
            print("\nCPF incorreto\n")#printa o resultado
    

    def deposita(self): #método depositar
        resultado = 0 #declara a variavel resultado
        cpf = input("CPF: ") #armazena o cpf
        import os #importa módulo OS
        if os.path.exists("%s.txt" % cpf): #checa se o arquivo do cpf existe
            arquivo = open("%s.txt" % cpf) #se sim, abre o mesmo
            linhas_arquivo = arquivo.readlines() #lê as linhas
            arquivo.close() #fecha o arquivo

            while True: #loop
                valor = float(input("---Utilize (.) para separações decimais---\nValor: ")) #armazena o valor para depositar
                resultado = round(float(linhas_arquivo[-2])+ float(valor), 2) #armazena o resultado
                linhas_arquivo[-2] = str(round(resultado,2 )) + "\n" #atualiza o saldo
                arquivo = open("%s.txt" % cpf, "w") #abre o arquivo
                arquivo.writelines(linhas_arquivo) #escreve no arquivo
                arquivo.close() #fecha o arquivo
                print("\nDepósito realizado\n") #printa o resultado
                operador = "   +   " #armazena o operador +
                resultado = operador + str(valor) #armazena o resultado com o operador 
                self.armazenar_extrato(cpf, resultado) #armazena tudo no extrato
                break #fim do loop
        else: #se não
            print("\nCliente não está cadastrado\n") #printa o resultado


    def saldo(self): #método saldo
        cpf = input("CPF: ") #pede CPF
        import os #importa módulo OS
        if os.path.exists("%s.txt" % cpf): #checa se existe o arquivo
            senha = input("Senha: ") #pede senha
            arquivo = open("%s.txt" % cpf, "r") #abre o arquivo
            linhas_arquivo = arquivo.readlines() #le as linhas
            arquivo.close() #fecha o arquivo
            if senha + "\n" == linhas_arquivo[-1]: #se a senha estiver correta
                print("\n Saldo:R$ %s \n" % linhas_arquivo[-2]) #printa o saldo
            else: # se não
                print("Senha incorreta") #printa o resultado
        else: # se não
            print("O cliente não está cadastrado") #printa o resultado



    def extrato(self): #método extrato
        import os #importa modulo OS
        cpf = input("CPF: ") #pede o CPF
        if os.path.exists("%s.txt" % cpf): #checa se existe o arquivo
            senha = input("Senha: ") #pede a senha
            arquivo = open("%s.txt" % cpf) #abre o arquivo
            linhas_arquivo = arquivo.readlines() #le as linhas
            arquivo.close() #fecha o arquivo
            if senha + "\n" == linhas_arquivo[-1]: # se a senha estiver correta
                nome = linhas_arquivo[0] #armazena o nome 
                nome = nome.replace("\n", "") #arruma o nome para printar
                conta = linhas_arquivo[2] #armazena o tipo de conta
                conta = conta.replace("\n", "") #arruma a conta para printar
                arquivo_extrato = open("%s_extrato.txt" % cpf) #abre o arquivo de extrato
                print("\n\n---------------Extrato---------------") #printa extrato
                print("Nome: " + nome) #printa o nome
                print("\nCPF: " + cpf) #printa o cpf
                print("\nConta: " + conta) #printa o tipo de conta
                arquivo_extrato = arquivo_extrato.readlines() #lê o extrato
                for line in arquivo_extrato: #para cada linha do extrato
                    print(line) #printa linha
                arquivo.close() #fecha arquivo
                print("\n-------------------------------------\n\n") #print para separar
            else: # se não
                print("\n\nSenha incorreta\n\n")#printa o resultado
        else: # se não 
            print("\n\nCliente não está cadastrado\n\n")#printa o resultado




    def armazenar_extrato(self, cpf, valor): #método de armazenar no extrato
        import os #importa OS
        from time import gmtime, strftime, sleep #importa TIME
        data = strftime("%d-%m-%Y %H:%M:%S") #pega a data e horario atual
        data = str(data) #armazena em uma variável
        arquivo = open("%s.txt" % cpf) #abre o arquivo do cpf
        linhas_arquivo = arquivo.readlines() #le as linhas
        arquivo.close() #fecha o arquivo
        valor = str(valor) #trasforma o valor em uma string
        saldo = linhas_arquivo[3] #armazena atual da conta
        saldo = str(saldo) #transforma em uma string
        saldo = saldo.replace('\n', '') #arruma para armazenar
        if linhas_arquivo[2] == "Comum\n": # se o a conta for do tipo comum
            comum_taxa = "0.03"# taxa de acordo com a conta
            arquivo_extrato = open("%s_extrato.txt" % cpf, "a")# abre o arquivo de extrato
            arquivo_extrato.write("\nData:  " + data + valor + "     Saldo:  " + saldo + "     Taxa:  " + comum_taxa)#armazena a data atual, valor, saldo e a taxa do banco.
            arquivo_extrato.close()#fecha o arquivo
        elif linhas_arquivo[2] == "Plus\n":# se a conta for do tipo plus
            plus_taxa = "0.01"# taxa de acordo com a conta
            arquivo_extrato = open("%s_extrato.txt" % cpf, "a")# abre o arquivo de extrato
            arquivo_extrato.write("\nData:  " + data + valor + "     Saldo:  " + saldo + "     Taxa:  " + plus_taxa)#armazena a data atual, valor, saldo e a taxa do banco.
            arquivo_extrato.close()#fecha o arquivo            
        elif linhas_arquivo[2] == "Salário\n":# se a conta for do tipo salário
            salario_taxa = "0.05"# taxa de acordo com a conta
            arquivo_extrato = open("%s_extrato.txt" % cpf, "a")# abre o arquivo de extrato
            arquivo_extrato.write("\nData:  " + data + valor + "     Saldo:  " + saldo + "     Taxa:  " + salario_taxa)#armazena a data atual, valor, saldo e a taxa do banco.
            arquivo_extrato.close()#fecha o arquivo


    def start(self):#método start
        while True:#loop
            menu = input(("1- Novo cliente\n2- Apaga cliente\n3- Debita\n4- Deposita\n5- Saldo\n6- Extrato\n\n\n0- Sai\n"))#pede as opções
            if menu == "1":# se o número escolhi for esse>
                self.novo_cliente()# executa a função desejada
            elif menu =="2":# se o número escolhi for esse>
                self.apaga_cliente()# executa a função desejada
            elif menu == "3":# se o número escolhi for esse>
                self.debita()# executa a função desejada
            elif menu == "4":# se o número escolhi for esse>
                self.deposita()# executa a função desejada
            elif menu == "5":# se o número escolhi for esse>
                self.saldo()# executa a função desejada
            elif menu == "6":# se o número escolhi for esse>
                self.extrato()# executa a função desejada
            elif menu == "0":# se o número escolhi for esse>
                break#fim do loop
            else:#se não
                continue#reinicia o loop




my_bank = Banco()#abre a classe em uma variável
my_bank.start()#inicia o método start
