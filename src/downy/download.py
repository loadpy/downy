import os
import requests
import threading
import psutil

# Todo: Create a better stoppable thread class.
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class Download():
    """
    Class for downloading content from the web more than the speed of light! (jk)
    """
    def __init__(self, url, filename="Default"):
        self._cores = psutil.cpu_count()
        self.url = url
        self.saveas = filename

    def get_cores(self):
        """
        Function to return the number of cores.
        """
        return self._cores

    def _download_chunk(self, headers, start):
        obj = requests.get(self.url,headers,stream = True)
        f = open(self.saveas,"ab+")
        f.seek(start)
        f.write(obj.content)
        f.close()

    def download(self):
        """
        Method for downloading the given content.
        """
        response_obj = requests.head(self.url)
        file_name = self.saveas
        file_size = int(response_obj.headers['content-length'])
        self._file_size = file_size
        if file_size == 0:
            raise ValueError('File Size is zero, hence probably an invalid URL.')

        path = os.path.expanduser('~') + "/Downloads"
        os.chdir(path)
        chunk = file_size // self._cores
        self._chunksize = chunk

        for i in range(self._cores):
            start = chunk*i
            end = start + chunk
            if i == self._cores-1:
                end = file_size
            # print(start,end)
            headers = {'Range': 'bytes=%d-%d' % (start, end)}
            thread = threading.Thread(target=self._download_chunk, args= (headers, start))
            thread.setDaemon(True)
            thread.start()

        main = threading.current_thread()
        for t in threading.enumerate():
            if t is main:
                 continue

    def get_chunk_size():
        return self._chunksize

    def get_filesize():
        return self._file_size
