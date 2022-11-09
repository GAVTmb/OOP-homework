dict_file = {1: '1.txt', 2: '2.txt', 3: '3.txt'}


def reading_files(dicts):
    general_vocabulary = {}
    for key, values in dicts.items():
        with open(values, encoding='utf-8') as file:
            list_of_strings = [values]
            number_of_rows = 0
            for line in file:
                list_of_strings.append(line)
                number_of_rows += 1
            general_vocabulary[number_of_rows] = list_of_strings
    return general_vocabulary


def file_recording():
    text_to_write = reading_files(dict_file)
    sort_text = dict(sorted(text_to_write.items()))
    for key, values in sort_text.items():
        with open('result.txt', 'at', encoding='utf-8') as resault:
            resault.write(f'{values[0]}\n')
            resault.write(f'{str(key)}\n')
            resault.write(f'{" ".join(values[1:])}\n')


file_recording()
