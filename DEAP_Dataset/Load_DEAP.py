import cPickle  # To read .dat files

 # Pickling or flattening, converts structured data into a data stream format
 #Here we are converting DEAP Dataset .dat files to .txt files

channels = ['Fp1', 'AF3', 'F3', 'F7', 'FC5', 'FC1',
            'C3', 'T7', 'CP5', 'CP1', 'P3', 'P7',
            'PO3', 'O1', 'Oz', 'Pz', 'Fp2', 'AF4',
            'Fz', 'F4', 'F8', 'FC6', 'FC2', 'Cz',
            'C4', 'T8', 'CP6', 'CP2', 'P4', 'P8',
            'PO4', 'O2']

nLabel = 4
nTrial = 40
nUser =32
nChannel = 32
nTime = 8064

valence= open("valence.txt", 'a+')
arousal = open("arousal.txt", 'a+')
dominance = open("dominance.txt", 'a+')
liking = open("liking.txt", 'a+')


for i in range(nUser):
    if i < 9:
        name = '0' + str(i + 1)
    else:
        name = i + 1
    fname = "data_preprocessed_python/s" + str(name) + ".dat"
    x = cPickle.load(open(fname, 'rb'))
    print(fname)

    for tr in range(nTrial):
        dfname = "data/s" + str(name) + "t" + str(tr+1) + ".txt"
        temp_data = open(dfname, 'w')
        for ch in range(nChannel):
            temp_data.write(channels[ch] + ",")
            for dat in range(nTime):
                if ch == 31:
                    temp_data.write(str(x['data'][tr][ch][dat]))
                else:
                    temp_data.write(str(x['data'][tr][ch][dat]) + ",")
            temp_data.write("\n")

        valence.write(str(x['labels'][tr][0]) + "\n")
        arousal.write(str(x['labels'][tr][1]) + "\n")
        dominance.write(str(x['labels'][tr][2]) + "\n")
        liking.write(str(x['labels'][tr][3]) + "\n")
        temp_data.close()
valence.close()
arousal.close()
dominance.close()
liking.close()
