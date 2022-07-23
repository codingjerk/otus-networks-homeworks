# OSPF (фильтрация между зонами: backbone-зона и другие)

## Задание

**Цель:**

Настроить OSPF офисе Москва.

Разделить сеть на зоны.

Настроить фильтрацию между зонами.

**Описание/Пошаговая инструкция выполнения домашнего задания:**

1. Маршрутизаторы R14-R15 находятся в зоне 0 - backbone.
2. Маршрутизаторы R12-R13 находятся в зоне 10. Дополнительно к маршрутам должны получать маршрут по умолчанию.
3. Маршрутизатор R19 находится в зоне 101 и получает только маршрут по умолчанию.
4. Маршрутизатор R20 находится в зоне 102 и получает все маршруты, кроме маршрутов до сетей зоны 101.
5. Настройка для IPv6 повторяет логику IPv4.

![Топология стенда, скриншот из Eve-NG](./topology.png)

## Решение

### Общая информация

Для конфигурирования OSPF, необходимо:

1. Включить OSPF-маршрутизацию:

```
router ospf 1 (ipv6 router ospf 1 для IPv6)
```

2. Задать `router-id`:

```
router-id <IP>
```

3. (опционально) Перевести неиспользуемые интерфейсы в пассивный режим:

```
passive-interface EthernetX/Y
passive-interface EthernetX₂/Y₂
...
```

и перечислить неиспользуемые интерфейсы, или:

```
passive-interface default
no passive-interface EthernetX/Y
no passive-interface EthernetX₂/Y₂
...
```

и перечислить используемые.

4. Для каждого внутреннего интерфейса задать зону:

```
interface EthernetX/Y
 ip ospf 1 area <AREA>
 ipv6 ospf 1 area <AREA>
```

Для проверки можно использовать:

```
show ip route ospf
show ip ospf neighbor
show ip ospf database
show ip ospf interface
```

Для аносирования маршрута по-умолчанию:

```
default-information originate always
```

### Настройка R14, R15, R12 и R13

`R14` и `R15` поместим в зону 0, также они должны анонсировать маршруты по-умолчанию:

`R14`:

```
router ospf 1
  router-id 193.1.6.20
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/3
  default-information originate always

ipv6 router ospf 1
  router-id 193.1.6.20
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/3
  default-information originate always

interface range Ethernet0/0-3
 ip ospf 1 area 0
 ipv6 ospf 1 area 0

```

`R15`:

```
router ospf 1
  router-id 193.1.6.30
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/3
  default-information originate always

ipv6 router ospf 1
  router-id 193.1.6.30
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/3
  default-information originate always

interface range Ethernet0/0-3
 ip ospf 1 area 0
 ipv6 ospf 1 area 0
```

Повторим для `R12` и `R13`, но без анонсирования маршрутов по-умолчанию и в зоне 10:

`R12`:

```
router ospf 1
  router-id 193.1.6.0
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/2
  no passive-interface Ethernet0/3

ipv6 router ospf 1
  router-id 193.1.6.0
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/2
  no passive-interface Ethernet0/3

interface range Ethernet0/0-3
 ip ospf 1 area 10
 ipv6 ospf 1 area 10
```

`R13`:

```
router ospf 1
  router-id 193.1.6.10
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/2
  no passive-interface Ethernet0/3

ipv6 router ospf 1
  router-id 193.1.6.10
  passive-interface default
  no passive-interface Ethernet0/0
  no passive-interface Ethernet0/1
  no passive-interface Ethernet0/2
  no passive-interface Ethernet0/3

interface range Ethernet0/0-3
  ip ospf 1 area 10
  ipv6 ospf 1 area 10
```

### Настройка R19

`R19` должен находиться в зоне 101.

Также он должен получать только маршрут по-умолчанию,

для этого на `R14` пропишем:

```
router ospf 1
  area 101 stub no-summary

ipv6 router ospf 1
  area 101 stub no-summary
```

И теперь настроим `R19`:

```
router ospf 1
  router-id 193.1.6.40
  area 101 stub no-summary
  passive-interface default
  no passive-interface Ethernet0/0

ipv6 router ospf 1
  router-id 193.1.6.40
  area 101 stub no-summary
  passive-interface default
  no passive-interface Ethernet0/0

interface range Ethernet0/0-3
  ip ospf 1 area 101
  ipv6 ospf 1 area 10
```

### Настройка R20

`R20`:

```
router ospf 1
  router-id 193.1.6.50
  passive-interface default
  no passive-interface Ethernet0/0

ipv6 router ospf 1
  router-id 193.1.6.50
  passive-interface default
  no passive-interface Ethernet0/0

interface range Ethernet0/0-3
  ip ospf 1 area 102
  ipv6 ospf 1 area 102
```

Для того, чтобы отфильтровать маршруты с зоны 101,
добавим фильтры на `R15`:

```
TODO
```

### Конфиги

TODO: R12-15, R19-20
