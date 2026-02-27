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
É um padrão criacional que permite a produção de famílias de objetos relacionados sem ter que especificar suas classes concretas.
1. ***Quais problemas esse padrão resolve?***
2. ***Como o padrão resolve esses problemas?***
