# Remove Dead Members
Этот скрипт предназначен для администраторов сообществ вконтакте. Он находит и удаляет мёртвые страницы из подписчиков группы. Для работы скрипта требуется: 
- установить библиотеку `vk_api`
- указать свой ключ для OAuth-авторизации в переменной `access_token`
- указать ID сообщества в переменной `group_id`

После чего можно запускать скрипт. Выполнение может занять несколько минут - в группе из 7000 подписчиков скрипт нашёл и удалил 200 мёртвых страниц где-то за 3 минуты.
