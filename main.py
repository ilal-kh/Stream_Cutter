from cutter import *
from window import *


root = Tk()
root.title("Стриморезка")
root.geometry('400x200')
txt_1 = create_block("Путь к видео", root, browsefunc_mp4, 0, 0)
txt_2 = create_block("Путь к файлу с тамкодами", root, browsefunc_txt, 0, 1)
txt_3 = create_block("Путь куда резать", root, browsefunc_dir, 0, 2)
btn_4 = create_cut_button('Разрежь меня', root, command=clicked, text_1=txt_1, text_2=txt_2, text_3=txt_3)
root.mainloop()