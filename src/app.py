from src.lyrics import *
import tkinter as tk

root = tk.Tk()
root.iconbitmap('./images/icon.png')

scope = 'user-read-currently-playing'
username = ''
client_id = ''
client_secret = ''
redirect_uri = 'http://localhost:8888/callback/'
client_access_token = ''

root.title(get_title(scope, username, client_id, client_secret, redirect_uri))
get_lyrics(scope, username, client_id, client_secret, redirect_uri, client_access_token)

with open('lyrics.json', 'r') as openfile:
    lyrics = json.load(openfile)['lyrics']

text = tk.Text(root, wrap='word', font=('PT Sans', '18'))
text.tag_configure('center', justify='center')
text.insert('1.0', lyrics)
text.tag_add('center', '1.0', 'end')
text.config(state='disabled')
text.pack(side='left', expand=True, fill='both')

scroll_y = tk.Scrollbar(root, orient='vertical', command=text.yview)
scroll_y.pack(side='left', expand=False, fill='y')

text.configure(yscrollcommand=scroll_y.set)

root.resizable(0, 1)
root.mainloop()
