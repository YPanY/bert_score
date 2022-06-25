from bert_score import score
import transformers
import csv



if __name__ == '__main__':
    output, reference
    output = open("./results/bart/output.txt", "r")
    ref = output = open("./results/bart/reference.txt", "r")

    # CSV
    reader = csv.reader(open('filename.csv', 'r'))
    new_csv = open('output.csv', 'w')
    writer = csv.writer(new_csv, delimiter=',')
    headers = reader.next()
    headers.append("Brand New Awesome Header")
    writer.writerow(headers)
    i = 1
    for row in reader:
        row.append(new data for my new header)
        writer.writerow(row)
        i += 1
        if i % 100 == 0:
            print(i)
            new_csv.flush()

    # [(P,R,F1),alignments] = score(["godzilla : the series is an american - japanese animated television series created by jeff kline and richard raynis . it originally aired on fox kids in the united states between september 1998 and april 2000 , and a sequel to ' godzilla ' ( 1998 ) . malcolm danare , kevin dunn and michael lerner reprise their roles from the movie . "],
    #                ["godzilla : the series is an animated science-fiction television series developed by jeff kline and richard raynis . "
    #                 ],lang="EN",idf=False,return_alignments=True)
    # print(P, R, F1, alignments)
    #
    # P, R, F1= score(["godzilla : the series is an american - japanese animated television series created by jeff kline and richard raynis . it originally aired on fox kids in the united states between september 1998 and april 2000 , and a sequel to ' godzilla ' ( 1998 ) . malcolm danare , kevin dunn and michael lerner reprise their roles from the movie . "],
    #                 ["godzilla : the series is an animated science-fiction television series developed by jeff kline and richard raynis . "
    #                  ], lang="EN", idf=False,alignment=[
    #         [0, 1, 2, 3, 4, 5, 6, 8, 6, 5, 0, 8, 10, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 3, 7, 11, 11, 22, 7, 14, 9, 7, 12, 14, 15, 16, 10, 1, 19, 15, 21, 8, 24, 5, 6, 4, 12, 9, 0, 1, 4, 13, 18, 2, 2, 20, 21, 22, 23, 2, 15, 16, 17, 23, 19, 20, 21, 17, 18, 18, 13, 13, 3, 4, 14, 9, 10, 24],
    #         [0, 1, 2, 3, 4, 5, 6, 13, 7, 35, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]])
    # print(P, R, F1)

    # score(["28-year-old chef found dead in San Francisco mall"],
    #       ["28-Year-Old Chef Found Dead at San Francisco Mall"], lang="EN", idf=False)