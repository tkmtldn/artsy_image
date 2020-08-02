import time
from src.getter import get_content
from src.saver import save_content

if __name__ == '__main__':
    # Input the name of the picture below.
    input_name = input()

    started = time.time()

    filename = f"{input_name}.jpg"
    dirname = str(time.time()).split('.')[0]
    data = open('fetch.txt', 'r').read()

    length, width = get_content(dirname, data)
    save_content(dirname, filename, length, width)
    print(f"Finished in {time.time() - started} seconds.")
