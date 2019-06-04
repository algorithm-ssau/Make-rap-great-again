# Make-rap-great-again

# Описание проекта
Данный сайт предназначен для любителей реп-культуры и баттлов в частности.
Он содержит информацию о популярных исполнителях, когда-либо участвоваших в Versus Battle.
Также на сайте присутствует информация по многим сезонам, которые проходили на этой площадке и общий сборник всех панчей, придуманных участниками.
Проект создан в рамках курса "Практикум на ЭВМ" в 2019 году студентами группы 6314 Факультета Информатики Самарского Университета.
Разработчики: Абдуллаев Евгений, Сомов Денис, Бессмертный Андрей, Щербинин Максим. 
Научный руководитель: Даниленко А.Н.

# Запуск сайта:
1) Необходимо скачать официальную версию Питона с сайта:  https://www.python.org/getit/windows/ и установить её.
2) Установите Django, прописав в командной строке: pip install django .
3) Для запуска, откройте командную строку, далее откройте папку с сайтом и в командной строке напишите: python manage.py runserver
4) Откройте сайт в браузере, перейдя по ссылке указанной в командной строке

# Размещение сайта на хостинге:
Мы разместили наш сайт на бесплатном хостинге Heroku. Для этого нужно было:
1) Зарегистрироваться на сайте 
2) Установить приложение
3) И далее в командной строке прописать следующее (находясь в директории сайта):
   1) git init
   2) git add .
   3) git commit -am "commit name"
   4) heroku create name-site --stack cedar
   5) git push heroku master
На этом моменте сайт уже создан и готов к работе.

Сейчас вы можете просто перейти на наш по ссылке:
https://rapisgreatagain.herokuapp.com/
