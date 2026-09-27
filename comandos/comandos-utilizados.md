# Comandos utilizados

Este arquivo contém os principais comandos utilizados durante o diagnóstico do processo Linux.

## 1. Execução da aplicação

```bash
python3 aplicacao/processos.py
```

O comando acima iniciou o programa Python utilizado no experimento.

## 2. Identificação do processo

```bash
ps -o pid,ppid,stat,pri,ni,%cpu,%mem,cmd -p 1163
```

Esse comando foi utilizado para verificar o PID, PPID, estado, prioridade, nice, uso de CPU e memória do processo.

```bash
ps -o pid,ppid,stat,cmd -p 103
```

Esse comando foi utilizado para identificar o processo pai do programa Python.


## 3. Árvore de processos

```bash
pstree -p 103
```

Esse comando foi utilizado para visualizar a relação hierárquica entre o Bash, o processo Python e suas threads.

## 4. Threads

```bash
ps -L -p 1163
```

Esse comando foi utilizado para verificar as threads existentes no processo Python.

## 5. Estado e recursos

```bash
ps -o pid,stat,%cpu,%mem,pri,ni,cmd -p 1163
```

Esse comando foi utilizado para verificar o estado do processo, uso de CPU e memória, prioridade e valor nice.

## 6. Alteração de prioridade

```bash
renice 5 -p 1163
```

Esse comando foi utilizado para alterar o valor nice do processo de 0 para 5.

## 7. Informações do /proc

```bash
grep -E 'Name|State|Pid|PPid|Threads|VmRSS' /proc/1163/status
```

Esse comando foi utilizado para consultar informações do processo, como nome, estado, PID, PPID, memória utilizada e quantidade de threads.

```bash
tr '\0' ' ' < /proc/1163/cmdline; echo
```

Esse comando foi utilizado para verificar o comando utilizado para iniciar o processo.

```bash
cat /proc/1163/limits
```

Esse comando foi utilizado para verificar os limites de recursos definidos para o processo.

```bash
ls /proc/1163/task
```

Esse comando foi utilizado para visualizar as threads pertencentes ao processo.

## 8. Sinais

```bash
kill -STOP 1163
```

Esse comando foi utilizado para suspender temporariamente a execução do processo.

```bash
ps -o pid,stat,cmd -p 1163
```

Esse comando foi utilizado para verificar a mudança de estado do processo após o SIGSTOP.

```bash
kill -CONT 1163
```

Esse comando foi utilizado para retomar a execução do processo que estava suspenso.

```bash
ps -o pid,stat,cmd -p 1163
```

Esse comando foi utilizado para confirmar que o processo voltou a executar após o SIGCONT.

```bash
kill -TERM 1163
```

Esse comando foi utilizado para encerrar o processo de forma controlada.

```bash
ps -p 1163
```

Esse comando foi utilizado para confirmar que o processo havia sido encerrado.
