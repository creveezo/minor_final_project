import os
import pickle

input_folder = "corpora_preprocessed"
freq = {}


def n_count(text, n, d={}):
    text = text.strip()
    for i in range(len(text)-n+1):
        if text[i:i+n] != ' ':
            d.setdefault(text[i:i+n], 0)
            d[text[i:i+n]] += 1
    return d


def make_freq(name, amount=100000000):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                lang = filename[:-4]
                print(f'working on {lang} for {name} corpora')
                freq[lang] = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}}
                count = 0
                for line in f:
                    if count < amount:
                        count += len(line)
                        for n_gram in freq[lang]:
                            freq[lang][n_gram] = n_count(line, int(n_gram), freq[lang][n_gram])
    name = 'n_gramm_dict_' + name + '.pkl'
    with open(name, 'wb') as f:
        pickle.dump(freq, f)


make_freq('10k', 10000)
make_freq('5k', 5000)
make_freq('1k', 1000)
make_freq('100', 100)
make_freq('total')
make_freq('1M', 1000000)
make_freq('500k', 500000)
make_freq('100k', 100000)
make_freq('50k', 50000)
