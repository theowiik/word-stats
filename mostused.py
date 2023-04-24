import os
import re
from collections import Counter
import plotly.graph_objs as go
import plotly

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return Counter(words)

def main():
    folder_path = "files"
    word_counts = Counter()

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            word_counts += count_words(file_path)

    most_common_words = word_counts.most_common(10)

    words, counts = zip(*most_common_words)

    fig = go.Figure(
        data=[go.Bar(x=words, y=counts)],
        layout=go.Layout(
            title="Most Common Words in .txt Files",
            xaxis=dict(title="Words"),
            yaxis=dict(title="Counts")
        )
    )

    plotly.offline.plot(fig, filename='most_common_words.html')

if __name__ == "__main__":
    main()
