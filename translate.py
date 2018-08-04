from google.cloud import translate
import re
translate_client = translate.Client.from_service_account_json(
        'Serbian Subs-674943e9498c.json')

new_srt_list = []
with open('test.srt') as f:
    srt_lines = f.readlines()
    for x, ind_line in enumerate(srt_lines):
        # print(x, ':', ind_lines)
        if re.match('[a-zA-Z]', ind_line):
            # The text to translate
            text = ind_line
            # The target language
            target = 'sr'
            # translation
            translation = translate_client.translate(text, target_language=target)
            new_line = translation['translatedText'] + '\n'
            # print(x, ':', new_line)
            new_srt_list.append(new_line)
        else:
            new_srt_list.append(ind_line)

with open('new_srt.srt', 'a', encoding='utf-8') as file:
    for new_lines in new_srt_list:
        file.write(new_lines)
        print('New Subtitles Complete')
