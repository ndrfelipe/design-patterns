# Requistos, Projeto de Software e Validação
Disciplina do curso de ADS da Cesar School.
## Padrões criacionais
Fornecem vários mecanismos de criação de objetos, os quais aumentam a flexibilidade e reutilização de código já existente.
### Factory method
Trata-se de um projeto criacional que resolve o problema de criar objetos de produtos sem especificar suas classes concretas.
1. ***Quais problemas esse padrão resolve?***
    1. Resolve a dependência de classes concretas (operador New sendo chamado diversas vezes no código).
    2. Resolve a dificuldade de manutenção.
    3. Resolve código ‘engessado’.

2. ***Como o padrão resolve esses problemas?***
    1. Fazendo o código depender de Interfaces/Abstrações.
    2. Centralizando a criação de objetos em um único ponto.
    3. Permitindo adicionar novas funcionalidades sem alterar o código antigo.

### Abstract factory
É um padrão criacional que permite a produção de famílias de objetos relacionados sem a necessidade de especificar suas classes concretas.
1. ***Quais problemas esse padrão resolve?***
    1. Ele resolve o problema da criação de famílias de objetos que possuem múltiplas variantes, garantindo que elas não se misturem de forma inconsistente. Por exemplo, considere três conceitos de móveis: Cadeira, Mesa e Poltrona. Eles podem ter variantes de estilo, tais como: Cadeira Moderna, Mesa Moderna e Poltrona Moderna; ou Cadeira Clássica, Mesa Clássica e Poltrona Clássica. Logo, depreende-se que esses itens constituem uma "família" de objetos com diversas variantes.
2. ***Como o padrão resolve esses problemas?***
    1. O Abstract Factory resolve esse problema criando uma camada extra de abstração: as Abstract Factories (Fábricas Abstratas), as quais declaram métodos responsáveis por criar todos os objetos abstratos da família.
    Seguindo o exemplo anterior, seria implementada uma interface MoveisFactory que teria os métodos de criação para os três objetos: criarCadeira(), criarPoltrona() e criarMesa(). A partir daí, são criadas as fábricas concretas para cada variante de estilo, como MoveisModernosFactory e MoveisClassicosFactory, onde os objetos concretos seriam instanciados.
    Dessa forma, esse padrão garante que todos os objetos e suas variantes sejam compatíveis entre si, respeitando os princípios de Responsabilidade Única (SRP) e do Aberto/Fechado (OCP).

### Builder
É um padrão criacional que permite a você construir objetos complexos passo a passo. O padrão permite que você produza diferentes tipos e representações de um objeto usando o mesmo código de construção.


1. ***Quais problemas esse padrão resolve?***
    1. Quando existem classes com construtores muito grandes, que exigem a passagem de muitos parâmetros para preencher os atributos. Frequentemente, alguns desses atributos não são utilizados em determinadas instâncias, gerando chamadas confusas e cheias de valores nulos. Isso resulta em um código parecido com este: <br>
        - *new ExemploClasse(123, 'ok', null, null, null)* <br>
        - *new ExemploDoisClasse(321, 'false', true, true, null)*
2. ***Como o padrão resolve esses problemas?*** <br>
    1. Por meio de classes Builders (Construtoras) que assumem a responsabilidade pela criação dos objetos passo a passo. O padrão sugere extrair o código de construção do objeto de sua própria classe e movê-lo para objetos builder separados. Dessa forma, você chama apenas as etapas de construção de que precisa, os construtores não ficam poluídos e o código cliente se torna muito mais limpo, legível e organizado.   

### Prototype
É um padrão criacional que permite copiar objetos existentes sem que o seu código fique dependente de suas classes concretas.

1. ***Quais problemas esse padrão resolve?***
    1. Ele resolve as falhas da abordagem direta de clonagem. Ao tentar copiar um objeto de fora dele, você pode esbarrar em atributos privados que não são visíveis externamente. Além disso, essa abordagem força o seu código a ficar acoplado à classe daquele objeto.
    2. Apresenta uma excelente alternativa à criação de múltiplas subclasses que servem apenas para inicializar objetos com configurações diferentes.
2. ***Como o padrão resolve esses problemas?***
    1. O padrão delega o processo de clonagem para o próprio objeto a ser clonado. Ele declara uma interface comum (geralmente com um método clonar() ou clone()) para todos os objetos que suportam a clonagem.
    2. Esse método cria um novo objeto da classe atual e copia todos os valores dos atributos do objeto antigo para o novo. Assim, quando você precisar de um objeto parecido com um já existente, basta cloná-lo e alterar apenas o que for necessário, em vez de instanciar e configurar um novo do zero.

### Singleton
É um padrão criacional que permite garantir que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para ela.
1. ***Quais problemas esse padrão resolve?***
    1. Ele evita a criação de múltiplas instâncias para objetos que gerenciam recursos compartilhados, como uma conexão com um banco de dados ou um arquivo de log. Isso previne o desperdício de memória e o comportamento inconsistente que poderiam ocorrer se várias partes do código tentassem instanciar e acessar esses recursos simultaneamente.
2. ***Como o padrão resolve esses problemas?***
    1. O padrão Singleton implementa uma classe com o construtor privado, de modo que sua chamada interna controle a criação do objeto, garantindo que o cliente trabalhe sempre com a mesma instância. Isso é realizado através da criação de um método de criação estático que chama o construtor privado para instanciar o objeto (apenas na primeira vez) e o salva em um campo estático. Todas as chamadas subsequentes para esse método simplesmente retornam o objeto que já está em cache.

### Como rodar
1. Para rodar o exemplo de Abstract Factory apenas entre na pasta com cd abstract-factory e rode no terminal 'python main.py'
2. Para rodar o exemplo de Builder apenas entre na pasta com 'cd builder' e rode no terminal 'python main.py'