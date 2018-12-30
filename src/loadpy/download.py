import os
import requests
import threading
import psutil # to get number of cores

cores = psutil.cpu_count()
# print(cores)

def get_info():
    data = {}
    data['url'] = input("Enter URL: ")
    data['name'] = input("Save as: ")
    return data

def download_chunk(headers, url, filename, start):
    obj = requests.get(url,headers,stream = True)
    f = open(filename,"ab+")
    f.seek(start)
    f.write(obj.content)
    f.close()

def download(data):
    response_obj = requests.head(data['url'])
    file_name = data['name']
    # print(response_obj.headers)
    file_size = int(response_obj.headers['content-length'])
    # print(file_size)

    if file_size == 0:
        print("Invalid URL")
        return

    path = os.path.expanduser('~') + "/Downloads"
    os.chdir(path)

    chunk = file_size // cores
    print("chunck: ",chunk)

    for i in range(cores):
        start = chunk*i
        end = start + chunk
        if i == cores-1:
            end = file_size
        # print(start,end)
        headers = {'Range': 'bytes=%d-%d' % (start, end)}
        thread = threading.Thread(target=download_chunk, args= (headers,data['url'],file_name,start))
        thread.setDaemon(True)
        thread.start()

    main = threading.current_thread()
    for t in threading.enumerate():
        if t is main:
             continue
        t.join()


if __name__ == '__main__':
    data = get_info()
    try:
        download(data)
        print("Downloaded")
    except:
        print("Some error occured")
