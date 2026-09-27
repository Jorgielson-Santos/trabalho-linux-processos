
# Estado e uso de recursos

Foi utilizado o comando:

```bash
ps -o pid,stat,%cpu,%mem,pri,ni,cmd -p 1163
```

Na primeira medição foi observado:

```text
PID   STAT  %CPU  %MEM  PRI  NI  CMD
1163  Sl+   2.1   0.5   19   0   python3 aplicacao/processos.py
```

Na segunda medição:

```text
PID   STAT  %CPU  %MEM  PRI  NI  CMD
1163  Sl+   2.6   0.5   19   0   python3 aplicacao/processos.py
```

O estado `S` indica que o processo estava em espera, comportamento esperado porque o programa utiliza `time.sleep(1)`.

O uso de CPU apresentou uma pequena variação entre 2,1% e 2,6%, enquanto o uso de memória permaneceu estável em 0,5%.

## Alteração do nice

Foi utilizado:

```bash
renice 5 -p 1163
```

Resultado:

```text
1163 (process ID) old priority 0, new priority 5
```

Depois da alteração:

```text
PID   STAT  %CPU  %MEM  PRI  NI  CMD
1163  SNl+  2.9   0.5   14   5   python3 aplicacao/processos.py
```

O valor nice foi alterado de 0 para 5, reduzindo a prioridade relativa do processo na disputa pela CPU.
