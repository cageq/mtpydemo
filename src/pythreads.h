#pragma once 
#include <Python.h>
 
// acquire GIL
class PyEnsureGilState
{
    public:
        PyEnsureGilState()
        {
            _state = PyGILState_Ensure();
        }

        ~PyEnsureGilState()
        {
            PyGILState_Release(_state);
        }

    private:
        PyGILState_STATE _state;
};


// allow other threads to run
class PyEnableThreads
{
    public:
        PyEnableThreads()
        {
            _state = PyEval_SaveThread();
        }

        ~PyEnableThreads()
        {
            PyEval_RestoreThread(_state);
        }

    private:
        PyThreadState* _state;
};

