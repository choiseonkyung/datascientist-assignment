import pandas as pd
from pandasql import *

paper_author = pd.read_csv("./paper_author.csv")
# print(paper_author)
paper_reference = pd.read_csv("./paper_reference.csv")
# print(paper_reference)

df_left_join = pd.merge(paper_author, paper_reference, how='left')


# 저자별 publication_count 구하기
def answer1():
    df_group = paper_author.groupby(['author_id']).count()
    publication_count_df = df_group.loc[:, ['paper_id']]
    publication_count_df.rename(columns={'paper_id':'publication_count'}, inplace=True)
    print(publication_count_df)


# 각 논문의 citation_count 구하기
def answer2():
    cit = df_left_join.groupby('reference_paper_id').count()
    cit_count_df = cit.loc[:, ['paper_id']]
    cit_count_df.rename(columns={'paper_id':'citation_count'}, inplace=True)
    print(cit_count_df)


# h-index 구하기
# a4저자가 발표한 논문의 수는 11편이고, 그 중 9편의 논문은 9회이상 인용됨
def answer3():
    a4_citations = [312, 313, 209, 166, 105, 84, 20, 11, 0, 9, 4]
    h_index = 0
    for tmp_h in range(len(a4_citations) + 1):
        check_num = 0
        for citation in a4_citations:
            if (tmp_h <= citation):
                check_num += 1
        if (tmp_h > check_num):
            h_index = tmp_h - 1
            break
        else:
            h_index = tmp_h

    print(h_index)


def answer4():
    pass


def answer5():
    pass


def answer6():
    pass


def answer7():
    pass


def answer8():
    pass





#
# if __name__ == '__main__':
#     answer1()
#     answer2()
#     answer3()
#     answer4()
#     answer5()
#     answer6()
#     answer7()
#     answer8()


