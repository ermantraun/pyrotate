import os
import time
import sys
import re
from zipfile import ZipFile

def parseArg() -> dict:
    args = sys.argv[1:]
    args_names = args[::2]
    args_values = args[1::2]
    if len(args_names) != len(args_values):
        raise ValueError('Неправильно введенные аргументы')
    args = {}
    for arg_matching_index in range(len(args_names)):
        args[args_names[arg_matching_index].replace('-', '')] = args_values[arg_matching_index]
    return args

def get_number_in_str(string):
    number = ''
    for index in range(len(string)):
        try:
            int(string[index])
            number += string[index]
        except ValueError:
            pass
    return number

def redistribute_archives(archives_dir_path, ls):
    for archive in reversed(ls):
        archive_number = get_number_in_str(archive)
        archive_path = archives_dir_path + '/' + archive
        new_archive_number = int(archive_number) + 1
        new_archive_path = archives_dir_path + '/' + 'logarchive' + str(new_archive_number)
        print(archive, archive_number, new_archive_number, new_archive_path, sep='---')
        os.rename(archive_path, new_archive_path)
        
def clear_file(file_path):
    print('Clear old log')
    open(file_path, 'wb').close()

def compress_file(file_path, archive_path, arcname=None):
    print('Compressing file: ', file_path, archive_path, sep='---')
    with ZipFile(archive_path, 'x') as myzip:
        myzip.write(file_path, arcname=arcname)
   
def rotate(file_path, max_log_arhives, send_to_server=False):
    disassembled_file_path = os.path.split(file_path)
    archives_dir_path = str(disassembled_file_path[0]) + '/rotate'
    new_archive_path = archives_dir_path + '/logarchive1'
    log_file_name = disassembled_file_path[-1]
    try:
        os.mkdir(archives_dir_path)
        print('1) Automatic archiving and moving in log exceeding the maximum size to the archive catalog')
        compress_file(file_path, new_archive_path, log_file_name)
        clear_file(file_path)
    except FileExistsError:
        ls = os.listdir(archives_dir_path)
        if len(ls) >= max_log_arhives:
            print('The number of archives has exceeded the maximum, redistribution is performed and the oldest archive is deleted/sent to the server: ...')
            oldest_archive_name = max(ls, key=get_number_in_str)
            oldest_archive_path = archives_dir_path + '/' + oldest_archive_name
            ls.remove(oldest_archive_name)
            if send_to_server == '1':
                print('1) Sending the oldest archive to the server: ' + oldest_archive_name)
                pass
            else:
                print('1) Deleted oldest archive: ' + oldest_archive_name)
                os.remove(oldest_archive_path)
                
            print('2) Redistribution of archives..')
            redistribute_archives(archives_dir_path, ls)
            
            print('3) Automatic archiving, clear and moving in log exceeding the maximum size to the archive catalog')
            compress_file(file_path, new_archive_path, log_file_name)
            clear_file(file_path)
        else:
            print('1) Redistribution of archives..')
            redistribute_archives(archives_dir_path, ls)
            print('2) Automatic archiving, clear and moving in log exceeding the maximum size to the archive catalog')
            compress_file(file_path, new_archive_path, log_file_name)
            clear_file(file_path)
            
    print('||| The rotation has been successfully completed! |||')
def send_to_server(server_address, port, tcp=False):
    pass


def monitor_log_file_size(file_path, max_size, interval, action, action_args):
    print('Starting log monitoring')
    while True:
        size = os.path.getsize(file_path) // (1024 ** 2)
        if size > max_size:
            print('Log file has exceeded the maximum size, rotation is performed')
            action(**action_args)
        time.sleep(interval)
        
def main():
    args = parseArg()
    print(args)
    action_args = {'file_path': args['path'], 'max_log_arhives': int(args['maxlog']), 
                   'send_to_server': args['server']}
    monitor_log_file_size(file_path=args['path'], max_size=int(args['maxsize']), 
                          interval=int(args['interval']), action=rotate, action_args=action_args)



if __name__ == "__main__":
    main()