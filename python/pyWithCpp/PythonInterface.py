#coding=utf-8

import sys
import os
import CConv

from FtpProcessor import FtpDownloader
from ZipProcessor import ZipProcessor

class ConvWrapper(object):

    def __init__(self):
        pass

    def notify(self, exp):
        print "python ConvWrapper-notify:", exp
        CConv.notify(exp)
        print CConv.get_string()

    def notify_progress(self, progress_type, cur_progress, total_progress):
        print "Python notify_progress:", progress_type, cur_progress, total_progress
        print CConv.notify_progress(progress_type, cur_progress, total_progress)

    def notify_process(self, process_type, log_info):
        print "Python notify_process:", process_type, log_info
        print CConv.notify_process(process_type, log_info)

    def get_app_path(self):
        return CConv.get_app_path()

    def get_backup_path(self):
        return CConv.get_backup_path()

    def stop_app_by_name(self, app_path, app_name):
        '''0=失败，1=成功
        '''
        return CConv.stop_app_by_name(app_path, app_name)

    def start_app_by_name(self, app_path, app_name):
        '''0=失败，1=成功
        '''
        return CConv.start_app_by_name(app_path, app_name)
    
    def do_update(self, script_path, script_name):
        '''进行升级操作。

        args:
            script_path：升级脚本所在路径，str。
            script_name：升级脚本名称，str，不带后缀。

        returns:
            int值。非0为成功，0=失败。
        '''
        try:
            self.notify_process(1, 'do-update: begin to run update-script file=%s/%s'%(script_path, script_name))
            update_function = self.__get_update_function(script_path, script_name)
            return int(update_function(os.path.abspath(script_path), self))
        except Exception, ex:
            print "Error in do_update:", ex
            return 0

    def do_download_ftp_file(self, remote_addr, remote_port, user_name, user_password, remote_file_name, local_file_name):
        '''从ftp上下载文件。

        args:
            remote_addr：ftp服务的远程ip地址，str。
            remote_port：ftp服务的远程端口，int。
            user_name：ftp登录用户名，str。
            user_password：ftp登录密码，str。
            remote_file_name：待下载的ftp文件路径，str。
            local_file_name：下载到本地的文件路径，str。

        returns:
            int值。非0为成功，0=失败。
        '''
        try:
            self.notify_process(1, 'download-ftp-file: begin to download-file=%s'%(remote_file_name))
            
            ftp = FtpDownloader()

            #连接到ftp
            if not ftp.connect(remote_addr, remote_port):
                self.notify_process(2, 'ftp-connect error: addr=%s, port=%d'%(remote_addr, remote_port))
                return 0

            #登录到ftp
            if not ftp.login(user_name, user_password):
                self.notify_process(2, 'ftp-login error: user=%s, pwd=%d'%(user_name, user_password))
                return 0

            #获取欢迎信息
            self.notify_process(1, ftp.getwelcome())

            #下载文件
            if not ftp.download_file(remote_file_name, local_file_name, self):
                self.notify_process(2, 'ftp-download-file error: file=%s'%(remote_file_name))
                return 0

            self.notify_process(3, 'ftp-download-file success.')
            return 1
        except Exception, ex:
            self.notify_process(2, "ftp-download-file error:%s"%(ex))
            return 0
        finally:
            ftp.quit()

    def do_zip_folder(self, zip_file_name, zip_dir):
        '''压缩文件夹.

        args:
            zip_file_name：生成的压缩文件的路径名称, str。
            zip_dir：需要压缩的文件夹, str。

        returns:
            int值。压缩成功返回非0，否则返回0。
        '''
        try:
            return int(ZipProcessor.zip_folder(zip_file_name, zip_dir))
        except Exception, ex:
            print "Error in do_zip_folder:", ex
            return 0

    def do_unzip_to_folder(self, zip_file_name, unzip_dir):
        '''解压缩到文件夹。

        args:
            zip_file_name：压缩文件的路径名称。
            unzip_dir：解压缩到的目标文件夹。

        returns:
            int值。解压缩成功返回非0，否则返回0。
        '''
        try:
            return int(ZipProcessor.unzip_to_folder(zip_file_name, unzip_dir, self))
        except Exception, ex:
            print "Error in do_unzip_to_folder:", ex
            return 0
        
    def __get_update_function(self, script_path, script_name):
        if script_path not in sys.path:
            sys.path.append(script_path)

        script_module = __import__(script_name)
        return getattr(script_module, 'process_update')


conv = ConvWrapper()

def do_update(script_path, script_name):
    '''进行升级操作。

    args:
        script_path：升级脚本所在路径，str。
        script_name：升级脚本名称，str，不带后缀。

    returns:
        int值。非0为成功，0=失败。
    '''
    return int(conv.do_update(script_path, script_name))

def do_download_ftp_file(remote_addr, remote_port, user_name, user_password, remote_file_name, local_file_name):
    '''从ftp上下载文件。

    args:
        remote_addr：ftp服务的远程ip地址，str。
        remote_port：ftp服务的远程端口，int。
        user_name：ftp登录用户名，str。
        user_password：ftp登录密码，str。
        remote_file_name：待下载的ftp文件路径，str。
        local_file_name：下载到本地的文件路径，str。

    returns:
        int值。非0为成功，0=失败。
    '''
    return int(conv.do_download_ftp_file(remote_addr, remote_port, user_name, user_password, remote_file_name, local_file_name))

def do_zip_folder(zip_file_name, zip_dir):
    '''压缩文件夹.

    args:
        zip_file_name：生成的压缩文件的路径名称, str。
        zip_dir：需要压缩的文件夹, str。

    returns:
        int值。压缩成功返回非0，否则返回0。
    '''
    return int(conv.do_zip_folder(zip_file_name, zip_dir))

def do_unzip_to_folder(zip_file_name, unzip_dir):
    '''解压缩到文件夹。

    args:
        zip_file_name：压缩文件的路径名称。
        unzip_dir：解压缩到的目标文件夹。

    returns:
        int值。解压缩成功返回非0，否则返回0。
    '''
    return int(conv.do_unzip_to_folder(zip_file_name, unzip_dir))

    
if __name__ == '__main__':
    #do_download_ftp_file('10.0.3.167', 21, 'anonymous', '', '/BaiduYunDownload/Effective_Modern_C++.pdf', 'Effective_Modern_C++.pdf')
    #do_update('./','testadd') 
    print 'PythonInterface module'
