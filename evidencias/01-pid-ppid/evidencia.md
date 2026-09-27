# PID e PPID

Comando utilizado:

```bash
ps -o pid,ppid,stat,pri,ni,%cpu,%mem,cmd -p 1163
```

Resultado observado:

```text
PID    PPID STAT PRI NI %CPU %MEM CMD
1163   103  Sl+   19  0   2.3  0.5 python3 aplicacao/processos.py
```

O processo analisado recebeu o PID 1163 e possuía PPID 103.

Para identificar o processo pai foi utilizado:

```bash
ps -o pid,ppid,stat,cmd -p 103
```

Resultado:

```text
PID    PPID STAT CMD
103    101  Ss   -bash
```

Assim, foi possível verificar que o Bash de PID 103 era o processo pai do programa Python.
