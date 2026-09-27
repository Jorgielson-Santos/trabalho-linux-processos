# Sinais

## SIGSTOP

Foi utilizado:

```bash
kill -STOP 1163
```

Em seguida:

```bash
ps -o pid,stat,cmd -p 1163
```

Resultado:

```text
PID   STAT  CMD
1163  TNl   python3 aplicacao/processos.py
```

O estado `T` mostrou que o processo foi suspenso, mas continuou existindo.

## SIGCONT

Foi utilizado:

```bash
kill -CONT 1163
```

Resultado da verificação:

```text
PID   STAT  CMD
1163  SNl   python3 aplicacao/processos.py
```

O processo saiu do estado `T` e voltou para `S`, indicando que sua execução foi retomada.

## SIGTERM

Por fim foi utilizado:

```bash
kill -TERM 1163
```

Depois:

```bash
ps -p 1163
```

Resultado:

```text
PID TTY          TIME CMD
```

Como não apareceu nenhuma linha com o PID 1163, foi confirmado que o processo havia sido encerrado.

Diferentemente do SIGSTOP, que apenas suspende temporariamente a execução, o SIGTERM encerra o processo.
