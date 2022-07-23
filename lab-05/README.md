# Маршрутизация на основе политик (PBR)

## Задание

**Цель:**

Настроить политику маршрутизации в офисе Чокурдах. Распределить трафик между 2 линками.

**Описание/Пошаговая инструкция выполнения домашнего задания:**

В этой самостоятельной работе мы ожидаем, что вы самостоятельно:

1. Настроите политику маршрутизации для сетей офиса Чокурдах.
  - Распределите трафик между двумя линками с провайдером.
  - Настроите отслеживание линка через технологию IP SLA. (только для IPv4)
2. Настройте для офиса Лабытнанги маршрут по-умолчанию.

![Топология стенда, скриншот из Eve-NG](./topology.png)

## Решение

### Распределение трафика между двумя линками и провайдером

Создадим 2 ACL, для разных линков,
по первому пустим трафик с `VPC30`, по другому -- с `VPC31`.

```
ip access-list standard ACL-VPC30
  permit 193.1.5.200 any
```

```
ip access-list standard ACL-VPC31
  permit 193.1.5.210 any
```

Теперь с использованием этих ACL, создадим `route-map` `split`:

```
route-map SPLIT permit 10
  match ip address ACL-VPC30
  set ip next-hop 193.1.3.23
```

```
route-map SPLIT permit 20
  match ip address ACL-VPC31
  set ip next-hop 193.1.3.31
```

Для входящего интерфейса укажем,
что пакеты с него следует маршрутизировать с
использованием политики
`route-map SPLIT`:

```
interface Ethernet0/2
  ip policy route-map SPLIT
```

<details>
  <summary>Проверим, что трафик маршрутизируется корректно</summary>

  ```
  TODO: ping + wireshark
  ```
</details>

### Отслеживание линка через технологию IP SLA

Настроим отслеживание линков с помощью ICMP:

```
ip sla 1
 icmp-echo 193.1.3.23 source-ip 193.1.5.1
 frequency 5

ip sla 2
 icmp-echo 193.1.3.31 source-ip 193.1.5.0
 frequency 5
```

И запустим его:

```
ip sla schedule 1 life forever start-time now
ip sla schedule 2 life forever start-time now

Теперь обновим наши `route-map`'ы:

```
route-map SPLIT permit 10
  match ip address ACL-VPC30
  set ip next-hop verify-availability 193.1.3.23 10 track 1
  set ip next-hop verify-availability 193.1.3.31 20 track 2

route-map SPLIT permit 20
  match ip address ACL-VPC31
  set ip next-hop verify-availability 193.1.3.31 10 track 2
  set ip next-hop verify-availability 193.1.3.23 20 track 1

track 1 ip sla 1 reachability
track 2 ip sla 2 reachability
```

### Маршрут по-умолчанию

Для роутераа `R27` (Лабытнанги) настроим маршруты по-умолчанию:

```
ip route 0.0.0.0 0.0.0.0 193.1.3.21
ipv6 route ::/0 2001:3::2:1
```

Проверяем, появились ли маршруты:

```
# show ip route

TODO

# show ipv6 route

TODO
```

## Конфиги

<details>
  <summary>R27</summary>

  ```
  TODO
  ```
</details>

<details>
  <summary>R28</summary>

  ```
  TODO
  ```
</details>
