from collections import Counter

class WordAnalyzer:
    def __init__(self, text):
        self.text = text

    def find_most_frequent_word(self):
        if not self.text.strip():
            return None  # Zwracamy None dla pustego tekstu
        words = self.text.lower().split()
        word_counts = Counter(words)
        max_count = max(word_counts.values())
        most_frequent_words = [word for word, count in word_counts.items() if count == max_count]
        return most_frequent_words[0]  # Jeśli jest kilka, zwracamy pierwsze według kolejności
