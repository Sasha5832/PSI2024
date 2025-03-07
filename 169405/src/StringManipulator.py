class StringManipulator:
    def __init__(self, text):
        self.text = text

    def reverse_string(self):
        return self.text[::-1]

    def count_words(self):
        return len(self.text.split())

    def capitalize_words(self):
        return " ".join(word.capitalize() for word in self.text.split())
