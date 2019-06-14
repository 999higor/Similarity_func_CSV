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

    
    with open('my.csv', 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        fieldname_lenght = len(fieldnames)
        Sim_lenght = len(Similarity)

        writer.writeheader()

        flag = True

        for dado in arquivo:

            sim00 = function.similaridade(Similarity[0],dado['#1 String'],dado['#2 String'])
            sim01 = function.similaridade(Similarity[1],dado['#1 String'],dado['#2 String'])
            sim02 = function.similaridade(Similarity[2],dado['#1 String'],dado['#2 String'])
            sim03 = function.similaridade(Similarity[3],dado['#1 String'],dado['#2 String'])
            sim04 = function.similaridade(Similarity[4],dado['#1 String'],dado['#2 String'])
            sim05 = function.similaridade(Similarity[5],dado['#1 String'],dado['#2 String'])
            sim06 = function.similaridade(Similarity[6],dado['#1 String'],dado['#2 String'])
            sim07 = function.similaridade(Similarity[7],dado['#1 String'],dado['#2 String'])
            sim08 = function.similaridade(Similarity[8],dado['#1 String'],dado['#2 String'])
            sim09 = function.similaridade(Similarity[9],dado['#1 String'],dado['#2 String'])
            sim10 = function.similaridade(Similarity[10],dado['#1 String'],dado['#2 String'])
            sim11 = function.similaridade(Similarity[11],dado['#1 String'],dado['#2 String'])
            sim12 = function.similaridade(Similarity[12],dado['#1 String'],dado['#2 String'])
            sim13 = function.similaridade(Similarity[13],dado['#1 String'],dado['#2 String'])
            sim14 = function.similaridade(Similarity[14],dado['#1 String'],dado['#2 String'])
            sim15 = function.similaridade(Similarity[15],dado['#1 String'],dado['#2 String'])
            sim16 = function.similaridade(Similarity[16],dado['#1 String'],dado['#2 String'])
            sim17 = function.similaridade(Similarity[17],dado['#1 String'],dado['#2 String'])
            sim18 = function.similaridade(Similarity[18],dado['#1 String'],dado['#2 String'])
            sim19 = function.similaridade(Similarity[19],dado['#1 String'],dado['#2 String'])


            writer.writerow({fieldnames[0]: dado['Quality'],
                fieldnames[1]: dado['#1 ID'], 
                fieldnames[2]: dado['#2 ID'], 
                fieldnames[3]: dado['#1 String'],
                fieldnames[4]: dado['#2 String'],
                fieldnames[5]: sim00,
                fieldnames[6]: sim01,
                fieldnames[7]: sim02,
                fieldnames[8]: sim03,
                fieldnames[9]: sim04,
                fieldnames[10]: sim05,
                fieldnames[11]: sim06,
                fieldnames[12]: sim07,
                fieldnames[13]: sim08,
                fieldnames[14]: sim09,
                fieldnames[15]: sim10,
                fieldnames[16]: sim11,
                fieldnames[17]: sim12,
                fieldnames[18]: sim13,
                fieldnames[19]: sim14,
                fieldnames[20]: sim15,
                fieldnames[21]: sim16,
                fieldnames[22]: sim17,
                fieldnames[23]: sim18,
                fieldnames[24]: sim19,
                
                })
            
            if (flag == True and dado['Quality'] == '1'):

                Hamming = sim00
                MLIPNS = sim01
                JaroWinkler = sim02
                Jaro = sim03
                StrCmp95 = sim04
                Jaccard = sim05
                Sorensen = sim06
                Tversky = sim07
                Overlap = sim08
                Cosine = sim09
                RatcliffObershelp = sim10
                EntropyNCD = sim11
                BZ2NCD = sim12
                LZMANCD = sim13
                ZLIBNCD = sim14
                Prefix = sim15
                Postfix = sim16
                NormalizedLevenshtein = sim17
                MetricLCS = sim18
                NGram = sim19
                flag = False

            if (flag == False and dado["Quality"] == '1'):

                if(sim00 < Hamming):
                    Hamming = sim00

                if(sim01 < MLIPNS):
                    MLIPNS = sim01

                if(sim02 < JaroWinkler):
                    JaroWinkler = sim02

                if(sim03 < Jaro):
                    Jaro = sim03

                if(sim04 > StrCmp95):
                    StrCmp95 = sim04

                if(sim05 < Jaccard):
                    Jaccard = sim05

                if(sim06 < Sorensen):
                    Sorensen = sim06

                if(sim07 < Tversky):
                    Tversky = sim07

                if(sim08 < Overlap):
                    Overlap = sim08

                if(sim09 < Cosine):
                    Cosine = sim09

                if(sim10 < RatcliffObershelp):
                    RatcliffObershelp = sim10

                if(sim11 < EntropyNCD):
                    EntropyNCD = sim11

                if(sim12 < BZ2NCD):
                    BZ2NCD = sim12

                if(sim13 < LZMANCD):
                    LZMANCD = sim13

                if(sim14 < ZLIBNCD):
                    ZLIBNCD = sim14

                if(sim15 < Prefix):
                    Prefix = sim15

                if(sim16 < Postfix):
                    Postfix = sim16

                if(sim17 < NormalizedLevenshtein):
                    NormalizedLevenshtein = sim17

                if(sim18 > MetricLCS):
                    MetricLCS = sim18

                if(sim19 > NGram):
                    NGram = sim19
    
        arq = open('result.txt', 'w')
        arq.write('Hamming: '+str(Hamming)+'\n')
        arq.write('MLIPNS: '+str(MLIPNS)+'\n')
        arq.write('JaroWinkler: '+str(JaroWinkler)+'\n')
        arq.write('Jaro: '+str(Jaro)+'\n')
        arq.write('StrCmp95: '+str(StrCmp95)+'\n')
        arq.write('Jaccard: '+str(Jaccard)+'\n')
        arq.write('Sorensen: '+str(Sorensen)+'\n')
        arq.write('Tversky: '+str(Tversky)+'\n')
        arq.write('Overlap: '+str(Overlap)+'\n')
        arq.write('Cosine: '+str(Cosine)+'\n')
        arq.write('RatcliffObershelp: '+str(RatcliffObershelp)+'\n')
        arq.write('EntropyNCD: '+str(EntropyNCD)+'\n')
        arq.write('BZ2NCD: '+str(BZ2NCD)+'\n')
        arq.write('LZMANCD: '+str(LZMANCD)+'\n')
        arq.write('ZLIBNCD: '+str(ZLIBNCD)+'\n')
        arq.write('Prefix: '+str(Prefix)+'\n')
        arq.write('Postfix: '+str(Postfix)+'\n')
        arq.write('NormalizedLevenshtein: '+str(NormalizedLevenshtein)+'\n')
        arq.write('MetricLCS: '+str(MetricLCS)+'\n')
        arq.write('NGram: '+str(NGram)+'\n')
        arq.close()       
            
                
            

                
            
if __name__ == "__main__":
    main()