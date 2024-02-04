//
// Created by Isai Gordeev on 08/01/2024.
//

// #include <Python.h>
// #include <stdio.h>

// PyMODINIT_FUNC PyInit_src() {
//     printf("Hi\n");
//     return NULL;
// }

// hello.cpp
#include <Python.h>

// Simple "Hello, World!" function
static PyObject* hello_world(PyObject* self, PyObject* args) {
    // Print "Hello, World!" to the console
    printf("Hello, World!\n");

    // Return None
    // Py_RETURN_NONE;
    return NULL;
}

// Method mapping for the module
static PyMethodDef methods[] = {
    {"hello_world", hello_world, METH_NOARGS, "Print 'Hello, World!'"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "hello",     // Module name
    NULL,        // Module documentation
    -1,          // Size of per-interpreter state, or -1 if the module keeps state in global variables.
    methods      // Method mapping
};

// Module initialization function
PyMODINIT_FUNC PyInit_hello(void) {
    return PyModule_Create(&module);
}

