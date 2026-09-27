# Análise do /proc

Foram analisadas quatro fontes relacionadas ao processo 1163.

## status

Comando:

```bash
grep -E 'Name|State|Pid|PPid|Threads|VmRSS' /proc/1163/status
```

Resultado:

```text
Name:   python3
State:  S (sleeping)
Pid:    1163
PPid:   103
TracerPid:      0
VmRSS:     10544 kB
Threads:        3
```

O arquivo permitiu verificar nome, estado, PID, PPID, memória utilizada e quantidade de threads.

## cmdline

Comando:

```bash
tr '\0' ' ' < /proc/1163/cmdline; echo
```

Resultado:

```text
python3 aplicacao/processos.py
```

Essa informação mostra o comando utilizado para iniciar o processo.

## limits

Comando:

```bash
cat /proc/1163/limits
```

Entre os valores observados estavam:

```text
Max stack size       8388608
Max processes        6861
Max open files       10240
```

O arquivo apresenta limites de recursos aplicados ao processo.

## task

Comando:

```bash
ls /proc/1163/task
```

Resultado:

```text
1163  1164  1165
```

Esses identificadores correspondem às três threads do processo.
