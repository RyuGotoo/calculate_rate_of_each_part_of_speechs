import collections
from janome.tokenizer import Tokenizer


class Blog(object):
    def __init__(self, text):
        self.pos_num = 0
        self.pos_counts = {}


def get_text():
    with open('text.txt') as f:
        text = f.read()
    return text


def create_blogs(text):
    blog = Blog(text)

    # 形態素解析
    pos_list = []
    for token in Tokenizer().tokenize(text):
        pos_list.append(token.part_of_speech.split(',')[0])
    blog.pos_num = len(pos_list)

    # 品詞 (pos) カウント
    pos_counts = collections.Counter(pos_list)
    blog.pos_counts = pos_counts
    return blog


def show_result(blog):
    blog.pos_counts = dict(sorted(blog.pos_counts.items(), key=lambda x: -x[1]))
    print(get_text())
    print()
    print('総単語数 :', blog.pos_num)
    for pos, count in blog.pos_counts.items():
        pct = (count / blog.pos_num) * 100
        print('{}: {} ( {}% )'.format(pos, count, round(pct, 1)))


def main():
    text = get_text()
    blog = create_blogs(text)
    show_result(blog)


if __name__ == '__main__':
    main()
