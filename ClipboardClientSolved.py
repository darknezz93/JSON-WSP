from ladon.clients.jsonwsp import JSONWSPClient
import pprint, os
from os.path import join, dirname, abspath


def print_result(jsonwsp_resp):
    if jsonwsp_resp.status == 200:
        if 'result' in jsonwsp_resp.response_dict:
            pprint.pprint(jsonwsp_resp.response_dict['result'], indent=2)
        else:
            pprint.pprint(jsonwsp_resp.response_dict)
    else:
        print("A problem occured while communicating with the service:\n")
        print(jsonwsp_resp.response_body)


def open_file(filename):
    dir = join(dirname(abspath(__file__)), 'files')
    path = os.path.join(dir, filename)
    return open(path, 'rb')


def save_file(filename, data_reader):
    dir = join(dirname(abspath(__file__)), 'download')
    path = os.path.join(dir, filename)
    file_to_write = open(path, 'wb')
    file_to_write.write(data_reader.read())
    file_to_write.close()


if __name__ == '__main__':
    base_url = 'http://localhost:8888'
    transfer_client = JSONWSPClient(base_url + '/ClipboardService/jsonwsp/description')

    fileName = "cat.jpg"

    jsonwsp_resp = transfer_client.upload(attachment=open_file(fileName))
    print_result(jsonwsp_resp)

    jsonwsp_resp = transfer_client.download()
    print_result(jsonwsp_resp)

    if jsonwsp_resp.status == 200:
        f = jsonwsp_resp.response_dict['result']
        save_file(fileName, f)
