import os.path
import View.ParserWrapper

if __name__ == '__main__':
    filename = os.path.dirname(__file__) + '/../file/11-水泥.csv'
    data = View.ParserWrapper.read_from_source(filename)
