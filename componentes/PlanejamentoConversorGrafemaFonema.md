# Fluxograma de Componentes Para o Conversor Grafema Fonema
* Ordem de execução do conversor

Componentes  |  Descrição
------------ | -----------
Dicionário de exceções | Lista contendo palavras que não seguem a regra uma das opções de palavras homônimas
Vogal Tônica | Encontra a vogal tônica a partir da aplicação inversa das regras de acentuação do português
Simplificador de Palavras (possibilidade) | Reduz dígrafos e outras representações de grafemas para um único caracter especial, permitindo a utilização de uma conversão 1 x 01
Probilístico | Encontra o fonema mais provável a partir do contexto de grafemas em que se encontra, classe gramatical, etc utilizando probabilidades obtidas de um dicionário grafema-fonema (forma de implementá-lo e fonte da probabilidade ainda incerta)
Classificador Sintático | Utilizaremos um classificador já implementado
Dicionário Grafema-Fonema | Poderá ser necessária a criação de um dicionário contendo palavras e suas conversões para fonemas no português brasileiro e seguindo a convenção fonética utilizada no projeto para o cálculo probabilístico
Análisa na Frase | Depois da conversão de cada palavra, será necessário verificar se, no contexto da frase completa, os fonemas terminais não se unem com os iniciais da palavra seguinte ou alteram sua pronuncia devido à elas

# Etapas
## Dicionário de exceções
~~~
O primeiro componente a ser implementado e estruturado será o * dicionário de exceções * 
Ele consiste de uma lista contendo todas as palavras que não seguem as regras fonéticas ou palavaras que apresentam escritas muito semelhantes (ou iguais) mas possuem pronuncias diferentes. Para a escolha das palavras que serão adicionadas ao dicionário, será feita uma análise de frequência desses gêneros de palavras de forma a descobrirmos quais palavras serão realmente usadas como guia para as regras fonéticas e quais serão apresentadas como exceções. Assim, no caso de palavras como "México" e "léxico", que possuem uma escrita muito semelhante mas pronuncias diferentes, uma delas será adicionada ao dicionário baseada em qual das pronúncias é menos frequente. Além disso, o dicionário será utilizado para armazenar palavras como "sede" e "sede", ambas substantivos com a mesma escrita e pronúncias diferentes. Nesse último caso, pode ser necessária uma análise do contexto da frase para podermos inferir com qual das duas palavras estamos trabalhando.
Para a implementação desse dicionário, será utilizada uma "hash table", pois como os dados são dificilmente mudados, podemos encontrar um hash perfeito para eles, sendo necessário um alto custo computacional apenas uma única vez (para criar a tabela), mas que nos permitirá a verificação de se uma palavra é exceção ou não em O(1), o que tornará o programa mais eficiente
~~~

## Vogal Tônica
~~~
Para encontrarmos a vogal tônica no português brasileiro é muito simples e esse será um conhecimento muito útil para a conversão para fonemas que será feita depois. 
Primeiramente verificamos se há alguma palavra acentuada, e, caso houver, ela será a tônica. Se não houver vogal acentuada, seguimos para a análise da terminação da palavra, de forma a verificar se ela é oxítona, paroxítona ou proparoxítona aplicando as regras de acentuação invertidas
~~~

## Simplificador de Palavras
~~~
Possivelmente será utilizado um simplificador de palavras 
