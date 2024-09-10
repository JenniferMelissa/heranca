#herança
#quando a classe decide ter filhos
#quando voce classes diferentes mas que possuem atributos e metodos em comum(pode ser todos, ou apenas alguns)
#desenvolve uma classe que chamamos de super classe, a super classe ela provavelmente nao é instanciada no programa principal, serve para reuinir metodos e atributos comuns de duas classes ou mais e a partir dela voce desenvolve as outras duas classes(ficando com 3 classes), a super classe e mais 2 classes
#e com as outras 2 classes, elas tem os atributos e metodos da super classe e a da sua classe que voce esta desenolvendo com seus atributos e metodos individuais, assim, economizando codigo
#subclasse pode ser super classe, e assim ela passa a ser super classe também

#super classe (classe-pai)
class Pessoa:
    #atributos
    cidade   = 'Brasília'
    telefone = '(61) 98884-5647'
    email    = 'nome@gmail.com'

#subclasse (classe-filho) Coloca parenteses na classe filho pois é assim que define heranca, Pessoa Fisica herda Pessoa
class PessoaFisica(Pessoa):
    #atributos
    nome   = 'Fulado de Tal'
    cpf    = '123.456.789.12'
    peso   = 90
    altura = 1.80

#subclasse 
class PessoaJuridica(Pessoa):
    nome_fantasia = 'Cobra Kai'
    razao_social  = 'Fulano de Tal'
    cnpj          = '62.245.916/0001-69'

#programa principal 
if __name__ == '__main__':
    #instancia dos objetos
    usuario = PessoaFisica()
    empresa = PessoaJuridica()

    print(f'{'-'*30} DADOS DO USUÁRIO {'-'*30}\n')
    print(f'Nome do usuário: {usuario.nome}.')
    print(f'CPF do usuário: {usuario.cpf}.')
    print(f'Peso do usuário: {usuario.peso}.')
    print(f'Altura do usuário: {usuario.altura}.')
    print(f'Cidade onde usuário mora: {usuario.cidade}.')
    print(f'Telefone do usuário: {usuario.telefone}.')
    print(f'E-mail do usuário: {usuario.email}.')

    print('\n')

    print(f'{'-'*30} DADOS DA EMPRESA JURÍDICA {'-'*30}\n')
    print(f'Nome da empresa: {empresa.nome_fantasia}.')
    print(f'CNPJ da empresa: {empresa.cnpj}.')
    print(f'Razão-Social da empresa: {empresa.razao_social}.')
    print(f'Cidade da empresa: {empresa.cidade}.')
    print(f'Telefone da empresa: {empresa.telefone}.')
    print(f'E-mail da empresa: {empresa.email}.')