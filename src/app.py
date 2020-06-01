from lyrics import *
import tkinter as tk


class Lyrix:
    def __init__(self, master):
        self.master = master
        self.scope = "user-read-currently-playing"
        self.username = ""  # Your username
        self.client_id = ""  # Get from Spotify Developers Dashboard
        self.client_secret = ""  # Get from Spotify Developers Dashboard
        self.redirect_uri = "http://localhost:8888/callback/"
        self.client_access_token = ""  # Add client access token from Genius API
        self.previous_name = ""
        self.name = ""

        root.title(
            get_title(
                self.scope,
                self.username,
                self.client_id,
                self.client_secret,
                self.redirect_uri,
            )
        )
        self.text = tk.Text(root, wrap="word", font=("PT Sans", "18"))
        self.scroll_y = tk.Scrollbar(root, orient="vertical", command=self.text.yview)

        get_lyrics(
            self.scope,
            self.username,
            self.client_id,
            self.client_secret,
            self.redirect_uri,
            self.client_access_token,
        )
        self.name = get_name(
            self.scope,
            self.username,
            self.client_id,
            self.client_secret,
            self.redirect_uri,
        )

        self.add_lyrics()
        self.new_lyrics()

    def add_lyrics(self):
        self.text.config(state="normal")

        with open("lyrics.json", "r") as openfile:
            lyrics = json.load(openfile)["lyrics"]

        self.text.tag_configure("center", justify="center")
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", lyrics)
        self.text.tag_add("center", "1.0", "end")
        self.text.config(state="disabled")
        self.text.pack(side="left", expand=True, fill="both")
        self.scroll_y.pack(side="left", expand=False, fill="y")

        self.text.configure(yscrollcommand=self.scroll_y.set)

    def new_lyrics(self):
        root.after(5000, self.new_lyrics)
        self.previous_name = self.name
        self.name = get_name(
            self.scope,
            self.username,
            self.client_id,
            self.client_secret,
            self.redirect_uri,
        )
        if self.name != self.previous_name:
            get_lyrics(
                self.scope,
                self.username,
                self.client_id,
                self.client_secret,
                self.redirect_uri,
                self.client_access_token,
            )

            self.previous_name = self.name

            self.name = get_name(
                self.scope,
                self.username,
                self.client_id,
                self.client_secret,
                self.redirect_uri,
            )

            root.title(
                get_title(
                    self.scope,
                    self.username,
                    self.client_id,
                    self.client_secret,
                    self.redirect_uri,
                )
            )

            self.add_lyrics()


root = tk.Tk()
lyrix = Lyrix(root)
root.mainloop()
