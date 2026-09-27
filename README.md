# Trabalho 1 — Diagnóstico de Processos em Linux

## Aluno

Jorgielson Casmpos Santos

## Disciplina

Sistemas Operacionais — Análise e Desenvolvimento de Sistemas

## 1. Descrição da aplicação

Para o experimento foi utilizado um programa simples desenvolvido em Python.

O programa foi criado com duas threads adicionais, além da thread principal. Cada thread executa pequenos cálculos e utiliza intervalos com `time.sleep(1)`, permitindo que o processo permaneça ativo por tempo suficiente para ser analisado pelo sistema operacional.

A aplicação foi escolhida por ser simples, segura para testes e fácil de controlar durante o experimento.

## 2. Ambiente utilizado

O experimento foi realizado no seguinte ambiente:

- Sistema operacional: Ubuntu 26.04.1 LTS
- Ambiente: WSL
- Linguagem utilizada: Python 3
- Shell utilizado: Bash

A aplicação foi executada com o comando:

```bash
python3 aplicacao/processos.py
```

## 3. PID e PPID

Durante a execução, o processo Python recebeu o PID:

```text
1163
```

O PPID identificado foi:

```text
103
```

O processo de PID 103 correspondia ao Bash.

Isso mostra que o Bash foi o processo pai do programa Python, pois foi a partir do terminal Bash que o programa foi iniciado.

A relação observada foi:

```text
bash (PID 103)
└── python3 (PID 1163)
```

## 4. Árvore de processos

O comando:

```bash
pstree -p 103
```

apresentou a seguinte estrutura:

```text
bash(103)───python3(1163)─┬─{python3}(1164)
                          └─{python3}(1165)
```

A árvore mostrou que o processo Python foi criado pelo Bash e também confirmou a existência de duas threads adicionais associadas ao processo.

## 5. Estado do processo

Durante a análise, o processo apresentou inicialmente o estado:

```text
Sl+
```

A letra `S` indica que o processo estava em estado de espera, ou sleeping.

Esse comportamento é coerente com o programa, pois ele utiliza `time.sleep(1)` entre as execuções.

A letra `l` indica que o processo possui múltiplas threads.

## 6. Uso de CPU e memória

Foram realizadas duas medições durante o experimento.

### Primeira medição

```text
CPU: 2,1%
Memória: 0,5%
```

### Segunda medição

```text
CPU: 2,6%
Memória: 0,5%
```

O uso de CPU apresentou uma pequena variação entre as duas medições, o que é esperado porque o programa alterna entre realizar cálculos e permanecer em espera.

O uso de memória permaneceu estável em 0,5%, comportamento compatível com uma aplicação simples.

## 7. Prioridade e nice

Inicialmente, o processo apresentou:

```text
PRI = 19
NI = 0
```

Foi utilizado o comando:

```bash
renice 5 -p 1163
```

Após a alteração, o processo apresentou:

```text
PRI = 14
NI = 5
```

O valor nice foi alterado de 0 para 5.

Com isso, o processo passou a possuir menor prioridade relativa na disputa pelo uso da CPU.

Após a alteração, o estado também passou a apresentar a letra `N`, indicando que o processo estava executando com valor nice positivo.

## 8. Threads

O comando:

```bash
ps -L -p 1163
```

apresentou três linhas de execução:

```text
PID     LWP
1163    1163
1163    1164
1163    1165
```

O processo possuía uma thread principal e duas threads adicionais.

A thread principal utilizava o identificador 1163, enquanto as threads adicionais utilizavam os identificadores 1164 e 1165.

As threads pertencem ao mesmo processo e compartilham seus recursos.

## 9. Análise do /proc

Foram analisadas quatro fontes no pseudo-sistema de arquivos `/proc`.

### 9.1 /proc/1163/status

Foram observadas as seguintes informações:

```text
Name: python3
State: S (sleeping)
Pid: 1163
PPid: 103
VmRSS: 10544 kB
Threads: 3
```

Esse arquivo permitiu confirmar o nome do processo, estado, PID, PPID, quantidade de memória utilizada e número de threads.

### 9.2 /proc/1163/cmdline

O conteúdo confirmou que o processo foi iniciado com:

```text
python3 aplicacao/processos.py
```

Esse arquivo é útil para verificar o comando e os argumentos utilizados na execução do processo.

### 9.3 /proc/1163/limits

O arquivo mostrou os limites de recursos aplicados ao processo.

Entre as informações observadas estavam:

```text
Max stack size: 8388608 bytes
Max open files: 10240
Max processes: 6861
```

Esses limites são definidos pelo sistema operacional para controlar a utilização de recursos por um processo.

### 9.4 /proc/1163/task

O diretório apresentou:

```text
1163  1164  1165
```

Esses identificadores correspondem às três threads existentes no processo.

## 10. Sinais

Durante o experimento foram aplicados os sinais SIGSTOP, SIGCONT e SIGTERM.

### SIGSTOP

Foi utilizado:

```bash
kill -STOP 1163
```

Após o comando, o estado do processo mudou para:

```text
TNl
```

A letra `T` indicou que o processo havia sido suspenso.

O processo continuou existindo, mas sua execução ficou temporariamente interrompida.

### SIGCONT

Foi utilizado:

```bash
kill -CONT 1163
```

Após o comando, o processo voltou ao estado:

```text
SNl
```

Isso confirmou que o processo retomou sua execução normalmente.

### SIGTERM

Por fim, foi utilizado:

```bash
kill -TERM 1163
```

Depois disso, o comando:

```bash
ps -p 1163
```

não encontrou mais o processo.

Isso confirmou que o processo havia sido encerrado.

## 11. Conclusão

O experimento permitiu observar na prática como o Linux gerencia processos.

Foi possível identificar PID e PPID, analisar a relação entre processo pai e filho, visualizar a árvore de processos, observar estados de execução, uso de CPU e memória, prioridade, valor nice e threads.

Também foram analisadas informações fornecidas pelo pseudo-sistema de arquivos `/proc`.

Os sinais SIGSTOP, SIGCONT e SIGTERM permitiram observar como um processo pode ser temporariamente suspenso, retomado e encerrado.

Os resultados obtidos foram coerentes com o funcionamento do programa utilizado e ajudaram a relacionar os conceitos de gerenciamento de processos estudados na disciplina com o comportamento real observado no sistema Linux.
