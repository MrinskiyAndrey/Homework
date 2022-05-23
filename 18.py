#Задание 18:
'''Создать функцию, которая вернет ближайшую к текущей странице главу.
Если две главы одинаково близко, то выбирается та,
которая находится на большей по порядку странице. '''

number = (int(input('Введите номер страницы: \n')))


def nearest_chapter(page: int):
    
    Table_of_contents = {
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}
    pages = list(Table_of_contents.values())    #Создание списка с номерами страниц глав
    tmp_dict = {}      #Создание временного словаря, формата {растояние до главы : номер страницы главы}
    i = 0
    while i < len(pages):
        tmp_dict[abs(page - pages[i])] = pages[i] #заполнение временного словаря.
        i+=1
    minimum = min(list(tmp_dict.keys()))   #минимальное расстояние до ближайшей главы
   
    result = tmp_dict.get(minimum)
    return result

print('Ближайшая глава на странице: ', nearest_chapter(number))
