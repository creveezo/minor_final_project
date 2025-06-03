import os

input_folder = "for_minor"
clean_folder = "corpora_preprocessed"

os.makedirs(clean_folder, exist_ok=True)


# Очистка и сохранение в новые файлы
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(clean_folder, filename)

        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f_in, \
             open(output_path, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                if line[0] != '#':
                    line = line.lower()
                    line = line[line.find('\t')+1:]
                    final = ''
                    for symb in line:
                        if symb not in '.:;,/?!’“”\'`[]§$()—¿¡{}*‘_"»„…':
                            if symb in '123456789':
                                symb = '0'
                            elif symb == '\u200b':
                                symb = ' '
                            final += symb
                    f_out.write(final)
