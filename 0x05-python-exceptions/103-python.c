#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    const char *type;
    PyListObject *list;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = Py_SIZE(list);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        type = Py_TYPE(list->ob_item[i])->tp_name;
        printf("Element %ld: %s\n", i, type);

        if (strcmp(type, "bytes") == 0) {
            print_python_bytes(list->ob_item[i]);
        } else if (strcmp(type, "float") == 0) {
            print_python_float(list->ob_item[i]);
        }
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    PyBytesObject *bytes;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = Py_SIZE(bytes);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    size = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02hhx%s", bytes->ob_sval[i], (i == size - 1) ? "\n" : " ");
    }
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p) {
    char *buffer;

    fflush(stdout);

    printf("[.] float object info\n");
    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(PyFloat_AS_DOUBLE(p), 'r', 0,
                                    Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);
}
