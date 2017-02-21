#pragma once

#include <Python.h>

#include <string>
using namespace std;

class CPythonActuator
{
private:
    PyObject *m_interface_module;

public:
    static CPythonActuator& instance();

    bool init();

    ///调用升级脚本，执行升级操作
    ///
    ///returns,0=失败
    int do_update(const string& script_path, const string& script_name);

    ///解压zip文件
    ///
    ///returns,0=失败
    int do_zip_folder(const string& zip_file_name, const string& zip_folder);
    ///压缩目录到zip文件
    ///
    ///returns,0=失败
    int do_unzip_to_folder(const string& zip_file_name, const string& unzip_folder);

    ///从ftp上下载文件
    ///
    ///returns,0=失败
    int do_download_ftp_file(const string& remote_addr,
                             int remote_port,
                             const string& user_name,
                             const string& user_password,
                             const string& remote_file_name,
                             const string& local_file_name);
private:
    CPythonActuator(void);
    ~CPythonActuator(void);
};

