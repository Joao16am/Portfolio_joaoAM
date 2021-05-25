class cifra:

    def __init__(self):
        self.raw_str = repr(input())
        self.message = []
        self.get_info()

        print(self.password)
        print(self.message)

    def get_info(self):
        parag = [c for c in range(len(self.raw_str)) if self.raw_str[c].isalpha() is False]
        self.password, text = (self.raw_str[1:parag[1]], self.raw_str[parag[1] + 2:len(self.raw_str) - 1])
        self.cleaner(text)

    def cleaner(self, text, alert = 0, clean_text = ''):
        text = text.replace(' ', '')
        text = text.replace(',', '')
        for i in range(len(text)):
            if text[i].isalpha() is True and alert == 1:
                clean_text += text[i]
            elif text[i].isalpha() is False and i + 1 < len(text):
                alert = 0
            else:
                alert = 1
        self.message = [clean_text[i - len(self.password):i] for i in range(len(self.password), len(clean_text), len(self.password)) if clean_text[i].isalpha() is True]



        return clean_text

cifra()
