from datetime import datetime

class Logger:
    @staticmethod
    def append(errorString):
        with open('errorlog.txt','w+') as f:
            curDate = datetime.now();
            f.write('{0}     '.format(str(curDate)) + errorString + '\n')
        print(errorString);