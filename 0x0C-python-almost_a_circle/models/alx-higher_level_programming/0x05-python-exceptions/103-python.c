#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;
    Py_ssize_t size, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = var_obj->ob_size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", var_obj->ob_alloc);

    for (i = 0; i < size; i++) {
        PyObject *element = list->ob_item[i];
        printf("Element %zd: ", i);

        if (PyBytes_Check(element)) {
            printf("bytes\n");
            print_python_bytes(element);
        } else if (PyFloat_Check(element)) {
            printf("float\n");
            print_python_float(element);
        } else if (PyTuple_Check(element) || PyList_Check(element)) {
            printf("tuple\n");
        } else if (PyLong_Check(element)) {
            printf("int\n");
        } else if (PyUnicode_Check(element)) {
            printf("str\n");
        } else {
            printf("[ERROR] Unknown type\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;
    Py_ssize_t size, i;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = var_obj->ob_size;

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    PyFloatObject *float_obj = (PyFloatObject *)p;
    
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", float_obj->ob_fval);
}

