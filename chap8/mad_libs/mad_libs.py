import re

class MadLibs:

    def __init__(self, mad_lib_file):
        #do nothting yet
        with open(mad_lib_file) as mlf:
            self.mad_lib_text = mlf.read()
            self.replaceable_words = []
            self.new_words = []

    def find_replaceable(self):
        repl_reg = re.compile(r"[A-Z]{4,}")
        self.replaceable_words = repl_reg.findall(self.mad_lib_text)

    def enter_new_words(self):
        for replaceable in self.replaceable_words:
            new_word = input("Please enter a {0}: ".format(replaceable.lower()))
            self.new_words.append(new_word)
