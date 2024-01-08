//
// Created by Isai Gordeev on 08/01/2024.
//

#include <Python.h>
#include <stdio.h>

PyMODINIT_FUNC PyInit_src() {
    printf("Hi\n");
    return NULL;
}
