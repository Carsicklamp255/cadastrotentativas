import csv
import os

file_name = 'cadastro.csv'

file_exist = os.path.exists('cadastro.csv')

file_exist = os.path.exists(file_name)
if not file_exist:
  with open(file_name, mode= 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['nome_completo', 'idade', 'CPF',
    'endereco','telefone', 'email','produto'])
    writer.writeheader()
    print(f'o arquivo {file_name} foi criado')

resposta = input("Você se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")
while not resposta == 'sair':
  def cadastro():  
      nome_completo = input('digite seu nome completo: ').strip().title()
      while not nome_completo.replace(" ", "").isalpha():
        print("digite apenas letras por favor")
        nome_completo = input("digite seu nome completo: ").strip().title()
      idade = input('digite sua idade: ')
      while not idade.isdigit():
        print("a idade deve ser infomado apenas com digitos!")
        idade = input('digite sua idade: ')
      CPF = input('digite seu CPF: ')
      while not CPF.isdigit():
        print('Digite apenas os digitos do CPF devem ser informados: ')
        CPF = input('digite seu CPF: ')
      endereco = input('digite seu endereço: ')
      telefone = input('digite seu número de telefone: ')
      while not telefone.isdigit():
        print("digite apenas o número de seu telefone para contato")
        telefone = input('digite seu número corretamete: ')
      email = input('digite seu email: ').strip()
      produto = input("digite o produto a ser entregue: ").strip()
      with open('cadastro.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome_completo, idade, CPF, endereco, telefone, email, produto])

        print('cadastro realizado com sucesso')

  def listar_cadastro():
      with open('cadastro.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Ler o cabeçalho
        for row in reader:
            for i in range(len(header)):
                print(f"{header[i]}: {row[i]}")
            print("-" * 40)
            break
          
  def consulta_cadastro():
      nome_completo = input('Digite o nome do cadastrado que deseja consultar: ').strip().title()
      with open('cadastro.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
          if row[0].strip().title() == nome_completo:
            print(row)
            break
        else:
          print('Cadastro não encontrado')

  def excluir_cadastro():
    nome_completo = input('Digite o nome do cadastro que deseja excluir: ').strip().title()
    with open('cadastro.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
          if row[0] == nome_completo.strip().title():
            rows.remove(row)
            break

        else:
          print('Cadastro não encontrado')

    with open('cadastro.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

        print('Cadastro excluido com sucesso')

  def saida_sistema():
    print("Saindo do sistema...")

  if resposta.lower() == 'cadastrar':
    cadastro()
    input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")
  if resposta.lower() == 'consultar':
    consulta_cadastro()
    input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")
  if resposta.lower() == 'excluir':
    excluir_cadastro()
    input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir, sair do sistema ou ver a lista toda? ")
  if resposta.lower() == 'sair':
    saida_sistema()
  if resposta.lower() == 'ver':
    listar_cadastro()
  elif resposta.lower:
    print('digite apenas as palavrar cadastrar, consultar, excluir, sair e ver!')
    input("Você deseja se cadastrar um usuario, consultar um cadastro, excluir ou sair do sistema? ")

              #def listar_cadastro():
               #   with open('cadastro.csv', 'r') as file:
                #      reader = csv.reader(file)
                 #     header = next(reader, None)  
                  #    
                   #   if header: 
                    #      for row in reader:
                     #         if any(row): 
                      #            for i in range(len(header)):
                       #               print(f"{header[i]}: {row[i]}")
                        #          print("-" * 40)
                      #else:
                       #kk   print("O arquivo CSV está vazio ou sem cabeçalho.")
