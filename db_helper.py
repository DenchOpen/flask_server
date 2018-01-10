# encoding: utf-8

__author__ = 'Dench'


def create_database():
    import models
    models.create_database()


def drop_database():
    import models
    models.drop_database()


if __name__ == '__main__':
    pass
