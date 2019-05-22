# Fluxograma de Componentes Para o Conversor Grafema Fonema
* Ordem de execução do conversor

Componentes  |  Descrição
------------ | -----------
**Dicionário de exceções** | Lista contendo palavras que não seguem a regra uma das opções de palavras homônimas
**Identificador de Vogal Tônica **| Encontra a vogal tônica a partir da aplicação inversa das regras de acentuação do português
**Simplificador de Palavras (possibilidade)** | Reduz dígrafos e outras representações de grafemas para um único caracter especial, permitindo a utilização de uma conversão 1 x 01
**Probabilístico** | Encontra o fonema mais provável a partir do contexto de grafemas em que se encontra, classe gramatical, etc utilizando probabilidades obtidas de um dicionário grafema-fonema (forma de implementá-lo e fonte da probabilidade ainda incerta)
**Classificador Sintático** | Utilizaremos um classificador já implementado
**Dicionário Grafema-Fonema** | Poderá ser necessária a criação de um dicionário contendo palavras e suas conversões para fonemas no português brasileiro e seguindo a convenção fonética utilizada no projeto para o cálculo probabilístico
**Análisa na Frase **| Depois da conversão de cada palavra, será necessário verificar se, no contexto da frase completa, os fonemas terminais não se unem com os iniciais da palavra seguinte ou alteram sua pronuncia devido à elas

# Etapas
## Dicionário de exceções
### Descrição
O primeiro componente a ser implementado e estruturado será o * dicionário de exceções * 
Ele consiste de uma lista contendo todas as palavras que não seguem as regras fonéticas ou palavaras que apresentam escritas muito semelhantes (ou iguais) mas possuem pronuncias diferentes. Para a escolha das palavras que serão adicionadas ao dicionário, será feita uma análise de frequência desses gêneros de palavras de forma a descobrirmos quais palavras serão realmente usadas como guia para as regras fonéticas e quais serão apresentadas como exceções. Assim, no caso de palavras como "México" e "léxico", que possuem uma escrita muito semelhante mas pronuncias diferentes, uma delas será adicionada ao dicionário baseada em qual das pronúncias é menos frequente. Além disso, o dicionário será utilizado para armazenar palavras como "sede" e "sede", ambas substantivos com a mesma escrita e pronúncias diferentes. Nesse último caso, pode ser necessária uma análise do contexto da frase para podermos inferir com qual das duas palavras estamos trabalhando . No caso de uma palavra estar presente no dicionário, não será necessária a realização da conversão pois está já estará associada à palavra.
### Implementação
Para a implementação desse dicionário, será utilizada uma "hash table", pois como os dados são dificilmente mudados, podemos encontrar um hash perfeito para eles, sendo necessário um alto custo computacional apenas uma única vez (para criar a tabela), mas que nos permitirá a verificação de se uma palavra é exceção ou não em O(1), o que tornará o programa mais eficiente

## Identificador da Vogal Tônica
### Descrição
Para encontrarmos a vogal tônica no português brasileiro é muito simples e esse será um conhecimento muito útil para a conversão para fonemas que será feita depois. 
### Implementação
Primeiramente verificamos se há alguma palavra acentuada, e, caso houver, ela será a tônica. Se não houver vogal acentuada, seguimos para a análise da terminação da palavra, de forma a verificar se ela é oxítona, paroxítona ou proparoxítona aplicando as regras de acentuação invertidas (<https://pt.wikipedia.org/wiki/Acentua%C3%A7%C3%A3o_gr%C3%A1fica#Regras_b%C3%A1sicas_de_acentua%C3%A7%C3%A3o_em_portugu%C3%AAs>). Essa etapa poderia ser realizada utilizando uma árvore de decisões, na qual as decisões seriam baseadas nas regras gramaticais.

## Simplificador de Palavras
### Descrição
Possivelmente será utilizado um simplificador de palavras para reduzir dígrafos e facilitar a conversão de grafemas para fonemas. Ele seria responsável por substituir os dígrafos e outros conjuntos de grafemas que representam apenas 1 fonema por caracteres especiais, o que permitiria uma conversão de 1 x 01. Isso significa que poderia ser implementado um conversor que converseria cada grafema por 1 ou 0 fonemas, o que facilitaria o trabalho de implementação do conversor.
### Implementação
Sua implementação seria tão simples quanto verificar os casos em que dois ou mais grafemas representam apenas um fonema (que seriam listados previamente) e substituí-los por caracteres especiais pré-definidos.

## Probabilístico (Conversor)
### Descrição
Para a identificação do fonema representado pelo grafema será utilizada uma função probabilística que representará a probabilidade de um certo fonema ser o fonema que representa o grafema, sendo o fonema de maior probabilidade o escolhido como a conversão. Ele será baseado no dicionário que será feito e encontrará a probabilidade baseado no número de palavras contendo uma certa pronuncia do grafema em um determinado contexto na palavra. Essa será a etapa responsável pela conversão propriamente dita.
### Implementação
Ainda não foi decidido o modelo probabilístico que será adotado.

## Classificador Sintático
### Descrição
O conhecimento da classe sintática de uma palavra permite uma nova análise quanto aos fonemas presentes, principalmente quanto a vogais abertas e fechadas. Por exemplo, o conhecimento de que uma palavra é um verbo nos permite utilizar algumas de suas desinências para identificar a pronúncia de uma vogal, como é o caso de "corro" e "corres", do verbo correr. No caso da conjugação para a primeira pesoa do singular, temos o primeiro "o" fechado, enquanto que para o caso da segunda pessoa do singular esse "o" é aberto. Além disso, algumas palavras possuem diferentes pronuncias dependendo de sua classe, como é o caso de "logo", que possue o primeiro "o" aberto quando é um advérbio e fechado quando é um substantivo.
### Implementação
Esse classificador já foi implementado anteriormente e utilizaremos o classificador presente no link: <link>.

## Dicionário Grafema-Fonema
### Descrição
Para a parte probabilística será necessário um banco de dados do qual se obterá as probabilidades de ocorrência, e, para tanto, precisaremos criar um dicionário contendo palavras associadas às suas conversões para o português brasileiro e seguindo as convenções de representação de fonemas que serão utilizadas no projeto (apresentados em "Tabela IPA-ASC II GEFF 2018.pdf" e referentes à coluna ASCII).
### Implementação
A criação desse dicionário envolverá uma parte que pode ser automatizada e uma parte manual. Primeiramente precisaremos encontrar um banco de dados contendo as palavras com suas conversões e a seguir remover os estrangeirismos e exceções (manual) e converter a convenção utilizada para a convenção ASCII se necessário (automatizado).

## Análise da Frase
### Descrição
Após todas as palavras terem sido convertidas para seus respectivos fonemas, será necessário fazer uma segunda verificação de forma a verificar se, no momento em que as palavras são faladas na frase, não há alteração nos fonemas em seus extremos. Um exemplo disso seria a combinação "casa amarela", na qual as palavras independentemente possuiriam um fonema para "a" em seu final (para o caso de "casa") e em seu início (para o caso de "amarela"), mas que, no momento da fala, se unem em apenas um fonema, como se fosse "casamarela".
### Implementação
A implementação dessa etapa corresponderá à simples verificação de alguns casos específicos em que essa modificação ocorre.