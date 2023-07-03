# Тестовое задание: Задача Python - Mini readability

Программа оформлена в виде утилиты командной строки, которой в качестве параметра указывается произвольный URL.

**Алгоритм работы программы:**
1. Получение html-страницы с помощью requests и BeautyfulSoup.
1. Получение списка тэгов из внешних файлов(header_tags, content_tags).
1. Выборка информации из html-страницы по указанным тэгам.
1. Формирование пути выходного файла посредством создания необходимых каталогов.
1. Запись результата в файл.

**URL для проверки:**
- https://lenta.ru/news/2023/07/01/orlov
- https://sport.rambler.ru/autosport/51029151-chempion-formuly-1-nazval-edinstvennogo-pilota-kotoryy-mozhet-sravnitsya-s-ferstappenom
- https://www.gazeta.ru/sport/news/2023/07/03/20798738.shtml
- https://cheremuha.com/2023/06/29/mne-protivno-uchastvovat-v-etom-deputat-vladimir-paxarev-o-procedure-vybora-kandidatov-dlya-doski-pochyota.html
- https://kub.media/news/6621-est-tolko-dva-gendera-rossii/
- https://sportrbc.ru/news/64a2b1369a79478f47539099
