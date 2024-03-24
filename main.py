import wikipedia                                                #для работы с Википедией
import tkinter                                                  #для созд-я графич интерфейса
import textwrap                                                 #для переноса строк из  текста

def wiki(event):                                                #event чтоб работала конкретно при нажатии нужн кнопки
    title = wikipedia.random()                                  #title = рандомн заголовок стр из Википедии
    try:                                                        #пытаемся
        page = wikipedia.summary(title)                         #присвоить переменной page о чем статья с заголовком title
        if len(page) < 75:                                      #если длина текста о чем статья < 75
            lbl.config(text=page)                               #в окне текст заменяем на переменную page (page - о чем эта статья)
        else:                                                   #иначе если длина текста о чем статья > 75
            page = textwrap.shorten(page, width=200)            #усекаем текст чтоб он поместился в ширину width
            lbl.config(text=page)                               #в окне текст заменяем на определяющую, где нужен перенос строки, переменную page (page - о чем эта статья)
    except wikipedia.DisambiguationError as e:                  #избегая Disambiguation ошибки в кач-ве е
        lbl.config(text='нажмите кнопку еще раз')

wikipedia.set_lang('ru')                                        #чтоб Вик-я была на рус яз
#создадим графическ интерфейс
root = tkinter.Tk()
root.title('вики api')                                          #заголовок окна
root.geometry('500x500')                                        #размер окна 500 на 500 пикселей
lbl = tkinter.Label(root, text='получи статью с Википедии')     #текст внутри окна
lbl.pack()                                                      #чтоб отобразилось в окне
btn = tkinter.Button(root, text='случайная статья')
btn.pack()                                                      #чтоб отобразилась в окне
btn.bind('<Button-1>', wiki)                                    #кнопка будет работать при нажатии лев кнопки мыши (<Button-1>)
root.mainloop()                                                 #зацикливаем появление окна (без этого оно не появится)
