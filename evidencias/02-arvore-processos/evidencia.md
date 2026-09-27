# Árvore de processos

Comando:

```bash
pstree -p 103
```

Resultado:

```text
bash(103)───python3(1163)─┬─{python3}(1164)
                          └─{python3}(1165)
```

A árvore mostra o Bash como processo pai do Python e também apresenta as duas threads adicionais do processo.

