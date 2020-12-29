#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Условние задания
# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

import sys

def add():
    name = input("Название товара? ")
    shop = input("Название магазина? ")
    coast = int(input("Введите его цену "))

    product = {
        'name': name,
        'shop': shop,
        'coast': coast,
    }

    products.append(product)

    if len(product) > 1:
        products.sort(key=lambda item: item.get('name', ''))


def list_():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    print(line)
    print(
        ' | {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Наименование товара",
            "Название магазина",
            "Стоимость"
        )
    )
    print(line)

    for idx, product in enumerate(products, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                product.get('name', ''),
                product.get('shop', ''),
                product.get('coast', 0)
            )
        )

    print(line)
def select():
    g = input("Введите название продукта ")
    count = 0
    for product in products:
        if g == product.get('name'):
            count += 1
            print(
                '{:>4}: {} {} {}'.format(count, product.get('name', ' '), product.get('shop', ' '),
                                         product.get('coast', ' '))
            )
    if count == 0:
        print("Товар не найден")

def help_():
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <магазин> - запросить товары в выбранном магазине")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def error():
    print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'list':
            list_()

        elif command.startswith('select'):
            g = input("Введите название продукта ")

        elif command == 'help':
            help_()

        else:
            error()