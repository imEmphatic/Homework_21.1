Задание 1
Переведите имеющиеся контроллеры с FBV на CBV.
Не забудьте про контроллер контактов. Для его замены можно воспользоваться 
View или TemplateView

Задание 2
Создайте новую модель блоговой записи со следующими полями:

заголовок;
slug (реализовать через CharField);
содержимое;
превью (изображение);
дата создания;
признак публикации;
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

CRUD реализуйте на основе CBV (
ListView
, 
DetailView
, 
CreateView
, 
UpdateView
, 
DeleteView
) Соблюдайте нейминг шаблонов для CBV контроллеров - …_list.html, …_detail.html, …_form.html.

Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:

При открытии отдельной статьи увеличивать счетчик просмотров.
Для решения этой задачи можно воспользоваться переопределением метода 
get_object()
 в 
DetailView
.

#   H o m e w o r k _ 2 1 . 1  
 #   H o m e w o r k _ 2 2 . 1  
 #   H o m e w o r k _ 2 2 . 1  
 