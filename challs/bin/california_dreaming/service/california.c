#include <Python.h>

// Flag: GCTF{S0m3th1ngs_t3ll1ng_m3_1_must_g0_h0m3}
int pin = 0;

/* Docstrings */
static char module_docstring[] =
    "All the leaves are brown and the sky is gray.";
static char dreams_docstring[] =
    "I've been for a walk on a winter's day.";
static char mama_docstring[] =
    "I'd be safe and warm if I was in L.A.";
static char papa_docstring[] =
    "California dreamin' on such a winter's day. (Takes an md5 digest)";

/* Available functions */
static PyObject *california_dreams(PyObject *self, PyObject *args);
static PyObject *california_mama(PyObject *self, PyObject *args);
static PyObject *california_papa(PyObject *self, PyObject *args);

/* Module specification */
static PyMethodDef module_methods[] = {
    {"dreams", california_dreams, METH_VARARGS, dreams_docstring},
    {"mama", california_mama, METH_VARARGS, mama_docstring},
    {"papa", california_papa, METH_VARARGS, papa_docstring},
    {NULL, NULL, 0, NULL}
};

/* Initialize the module */
PyMODINIT_FUNC initcalifornia(void)
{
    PyObject *m = Py_InitModule3("california", module_methods, module_docstring);
    if (m == NULL)
        return;

}

static PyObject *california_dreams(PyObject *self, PyObject *args)
{
    int correct_pin = 73313;

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "i", &pin))
        return NULL;

    int difference = pin ^ correct_pin;

    if (difference == 0) {
        return Py_True;
    }
    else {
        return Py_False;
    }
}

static PyObject *california_mama(PyObject *self, PyObject *args)
{
    char * pass_phrase;
    char * s = "Sure";
    char * t = "To";
    char * b = "Be";
    char * w = "Wear";
    char * h = "Hair";
    char * i = "In";
    char * y = "Your";
    char * f = "Flowers";

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "s", &pass_phrase))
        return NULL;

    if (strncmp(pass_phrase + 3, s, 4)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 8, t, 2)) {
        return Py_False;
    }
    if (strncmp(pass_phrase, b, 2)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 11, w, 4)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 32, h, 4)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 24, i, 2)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 27, y, 4)) {
        return Py_False;
    }
    if (strncmp(pass_phrase + 16, f, 7)) {
        return Py_False;
    }

    int count = 0;
    int length = strlen(pass_phrase);
    int j;
    for (j = 0; j < length; j++) {
        if (pass_phrase[j] == ' ') {
            ++count;
        }
    }

    if (count != 7) {
        return Py_False;
    }

    return Py_True;
}

static PyObject *california_papa(PyObject *self, PyObject *args)
{
    char * digest;
    char transform[16];
    char flag[43] = "\xc9\x04\x42\x0c\x0a\xd0\x9c\xc8\xc9\xb6\xe3\x2a\x86\xdf\x03\xdb\xfa\x74\x7a\x26\x40\xed\xcb\xfa\x97\xf1\xd4\x2a\xb7\xd5\x05\xf7\xfa\x18\x71\x7a\x2e\xeb\x9c\xc8\xc9\xbf";

    /* Parse the input tuple */
    if (!PyArg_ParseTuple(args, "s", &digest))
        return NULL;

    int i;
    for (i = 0; i < 16; i++) {
        transform[i] = digest[i] ^ *(((char *) &pin) + (i % 4));
    }

    for (i = 0; i < 42; i++) {
        flag[i] ^= transform[i % 16];
    }

    /* Build the output tuple */
    PyObject *ret = Py_BuildValue("s", flag);
    return ret;
}
