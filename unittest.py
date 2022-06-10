from bert_score import score
import transformers

def test_something():
        print("hey")


if __name__ == '__main__':
    P,R,F1 = score(["godzilla : the series is an american - japanese animated television series created by jeff kline and richard raynis . it originally aired on fox kids in the united states between september 1998 and april 2000 , and a sequel to ' godzilla ' ( 1998 ) . malcolm danare , kevin dunn and michael lerner reprise their roles from the movie . "],
                   ["godzilla : the series is an animated science-fiction television series developed by jeff kline and richard raynis . "
                    ],lang="EN",idf=False)
    print(P,R,F1)
