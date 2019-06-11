# -*- encoding: utf-8 -*-
"""
@author: jiaxinxin
@license: (C) Copyright 2015-2019, Palmax Corporation Limited.
@contact:jiaxinxin@palmax.cn
@software: PyCharm
@file: builder.py
@time: 2019-06-11 10:33
@desc:
"""


class Building(object):

    def __init__(self):
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class House(Building):

    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big'


class Flat(Building):

    def build_floor(self):
        self.floor = 'More than One'

    def build_size(self):
        self.size = 'Small'


class ComplexBuilding(object):

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


class ComplexHouse(ComplexBuilding):

    def build_floor(self):
        self.floor = 'One'

    def build_size(self):
        self.size = 'Big and fancy'


def construct_building(cls):
    building = cls()
    building.build_floor()
    building.build_size()
    return building


if __name__ == '__main__':
    house = House()
    print(house)
    flat = Flat()
    print(flat)
    complex_house = construct_building(ComplexHouse)
    print(complex_house)
