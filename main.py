import csv
import function

def main():
   
    arquivo = open('arquivo.csv')
    arquivo = csv.DictReader(arquivo)

    Similarity = ['Hamming',
        'MLIPNS',
        'JaroWinkler',
        'Jaro',
        'StrCmp95',
        'Jaccard',
        'Sorensen',
        'Tversky',
        'Overlap',
        'Cosine',
        'RatcliffObershelp',
        'EntropyNCD',
        'BZ2NCD',
        'LZMANCD',
        'ZLIBNCD',
        'Prefix',
        'Postfix',
        'NormalizedLevenshtein',
        'MetricLCS',
        'NGram']

    fieldnames = ['Quality', 
        '#1 ID', 
        '#2 ID', 
        '#1 String', 
        '#2 String',
        'Hamming',
        'MLIPNS',
        'JaroWinkler',
        'Jaro',
        'StrCmp95',
        'Jaccard',
        'Sorensen',
        'Tversky',
        'Overlap',
        'Cosine',
        'RatcliffObershelp',
        'EntropyNCD',
        'BZ2NCD',
        'LZMANCD',
        'ZLIBNCD',
        'Prefix',
        'Postfix',
        'NormalizedLevenshtein',
        'MetricLCS',
        'NGram'
        ] 

    result = []

    result_deuruim = ['Hamming',
        'MLIPNS',
        'JaroWinkler',
        'Jaro',
        'StrCmp95',
        'Jaccard',
        'Sorensen',
        'Tversky',
        'Overlap',
        'Cosine',
        'RatcliffObershelp',
        'EntropyNCD',
        'BZ2NCD',
        'LZMANCD',
        'ZLIBNCD',
        'Prefix',
        'Postfix',
        'NormalizedLevenshtein',
        'MetricLCS',
        'NGram']

    with open('csv_result.csv', 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        flag = True
        linha = {}

        for dado in arquivo:
            result.clear()

            for h in range(0,5):
                linha[fieldnames[h]] = dado[fieldnames[h]]

            for j in range(len(Similarity)):
                result.append(function.similaridade(Similarity[j], dado['#1 String'], dado['#2 String']))
                linha[fieldnames[j+5]] = result[j]        
                
            writer.writerow(linha)

            if(flag == True and dado['Quality'] == '1'):
                
                for i in range(len(Similarity)):
                    result_deuruim[i] = result[i]
                flag = False

            if(flag == False and dado['Quality'] == '1'):

                for i in range(len(Similarity)):
                    if result[i] < result_deuruim[i]:
                        result_deuruim[i] = result[i]

    arq = open('result.txt', 'w')

    for i in range(len(Similarity)):
        arq.write(Similarity[i] + " : "+ str(result_deuruim[i])+'\n')
    arq.close()
                          
if __name__ == "__main__":
    main()