# Алгоритм Эрли

Forked from [Artur-mipt/Formal-Languages](https://github.com/Artur-mipt/Formal-Languages).

Исправлен небольшой баг, изменен ввод грамматики: программа читает данные из файла,
а не из консоли.

## Постановка задачи

Дана контекстно-свободная грамматика G и слово w. Нужно узнать, принадлежит ли слово w
языку, задаваемому этой грамматикой L(G).

Вывести, соответственно, true или false.

## Использование

Ввод грамматики осуществляется в файле `grammar.json`. Здесь `check` - слово, которое
необходимо проверить на принадлежность языку, `rules` - правила грамматики вида
`<N> -> <expr>`, где `N` - нетерминальный символ, `expr` - цепочка множества `(NxT)*`
(`T` - терминальный символ). Аксиомой грамматики является символ `S`.

Запустить программу можно с помощью

```
python3 main.py
```
