import pandas as pd
from pandasql import *

paper_author = pd.read_csv("./paper_author.csv")
# print(paper_author)
paper_reference = pd.read_csv("./paper_reference.csv")
# print(paper_reference)

def answer1():
    with open("./answer1.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer2():
    with open("./answer2.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)


def answer3():
    with open("./answer3.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer4():
    with open("./answer4.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer5():
    with open("./answer5.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer6():
    with open("./answer6.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer7():
    with open("./answer7.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)

def answer8():
    with open("./answer8.sql", "r") as f:
        sql = ''
        while True:
            line = f.readline()
            if not line: break
            a = str(line)
            sql = sql + a

    print(sql)
    df = sqldf(sql, globals())
    print(df)


if __name__ == '__main__':
    answer1()
    answer2()
    answer3()
    answer4()
    answer5()
    answer6()
    answer7()
    answer8()


