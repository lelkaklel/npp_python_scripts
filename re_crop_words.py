#-*- coding:utf-8 -*-
# soloviov.ae (lelkaklel@gmail.com) 2017
#
# Скрипт для плагина PythonScript текстового редактора Notepad++
#
# Скрипт запрашивает у пользователя регулярное выражение 
# и заменяет весь текст на отсортированный список уникальных 
# значений первых групп из найденных вхождений шаблона.

re_template_text = r"PG_SALESISISCACHE\.([\[\]\w\d]+)"

re_template_text = notepad.prompt('Please, print Python regex template...', 'RegEx template', re_template_text)

if re_template_text:

    matches = set()

    def match_found(m):
        matches.add(m.group(1))
        
    editor.research(re_template_text, match_found) 

    editor.clearAll()  # cleares all text in the current document

    matches = sorted(matches, key=lambda s: s.lower())

    for m in matches:
        editor.addText('{}\n'.format(m))


