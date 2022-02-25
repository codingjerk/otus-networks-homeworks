# Lab 01 -- Router on Stick

> Настройка VLAN и маршрутизации между VLAN методом «Router on Stick»

Для начала, соберём в симуляторе минимальный стенд с
двумя коммутаторами, двумя конечными узлами (ПК) и
маршрутизатором:

![Стенд сети](images/01-stand.png)

## Sources

https://github.com/IBashlakov/Otus_Network_Engineer_2022/blob/bb184670c2e10c7e74d0770ed8d90f371810c883/lab01/README.md

https://github.com/sag81/otus-networks/tree/master/workshop/02

https://github.com/fazzzan/Myotus-networks/blob/f97777eeb3787798b1662b1411c7900d861c9332/LECTURES/LABS_old/lab1/README.md

## TODO

- Документация (таблицы)
- Решение
  - Базовая конфигурация (авторизация, vty, banner, secret, no ip domain lookup, hostname)
  - Настройка коммутаторов
    - Настройка access / trunk портов
    - Создание VLAN, указание портов под VLAN
    - Изменение native VLAN
  - Настройка маршрутизатора
    - .1q encapsulation
  - Настройка конечных узлов
- Проверка
