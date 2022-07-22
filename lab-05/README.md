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

# TODO: Распределение трафика между двумя линками и провайдером

```
Router(config)# access-list 50 permit 192.168.50.0 0.0.0.255
Router(config)# route-map BALANS permit 10
Router(config-route-map)# match ip address 50 - эта команда указывает на то, что трафик будет отфилтровываться на основе ACL номер 50.
Router(config-route-map)# set ip next-hop 100.100.100.29 - эта команда указывает, что для трафика отфилтрованного при помощи ACL номер 50 адресом следующего перехода будет 100.100.100.29
```

```
ip policy route-map 50
```

ИЛИ

```
!
track 1 ip sla 1 reachability
!
track 2 ip sla 2 reachability
!
interface Ethernet0/2
 ip policy route-map office
!
no ip route 0.0.0.0 0.0.0.0 5.20.26.0
no ip route 0.0.0.0 0.0.0.0 5.20.25.2 2
ip route 0.0.0.0 0.0.0.0 5.20.26.0 track 1
ip route 0.0.0.0 0.0.0.0 5.20.25.2 2 track 2
!
ip access-list standard VPC30
 permit 100.1.10.16 0.0.0.15
ip access-list standard VPC31
 permit 100.1.20.16 0.0.0.15
!
ip sla 1
 icmp-echo 5.20.26.0 source-ip 5.20.26.1
 threshold 2
 timeout 2
 frequency 4
ip sla schedule 1 start-time now
ip sla 2
 icmp-echo 5.20.25.2 source-ip 5.20.25.3
 threshold 2
 timeout 2
 frequency 4
ip sla schedule 2 start-time now
!
route-map office permit 10
 match ip address VPC30
 set ip next-hop verify-availability 5.20.25.2 10 track 2
!
route-map office permit 20
 match ip address VPC31
!
route-map office deny 50
!
```

# TODO: Отслеживание линка через технологию IP SLA

https://github.com/sirrax/otus-network-engineer-28-01-2022/tree/main/dz/lab-6-PBR#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%BE%D1%82%D1%81%D0%BB%D0%B5%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BB%D0%B8%D0%BD%D0%BA%D0%B0-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8E-ip-sla

# TODO: Маршрут по-умолчанию

```
ip route 0.0.0.0 0.0.0.0 <IP>
```

# TODO: конфиги
