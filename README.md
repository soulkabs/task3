# task3

В магазине 5 касс, в каждый момент времени к кассе стоит очередь некоторой длины. Каждые 30 минут измеряется средняя длина очереди в каждую кассу и для каждой кассы это значение записывается в соответствующий ей файл (всего 5 файлов).

Каждое значение заканчивается символом новой строки. 
Магазин работает 8 часов в день.
Рассматривается только один день. 
На момент запуска приложения все значения уже находятся в файлах.

Написать программу, которая по данным замеров определяет интервал времени, когда в магазине было наибольшее количество посетителей за день.
Аргумент программы - путь к каталогу с файлами. В каталоге будут 5 файлов: Cash1.txt, Cash2.txt ... Cash5.txt. 

Пример одного из файлов:
1\n
1.2\n
1.3\n
1.34\n
1.5\n
1.9\n
1.7\n
1.832\n
1.91\n
2.3\n
2.5\n
4.9\n
3.5\n
2.34\n
1.242\n
1.01\n

Выведите номер интервала, в котором было наибольшее число посетителей в очередях магазина на всех кассах.
Первый интервал идет под номером 1, последний под номером 16. 
В случае обнаружения нескольких интервалов следует выводить первый из них.
