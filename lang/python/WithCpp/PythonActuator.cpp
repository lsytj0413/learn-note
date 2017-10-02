#include "PythonActuator.h"

#include "PythonWrapper.h"
#include "../log/GPC_SimpleLog.h"

CPythonActuator::CPythonActuator(void)
    :m_interface_module(NULL)
{
}


CPythonActuator::~CPythonActuator(void)
{
    if (Py_IsInitialized())
    {
        Py_Finalize();
    }
}

CPythonActuator& CPythonActuator::instance()
{
    static CPythonActuator instance;

    return instance;
}

bool CPythonActuator::init()
{
    //初始化解释器
    Py_Initialize();
    if (!Py_IsInitialized())
    {
        RUN_LOG_PRINT("CPythonActuator:init initialize Python Error. \n");
        return false;
    }

    //导出C++代码模块到Python中
    PyObject *p_cconv_module = Py_InitModule("CConv", CConvMethods);
    if(NULL == p_cconv_module)
    {
        RUN_LOG_PRINT("CPythonActuator:init init CConv module Error. \n");
        return false;
    }

    //引入脚本路径
    PyRun_SimpleString("import sys");
    //发布时这个路径是需要更改的
    PyRun_SimpleString("sys.path.append('../../UpdateServiceAgent/src/script')");

    //加载interface模块
    PyObject *p_interface_name = PyString_FromString("PythonInterface");
    m_interface_module = PyImport_Import(p_interface_name);
    if (NULL == m_interface_module)
    {
        RUN_LOG_PRINT("CPythonActuator:init load module PythonInterface Error. \n");
        return false;
    }
    Py_DecRef(p_interface_name);

    return true;
}

int CPythonActuator::do_update(const string& script_path, const string& script_name)
{
    if (NULL == m_interface_module)
    {
        return 0;
    }

    //查找函数
    PyObject *p_update_func = PyObject_GetAttrString(m_interface_module, "do_update");
    if (NULL == p_update_func || !PyCallable_Check(p_update_func))
    {
        RUN_LOG_PRINT("CPythonActuator:do_update can't find Python function=do_update. \n");
        return 0;
    }

    //创建参数
    PyObject *p_args = PyTuple_New(2);
    PyTuple_SetItem(p_args, 0, Py_BuildValue("s", script_path.c_str()));
    PyTuple_SetItem(p_args, 1, Py_BuildValue("s", script_name.c_str()));

    //调用python函数
    PyObject *p_ret = PyObject_CallObject(p_update_func, p_args);
    if (NULL == p_ret)
    {
        RUN_LOG_PRINT("CPythonActuator:do_update no return value in Python function:do_update. \n");
        return 0;
    }

    int i_ret = 0;
    PyArg_Parse(p_ret, "i", &i_ret);
    return i_ret;
}

int CPythonActuator::do_zip_folder(const string& zip_file_name, const string& zip_folder)
{
    if (NULL == m_interface_module)
    {
        return 0;
    }

    //查找函数
    PyObject *p_zip_folder_func = PyObject_GetAttrString(m_interface_module, "do_zip_folder");
    if (NULL == p_zip_folder_func || !PyCallable_Check(p_zip_folder_func))
    {
        RUN_LOG_PRINT("CPythonActuator:do_zip_folder can't find Python function=do_zip_folder. \n");
        return 0;
    }

    //创建参数
    PyObject *p_args = PyTuple_New(2);
    PyTuple_SetItem(p_args, 0, Py_BuildValue("s", zip_file_name.c_str()));
    PyTuple_SetItem(p_args, 1, Py_BuildValue("s", zip_folder.c_str()));

    //调用python函数
    PyObject *p_ret = PyObject_CallObject(p_zip_folder_func, p_args);
    if (NULL == p_ret)
    {
        RUN_LOG_PRINT("CPythonActuator:do_zip_folder no return value in Python function:do_zip_folder. \n");
        return 0;
    }

    int i_ret = 0;
    PyArg_Parse(p_ret, "i", &i_ret);
    return i_ret;
}

int CPythonActuator::do_unzip_to_folder(const string& zip_file_name, const string& unzip_folder)
{
    if (NULL == m_interface_module)
    {
        return 0;
    }

    //查找函数
    PyObject *p_unzip_to_folder_func = PyObject_GetAttrString(m_interface_module, "do_unzip_to_folder");
    if (NULL == p_unzip_to_folder_func || !PyCallable_Check(p_unzip_to_folder_func))
    {
        RUN_LOG_PRINT("CPythonActuator:do_unzip_to_folder can't find Python function=do_unzip_to_folder. \n");
        return 0;
    }

    //创建参数
    PyObject *p_args = PyTuple_New(2);
    PyTuple_SetItem(p_args, 0, Py_BuildValue("s", zip_file_name.c_str()));
    PyTuple_SetItem(p_args, 1, Py_BuildValue("s",  unzip_folder.c_str()));

    //调用python函数
    PyObject *p_ret = PyObject_CallObject(p_unzip_to_folder_func, p_args);
    if (NULL == p_ret)
    {
        RUN_LOG_PRINT("CPythonActuator:do_unzip_to_folder no return value in Python function:do_unzip_to_folder. \n");
        return 0;
    }

    int i_ret = 0;
    PyArg_Parse(p_ret, "i", &i_ret);
    return i_ret;
}

int CPythonActuator::do_download_ftp_file(const string& remote_addr,
                                          int remote_port,
                                          const string& user_name,
                                          const string& user_password,
                                          const string& remote_file_name,
                                          const string& local_file_name)
{
    if (NULL == m_interface_module)
    {
        return 0;
    }

    //查找函数
    PyObject *p_download_ftp_file_func = PyObject_GetAttrString(m_interface_module, "do_download_ftp_file");
    if (NULL == p_download_ftp_file_func || !PyCallable_Check(p_download_ftp_file_func))
    {
        RUN_LOG_PRINT("CPythonActuator:do_download_ftp_file can't find Python function=do_download_ftp_file. \n");
        return 0;
    }

    //创建参数
    PyObject *p_args = PyTuple_New(6);
    PyTuple_SetItem(p_args, 0, Py_BuildValue("s", remote_addr.c_str()));
    PyTuple_SetItem(p_args, 1, Py_BuildValue("i",  remote_port));
    PyTuple_SetItem(p_args, 2, Py_BuildValue("s", user_name.c_str()));
    PyTuple_SetItem(p_args, 3, Py_BuildValue("s", user_password.c_str()));
    PyTuple_SetItem(p_args, 4, Py_BuildValue("s", remote_file_name.c_str()));
    PyTuple_SetItem(p_args, 5, Py_BuildValue("s", local_file_name.c_str()));

    //调用python函数
    PyObject *p_ret = PyObject_CallObject(p_download_ftp_file_func, p_args);
    if (NULL == p_ret)
    {
        RUN_LOG_PRINT("CPythonActuator:do_download_ftp_file no return value in Python function:do_download_ftp_file. \n");
        return 0;
    }

    int i_ret = 0;
    PyArg_Parse(p_ret, "i", &i_ret);
    return i_ret;
}
