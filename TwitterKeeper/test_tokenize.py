def tokenize(d):
        result = d.split("/")
        result = list(filter(None, result))
        return result

def prepared_Text( text_list):
        new_text = []
        for text in text_list:
            new_text.append(self.preprocessText(text["text"]))
        return new_text
str = "B/A/C/D"
list = []
B = prepared_Text(list)
A = tokenize(str)
print(B)