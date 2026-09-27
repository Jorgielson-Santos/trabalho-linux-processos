# Threads

Foi utilizado:

```bash
ps -L -p 1163
```

Resultado:

```text
PID     LWP TTY          TIME CMD
1163    1163 pts/0    00:00:00 python3
1163    1164 pts/0    00:00:09 Thread-1 (taref
1163    1165 pts/0    00:00:09 Thread-2 (taref
```

O processo possui três linhas de execução observáveis.

O LWP 1163 corresponde à thread principal, enquanto 1164 e 1165 correspondem às duas threads criadas pelo programa.

As threads pertencem ao mesmo processo e compartilham seus recursos.
