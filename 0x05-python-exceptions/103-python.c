#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_float - print some basic infor about Python
 * float objects
 * @p: pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	double d;
	char *s = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	d = ((PyFloatObject *)(p))->ob_fval;
	s = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
	fflush(stdout);
}

/**
 * print_python_bytes - print some basic info about Python
 * byte objects
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	size_t i, bytes;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval;
	bytes = PyBytes_Size(p);
	printf("  size: %ld\n", bytes);
	printf("  trying string: %s\n", str);
	if (bytes >= 10)
		bytes = 10;
	else
		bytes++;
	printf("  first %ld bytes: ", bytes);
	for (i = 0; i < bytes - 1; i++)
		printf("%02hhx ", str[i]);
	printf("%02hhx", str[i]);
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_list - print some basic info about Python lists
 * @p: pointer to PyObject p
 */
void print_python_list(PyObject *p)
{
	size_t i, allocated, size;
	const char *dataType;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %li\n", allocated);
	for (i = 0; i < size; i++)
	{
		dataType = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, dataType);
		if (strcmp(dataType, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(dataType, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
	fflush(stdout);}
