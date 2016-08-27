#pragma once

#include <Python.h>
//该文件定义向Python导出的函数

#include <iostream>
using namespace std;

#include "../log/GPC_SimpleLog.h"
#include "../process/UpdateSystemProcessor.h"
#include "../config/ConfigHelper.h"
#include "../sysmonitor/SystemAdapter.h"

extern "C"
{
    //通知函数，由Python脚本调用
    static PyObject* notify_wrapper(PyObject *self, PyObject *args)
    {
        char *msg;
        if (!PyArg_ParseTuple(args, "s", &msg))
        {
            return NULL;
        }

        cout<<"notify_wrapper:"<<msg<<endl;

        Py_IncRef(Py_None);
        return Py_None;
    };

    //测试由脚本获取C++中的值
    static PyObject* get_string_wrapper(PyObject *self, PyObject *args)
    {
        return Py_BuildValue("s", "get_string_wrapper");
    };

    static PyObject* get_backup_path_wrapper(PyObject *self, PyObject *args)
    {
        string t_backup_path = CConfigHelper::instance().get_app_backup_save_path();
        return Py_BuildValue("s", t_backup_path.c_str());
    };

    static PyObject* get_app_path_wrapper(PyObject *self, PyObject *args)
    {
        string t_app_path = CConfigHelper::instance().get_app_exe_path();
        return Py_BuildValue("s", t_app_path.c_str());
    };

    static PyObject* start_app_by_name_wrapper(PyObject *self, PyObject *args)
    {
        char *app_path = NULL;
        char *app_name = NULL;
        if (!PyArg_ParseTuple(args, "ss", &app_path, &app_name))
        {
            return NULL;
        }

        int i_result = CSystemAdapter::start_process_by_name(string(app_path), string(app_name));
        return Py_BuildValue("i", i_result);
    }

    static PyObject* stop_app_by_name_wrapper(PyObject *self, PyObject *args)
    {
        char *app_path = NULL;
        char *app_name = NULL;
        if (!PyArg_ParseTuple(args, "ss", &app_path, &app_name))
        {
            return NULL;
        }

        int i_result = CSystemAdapter::stop_process_by_name(string(app_path), string(app_name));
        return Py_BuildValue("i", i_result);
    }

    //通知处理进度的信息
    static PyObject* notify_progress_wrapper(PyObject *self, PyObject *args)
    {
        int i_progress_type = 0;
        int i_cur_progress = 0;
        int i_total_progress = 0;
        if (!PyArg_ParseTuple(args, "iii", &i_progress_type, &i_cur_progress, &i_total_progress))
        {
            return NULL;
        }

        RUN_LOG_PRINT("Python notify progress_info: type=%d, cur=%d, total=%d.  \n", i_progress_type, i_cur_progress, i_total_progress);
        CUpdateSystemProcessor::instance().send_progress_message(i_progress_type, i_cur_progress, i_total_progress);

        return Py_BuildValue("i", 1);
    };

    //通知升级过程中的日志信息
    static PyObject* notify_process_wrapper(PyObject *self, PyObject *args)
    {
        int i_process_type = 0;
        char *log_info = NULL;
        if (!PyArg_ParseTuple(args, "is", &i_process_type, &log_info))
        {
            return NULL;
        }

        string t_log_info(log_info);
        RUN_LOG_PRINT("Python notify process_info: type=%d, log=%s. \n",i_process_type, t_log_info.c_str());
        CUpdateSystemProcessor::instance().send_process_message(i_process_type, t_log_info);

        return Py_BuildValue("i", 1);
    };
};

static PyMethodDef CConvMethods[] = {
    {"notify", notify_wrapper, METH_VARARGS, "notify exp to C++."},
    {"get_string", get_string_wrapper, METH_VARARGS, "get_string_in_C++"},
    {"get_backup_path", get_backup_path_wrapper, METH_VARARGS, "get app backup path in C++"},
    {"get_app_path", get_app_path_wrapper, METH_VARARGS, "get app exe path in C++"},
    {"start_app_by_name", start_app_by_name_wrapper, METH_VARARGS, "start exe in C++"},
    {"stop_app_by_name", stop_app_by_name_wrapper, METH_VARARGS, "stop exe in C++"},
    {"notify_progress", notify_progress_wrapper, METH_VARARGS, "notify progress info"},
    {"notify_process", notify_process_wrapper, METH_VARARGS, "notify process info"},
    {NULL, NULL, 0, NULL}
};
