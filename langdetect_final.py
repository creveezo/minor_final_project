import pickle
from counter import n_count

with open('dicts/n_gramm_dict_50k.pkl', 'rb') as f:
    n_gramms = pickle.load(f)
languages = list(n_gramms.keys())
user_score = {}
total = {}


# предобработка пользовательского ввода
def preprocess(text):
    ignore = ':;/’“”\'`[]§$()—#{}*‘_"»„'
    divider = '.?!¿¡…'
    nums = '123456789'
    text = text.lower()
    text = text.replace('...', '.')
    text = text.replace('.\n', '\n')
    for symb in divider:
        text = text.replace(symb+' ', '\n')
        text = text.replace(symb, '\n')
    res = ''
    for i in text:
        if i not in ignore:
            res += i
        if i in nums:
            res += "0"
    return res


def n_count_lines(text, n):
    text = text.strip()
    res = {}
    lines = text.split('\n')
    for line in lines:
        for i in range(len(line)-n+1):
            if line[i:i+n] != ' ':
                res.setdefault(line[i:i+n], 0)
                res[line[i:i+n]] += 1
    return res


print('Введите текст. Когда вы закончите, с новой строки введите "%%stop%%" без кавычек')

# цикл реализующий многострочный пользовательский ввод
user_input = ''
i = preprocess(input())
while i != '%%stop%%':
    user_input += i
    i = preprocess(input())

# непосредственно посчет для каждой н-граммы отдельно
n = 5
# для каждого языка отдельно
for lang in languages:
    user_score[lang] = 0
    user_dict = n_count(user_input, n)
    for n_gr in user_dict:
        current = n_gramms[lang][str(n)]
        if n_gr in current:
            a = current[n_gr]/sum(current.values()) * user_dict[n_gr]/sum(user_dict.values())
            user_score[lang] += a
if sum(user_score.values()) == 0:
    print('Это не похоже ни на один из доступных мне языков.')
else:
    user_score = {k: (v / sum(user_score.values()) * 100) for k, v in user_score.items()}
    user_score = sorted(user_score.items(), key=lambda item: item[1], reverse=True)
    print(user_score)
    # подводим итоги
    print('================== и т о г и ==================')
    for i in range(0,3):
        print(f'С вероятностью {round(user_score[i][1], 1)}% данный текст написан на следующем языке: {user_score[i][0]}')