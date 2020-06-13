r"""Wrapper for libiec61850_common_api.h

Generated with:
/home/user/.local/bin/ctypesgen -l /usr/local/lib/libiec61850.so -I /usr/local/include/libiec61850 src/common/inc/libiec61850_common_api.h src/common/inc/linked_list.h src/iec61850/inc/iec61850_client.h src/iec61850/inc/iec61850_common.h src/iec61850/inc/iec61850_server.h src/iec61850/inc/iec61850_model.h src/iec61850/inc/iec61850_cdc.h src/iec61850/inc/iec61850_dynamic_model.h src/iec61850/inc/iec61850_config_file_parser.h src/mms/inc/mms_value.h src/mms/inc/mms_common.h src/mms/inc/mms_types.h src/mms/inc/mms_type_spec.h src/mms/inc/mms_client_connection.h src/mms/inc/iso_connection_parameters.h -o lib61850.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["/usr/local/lib/libiec61850.so"] = load_library("/usr/local/lib/libiec61850.so")

# 1 libraries
# End libraries

# No modules

enum_anon_20 = c_int# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_NONE = 0# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONNECTION_REJECTED = 1# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONNECTION_LOST = 2# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_TIMEOUT = 3# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_PARSING_RESPONSE = 4# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_HARDWARE_FAULT = 5# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONCLUDE_REJECTED = 6# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_INVALID_ARGUMENTS = 7# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_OUTSTANDING_CALL_LIMIT = 8# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_OTHER = 9# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_VMDSTATE_OTHER = 10# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_APPLICATION_REFERENCE_OTHER = 20# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OTHER = 30# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_INVALID_ADDRESS = 31# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_UNSUPPORTED = 32# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_INCONSISTENT = 33# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_UNDEFINED = 34# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_EXISTS = 35# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_ATTRIBUTE_INCONSISTENT = 36# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_RESOURCE_OTHER = 40# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_RESOURCE_CAPABILITY_UNAVAILABLE = 41# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_OTHER = 50# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_OBJECT_CONSTRAINT_CONFLICT = 55# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_PREEMPT_OTHER = 60# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_TIME_RESOLUTION_OTHER = 70# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OTHER = 80# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_NON_EXISTENT = 81# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_UNSUPPORTED = 82# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_DENIED = 83# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_INVALIDATED = 84# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_VALUE_INVALID = 85# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_TEMPORARILY_UNAVAILABLE = 86# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_OTHER = 90# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_AMBIGUOUS = 91# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_BUSY = 92# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_SYNTAX_ERROR = 93# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_CONTENT_TYPE_INVALID = 94# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_POSITION_INVALID = 95# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_ACCESS_DENIED = 96# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_NON_EXISTENT = 97# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_DUPLICATE_FILENAME = 98# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_INSUFFICIENT_SPACE_IN_FILESTORE = 99# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_OTHER = 100# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNKNOWN_PDU_TYPE = 101# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_INVALID_PDU = 102# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_SERVICE = 103# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_MODIFIER = 104# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_REQUEST_INVALID_ARGUMENT = 105# /usr/local/include/libiec61850/mms_common.h: 103

MmsError = enum_anon_20# /usr/local/include/libiec61850/mms_common.h: 103

enum_anon_21 = c_int# /usr/local/include/libiec61850/mms_common.h: 135

MMS_ARRAY = 0# /usr/local/include/libiec61850/mms_common.h: 135

MMS_STRUCTURE = 1# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BOOLEAN = 2# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BIT_STRING = 3# /usr/local/include/libiec61850/mms_common.h: 135

MMS_INTEGER = 4# /usr/local/include/libiec61850/mms_common.h: 135

MMS_UNSIGNED = 5# /usr/local/include/libiec61850/mms_common.h: 135

MMS_FLOAT = 6# /usr/local/include/libiec61850/mms_common.h: 135

MMS_OCTET_STRING = 7# /usr/local/include/libiec61850/mms_common.h: 135

MMS_VISIBLE_STRING = 8# /usr/local/include/libiec61850/mms_common.h: 135

MMS_GENERALIZED_TIME = 9# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BINARY_TIME = 10# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BCD = 11# /usr/local/include/libiec61850/mms_common.h: 135

MMS_OBJ_ID = 12# /usr/local/include/libiec61850/mms_common.h: 135

MMS_STRING = 13# /usr/local/include/libiec61850/mms_common.h: 135

MMS_UTC_TIME = 14# /usr/local/include/libiec61850/mms_common.h: 135

MMS_DATA_ACCESS_ERROR = 15# /usr/local/include/libiec61850/mms_common.h: 135

MmsType = enum_anon_21# /usr/local/include/libiec61850/mms_common.h: 135

# /usr/local/include/libiec61850/mms_common.h: 137
class struct_sMmsDomain(Structure):
    pass

MmsDomain = struct_sMmsDomain# /usr/local/include/libiec61850/mms_common.h: 137

# /usr/local/include/libiec61850/mms_common.h: 145
class struct_sMmsAccessSpecifier(Structure):
    pass

struct_sMmsAccessSpecifier.__slots__ = [
    'domain',
    'variableName',
    'arrayIndex',
    'componentName',
]
struct_sMmsAccessSpecifier._fields_ = [
    ('domain', POINTER(MmsDomain)),
    ('variableName', String),
    ('arrayIndex', c_int),
    ('componentName', String),
]

MmsAccessSpecifier = struct_sMmsAccessSpecifier# /usr/local/include/libiec61850/mms_common.h: 145

# /usr/local/include/libiec61850/mms_common.h: 153
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'domainId',
    'itemId',
    'arrayIndex',
    'componentName',
]
struct_anon_22._fields_ = [
    ('domainId', String),
    ('itemId', String),
    ('arrayIndex', c_int32),
    ('componentName', String),
]

MmsVariableAccessSpecification = struct_anon_22# /usr/local/include/libiec61850/mms_common.h: 153

# /usr/local/include/libiec61850/mms_common.h: 155
class struct_sMmsNamedVariableList(Structure):
    pass

MmsNamedVariableList = POINTER(struct_sMmsNamedVariableList)# /usr/local/include/libiec61850/mms_common.h: 155

MmsNamedVariableListEntry = POINTER(struct_sMmsAccessSpecifier)# /usr/local/include/libiec61850/mms_common.h: 156

# /usr/local/include/libiec61850/mms_common.h: 164
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'arc',
    'arcCount',
]
struct_anon_23._fields_ = [
    ('arc', c_uint16 * int(10)),
    ('arcCount', c_int),
]

ItuObjectIdentifier = struct_anon_23# /usr/local/include/libiec61850/mms_common.h: 164

# /usr/local/include/libiec61850/mms_common.h: 172
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'apTitle',
    'aeQualifier',
]
struct_anon_24._fields_ = [
    ('apTitle', ItuObjectIdentifier),
    ('aeQualifier', c_int),
]

IsoApplicationReference = struct_anon_24# /usr/local/include/libiec61850/mms_common.h: 172

enum_anon_25 = c_int# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_NO_RESPONSE = 0# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_OK = (MMS_VALUE_NO_RESPONSE + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_ACCESS_DENIED = (MMS_VALUE_OK + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_VALUE_INVALID = (MMS_VALUE_ACCESS_DENIED + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_TEMPORARILY_UNAVAILABLE = (MMS_VALUE_VALUE_INVALID + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_OBJECT_ACCESS_UNSUPPORTED = (MMS_VALUE_TEMPORARILY_UNAVAILABLE + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MmsValueIndication = enum_anon_25# /usr/local/include/libiec61850/mms_types.h: 36

# /usr/local/include/libiec61850/mms_types.h: 50
class struct_sMmsVariableSpecification(Structure):
    pass

MmsVariableSpecification = struct_sMmsVariableSpecification# /usr/local/include/libiec61850/mms_types.h: 46

# /usr/local/include/libiec61850/mms_types.h: 55
class struct_sMmsArray(Structure):
    pass

struct_sMmsArray.__slots__ = [
    'elementCount',
    'elementTypeSpec',
]
struct_sMmsArray._fields_ = [
    ('elementCount', c_int),
    ('elementTypeSpec', POINTER(MmsVariableSpecification)),
]

# /usr/local/include/libiec61850/mms_types.h: 59
class struct_sMmsStructure(Structure):
    pass

struct_sMmsStructure.__slots__ = [
    'elementCount',
    'elements',
]
struct_sMmsStructure._fields_ = [
    ('elementCount', c_int),
    ('elements', POINTER(POINTER(MmsVariableSpecification))),
]

# /usr/local/include/libiec61850/mms_types.h: 66
class struct_sMmsFloat(Structure):
    pass

struct_sMmsFloat.__slots__ = [
    'exponentWidth',
    'formatWidth',
]
struct_sMmsFloat._fields_ = [
    ('exponentWidth', c_uint8),
    ('formatWidth', c_uint8),
]

# /usr/local/include/libiec61850/mms_types.h: 53
class union_uMmsTypeSpecification(Union):
    pass

union_uMmsTypeSpecification.__slots__ = [
    'array',
    'structure',
    'boolean',
    'integer',
    'unsignedInteger',
    'floatingpoint',
    'bitString',
    'octetString',
    'visibleString',
    'mmsString',
    'utctime',
    'binaryTime',
]
union_uMmsTypeSpecification._fields_ = [
    ('array', struct_sMmsArray),
    ('structure', struct_sMmsStructure),
    ('boolean', c_int),
    ('integer', c_int),
    ('unsignedInteger', c_int),
    ('floatingpoint', struct_sMmsFloat),
    ('bitString', c_int),
    ('octetString', c_int),
    ('visibleString', c_int),
    ('mmsString', c_int),
    ('utctime', c_int),
    ('binaryTime', c_int),
]

struct_sMmsVariableSpecification.__slots__ = [
    'type',
    'name',
    'typeSpec',
]
struct_sMmsVariableSpecification._fields_ = [
    ('type', MmsType),
    ('name', String),
    ('typeSpec', union_uMmsTypeSpecification),
]

enum_anon_26 = c_int# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_NO_RESPONSE = (-2)# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_SUCCESS = (-1)# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_INVALIDATED = 0# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_HARDWARE_FAULT = 1# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_TEMPORARILY_UNAVAILABLE = 2# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_ACCESS_DENIED = 3# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_UNDEFINED = 4# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_INVALID_ADDRESS = 5# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_TYPE_UNSUPPORTED = 6# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_TYPE_INCONSISTENT = 7# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 8# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_ACCESS_UNSUPPORTED = 9# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_NONE_EXISTENT = 10# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_OBJECT_VALUE_INVALID = 11# /usr/local/include/libiec61850/mms_value.h: 62

DATA_ACCESS_ERROR_UNKNOWN = 12# /usr/local/include/libiec61850/mms_value.h: 62

MmsDataAccessError = enum_anon_26# /usr/local/include/libiec61850/mms_value.h: 62

# /usr/local/include/libiec61850/mms_value.h: 67
class struct_sMmsValue(Structure):
    pass

MmsValue = struct_sMmsValue# /usr/local/include/libiec61850/mms_value.h: 67

# /usr/local/include/libiec61850/mms_value.h: 81
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createArray", "cdecl"):
    MmsValue_createArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createArray", "cdecl")
    MmsValue_createArray.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsValue_createArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 92
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getArraySize", "cdecl"):
    MmsValue_getArraySize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getArraySize", "cdecl")
    MmsValue_getArraySize.argtypes = [POINTER(MmsValue)]
    MmsValue_getArraySize.restype = c_uint32

# /usr/local/include/libiec61850/mms_value.h: 102
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getElement", "cdecl"):
    MmsValue_getElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getElement", "cdecl")
    MmsValue_getElement.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getElement.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createEmptyArray", "cdecl"):
    MmsValue_createEmptyArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createEmptyArray", "cdecl")
    MmsValue_createEmptyArray.argtypes = [c_int]
    MmsValue_createEmptyArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 126
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setElement", "cdecl"):
    MmsValue_setElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setElement", "cdecl")
    MmsValue_setElement.argtypes = [POINTER(MmsValue), c_int, POINTER(MmsValue)]
    MmsValue_setElement.restype = None

# /usr/local/include/libiec61850/mms_value.h: 134
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getDataAccessError", "cdecl"):
    MmsValue_getDataAccessError = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getDataAccessError", "cdecl")
    MmsValue_getDataAccessError.argtypes = [POINTER(MmsValue)]
    MmsValue_getDataAccessError.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_value.h: 144
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toInt64", "cdecl"):
    MmsValue_toInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toInt64", "cdecl")
    MmsValue_toInt64.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt64.restype = c_int64

# /usr/local/include/libiec61850/mms_value.h: 154
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toInt32", "cdecl"):
    MmsValue_toInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toInt32", "cdecl")
    MmsValue_toInt32.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt32.restype = c_int32

# /usr/local/include/libiec61850/mms_value.h: 164
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toUint32", "cdecl"):
    MmsValue_toUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toUint32", "cdecl")
    MmsValue_toUint32.argtypes = [POINTER(MmsValue)]
    MmsValue_toUint32.restype = c_uint32

# /usr/local/include/libiec61850/mms_value.h: 174
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toDouble", "cdecl"):
    MmsValue_toDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toDouble", "cdecl")
    MmsValue_toDouble.argtypes = [POINTER(MmsValue)]
    MmsValue_toDouble.restype = c_double

# /usr/local/include/libiec61850/mms_value.h: 184
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toFloat", "cdecl"):
    MmsValue_toFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toFloat", "cdecl")
    MmsValue_toFloat.argtypes = [POINTER(MmsValue)]
    MmsValue_toFloat.restype = c_float

# /usr/local/include/libiec61850/mms_value.h: 194
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toUnixTimestamp", "cdecl"):
    MmsValue_toUnixTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toUnixTimestamp", "cdecl")
    MmsValue_toUnixTimestamp.argtypes = [POINTER(MmsValue)]
    MmsValue_toUnixTimestamp.restype = c_uint32

# /usr/local/include/libiec61850/mms_value.h: 202
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setFloat", "cdecl"):
    MmsValue_setFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setFloat", "cdecl")
    MmsValue_setFloat.argtypes = [POINTER(MmsValue), c_float]
    MmsValue_setFloat.restype = None

# /usr/local/include/libiec61850/mms_value.h: 210
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDouble", "cdecl"):
    MmsValue_setDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDouble", "cdecl")
    MmsValue_setDouble.argtypes = [POINTER(MmsValue), c_double]
    MmsValue_setDouble.restype = None

# /usr/local/include/libiec61850/mms_value.h: 219
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt8", "cdecl"):
    MmsValue_setInt8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt8", "cdecl")
    MmsValue_setInt8.argtypes = [POINTER(MmsValue), c_int8]
    MmsValue_setInt8.restype = None

# /usr/local/include/libiec61850/mms_value.h: 228
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt16", "cdecl"):
    MmsValue_setInt16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt16", "cdecl")
    MmsValue_setInt16.argtypes = [POINTER(MmsValue), c_int16]
    MmsValue_setInt16.restype = None

# /usr/local/include/libiec61850/mms_value.h: 237
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt32", "cdecl"):
    MmsValue_setInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt32", "cdecl")
    MmsValue_setInt32.argtypes = [POINTER(MmsValue), c_int32]
    MmsValue_setInt32.restype = None

# /usr/local/include/libiec61850/mms_value.h: 246
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt64", "cdecl"):
    MmsValue_setInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt64", "cdecl")
    MmsValue_setInt64.argtypes = [POINTER(MmsValue), c_int64]
    MmsValue_setInt64.restype = None

# /usr/local/include/libiec61850/mms_value.h: 255
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint8", "cdecl"):
    MmsValue_setUint8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint8", "cdecl")
    MmsValue_setUint8.argtypes = [POINTER(MmsValue), c_uint8]
    MmsValue_setUint8.restype = None

# /usr/local/include/libiec61850/mms_value.h: 264
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint16", "cdecl"):
    MmsValue_setUint16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint16", "cdecl")
    MmsValue_setUint16.argtypes = [POINTER(MmsValue), c_uint16]
    MmsValue_setUint16.restype = None

# /usr/local/include/libiec61850/mms_value.h: 273
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint32", "cdecl"):
    MmsValue_setUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint32", "cdecl")
    MmsValue_setUint32.argtypes = [POINTER(MmsValue), c_uint32]
    MmsValue_setUint32.restype = None

# /usr/local/include/libiec61850/mms_value.h: 283
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBoolean", "cdecl"):
    MmsValue_setBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBoolean", "cdecl")
    MmsValue_setBoolean.argtypes = [POINTER(MmsValue), c_bool]
    MmsValue_setBoolean.restype = None

# /usr/local/include/libiec61850/mms_value.h: 292
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBoolean", "cdecl"):
    MmsValue_getBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBoolean", "cdecl")
    MmsValue_getBoolean.argtypes = [POINTER(MmsValue)]
    MmsValue_getBoolean.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toString", "cdecl"):
    MmsValue_toString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toString", "cdecl")
    MmsValue_toString.argtypes = [POINTER(MmsValue)]
    MmsValue_toString.restype = c_char_p

# /usr/local/include/libiec61850/mms_value.h: 312
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getStringSize", "cdecl"):
    MmsValue_getStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getStringSize", "cdecl")
    MmsValue_getStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getStringSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 315
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setVisibleString", "cdecl"):
    MmsValue_setVisibleString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setVisibleString", "cdecl")
    MmsValue_setVisibleString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setVisibleString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 327
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringBit", "cdecl"):
    MmsValue_setBitStringBit = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringBit", "cdecl")
    MmsValue_setBitStringBit.argtypes = [POINTER(MmsValue), c_int, c_bool]
    MmsValue_setBitStringBit.restype = None

# /usr/local/include/libiec61850/mms_value.h: 338
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringBit", "cdecl"):
    MmsValue_getBitStringBit = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringBit", "cdecl")
    MmsValue_getBitStringBit.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getBitStringBit.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 346
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_deleteAllBitStringBits", "cdecl"):
    MmsValue_deleteAllBitStringBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_deleteAllBitStringBits", "cdecl")
    MmsValue_deleteAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteAllBitStringBits.restype = None

# /usr/local/include/libiec61850/mms_value.h: 355
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringSize", "cdecl"):
    MmsValue_getBitStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringSize", "cdecl")
    MmsValue_getBitStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 363
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringByteSize", "cdecl"):
    MmsValue_getBitStringByteSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringByteSize", "cdecl")
    MmsValue_getBitStringByteSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringByteSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 371
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getNumberOfSetBits", "cdecl"):
    MmsValue_getNumberOfSetBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getNumberOfSetBits", "cdecl")
    MmsValue_getNumberOfSetBits.argtypes = [POINTER(MmsValue)]
    MmsValue_getNumberOfSetBits.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 379
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setAllBitStringBits", "cdecl"):
    MmsValue_setAllBitStringBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setAllBitStringBits", "cdecl")
    MmsValue_setAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_setAllBitStringBits.restype = None

# /usr/local/include/libiec61850/mms_value.h: 390
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringAsInteger", "cdecl"):
    MmsValue_getBitStringAsInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringAsInteger", "cdecl")
    MmsValue_getBitStringAsInteger.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsInteger.restype = c_uint32

# /usr/local/include/libiec61850/mms_value.h: 402
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringFromInteger", "cdecl"):
    MmsValue_setBitStringFromInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringFromInteger", "cdecl")
    MmsValue_setBitStringFromInteger.argtypes = [POINTER(MmsValue), c_uint32]
    MmsValue_setBitStringFromInteger.restype = None

# /usr/local/include/libiec61850/mms_value.h: 413
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringAsIntegerBigEndian", "cdecl"):
    MmsValue_getBitStringAsIntegerBigEndian = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringAsIntegerBigEndian", "cdecl")
    MmsValue_getBitStringAsIntegerBigEndian.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsIntegerBigEndian.restype = c_uint32

# /usr/local/include/libiec61850/mms_value.h: 425
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringFromIntegerBigEndian", "cdecl"):
    MmsValue_setBitStringFromIntegerBigEndian = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringFromIntegerBigEndian", "cdecl")
    MmsValue_setBitStringFromIntegerBigEndian.argtypes = [POINTER(MmsValue), c_uint32]
    MmsValue_setBitStringFromIntegerBigEndian.restype = None

# /usr/local/include/libiec61850/mms_value.h: 433
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTime", "cdecl"):
    MmsValue_setUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTime", "cdecl")
    MmsValue_setUtcTime.argtypes = [POINTER(MmsValue), c_uint32]
    MmsValue_setUtcTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 442
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeMs", "cdecl"):
    MmsValue_setUtcTimeMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeMs", "cdecl")
    MmsValue_setUtcTimeMs.argtypes = [POINTER(MmsValue), c_uint64]
    MmsValue_setUtcTimeMs.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 454
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeByBuffer", "cdecl"):
    MmsValue_setUtcTimeByBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeByBuffer", "cdecl")
    MmsValue_setUtcTimeByBuffer.argtypes = [POINTER(MmsValue), POINTER(c_uint8)]
    MmsValue_setUtcTimeByBuffer.restype = None

# /usr/local/include/libiec61850/mms_value.h: 465
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeBuffer", "cdecl"):
    MmsValue_getUtcTimeBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeBuffer", "cdecl")
    MmsValue_getUtcTimeBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeBuffer.restype = POINTER(c_uint8)

# /usr/local/include/libiec61850/mms_value.h: 476
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeInMs", "cdecl"):
    MmsValue_getUtcTimeInMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeInMs", "cdecl")
    MmsValue_getUtcTimeInMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeInMs.restype = c_uint64

# /usr/local/include/libiec61850/mms_value.h: 487
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeInMsWithUs", "cdecl"):
    MmsValue_getUtcTimeInMsWithUs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeInMsWithUs", "cdecl")
    MmsValue_getUtcTimeInMsWithUs.argtypes = [POINTER(MmsValue), POINTER(c_uint32)]
    MmsValue_getUtcTimeInMsWithUs.restype = c_uint64

# /usr/local/include/libiec61850/mms_value.h: 504
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeQuality", "cdecl"):
    MmsValue_setUtcTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeQuality", "cdecl")
    MmsValue_setUtcTimeQuality.argtypes = [POINTER(MmsValue), c_uint8]
    MmsValue_setUtcTimeQuality.restype = None

# /usr/local/include/libiec61850/mms_value.h: 521
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeQuality", "cdecl"):
    MmsValue_getUtcTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeQuality", "cdecl")
    MmsValue_getUtcTimeQuality.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeQuality.restype = c_uint8

# /usr/local/include/libiec61850/mms_value.h: 530
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBinaryTime", "cdecl"):
    MmsValue_setBinaryTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBinaryTime", "cdecl")
    MmsValue_setBinaryTime.argtypes = [POINTER(MmsValue), c_uint64]
    MmsValue_setBinaryTime.restype = None

# /usr/local/include/libiec61850/mms_value.h: 540
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBinaryTimeAsUtcMs", "cdecl"):
    MmsValue_getBinaryTimeAsUtcMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBinaryTimeAsUtcMs", "cdecl")
    MmsValue_getBinaryTimeAsUtcMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getBinaryTimeAsUtcMs.restype = c_uint64

# /usr/local/include/libiec61850/mms_value.h: 554
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setOctetString", "cdecl"):
    MmsValue_setOctetString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setOctetString", "cdecl")
    MmsValue_setOctetString.argtypes = [POINTER(MmsValue), POINTER(c_uint8), c_int]
    MmsValue_setOctetString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 567
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringSize", "cdecl"):
    MmsValue_getOctetStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringSize", "cdecl")
    MmsValue_getOctetStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringSize.restype = c_uint16

# /usr/local/include/libiec61850/mms_value.h: 580
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringMaxSize", "cdecl"):
    MmsValue_getOctetStringMaxSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringMaxSize", "cdecl")
    MmsValue_getOctetStringMaxSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringMaxSize.restype = c_uint16

# /usr/local/include/libiec61850/mms_value.h: 591
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringBuffer", "cdecl"):
    MmsValue_getOctetStringBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringBuffer", "cdecl")
    MmsValue_getOctetStringBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringBuffer.restype = POINTER(c_uint8)

# /usr/local/include/libiec61850/mms_value.h: 606
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_update", "cdecl"):
    MmsValue_update = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_update", "cdecl")
    MmsValue_update.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_update.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 620
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_equals", "cdecl"):
    MmsValue_equals = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_equals", "cdecl")
    MmsValue_equals.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equals.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 635
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_equalTypes", "cdecl"):
    MmsValue_equalTypes = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_equalTypes", "cdecl")
    MmsValue_equalTypes.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equalTypes.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 642
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDataAccessError", "cdecl"):
    MmsValue_newDataAccessError = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDataAccessError", "cdecl")
    MmsValue_newDataAccessError.argtypes = [MmsDataAccessError]
    MmsValue_newDataAccessError.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 645
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newInteger", "cdecl"):
    MmsValue_newInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newInteger", "cdecl")
    MmsValue_newInteger.argtypes = [c_int]
    MmsValue_newInteger.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 648
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUnsigned", "cdecl"):
    MmsValue_newUnsigned = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUnsigned", "cdecl")
    MmsValue_newUnsigned.argtypes = [c_int]
    MmsValue_newUnsigned.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 651
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBoolean", "cdecl"):
    MmsValue_newBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBoolean", "cdecl")
    MmsValue_newBoolean.argtypes = [c_bool]
    MmsValue_newBoolean.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 661
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBitString", "cdecl"):
    MmsValue_newBitString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBitString", "cdecl")
    MmsValue_newBitString.argtypes = [c_int]
    MmsValue_newBitString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 664
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newOctetString", "cdecl"):
    MmsValue_newOctetString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newOctetString", "cdecl")
    MmsValue_newOctetString.argtypes = [c_int, c_int]
    MmsValue_newOctetString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 667
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newStructure", "cdecl"):
    MmsValue_newStructure = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newStructure", "cdecl")
    MmsValue_newStructure.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newStructure.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 670
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createEmptyStructure", "cdecl"):
    MmsValue_createEmptyStructure = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createEmptyStructure", "cdecl")
    MmsValue_createEmptyStructure.argtypes = [c_int]
    MmsValue_createEmptyStructure.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 673
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDefaultValue", "cdecl"):
    MmsValue_newDefaultValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDefaultValue", "cdecl")
    MmsValue_newDefaultValue.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newDefaultValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 676
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt8", "cdecl"):
    MmsValue_newIntegerFromInt8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt8", "cdecl")
    MmsValue_newIntegerFromInt8.argtypes = [c_int8]
    MmsValue_newIntegerFromInt8.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 679
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt16", "cdecl"):
    MmsValue_newIntegerFromInt16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt16", "cdecl")
    MmsValue_newIntegerFromInt16.argtypes = [c_int16]
    MmsValue_newIntegerFromInt16.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 682
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt32", "cdecl"):
    MmsValue_newIntegerFromInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt32", "cdecl")
    MmsValue_newIntegerFromInt32.argtypes = [c_int32]
    MmsValue_newIntegerFromInt32.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 685
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt64", "cdecl"):
    MmsValue_newIntegerFromInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt64", "cdecl")
    MmsValue_newIntegerFromInt64.argtypes = [c_int64]
    MmsValue_newIntegerFromInt64.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 688
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUnsignedFromUint32", "cdecl"):
    MmsValue_newUnsignedFromUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUnsignedFromUint32", "cdecl")
    MmsValue_newUnsignedFromUint32.argtypes = [c_uint32]
    MmsValue_newUnsignedFromUint32.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 691
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newFloat", "cdecl"):
    MmsValue_newFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newFloat", "cdecl")
    MmsValue_newFloat.argtypes = [c_float]
    MmsValue_newFloat.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 694
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDouble", "cdecl"):
    MmsValue_newDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDouble", "cdecl")
    MmsValue_newDouble.argtypes = [c_double]
    MmsValue_newDouble.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 707
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_clone", "cdecl"):
    MmsValue_clone = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_clone", "cdecl")
    MmsValue_clone.argtypes = [POINTER(MmsValue)]
    MmsValue_clone.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 720
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_cloneToBuffer", "cdecl"):
    MmsValue_cloneToBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_cloneToBuffer", "cdecl")
    MmsValue_cloneToBuffer.argtypes = [POINTER(MmsValue), POINTER(c_uint8)]
    MmsValue_cloneToBuffer.restype = POINTER(c_uint8)

# /usr/local/include/libiec61850/mms_value.h: 734
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getSizeInMemory", "cdecl"):
    MmsValue_getSizeInMemory = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getSizeInMemory", "cdecl")
    MmsValue_getSizeInMemory.argtypes = [POINTER(MmsValue)]
    MmsValue_getSizeInMemory.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 746
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_delete", "cdecl"):
    MmsValue_delete = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_delete", "cdecl")
    MmsValue_delete.argtypes = [POINTER(MmsValue)]
    MmsValue_delete.restype = None

# /usr/local/include/libiec61850/mms_value.h: 761
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_deleteConditional", "cdecl"):
    MmsValue_deleteConditional = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_deleteConditional", "cdecl")
    MmsValue_deleteConditional.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteConditional.restype = None

# /usr/local/include/libiec61850/mms_value.h: 773
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleString", "cdecl"):
    MmsValue_newVisibleString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleString", "cdecl")
    MmsValue_newVisibleString.argtypes = [String]
    MmsValue_newVisibleString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 787
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleStringWithSize", "cdecl"):
    MmsValue_newVisibleStringWithSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleStringWithSize", "cdecl")
    MmsValue_newVisibleStringWithSize.argtypes = [c_int]
    MmsValue_newVisibleStringWithSize.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 801
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsStringWithSize", "cdecl"):
    MmsValue_newMmsStringWithSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsStringWithSize", "cdecl")
    MmsValue_newMmsStringWithSize.argtypes = [c_int]
    MmsValue_newMmsStringWithSize.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 815
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBinaryTime", "cdecl"):
    MmsValue_newBinaryTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBinaryTime", "cdecl")
    MmsValue_newBinaryTime.argtypes = [c_bool]
    MmsValue_newBinaryTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 826
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleStringFromByteArray", "cdecl"):
    MmsValue_newVisibleStringFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleStringFromByteArray", "cdecl")
    MmsValue_newVisibleStringFromByteArray.argtypes = [POINTER(c_uint8), c_int]
    MmsValue_newVisibleStringFromByteArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 837
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsStringFromByteArray", "cdecl"):
    MmsValue_newMmsStringFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsStringFromByteArray", "cdecl")
    MmsValue_newMmsStringFromByteArray.argtypes = [POINTER(c_uint8), c_int]
    MmsValue_newMmsStringFromByteArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 847
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsString", "cdecl"):
    MmsValue_newMmsString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsString", "cdecl")
    MmsValue_newMmsString.argtypes = [String]
    MmsValue_newMmsString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 856
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setMmsString", "cdecl"):
    MmsValue_setMmsString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setMmsString", "cdecl")
    MmsValue_setMmsString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setMmsString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 865
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUtcTime", "cdecl"):
    MmsValue_newUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUtcTime", "cdecl")
    MmsValue_newUtcTime.argtypes = [c_uint32]
    MmsValue_newUtcTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 875
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUtcTimeByMsTime", "cdecl"):
    MmsValue_newUtcTimeByMsTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUtcTimeByMsTime", "cdecl")
    MmsValue_newUtcTimeByMsTime.argtypes = [c_uint64]
    MmsValue_newUtcTimeByMsTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 880
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDeletable", "cdecl"):
    MmsValue_setDeletable = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDeletable", "cdecl")
    MmsValue_setDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletable.restype = None

# /usr/local/include/libiec61850/mms_value.h: 883
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDeletableRecursive", "cdecl"):
    MmsValue_setDeletableRecursive = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDeletableRecursive", "cdecl")
    MmsValue_setDeletableRecursive.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletableRecursive.restype = None

# /usr/local/include/libiec61850/mms_value.h: 897
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_isDeletable", "cdecl"):
    MmsValue_isDeletable = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_isDeletable", "cdecl")
    MmsValue_isDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_isDeletable.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 905
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getType", "cdecl"):
    MmsValue_getType = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getType", "cdecl")
    MmsValue_getType.argtypes = [POINTER(MmsValue)]
    MmsValue_getType.restype = MmsType

# /usr/local/include/libiec61850/mms_value.h: 916
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getSubElement", "cdecl"):
    MmsValue_getSubElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getSubElement", "cdecl")
    MmsValue_getSubElement.argtypes = [POINTER(MmsValue), POINTER(MmsVariableSpecification), String]
    MmsValue_getSubElement.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 926
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getTypeString", "cdecl"):
    MmsValue_getTypeString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getTypeString", "cdecl")
    MmsValue_getTypeString.argtypes = [POINTER(MmsValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsValue_getTypeString.restype = ReturnString
    else:
        MmsValue_getTypeString.restype = String
        MmsValue_getTypeString.errcheck = ReturnString

# /usr/local/include/libiec61850/mms_value.h: 941
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_printToBuffer", "cdecl"):
    MmsValue_printToBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_printToBuffer", "cdecl")
    MmsValue_printToBuffer.argtypes = [POINTER(MmsValue), String, c_int]
    MmsValue_printToBuffer.restype = c_char_p

# /usr/local/include/libiec61850/mms_value.h: 956
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_decodeMmsData", "cdecl"):
    MmsValue_decodeMmsData = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_decodeMmsData", "cdecl")
    MmsValue_decodeMmsData.argtypes = [POINTER(c_uint8), c_int, c_int, POINTER(c_int)]
    MmsValue_decodeMmsData.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 971
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_encodeMmsData", "cdecl"):
    MmsValue_encodeMmsData = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_encodeMmsData", "cdecl")
    MmsValue_encodeMmsData.argtypes = [POINTER(MmsValue), POINTER(c_uint8), c_int, c_bool]
    MmsValue_encodeMmsData.restype = c_int

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 44
class struct_sLinkedList(Structure):
    pass

struct_sLinkedList.__slots__ = [
    'data',
    'next',
]
struct_sLinkedList._fields_ = [
    ('data', POINTER(None)),
    ('next', POINTER(struct_sLinkedList)),
]

LinkedList = POINTER(struct_sLinkedList)# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 52

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 60
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_create", "cdecl"):
    LinkedList_create = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_create", "cdecl")
    LinkedList_create.argtypes = []
    LinkedList_create.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 72
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroy", "cdecl"):
    LinkedList_destroy = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroy", "cdecl")
    LinkedList_destroy.argtypes = [LinkedList]
    LinkedList_destroy.restype = None

LinkedListValueDeleteFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 75

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 89
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroyDeep", "cdecl"):
    LinkedList_destroyDeep = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroyDeep", "cdecl")
    LinkedList_destroyDeep.argtypes = [LinkedList, LinkedListValueDeleteFunction]
    LinkedList_destroyDeep.restype = None

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 100
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroyStatic", "cdecl"):
    LinkedList_destroyStatic = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroyStatic", "cdecl")
    LinkedList_destroyStatic.argtypes = [LinkedList]
    LinkedList_destroyStatic.restype = None

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_add", "cdecl"):
    LinkedList_add = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_add", "cdecl")
    LinkedList_add.argtypes = [LinkedList, POINTER(None)]
    LinkedList_add.restype = None

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 123
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_contains", "cdecl"):
    LinkedList_contains = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_contains", "cdecl")
    LinkedList_contains.argtypes = [LinkedList, POINTER(None)]
    LinkedList_contains.restype = c_bool

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 134
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_remove", "cdecl"):
    LinkedList_remove = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_remove", "cdecl")
    LinkedList_remove.argtypes = [LinkedList, POINTER(None)]
    LinkedList_remove.restype = c_bool

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 143
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_get", "cdecl"):
    LinkedList_get = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_get", "cdecl")
    LinkedList_get.argtypes = [LinkedList, c_int]
    LinkedList_get.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 151
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getNext", "cdecl"):
    LinkedList_getNext = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getNext", "cdecl")
    LinkedList_getNext.argtypes = [LinkedList]
    LinkedList_getNext.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getLastElement", "cdecl"):
    LinkedList_getLastElement = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getLastElement", "cdecl")
    LinkedList_getLastElement.argtypes = [LinkedList]
    LinkedList_getLastElement.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 167
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_insertAfter", "cdecl"):
    LinkedList_insertAfter = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_insertAfter", "cdecl")
    LinkedList_insertAfter.argtypes = [LinkedList, POINTER(None)]
    LinkedList_insertAfter.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 177
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_size", "cdecl"):
    LinkedList_size = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_size", "cdecl")
    LinkedList_size.argtypes = [LinkedList]
    LinkedList_size.restype = c_int

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 179
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getData", "cdecl"):
    LinkedList_getData = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getData", "cdecl")
    LinkedList_getData.argtypes = [LinkedList]
    LinkedList_getData.restype = POINTER(c_ubyte)
    LinkedList_getData.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 183
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_printStringList", "cdecl"):
    LinkedList_printStringList = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_printStringList", "cdecl")
    LinkedList_printStringList.argtypes = [LinkedList]
    LinkedList_printStringList.restype = None

# /usr/local/include/libiec61850/logging_api.h: 78
class struct_sLogStorage(Structure):
    pass

LogStorage = POINTER(struct_sLogStorage)# /usr/local/include/libiec61850/logging_api.h: 50

LogEntryCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_uint64, c_uint64, c_bool)# /usr/local/include/libiec61850/logging_api.h: 62

LogEntryDataCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), String, POINTER(c_uint8), c_int, c_uint8, c_bool)# /usr/local/include/libiec61850/logging_api.h: 76

struct_sLogStorage.__slots__ = [
    'instanceData',
    'maxLogEntries',
    'addEntry',
    'addEntryData',
    'getEntries',
    'getEntriesAfter',
    'getOldestAndNewestEntries',
    'destroy',
]
struct_sLogStorage._fields_ = [
    ('instanceData', POINTER(None)),
    ('maxLogEntries', c_int),
    ('addEntry', CFUNCTYPE(UNCHECKED(c_uint64), LogStorage, c_uint64)),
    ('addEntryData', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, c_uint64, String, POINTER(c_uint8), c_int, c_uint8)),
    ('getEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, c_uint64, c_uint64, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getEntriesAfter', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, c_uint64, c_uint64, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getOldestAndNewestEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, POINTER(c_uint64), POINTER(c_uint64), POINTER(c_uint64), POINTER(c_uint64))),
    ('destroy', CFUNCTYPE(UNCHECKED(None), LogStorage)),
]

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 55
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_anon_27._fields_ = [
    ('vlanPriority', c_uint8),
    ('vlanId', c_uint16),
    ('appId', c_uint16),
    ('dstAddress', c_uint8 * int(6)),
]

PhyComAddress = struct_anon_27# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 55

enum_anon_28 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

CONTROL_MODEL_STATUS_ONLY = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

CONTROL_MODEL_DIRECT_NORMAL = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

CONTROL_MODEL_SBO_NORMAL = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

CONTROL_MODEL_DIRECT_ENHANCED = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

CONTROL_MODEL_SBO_ENHANCED = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

ControlModel = enum_anon_28# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 87

enum_anon_29 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_UNKNOWN = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_NOT_SUPPORTED = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_SWITCHING_HIERARCHY = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_SELECT_FAILED = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_INVALID_POSITION = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_POSITION_REACHED = 5# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_PARAMETER_CHANGE_IN_EXECUTION = 6# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_STEP_LIMIT = 7# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_MODE = 8# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_PROCESS = 9# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_INTERLOCKING = 10# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_SYNCHROCHECK = 11# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_COMMAND_ALREADY_IN_EXECUTION = 12# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_BLOCKED_BY_HEALTH = 13# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_1_OF_N_CONTROL = 14# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ABORTION_BY_CANCEL = 15# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_TIME_LIMIT_OVER = 16# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ABORTION_BY_TRIP = 17# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_OBJECT_NOT_SELECTED = 18# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_OBJECT_ALREADY_SELECTED = 19# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_NO_ACCESS_AUTHORITY = 20# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ENDED_WITH_OVERSHOOT = 21# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ABORTION_DUE_TO_DEVIATION = 22# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ABORTION_BY_COMMUNICATION_LOSS = 23# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_ABORTION_BY_COMMAND = 24# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_NONE = 25# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_INCONSISTENT_PARAMETERS = 26# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ADD_CAUSE_LOCKED_BY_OTHER_CLIENT = 27# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

ControlAddCause = enum_anon_29# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 218

enum_eFunctionalConstraint = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_ST = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_MX = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_SP = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_SV = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_CF = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_DC = 5# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_SG = 6# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_SE = 7# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_SR = 8# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_OR = 9# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_BL = 10# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_EX = 11# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_CO = 12# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_US = 13# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_MS = 14# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_RP = 15# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_BR = 16# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_LG = 17# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_GO = 18# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_ALL = 99# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

IEC61850_FC_NONE = (-1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

FunctionalConstraint = enum_eFunctionalConstraint# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 291

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 296
if _libs["/usr/local/lib/libiec61850.so"].has("FunctionalConstraint_toString", "cdecl"):
    FunctionalConstraint_toString = _libs["/usr/local/lib/libiec61850.so"].get("FunctionalConstraint_toString", "cdecl")
    FunctionalConstraint_toString.argtypes = [FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        FunctionalConstraint_toString.restype = ReturnString
    else:
        FunctionalConstraint_toString.restype = String
        FunctionalConstraint_toString.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 303
if _libs["/usr/local/lib/libiec61850.so"].has("FunctionalConstraint_fromString", "cdecl"):
    FunctionalConstraint_fromString = _libs["/usr/local/lib/libiec61850.so"].get("FunctionalConstraint_fromString", "cdecl")
    FunctionalConstraint_fromString.argtypes = [String]
    FunctionalConstraint_fromString.restype = FunctionalConstraint

Quality = c_uint16# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 314

Validity = c_uint16# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 315

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 340
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_getValidity", "cdecl"):
    Quality_getValidity = _libs["/usr/local/lib/libiec61850.so"].get("Quality_getValidity", "cdecl")
    Quality_getValidity.argtypes = [POINTER(Quality)]
    Quality_getValidity.restype = Validity

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 343
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_setValidity", "cdecl"):
    Quality_setValidity = _libs["/usr/local/lib/libiec61850.so"].get("Quality_setValidity", "cdecl")
    Quality_setValidity.argtypes = [POINTER(Quality), Validity]
    Quality_setValidity.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 346
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_setFlag", "cdecl"):
    Quality_setFlag = _libs["/usr/local/lib/libiec61850.so"].get("Quality_setFlag", "cdecl")
    Quality_setFlag.argtypes = [POINTER(Quality), c_int]
    Quality_setFlag.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 349
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_unsetFlag", "cdecl"):
    Quality_unsetFlag = _libs["/usr/local/lib/libiec61850.so"].get("Quality_unsetFlag", "cdecl")
    Quality_unsetFlag.argtypes = [POINTER(Quality), c_int]
    Quality_unsetFlag.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 352
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_isFlagSet", "cdecl"):
    Quality_isFlagSet = _libs["/usr/local/lib/libiec61850.so"].get("Quality_isFlagSet", "cdecl")
    Quality_isFlagSet.argtypes = [POINTER(Quality), c_int]
    Quality_isFlagSet.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 355
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_fromMmsValue", "cdecl"):
    Quality_fromMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Quality_fromMmsValue", "cdecl")
    Quality_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Quality_fromMmsValue.restype = Quality

enum_anon_30 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

DBPOS_INTERMEDIATE_STATE = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

DBPOS_OFF = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

DBPOS_ON = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

DBPOS_BAD_STATE = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

Dbpos = enum_anon_30# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 370

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 381
if _libs["/usr/local/lib/libiec61850.so"].has("Dbpos_fromMmsValue", "cdecl"):
    Dbpos_fromMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Dbpos_fromMmsValue", "cdecl")
    Dbpos_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Dbpos_fromMmsValue.restype = Dbpos

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 391
if _libs["/usr/local/lib/libiec61850.so"].has("Dbpos_toMmsValue", "cdecl"):
    Dbpos_toMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Dbpos_toMmsValue", "cdecl")
    Dbpos_toMmsValue.argtypes = [POINTER(MmsValue), Dbpos]
    Dbpos_toMmsValue.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 404
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'val',
]
union_anon_31._fields_ = [
    ('val', c_uint8 * int(8)),
]

Timestamp = union_anon_31# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 404

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 406
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_create", "cdecl"):
    Timestamp_create = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_create", "cdecl")
    Timestamp_create.argtypes = []
    Timestamp_create.restype = POINTER(Timestamp)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 409
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_createFromByteArray", "cdecl"):
    Timestamp_createFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_createFromByteArray", "cdecl")
    Timestamp_createFromByteArray.argtypes = [POINTER(c_uint8)]
    Timestamp_createFromByteArray.restype = POINTER(Timestamp)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 413
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_destroy", "cdecl"):
    Timestamp_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_destroy", "cdecl")
    Timestamp_destroy.argtypes = [POINTER(Timestamp)]
    Timestamp_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 416
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_clearFlags", "cdecl"):
    Timestamp_clearFlags = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_clearFlags", "cdecl")
    Timestamp_clearFlags.argtypes = [POINTER(Timestamp)]
    Timestamp_clearFlags.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 419
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getTimeInSeconds", "cdecl"):
    Timestamp_getTimeInSeconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getTimeInSeconds", "cdecl")
    Timestamp_getTimeInSeconds.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInSeconds.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 422
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getTimeInMs", "cdecl"):
    Timestamp_getTimeInMs = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getTimeInMs", "cdecl")
    Timestamp_getTimeInMs.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInMs.restype = c_uint64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 425
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_isLeapSecondKnown", "cdecl"):
    Timestamp_isLeapSecondKnown = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_isLeapSecondKnown", "cdecl")
    Timestamp_isLeapSecondKnown.argtypes = [POINTER(Timestamp)]
    Timestamp_isLeapSecondKnown.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 428
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setLeapSecondKnown", "cdecl"):
    Timestamp_setLeapSecondKnown = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setLeapSecondKnown", "cdecl")
    Timestamp_setLeapSecondKnown.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setLeapSecondKnown.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 431
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_hasClockFailure", "cdecl"):
    Timestamp_hasClockFailure = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_hasClockFailure", "cdecl")
    Timestamp_hasClockFailure.argtypes = [POINTER(Timestamp)]
    Timestamp_hasClockFailure.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 434
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setClockFailure", "cdecl"):
    Timestamp_setClockFailure = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setClockFailure", "cdecl")
    Timestamp_setClockFailure.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockFailure.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 437
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_isClockNotSynchronized", "cdecl"):
    Timestamp_isClockNotSynchronized = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_isClockNotSynchronized", "cdecl")
    Timestamp_isClockNotSynchronized.argtypes = [POINTER(Timestamp)]
    Timestamp_isClockNotSynchronized.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 440
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setClockNotSynchronized", "cdecl"):
    Timestamp_setClockNotSynchronized = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setClockNotSynchronized", "cdecl")
    Timestamp_setClockNotSynchronized.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockNotSynchronized.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 443
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getSubsecondPrecision", "cdecl"):
    Timestamp_getSubsecondPrecision = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getSubsecondPrecision", "cdecl")
    Timestamp_getSubsecondPrecision.argtypes = [POINTER(Timestamp)]
    Timestamp_getSubsecondPrecision.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 451
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setSubsecondPrecision", "cdecl"):
    Timestamp_setSubsecondPrecision = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setSubsecondPrecision", "cdecl")
    Timestamp_setSubsecondPrecision.argtypes = [POINTER(Timestamp), c_int]
    Timestamp_setSubsecondPrecision.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 454
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setTimeInSeconds", "cdecl"):
    Timestamp_setTimeInSeconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setTimeInSeconds", "cdecl")
    Timestamp_setTimeInSeconds.argtypes = [POINTER(Timestamp), c_uint32]
    Timestamp_setTimeInSeconds.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 457
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setTimeInMilliseconds", "cdecl"):
    Timestamp_setTimeInMilliseconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setTimeInMilliseconds", "cdecl")
    Timestamp_setTimeInMilliseconds.argtypes = [POINTER(Timestamp), c_uint64]
    Timestamp_setTimeInMilliseconds.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 460
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setByMmsUtcTime", "cdecl"):
    Timestamp_setByMmsUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setByMmsUtcTime", "cdecl")
    Timestamp_setByMmsUtcTime.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_setByMmsUtcTime.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 468
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_toMmsValue", "cdecl"):
    Timestamp_toMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_toMmsValue", "cdecl")
    Timestamp_toMmsValue.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_toMmsValue.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 476
if _libs["/usr/local/lib/libiec61850.so"].has("LibIEC61850_getVersionString", "cdecl"):
    LibIEC61850_getVersionString = _libs["/usr/local/lib/libiec61850.so"].get("LibIEC61850_getVersionString", "cdecl")
    LibIEC61850_getVersionString.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        LibIEC61850_getVersionString.restype = ReturnString
    else:
        LibIEC61850_getVersionString.restype = String
        LibIEC61850_getVersionString.errcheck = ReturnString

# /usr/local/include/libiec61850/mms_type_spec.h: 56
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_destroy", "cdecl"):
    MmsVariableSpecification_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_destroy", "cdecl")
    MmsVariableSpecification_destroy.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_destroy.restype = None

# /usr/local/include/libiec61850/mms_type_spec.h: 71
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildValue", "cdecl"):
    MmsVariableSpecification_getChildValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildValue", "cdecl")
    MmsVariableSpecification_getChildValue.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue), String]
    MmsVariableSpecification_getChildValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_type_spec.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getNamedVariableRecursive", "cdecl"):
    MmsVariableSpecification_getNamedVariableRecursive = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getNamedVariableRecursive", "cdecl")
    MmsVariableSpecification_getNamedVariableRecursive.argtypes = [POINTER(MmsVariableSpecification), String]
    MmsVariableSpecification_getNamedVariableRecursive.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 93
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getType", "cdecl"):
    MmsVariableSpecification_getType = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getType", "cdecl")
    MmsVariableSpecification_getType.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getType.restype = MmsType

# /usr/local/include/libiec61850/mms_type_spec.h: 104
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_isValueOfType", "cdecl"):
    MmsVariableSpecification_isValueOfType = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_isValueOfType", "cdecl")
    MmsVariableSpecification_isValueOfType.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue)]
    MmsVariableSpecification_isValueOfType.restype = c_bool

# /usr/local/include/libiec61850/mms_type_spec.h: 116
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getName", "cdecl"):
    MmsVariableSpecification_getName = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getName", "cdecl")
    MmsVariableSpecification_getName.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getName.restype = c_char_p

# /usr/local/include/libiec61850/mms_type_spec.h: 120
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getStructureElements", "cdecl"):
    MmsVariableSpecification_getStructureElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getStructureElements", "cdecl")
    MmsVariableSpecification_getStructureElements.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getStructureElements.restype = LinkedList

# /usr/local/include/libiec61850/mms_type_spec.h: 133
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getSize", "cdecl"):
    MmsVariableSpecification_getSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getSize", "cdecl")
    MmsVariableSpecification_getSize.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getSize.restype = c_int

# /usr/local/include/libiec61850/mms_type_spec.h: 135
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByIndex = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl")
    MmsVariableSpecification_getChildSpecificationByIndex.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsVariableSpecification_getChildSpecificationByIndex.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 147
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByName", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByName = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByName", "cdecl")
    MmsVariableSpecification_getChildSpecificationByName.argtypes = [POINTER(MmsVariableSpecification), String, POINTER(c_int)]
    MmsVariableSpecification_getChildSpecificationByName.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 150
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getArrayElementSpecification", "cdecl"):
    MmsVariableSpecification_getArrayElementSpecification = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getArrayElementSpecification", "cdecl")
    MmsVariableSpecification_getArrayElementSpecification.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getArrayElementSpecification.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 154
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getExponentWidth", "cdecl"):
    MmsVariableSpecification_getExponentWidth = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getExponentWidth", "cdecl")
    MmsVariableSpecification_getExponentWidth.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getExponentWidth.restype = c_int

# /usr/local/include/libiec61850/tls_config.h: 37
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# /usr/local/include/libiec61850/tls_config.h: 37

enum_anon_32 = c_int# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_NONE = 0# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_PASSWORD = 1# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_CERTIFICATE = 2# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_TLS = 3# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

AcseAuthenticationMechanism = enum_anon_32# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

# /usr/local/include/libiec61850/iso_connection_parameters.h: 60
class struct_sAcseAuthenticationParameter(Structure):
    pass

AcseAuthenticationParameter = POINTER(struct_sAcseAuthenticationParameter)# /usr/local/include/libiec61850/iso_connection_parameters.h: 58

# /usr/local/include/libiec61850/iso_connection_parameters.h: 66
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'octetString',
    'passwordLength',
]
struct_anon_33._fields_ = [
    ('octetString', POINTER(c_uint8)),
    ('passwordLength', c_int),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 72
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'buf',
    'length',
]
struct_anon_34._fields_ = [
    ('buf', POINTER(c_uint8)),
    ('length', c_int),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 64
class union_anon_35(Union):
    pass

union_anon_35.__slots__ = [
    'password',
    'certificate',
]
union_anon_35._fields_ = [
    ('password', struct_anon_33),
    ('certificate', struct_anon_34),
]

struct_sAcseAuthenticationParameter.__slots__ = [
    'mechanism',
    'value',
]
struct_sAcseAuthenticationParameter._fields_ = [
    ('mechanism', AcseAuthenticationMechanism),
    ('value', union_anon_35),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_create", "cdecl"):
    AcseAuthenticationParameter_create = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_create", "cdecl")
    AcseAuthenticationParameter_create.argtypes = []
    AcseAuthenticationParameter_create.restype = AcseAuthenticationParameter

# /usr/local/include/libiec61850/iso_connection_parameters.h: 85
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_destroy", "cdecl"):
    AcseAuthenticationParameter_destroy = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_destroy", "cdecl")
    AcseAuthenticationParameter_destroy.argtypes = [AcseAuthenticationParameter]
    AcseAuthenticationParameter_destroy.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 88
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_setAuthMechanism", "cdecl"):
    AcseAuthenticationParameter_setAuthMechanism = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_setAuthMechanism", "cdecl")
    AcseAuthenticationParameter_setAuthMechanism.argtypes = [AcseAuthenticationParameter, AcseAuthenticationMechanism]
    AcseAuthenticationParameter_setAuthMechanism.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_setPassword", "cdecl"):
    AcseAuthenticationParameter_setPassword = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_setPassword", "cdecl")
    AcseAuthenticationParameter_setPassword.argtypes = [AcseAuthenticationParameter, String]
    AcseAuthenticationParameter_setPassword.restype = None

AcseAuthenticator = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), AcseAuthenticationParameter, POINTER(POINTER(None)), POINTER(IsoApplicationReference))# /usr/local/include/libiec61850/iso_connection_parameters.h: 105

# /usr/local/include/libiec61850/iso_connection_parameters.h: 115
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'size',
    'value',
]
struct_anon_36._fields_ = [
    ('size', c_uint8),
    ('value', c_uint8 * int(4)),
]

TSelector = struct_anon_36# /usr/local/include/libiec61850/iso_connection_parameters.h: 115

# /usr/local/include/libiec61850/iso_connection_parameters.h: 125
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'size',
    'value',
]
struct_anon_37._fields_ = [
    ('size', c_uint8),
    ('value', c_uint8 * int(16)),
]

SSelector = struct_anon_37# /usr/local/include/libiec61850/iso_connection_parameters.h: 125

# /usr/local/include/libiec61850/iso_connection_parameters.h: 135
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'size',
    'value',
]
struct_anon_38._fields_ = [
    ('size', c_uint8),
    ('value', c_uint8 * int(16)),
]

PSelector = struct_anon_38# /usr/local/include/libiec61850/iso_connection_parameters.h: 135

# /usr/local/include/libiec61850/iso_connection_parameters.h: 137
class struct_sIsoConnectionParameters(Structure):
    pass

struct_sIsoConnectionParameters.__slots__ = [
    'acseAuthParameter',
    'hostname',
    'tcpPort',
    'remoteApTitle',
    'remoteApTitleLen',
    'remoteAEQualifier',
    'remotePSelector',
    'remoteSSelector',
    'remoteTSelector',
    'localApTitle',
    'localApTitleLen',
    'localAEQualifier',
    'localPSelector',
    'localSSelector',
    'localTSelector',
]
struct_sIsoConnectionParameters._fields_ = [
    ('acseAuthParameter', AcseAuthenticationParameter),
    ('hostname', String),
    ('tcpPort', c_int),
    ('remoteApTitle', c_uint8 * int(10)),
    ('remoteApTitleLen', c_int),
    ('remoteAEQualifier', c_int),
    ('remotePSelector', PSelector),
    ('remoteSSelector', SSelector),
    ('remoteTSelector', TSelector),
    ('localApTitle', c_uint8 * int(10)),
    ('localApTitleLen', c_int),
    ('localAEQualifier', c_int),
    ('localPSelector', PSelector),
    ('localSSelector', SSelector),
    ('localTSelector', TSelector),
]

IsoConnectionParameters = POINTER(struct_sIsoConnectionParameters)# /usr/local/include/libiec61850/iso_connection_parameters.h: 165

# /usr/local/include/libiec61850/iso_connection_parameters.h: 176
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_create", "cdecl"):
    IsoConnectionParameters_create = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_create", "cdecl")
    IsoConnectionParameters_create.argtypes = []
    IsoConnectionParameters_create.restype = IsoConnectionParameters

# /usr/local/include/libiec61850/iso_connection_parameters.h: 187
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_destroy", "cdecl"):
    IsoConnectionParameters_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_destroy", "cdecl")
    IsoConnectionParameters_destroy.argtypes = [IsoConnectionParameters]
    IsoConnectionParameters_destroy.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 191
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setTlsConfiguration", "cdecl"):
    IsoConnectionParameters_setTlsConfiguration = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setTlsConfiguration", "cdecl")
    IsoConnectionParameters_setTlsConfiguration.argtypes = [IsoConnectionParameters, TLSConfiguration]
    IsoConnectionParameters_setTlsConfiguration.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 202
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl"):
    IsoConnectionParameters_setAcseAuthenticationParameter = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl")
    IsoConnectionParameters_setAcseAuthenticationParameter.argtypes = [IsoConnectionParameters, AcseAuthenticationParameter]
    IsoConnectionParameters_setAcseAuthenticationParameter.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 216
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setTcpParameters", "cdecl"):
    IsoConnectionParameters_setTcpParameters = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setTcpParameters", "cdecl")
    IsoConnectionParameters_setTcpParameters.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setTcpParameters.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 231
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setRemoteApTitle", "cdecl"):
    IsoConnectionParameters_setRemoteApTitle = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setRemoteApTitle", "cdecl")
    IsoConnectionParameters_setRemoteApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setRemoteApTitle.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 246
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setRemoteAddresses", "cdecl"):
    IsoConnectionParameters_setRemoteAddresses = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setRemoteAddresses", "cdecl")
    IsoConnectionParameters_setRemoteAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setRemoteAddresses.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 261
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setLocalApTitle", "cdecl"):
    IsoConnectionParameters_setLocalApTitle = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setLocalApTitle", "cdecl")
    IsoConnectionParameters_setLocalApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setLocalApTitle.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 276
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setLocalAddresses", "cdecl"):
    IsoConnectionParameters_setLocalAddresses = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setLocalAddresses", "cdecl")
    IsoConnectionParameters_setLocalAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setLocalAddresses.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 54
class struct_sMmsConnectionParameters(Structure):
    pass

struct_sMmsConnectionParameters.__slots__ = [
    'maxServOutstandingCalling',
    'maxServOutstandingCalled',
    'dataStructureNestingLevel',
    'maxPduSize',
    'servicesSupported',
]
struct_sMmsConnectionParameters._fields_ = [
    ('maxServOutstandingCalling', c_int),
    ('maxServOutstandingCalled', c_int),
    ('dataStructureNestingLevel', c_int),
    ('maxPduSize', c_int),
    ('servicesSupported', c_uint8 * int(11)),
]

MmsConnectionParameters = struct_sMmsConnectionParameters# /usr/local/include/libiec61850/mms_client_connection.h: 54

# /usr/local/include/libiec61850/mms_client_connection.h: 60
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'vendorName',
    'modelName',
    'revision',
]
struct_anon_39._fields_ = [
    ('vendorName', String),
    ('modelName', String),
    ('revision', String),
]

MmsServerIdentity = struct_anon_39# /usr/local/include/libiec61850/mms_client_connection.h: 60

enum_anon_40 = c_int# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSED = 0# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTING = (MMS_CONNECTION_STATE_CLOSED + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTED = (MMS_CONNECTION_STATE_CONNECTING + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSING = (MMS_CONNECTION_STATE_CONNECTED + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MmsConnectionState = enum_anon_40# /usr/local/include/libiec61850/mms_client_connection.h: 67

MmsInformationReportHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, String, POINTER(MmsValue), c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 69

# /usr/local/include/libiec61850/mms_client_connection.h: 75
class struct_sMmsConnection(Structure):
    pass

MmsConnection = POINTER(struct_sMmsConnection)# /usr/local/include/libiec61850/mms_client_connection.h: 75

# /usr/local/include/libiec61850/mms_client_connection.h: 88
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_create", "cdecl"):
    MmsConnection_create = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_create", "cdecl")
    MmsConnection_create.argtypes = []
    MmsConnection_create.restype = MmsConnection

# /usr/local/include/libiec61850/mms_client_connection.h: 98
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_createSecure", "cdecl"):
    MmsConnection_createSecure = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_createSecure", "cdecl")
    MmsConnection_createSecure.argtypes = [TLSConfiguration]
    MmsConnection_createSecure.restype = MmsConnection

# /usr/local/include/libiec61850/mms_client_connection.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_createNonThreaded", "cdecl"):
    MmsConnection_createNonThreaded = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_createNonThreaded", "cdecl")
    MmsConnection_createNonThreaded.argtypes = [TLSConfiguration]
    MmsConnection_createNonThreaded.restype = MmsConnection

MmsRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(c_uint8), c_int, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 125

# /usr/local/include/libiec61850/mms_client_connection.h: 139
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setRawMessageHandler", "cdecl"):
    MmsConnection_setRawMessageHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setRawMessageHandler", "cdecl")
    MmsConnection_setRawMessageHandler.argtypes = [MmsConnection, MmsRawMessageHandler, POINTER(None)]
    MmsConnection_setRawMessageHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 152
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setFilestoreBasepath", "cdecl"):
    MmsConnection_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setFilestoreBasepath", "cdecl")
    MmsConnection_setFilestoreBasepath.argtypes = [MmsConnection, String]
    MmsConnection_setFilestoreBasepath.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 161
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setRequestTimeout", "cdecl"):
    MmsConnection_setRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setRequestTimeout", "cdecl")
    MmsConnection_setRequestTimeout.argtypes = [MmsConnection, c_uint32]
    MmsConnection_setRequestTimeout.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 171
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getRequestTimeout", "cdecl"):
    MmsConnection_getRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getRequestTimeout", "cdecl")
    MmsConnection_getRequestTimeout.argtypes = [MmsConnection]
    MmsConnection_getRequestTimeout.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 180
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectTimeout", "cdecl"):
    MmsConnection_setConnectTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectTimeout", "cdecl")
    MmsConnection_setConnectTimeout.argtypes = [MmsConnection, c_uint32]
    MmsConnection_setConnectTimeout.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 194
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setInformationReportHandler", "cdecl"):
    MmsConnection_setInformationReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setInformationReportHandler", "cdecl")
    MmsConnection_setInformationReportHandler.argtypes = [MmsConnection, MmsInformationReportHandler, POINTER(None)]
    MmsConnection_setInformationReportHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getIsoConnectionParameters", "cdecl"):
    MmsConnection_getIsoConnectionParameters = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getIsoConnectionParameters", "cdecl")
    MmsConnection_getIsoConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getIsoConnectionParameters.restype = IsoConnectionParameters

# /usr/local/include/libiec61850/mms_client_connection.h: 213
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getMmsConnectionParameters", "cdecl"):
    MmsConnection_getMmsConnectionParameters = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getMmsConnectionParameters", "cdecl")
    MmsConnection_getMmsConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getMmsConnectionParameters.restype = MmsConnectionParameters

MmsConnectionStateChangedHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None), MmsConnectionState)# /usr/local/include/libiec61850/mms_client_connection.h: 215

# /usr/local/include/libiec61850/mms_client_connection.h: 218
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectionStateChangedHandler", "cdecl"):
    MmsConnection_setConnectionStateChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectionStateChangedHandler", "cdecl")
    MmsConnection_setConnectionStateChangedHandler.argtypes = [MmsConnection, MmsConnectionStateChangedHandler, POINTER(None)]
    MmsConnection_setConnectionStateChangedHandler.restype = None

MmsConnectionLostHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None))# /usr/local/include/libiec61850/mms_client_connection.h: 226

# /usr/local/include/libiec61850/mms_client_connection.h: 235
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectionLostHandler", "cdecl"):
    MmsConnection_setConnectionLostHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectionLostHandler", "cdecl")
    MmsConnection_setConnectionLostHandler.argtypes = [MmsConnection, MmsConnectionLostHandler, POINTER(None)]
    MmsConnection_setConnectionLostHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 244
for _lib in _libs.values():
    if not _lib.has("MmsConnection_setIsoConnectionParameters", "cdecl"):
        continue
    MmsConnection_setIsoConnectionParameters = _lib.get("MmsConnection_setIsoConnectionParameters", "cdecl")
    MmsConnection_setIsoConnectionParameters.argtypes = [MmsConnection, POINTER(IsoConnectionParameters)]
    MmsConnection_setIsoConnectionParameters.restype = None
    break

# /usr/local/include/libiec61850/mms_client_connection.h: 252
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_destroy", "cdecl"):
    MmsConnection_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_destroy", "cdecl")
    MmsConnection_destroy.argtypes = [MmsConnection]
    MmsConnection_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 272
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_connect", "cdecl"):
    MmsConnection_connect = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_connect", "cdecl")
    MmsConnection_connect.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connect.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 275
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_connectAsync", "cdecl"):
    MmsConnection_connectAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_connectAsync", "cdecl")
    MmsConnection_connectAsync.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connectAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 286
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_tick", "cdecl"):
    MmsConnection_tick = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_tick", "cdecl")
    MmsConnection_tick.argtypes = [MmsConnection]
    MmsConnection_tick.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 297
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_close", "cdecl"):
    MmsConnection_close = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_close", "cdecl")
    MmsConnection_close.argtypes = [MmsConnection]
    MmsConnection_close.restype = None

MmsConnection_ConcludeAbortHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsError, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 300

# /usr/local/include/libiec61850/mms_client_connection.h: 314
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_abort", "cdecl"):
    MmsConnection_abort = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_abort", "cdecl")
    MmsConnection_abort.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abort.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 317
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_abortAsync", "cdecl"):
    MmsConnection_abortAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_abortAsync", "cdecl")
    MmsConnection_abortAsync.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abortAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 331
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_conclude", "cdecl"):
    MmsConnection_conclude = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_conclude", "cdecl")
    MmsConnection_conclude.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_conclude.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 334
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_concludeAsync", "cdecl"):
    MmsConnection_concludeAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_concludeAsync", "cdecl")
    MmsConnection_concludeAsync.argtypes = [MmsConnection, POINTER(MmsError), MmsConnection_ConcludeAbortHandler, POINTER(None)]
    MmsConnection_concludeAsync.restype = None

MmsConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 337

MmsConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 340

# /usr/local/include/libiec61850/mms_client_connection.h: 353
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVMDVariableNames", "cdecl"):
    MmsConnection_getVMDVariableNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVMDVariableNames", "cdecl")
    MmsConnection_getVMDVariableNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVMDVariableNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 356
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVMDVariableNamesAsync", "cdecl"):
    MmsConnection_getVMDVariableNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVMDVariableNamesAsync", "cdecl")
    MmsConnection_getVMDVariableNamesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVMDVariableNamesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 371
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainNames", "cdecl"):
    MmsConnection_getDomainNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainNames", "cdecl")
    MmsConnection_getDomainNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getDomainNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 386
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainNamesAsync", "cdecl"):
    MmsConnection_getDomainNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainNamesAsync", "cdecl")
    MmsConnection_getDomainNamesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainNamesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 401
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableNames", "cdecl"):
    MmsConnection_getDomainVariableNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableNames", "cdecl")
    MmsConnection_getDomainVariableNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 419
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableNamesAsync", "cdecl")
    MmsConnection_getDomainVariableNamesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableNamesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 434
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableListNames", "cdecl"):
    MmsConnection_getDomainVariableListNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableListNames", "cdecl")
    MmsConnection_getDomainVariableListNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableListNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 437
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableListNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableListNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableListNamesAsync", "cdecl")
    MmsConnection_getDomainVariableListNamesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableListNamesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 452
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainJournals", "cdecl"):
    MmsConnection_getDomainJournals = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainJournals", "cdecl")
    MmsConnection_getDomainJournals.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainJournals.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 455
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainJournalsAsync", "cdecl"):
    MmsConnection_getDomainJournalsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainJournalsAsync", "cdecl")
    MmsConnection_getDomainJournalsAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainJournalsAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 469
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVariableListNamesAssociationSpecific.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 472
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVariableListNamesAssociationSpecificAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 488
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariable", "cdecl"):
    MmsConnection_readVariable = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariable", "cdecl")
    MmsConnection_readVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_readVariable.restype = POINTER(MmsValue)

MmsConnection_ReadVariableHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, POINTER(MmsValue))# /usr/local/include/libiec61850/mms_client_connection.h: 493

# /usr/local/include/libiec61850/mms_client_connection.h: 506
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableAsync", "cdecl"):
    MmsConnection_readVariableAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableAsync", "cdecl")
    MmsConnection_readVariableAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 522
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableComponent", "cdecl"):
    MmsConnection_readVariableComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableComponent", "cdecl")
    MmsConnection_readVariableComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, String]
    MmsConnection_readVariableComponent.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 540
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableComponentAsync", "cdecl"):
    MmsConnection_readVariableComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableComponentAsync", "cdecl")
    MmsConnection_readVariableComponentAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableComponentAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 558
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readArrayElements", "cdecl"):
    MmsConnection_readArrayElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readArrayElements", "cdecl")
    MmsConnection_readArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, c_uint32]
    MmsConnection_readArrayElements.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 578
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readArrayElementsAsync", "cdecl"):
    MmsConnection_readArrayElementsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readArrayElementsAsync", "cdecl")
    MmsConnection_readArrayElementsAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, c_uint32, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readArrayElementsAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 595
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponent", "cdecl")
    MmsConnection_readSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, String]
    MmsConnection_readSingleArrayElementWithComponent.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 600
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_readSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readSingleArrayElementWithComponentAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 617
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readMultipleVariables", "cdecl"):
    MmsConnection_readMultipleVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readMultipleVariables", "cdecl")
    MmsConnection_readMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_readMultipleVariables.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 622
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readMultipleVariablesAsync", "cdecl"):
    MmsConnection_readMultipleVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readMultipleVariablesAsync", "cdecl")
    MmsConnection_readMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readMultipleVariablesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 640
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariable", "cdecl"):
    MmsConnection_writeVariable = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariable", "cdecl")
    MmsConnection_writeVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue)]
    MmsConnection_writeVariable.restype = MmsDataAccessError

MmsConnection_WriteVariableHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, MmsDataAccessError)# /usr/local/include/libiec61850/mms_client_connection.h: 644

# /usr/local/include/libiec61850/mms_client_connection.h: 647
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariableAsync", "cdecl"):
    MmsConnection_writeVariableAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariableAsync", "cdecl")
    MmsConnection_writeVariableAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeVariableAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 666
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponent", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, String, POINTER(MmsValue)]
    MmsConnection_writeSingleArrayElementWithComponent.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_client_connection.h: 671
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_uint32, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeSingleArrayElementWithComponentAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 695
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeArrayElements", "cdecl"):
    MmsConnection_writeArrayElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeArrayElements", "cdecl")
    MmsConnection_writeArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue)]
    MmsConnection_writeArrayElements.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_client_connection.h: 700
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeArrayElementsAsync", "cdecl"):
    MmsConnection_writeArrayElementsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeArrayElementsAsync", "cdecl")
    MmsConnection_writeArrayElementsAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeArrayElementsAsync.restype = c_uint32

MmsConnection_WriteMultipleVariablesHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, LinkedList)# /usr/local/include/libiec61850/mms_client_connection.h: 707

# /usr/local/include/libiec61850/mms_client_connection.h: 728
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeMultipleVariables", "cdecl"):
    MmsConnection_writeMultipleVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeMultipleVariables", "cdecl")
    MmsConnection_writeMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeMultipleVariables.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 733
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeMultipleVariablesAsync", "cdecl"):
    MmsConnection_writeMultipleVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeMultipleVariablesAsync", "cdecl")
    MmsConnection_writeMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeMultipleVariablesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 754
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeNamedVariableList", "cdecl"):
    MmsConnection_writeNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeNamedVariableList", "cdecl")
    MmsConnection_writeNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), c_bool, String, String, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeNamedVariableList.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 760
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeNamedVariableListAsync", "cdecl"):
    MmsConnection_writeNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeNamedVariableListAsync", "cdecl")
    MmsConnection_writeNamedVariableListAsync.argtypes = [MmsConnection, POINTER(MmsError), c_bool, String, String, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeNamedVariableListAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 774
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableAccessAttributes", "cdecl"):
    MmsConnection_getVariableAccessAttributes = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableAccessAttributes", "cdecl")
    MmsConnection_getVariableAccessAttributes.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_getVariableAccessAttributes.restype = POINTER(MmsVariableSpecification)

MmsConnection_GetVariableAccessAttributesHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, POINTER(MmsVariableSpecification))# /usr/local/include/libiec61850/mms_client_connection.h: 779

# /usr/local/include/libiec61850/mms_client_connection.h: 783
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableAccessAttributesAsync", "cdecl"):
    MmsConnection_getVariableAccessAttributesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableAccessAttributesAsync", "cdecl")
    MmsConnection_getVariableAccessAttributesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_GetVariableAccessAttributesHandler, POINTER(None)]
    MmsConnection_getVariableAccessAttributesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 803
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValues", "cdecl"):
    MmsConnection_readNamedVariableListValues = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValues", "cdecl")
    MmsConnection_readNamedVariableListValues.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_bool]
    MmsConnection_readNamedVariableListValues.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 808
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 825
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, c_bool]
    MmsConnection_readNamedVariableListValuesAssociationSpecific.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 830
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(MmsError), String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 848
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableList", "cdecl"):
    MmsConnection_defineNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableList", "cdecl")
    MmsConnection_defineNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList]
    MmsConnection_defineNamedVariableList.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 852
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAsync", "cdecl")
    MmsConnection_defineNamedVariableListAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 868
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_defineNamedVariableListAssociationSpecific.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 872
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 892
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectory", "cdecl"):
    MmsConnection_readNamedVariableListDirectory = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectory", "cdecl")
    MmsConnection_readNamedVariableListDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectory.restype = LinkedList

MmsConnection_ReadNVLDirectoryHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 897

# /usr/local/include/libiec61850/mms_client_connection.h: 901
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 916
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 920
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(MmsError), String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 938
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteNamedVariableList", "cdecl"):
    MmsConnection_deleteNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteNamedVariableList", "cdecl")
    MmsConnection_deleteNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_deleteNamedVariableList.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 942
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteNamedVariableListAsync", "cdecl")
    MmsConnection_deleteNamedVariableListAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteNamedVariableListAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 955
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_deleteAssociationSpecificNamedVariableList.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 960
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.argtypes = [MmsConnection, POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 974
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_create", "cdecl"):
    MmsVariableAccessSpecification_create = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_create", "cdecl")
    MmsVariableAccessSpecification_create.argtypes = [String, String]
    MmsVariableAccessSpecification_create.restype = POINTER(MmsVariableAccessSpecification)

# /usr/local/include/libiec61850/mms_client_connection.h: 993
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_createAlternateAccess", "cdecl"):
    MmsVariableAccessSpecification_createAlternateAccess = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_createAlternateAccess", "cdecl")
    MmsVariableAccessSpecification_createAlternateAccess.argtypes = [String, String, c_int32, String]
    MmsVariableAccessSpecification_createAlternateAccess.restype = POINTER(MmsVariableAccessSpecification)

# /usr/local/include/libiec61850/mms_client_connection.h: 1003
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_destroy", "cdecl"):
    MmsVariableAccessSpecification_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_destroy", "cdecl")
    MmsVariableAccessSpecification_destroy.argtypes = [POINTER(MmsVariableAccessSpecification)]
    MmsVariableAccessSpecification_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1015
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setLocalDetail", "cdecl"):
    MmsConnection_setLocalDetail = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setLocalDetail", "cdecl")
    MmsConnection_setLocalDetail.argtypes = [MmsConnection, c_int32]
    MmsConnection_setLocalDetail.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1018
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getLocalDetail", "cdecl"):
    MmsConnection_getLocalDetail = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getLocalDetail", "cdecl")
    MmsConnection_getLocalDetail.argtypes = [MmsConnection]
    MmsConnection_getLocalDetail.restype = c_int32

# /usr/local/include/libiec61850/mms_client_connection.h: 1029
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_identify", "cdecl"):
    MmsConnection_identify = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_identify", "cdecl")
    MmsConnection_identify.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_identify.restype = POINTER(MmsServerIdentity)

MmsConnection_IdentifyHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, String, String, String)# /usr/local/include/libiec61850/mms_client_connection.h: 1033

# /usr/local/include/libiec61850/mms_client_connection.h: 1037
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_identifyAsync", "cdecl"):
    MmsConnection_identifyAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_identifyAsync", "cdecl")
    MmsConnection_identifyAsync.argtypes = [MmsConnection, POINTER(MmsError), MmsConnection_IdentifyHandler, POINTER(None)]
    MmsConnection_identifyAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1041
if _libs["/usr/local/lib/libiec61850.so"].has("MmsServerIdentity_destroy", "cdecl"):
    MmsServerIdentity_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsServerIdentity_destroy", "cdecl")
    MmsServerIdentity_destroy.argtypes = [POINTER(MmsServerIdentity)]
    MmsServerIdentity_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1056
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getServerStatus", "cdecl"):
    MmsConnection_getServerStatus = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getServerStatus", "cdecl")
    MmsConnection_getServerStatus.argtypes = [MmsConnection, POINTER(MmsError), POINTER(c_int), POINTER(c_int), c_bool]
    MmsConnection_getServerStatus.restype = None

MmsConnection_GetServerStatusHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, c_int, c_int)# /usr/local/include/libiec61850/mms_client_connection.h: 1060

# /usr/local/include/libiec61850/mms_client_connection.h: 1063
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getServerStatusAsync", "cdecl"):
    MmsConnection_getServerStatusAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getServerStatusAsync", "cdecl")
    MmsConnection_getServerStatusAsync.argtypes = [MmsConnection, POINTER(MmsError), c_bool, MmsConnection_GetServerStatusHandler, POINTER(None)]
    MmsConnection_getServerStatusAsync.restype = c_uint32

MmsFileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, c_uint32, c_uint64)# /usr/local/include/libiec61850/mms_client_connection.h: 1071

MmsConnection_FileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, String, c_uint32, c_uint64, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1081

MmsFileReadHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(c_uint8), c_uint32)# /usr/local/include/libiec61850/mms_client_connection.h: 1085

MmsConnection_FileReadHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, c_int32, POINTER(c_uint8), c_uint32, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1101

# /usr/local/include/libiec61850/mms_client_connection.h: 1114
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileOpen", "cdecl"):
    MmsConnection_fileOpen = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileOpen", "cdecl")
    MmsConnection_fileOpen.argtypes = [MmsConnection, POINTER(MmsError), String, c_uint32, POINTER(c_uint32), POINTER(c_uint64)]
    MmsConnection_fileOpen.restype = c_int32

MmsConnection_FileOpenHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, c_int32, c_uint32, c_uint64)# /usr/local/include/libiec61850/mms_client_connection.h: 1118

# /usr/local/include/libiec61850/mms_client_connection.h: 1121
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileOpenAsync", "cdecl"):
    MmsConnection_fileOpenAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileOpenAsync", "cdecl")
    MmsConnection_fileOpenAsync.argtypes = [MmsConnection, POINTER(MmsError), String, c_uint32, MmsConnection_FileOpenHandler, POINTER(None)]
    MmsConnection_fileOpenAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1137
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRead", "cdecl"):
    MmsConnection_fileRead = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRead", "cdecl")
    MmsConnection_fileRead.argtypes = [MmsConnection, POINTER(MmsError), c_int32, MmsFileReadHandler, POINTER(None)]
    MmsConnection_fileRead.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 1140
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileReadAsync", "cdecl"):
    MmsConnection_fileReadAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileReadAsync", "cdecl")
    MmsConnection_fileReadAsync.argtypes = [MmsConnection, POINTER(MmsError), c_int32, MmsConnection_FileReadHandler, POINTER(None)]
    MmsConnection_fileReadAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1150
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileClose", "cdecl"):
    MmsConnection_fileClose = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileClose", "cdecl")
    MmsConnection_fileClose.argtypes = [MmsConnection, POINTER(MmsError), c_int32]
    MmsConnection_fileClose.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1153
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileCloseAsync", "cdecl"):
    MmsConnection_fileCloseAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileCloseAsync", "cdecl")
    MmsConnection_fileCloseAsync.argtypes = [MmsConnection, POINTER(MmsError), c_uint32, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileCloseAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1163
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileDelete", "cdecl"):
    MmsConnection_fileDelete = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileDelete", "cdecl")
    MmsConnection_fileDelete.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_fileDelete.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1166
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileDeleteAsync", "cdecl"):
    MmsConnection_fileDeleteAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileDeleteAsync", "cdecl")
    MmsConnection_fileDeleteAsync.argtypes = [MmsConnection, POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileDeleteAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1178
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRename", "cdecl"):
    MmsConnection_fileRename = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRename", "cdecl")
    MmsConnection_fileRename.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_fileRename.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1181
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRenameAsync", "cdecl"):
    MmsConnection_fileRenameAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRenameAsync", "cdecl")
    MmsConnection_fileRenameAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileRenameAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1193
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_obtainFile", "cdecl"):
    MmsConnection_obtainFile = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_obtainFile", "cdecl")
    MmsConnection_obtainFile.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_obtainFile.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1196
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_obtainFileAsync", "cdecl"):
    MmsConnection_obtainFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_obtainFileAsync", "cdecl")
    MmsConnection_obtainFileAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_obtainFileAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1216
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getFileDirectory", "cdecl"):
    MmsConnection_getFileDirectory = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getFileDirectory", "cdecl")
    MmsConnection_getFileDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsFileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectory.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 1220
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getFileDirectoryAsync", "cdecl"):
    MmsConnection_getFileDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getFileDirectoryAsync", "cdecl")
    MmsConnection_getFileDirectoryAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsConnection_FileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectoryAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1227
class struct_sMmsJournalEntry(Structure):
    pass

MmsJournalEntry = POINTER(struct_sMmsJournalEntry)# /usr/local/include/libiec61850/mms_client_connection.h: 1223

# /usr/local/include/libiec61850/mms_client_connection.h: 1233
class struct_sMmsJournalVariable(Structure):
    pass

MmsJournalVariable = POINTER(struct_sMmsJournalVariable)# /usr/local/include/libiec61850/mms_client_connection.h: 1225

struct_sMmsJournalEntry.__slots__ = [
    'entryID',
    'occurenceTime',
    'journalVariables',
]
struct_sMmsJournalEntry._fields_ = [
    ('entryID', POINTER(MmsValue)),
    ('occurenceTime', POINTER(MmsValue)),
    ('journalVariables', LinkedList),
]

struct_sMmsJournalVariable.__slots__ = [
    'tag',
    'value',
]
struct_sMmsJournalVariable._fields_ = [
    ('tag', String),
    ('value', POINTER(MmsValue)),
]

# /usr/local/include/libiec61850/mms_client_connection.h: 1252
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_destroy", "cdecl"):
    MmsJournalEntry_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_destroy", "cdecl")
    MmsJournalEntry_destroy.argtypes = [MmsJournalEntry]
    MmsJournalEntry_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1254
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getEntryID", "cdecl"):
    MmsJournalEntry_getEntryID = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getEntryID", "cdecl")
    MmsJournalEntry_getEntryID.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getEntryID.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 1257
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getOccurenceTime", "cdecl"):
    MmsJournalEntry_getOccurenceTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getOccurenceTime", "cdecl")
    MmsJournalEntry_getOccurenceTime.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getOccurenceTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 1261
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getJournalVariables", "cdecl"):
    MmsJournalEntry_getJournalVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getJournalVariables", "cdecl")
    MmsJournalEntry_getJournalVariables.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getJournalVariables.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1263
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalVariable_getTag", "cdecl"):
    MmsJournalVariable_getTag = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalVariable_getTag", "cdecl")
    MmsJournalVariable_getTag.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getTag.restype = c_char_p

# /usr/local/include/libiec61850/mms_client_connection.h: 1266
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalVariable_getValue", "cdecl"):
    MmsJournalVariable_getValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalVariable_getValue", "cdecl")
    MmsJournalVariable_getValue.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getValue.restype = POINTER(MmsValue)

MmsConnection_ReadJournalHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1270

# /usr/local/include/libiec61850/mms_client_connection.h: 1274
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalTimeRange", "cdecl"):
    MmsConnection_readJournalTimeRange = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalTimeRange", "cdecl")
    MmsConnection_readJournalTimeRange.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalTimeRange.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1278
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalTimeRangeAsync", "cdecl"):
    MmsConnection_readJournalTimeRangeAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalTimeRangeAsync", "cdecl")
    MmsConnection_readJournalTimeRangeAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalTimeRangeAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1282
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalStartAfter", "cdecl"):
    MmsConnection_readJournalStartAfter = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalStartAfter", "cdecl")
    MmsConnection_readJournalStartAfter.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalStartAfter.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1286
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalStartAfterAsync", "cdecl"):
    MmsConnection_readJournalStartAfterAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalStartAfterAsync", "cdecl")
    MmsConnection_readJournalStartAfterAsync.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalStartAfterAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_client_connection.h: 1295
if _libs["/usr/local/lib/libiec61850.so"].has("MmsServerIdentity_destroy", "cdecl"):
    MmsServerIdentity_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsServerIdentity_destroy", "cdecl")
    MmsServerIdentity_destroy.argtypes = [POINTER(MmsServerIdentity)]
    MmsServerIdentity_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 43
class struct_sClientDataSet(Structure):
    pass

ClientDataSet = POINTER(struct_sClientDataSet)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 43

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 46
class struct_sClientReport(Structure):
    pass

ClientReport = POINTER(struct_sClientReport)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 46

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 49
class struct_sClientReportControlBlock(Structure):
    pass

ClientReportControlBlock = POINTER(struct_sClientReportControlBlock)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 49

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 52
class struct_sClientGooseControlBlock(Structure):
    pass

ClientGooseControlBlock = POINTER(struct_sClientGooseControlBlock)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 52

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 61
class struct_sIedConnection(Structure):
    pass

IedConnection = POINTER(struct_sIedConnection)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 61

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 69
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'ctlNum',
    'error',
    'addCause',
]
struct_anon_41._fields_ = [
    ('ctlNum', c_int),
    ('error', c_int),
    ('addCause', ControlAddCause),
]

LastApplError = struct_anon_41# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 69

enum_anon_42 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CLOSED = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CONNECTING = (IED_STATE_CLOSED + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CONNECTED = (IED_STATE_CONNECTING + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IED_STATE_CLOSING = (IED_STATE_CONNECTED + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

IedConnectionState = enum_anon_42# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 78

enum_anon_43 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OK = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_NOT_CONNECTED = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_ALREADY_CONNECTED = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_CONNECTION_LOST = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_SERVICE_NOT_SUPPORTED = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_CONNECTION_REJECTED = 5# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OUTSTANDING_CALL_LIMIT_REACHED = 6# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_USER_PROVIDED_INVALID_ARGUMENT = 10# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_ENABLE_REPORT_FAILED_DATASET_MISMATCH = 11# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_REFERENCE_INVALID = 12# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_UNEXPECTED_VALUE_RECEIVED = 13# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_TIMEOUT = 20# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_ACCESS_DENIED = 21# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_DOES_NOT_EXIST = 22# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_EXISTS = 23# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_ACCESS_UNSUPPORTED = 24# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_TYPE_INCONSISTENT = 25# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_TEMPORARILY_UNAVAILABLE = 26# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_UNDEFINED = 27# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_INVALID_ADDRESS = 28# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_HARDWARE_FAULT = 29# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_TYPE_UNSUPPORTED = 30# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 31# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_VALUE_INVALID = 32# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_OBJECT_INVALIDATED = 33# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_MALFORMED_MESSAGE = 34# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_SERVICE_NOT_IMPLEMENTED = 98# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IED_ERROR_UNKNOWN = 99# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

IedClientError = enum_anon_43# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 170

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 186
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_create", "cdecl"):
    IedConnection_create = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_create", "cdecl")
    IedConnection_create.argtypes = []
    IedConnection_create.restype = IedConnection

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createEx", "cdecl"):
    IedConnection_createEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createEx", "cdecl")
    IedConnection_createEx.argtypes = [TLSConfiguration, c_bool]
    IedConnection_createEx.restype = IedConnection

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 221
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createWithTlsSupport", "cdecl"):
    IedConnection_createWithTlsSupport = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createWithTlsSupport", "cdecl")
    IedConnection_createWithTlsSupport.argtypes = [TLSConfiguration]
    IedConnection_createWithTlsSupport.restype = IedConnection

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_destroy", "cdecl"):
    IedConnection_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_destroy", "cdecl")
    IedConnection_destroy.argtypes = [IedConnection]
    IedConnection_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 245
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setConnectTimeout", "cdecl"):
    IedConnection_setConnectTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setConnectTimeout", "cdecl")
    IedConnection_setConnectTimeout.argtypes = [IedConnection, c_uint32]
    IedConnection_setConnectTimeout.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 257
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRequestTimeout", "cdecl"):
    IedConnection_setRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRequestTimeout", "cdecl")
    IedConnection_setRequestTimeout.argtypes = [IedConnection, c_uint32]
    IedConnection_setRequestTimeout.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 267
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRequestTimeout", "cdecl"):
    IedConnection_getRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRequestTimeout", "cdecl")
    IedConnection_getRequestTimeout.argtypes = [IedConnection]
    IedConnection_getRequestTimeout.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 282
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_tick", "cdecl"):
    IedConnection_tick = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_tick", "cdecl")
    IedConnection_tick.argtypes = [IedConnection]
    IedConnection_tick.restype = c_bool

IedConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 295

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 312
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_connect", "cdecl"):
    IedConnection_connect = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_connect", "cdecl")
    IedConnection_connect.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connect.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 328
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_connectAsync", "cdecl"):
    IedConnection_connectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_connectAsync", "cdecl")
    IedConnection_connectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connectAsync.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 343
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_abort", "cdecl"):
    IedConnection_abort = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_abort", "cdecl")
    IedConnection_abort.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abort.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 359
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_abortAsync", "cdecl"):
    IedConnection_abortAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_abortAsync", "cdecl")
    IedConnection_abortAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abortAsync.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 374
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_release", "cdecl"):
    IedConnection_release = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_release", "cdecl")
    IedConnection_release.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_release.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 389
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_releaseAsync", "cdecl"):
    IedConnection_releaseAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_releaseAsync", "cdecl")
    IedConnection_releaseAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_releaseAsync.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 399
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_close", "cdecl"):
    IedConnection_close = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_close", "cdecl")
    IedConnection_close.argtypes = [IedConnection]
    IedConnection_close.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 411
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getState", "cdecl"):
    IedConnection_getState = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getState", "cdecl")
    IedConnection_getState.argtypes = [IedConnection]
    IedConnection_getState.restype = IedConnectionState

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 421
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLastApplError", "cdecl"):
    IedConnection_getLastApplError = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLastApplError", "cdecl")
    IedConnection_getLastApplError.argtypes = [IedConnection]
    IedConnection_getLastApplError.restype = LastApplError

IedConnectionClosedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 432

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 444
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installConnectionClosedHandler", "cdecl"):
    IedConnection_installConnectionClosedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installConnectionClosedHandler", "cdecl")
    IedConnection_installConnectionClosedHandler.argtypes = [IedConnection, IedConnectionClosedHandler, POINTER(None)]
    IedConnection_installConnectionClosedHandler.restype = None

IedConnection_StateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection, IedConnectionState)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 455

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 465
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installStateChangedHandler", "cdecl"):
    IedConnection_installStateChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installStateChangedHandler", "cdecl")
    IedConnection_installStateChangedHandler.argtypes = [IedConnection, IedConnection_StateChangedHandler, POINTER(None)]
    IedConnection_installStateChangedHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 478
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getMmsConnection", "cdecl"):
    IedConnection_getMmsConnection = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getMmsConnection", "cdecl")
    IedConnection_getMmsConnection.argtypes = [IedConnection]
    IedConnection_getMmsConnection.restype = MmsConnection

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 511
class struct_sClientSVControlBlock(Structure):
    pass

ClientSVControlBlock = POINTER(struct_sClientSVControlBlock)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 511

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 529
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_create", "cdecl"):
    ClientSVControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_create", "cdecl")
    ClientSVControlBlock_create.argtypes = [IedConnection, String]
    ClientSVControlBlock_create.restype = ClientSVControlBlock

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 537
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_destroy", "cdecl"):
    ClientSVControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_destroy", "cdecl")
    ClientSVControlBlock_destroy.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 547
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_isMulticast", "cdecl"):
    ClientSVControlBlock_isMulticast = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_isMulticast", "cdecl")
    ClientSVControlBlock_isMulticast.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_isMulticast.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 557
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getLastComError", "cdecl"):
    ClientSVControlBlock_getLastComError = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getLastComError", "cdecl")
    ClientSVControlBlock_getLastComError.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getLastComError.restype = IedClientError

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 561
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_setSvEna", "cdecl"):
    ClientSVControlBlock_setSvEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_setSvEna", "cdecl")
    ClientSVControlBlock_setSvEna.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setSvEna.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 564
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSvEna", "cdecl"):
    ClientSVControlBlock_getSvEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSvEna", "cdecl")
    ClientSVControlBlock_getSvEna.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSvEna.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 567
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_setResv", "cdecl"):
    ClientSVControlBlock_setResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_setResv", "cdecl")
    ClientSVControlBlock_setResv.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setResv.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 570
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getResv", "cdecl"):
    ClientSVControlBlock_getResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getResv", "cdecl")
    ClientSVControlBlock_getResv.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getResv.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 572
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getMsvID", "cdecl"):
    ClientSVControlBlock_getMsvID = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getMsvID", "cdecl")
    ClientSVControlBlock_getMsvID.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getMsvID.restype = ReturnString
    else:
        ClientSVControlBlock_getMsvID.restype = String
        ClientSVControlBlock_getMsvID.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 586
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getDatSet", "cdecl"):
    ClientSVControlBlock_getDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getDatSet", "cdecl")
    ClientSVControlBlock_getDatSet.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getDatSet.restype = ReturnString
    else:
        ClientSVControlBlock_getDatSet.restype = String
        ClientSVControlBlock_getDatSet.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 590
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getConfRev", "cdecl"):
    ClientSVControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getConfRev", "cdecl")
    ClientSVControlBlock_getConfRev.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getConfRev.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 593
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSmpRate", "cdecl"):
    ClientSVControlBlock_getSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSmpRate", "cdecl")
    ClientSVControlBlock_getSmpRate.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpRate.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 602
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getDstAddress", "cdecl"):
    ClientSVControlBlock_getDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getDstAddress", "cdecl")
    ClientSVControlBlock_getDstAddress.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getDstAddress.restype = PhyComAddress

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 611
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getOptFlds", "cdecl"):
    ClientSVControlBlock_getOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getOptFlds", "cdecl")
    ClientSVControlBlock_getOptFlds.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getOptFlds.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 619
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSmpMod", "cdecl"):
    ClientSVControlBlock_getSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSmpMod", "cdecl")
    ClientSVControlBlock_getSmpMod.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpMod.restype = c_uint8

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 629
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getNoASDU", "cdecl"):
    ClientSVControlBlock_getNoASDU = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getNoASDU", "cdecl")
    ClientSVControlBlock_getNoASDU.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getNoASDU.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 680
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_create", "cdecl"):
    ClientGooseControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_create", "cdecl")
    ClientGooseControlBlock_create.argtypes = [String]
    ClientGooseControlBlock_create.restype = ClientGooseControlBlock

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 683
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_destroy", "cdecl"):
    ClientGooseControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_destroy", "cdecl")
    ClientGooseControlBlock_destroy.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 686
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getGoEna", "cdecl"):
    ClientGooseControlBlock_getGoEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getGoEna", "cdecl")
    ClientGooseControlBlock_getGoEna.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoEna.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 689
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setGoEna", "cdecl"):
    ClientGooseControlBlock_setGoEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setGoEna", "cdecl")
    ClientGooseControlBlock_setGoEna.argtypes = [ClientGooseControlBlock, c_bool]
    ClientGooseControlBlock_setGoEna.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 691
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getGoID", "cdecl"):
    ClientGooseControlBlock_getGoID = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getGoID", "cdecl")
    ClientGooseControlBlock_getGoID.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoID.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 695
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setGoID", "cdecl"):
    ClientGooseControlBlock_setGoID = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setGoID", "cdecl")
    ClientGooseControlBlock_setGoID.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setGoID.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 697
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDatSet", "cdecl"):
    ClientGooseControlBlock_getDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDatSet", "cdecl")
    ClientGooseControlBlock_getDatSet.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDatSet.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 701
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDatSet", "cdecl"):
    ClientGooseControlBlock_setDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDatSet", "cdecl")
    ClientGooseControlBlock_setDatSet.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setDatSet.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 704
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getConfRev", "cdecl"):
    ClientGooseControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getConfRev", "cdecl")
    ClientGooseControlBlock_getConfRev.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getConfRev.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 707
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getNdsComm", "cdecl"):
    ClientGooseControlBlock_getNdsComm = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getNdsComm", "cdecl")
    ClientGooseControlBlock_getNdsComm.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getNdsComm.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 710
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getMinTime", "cdecl"):
    ClientGooseControlBlock_getMinTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getMinTime", "cdecl")
    ClientGooseControlBlock_getMinTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMinTime.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 713
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getMaxTime", "cdecl"):
    ClientGooseControlBlock_getMaxTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getMaxTime", "cdecl")
    ClientGooseControlBlock_getMaxTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMaxTime.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 716
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getFixedOffs", "cdecl"):
    ClientGooseControlBlock_getFixedOffs = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getFixedOffs", "cdecl")
    ClientGooseControlBlock_getFixedOffs.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getFixedOffs.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 719
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress", "cdecl"):
    ClientGooseControlBlock_getDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress", "cdecl")
    ClientGooseControlBlock_getDstAddress.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress.restype = PhyComAddress

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 722
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress", "cdecl"):
    ClientGooseControlBlock_setDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress", "cdecl")
    ClientGooseControlBlock_setDstAddress.argtypes = [ClientGooseControlBlock, PhyComAddress]
    ClientGooseControlBlock_setDstAddress.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 724
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_getDstAddress_addr = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_addr", "cdecl")
    ClientGooseControlBlock_getDstAddress_addr.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_addr.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 728
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_setDstAddress_addr = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_addr", "cdecl")
    ClientGooseControlBlock_setDstAddress_addr.argtypes = [ClientGooseControlBlock, POINTER(MmsValue)]
    ClientGooseControlBlock_setDstAddress_addr.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 731
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_getDstAddress_priority = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_priority", "cdecl")
    ClientGooseControlBlock_getDstAddress_priority.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_priority.restype = c_uint8

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 734
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_setDstAddress_priority = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_priority", "cdecl")
    ClientGooseControlBlock_setDstAddress_priority.argtypes = [ClientGooseControlBlock, c_uint8]
    ClientGooseControlBlock_setDstAddress_priority.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 737
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_vid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_vid", "cdecl")
    ClientGooseControlBlock_getDstAddress_vid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_vid.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 740
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_vid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_vid", "cdecl")
    ClientGooseControlBlock_setDstAddress_vid.argtypes = [ClientGooseControlBlock, c_uint16]
    ClientGooseControlBlock_setDstAddress_vid.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 743
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_appid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_appid", "cdecl")
    ClientGooseControlBlock_getDstAddress_appid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_appid.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 746
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_appid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_appid", "cdecl")
    ClientGooseControlBlock_setDstAddress_appid.argtypes = [ClientGooseControlBlock, c_uint16]
    ClientGooseControlBlock_setDstAddress_appid.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 781
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getGoCBValues", "cdecl"):
    IedConnection_getGoCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getGoCBValues", "cdecl")
    IedConnection_getGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientGooseControlBlock]
    IedConnection_getGoCBValues.restype = ClientGooseControlBlock

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 805
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setGoCBValues", "cdecl"):
    IedConnection_setGoCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setGoCBValues", "cdecl")
    IedConnection_setGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientGooseControlBlock, c_uint32, c_bool]
    IedConnection_setGoCBValues.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 831
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readObject", "cdecl"):
    IedConnection_readObject = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readObject", "cdecl")
    IedConnection_readObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readObject.restype = POINTER(MmsValue)

IedConnection_ReadObjectHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, POINTER(MmsValue))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 835

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 850
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readObjectAsync", "cdecl"):
    IedConnection_readObjectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readObjectAsync", "cdecl")
    IedConnection_readObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_ReadObjectHandler, POINTER(None)]
    IedConnection_readObjectAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 863
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeObject", "cdecl"):
    IedConnection_writeObject = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeObject", "cdecl")
    IedConnection_writeObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue)]
    IedConnection_writeObject.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 880
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeObjectAsync", "cdecl"):
    IedConnection_writeObjectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeObjectAsync", "cdecl")
    IedConnection_writeObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue), IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_writeObjectAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 892
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readBooleanValue", "cdecl"):
    IedConnection_readBooleanValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readBooleanValue", "cdecl")
    IedConnection_readBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readBooleanValue.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 903
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readFloatValue", "cdecl"):
    IedConnection_readFloatValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readFloatValue", "cdecl")
    IedConnection_readFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readFloatValue.restype = c_float

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 917
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readStringValue", "cdecl"):
    IedConnection_readStringValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readStringValue", "cdecl")
    IedConnection_readStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        IedConnection_readStringValue.restype = ReturnString
    else:
        IedConnection_readStringValue.restype = String
        IedConnection_readStringValue.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 931
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readInt32Value", "cdecl"):
    IedConnection_readInt32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readInt32Value", "cdecl")
    IedConnection_readInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt32Value.restype = c_int32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 944
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readInt64Value", "cdecl"):
    IedConnection_readInt64Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readInt64Value", "cdecl")
    IedConnection_readInt64Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt64Value.restype = c_int64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 957
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readUnsigned32Value", "cdecl"):
    IedConnection_readUnsigned32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readUnsigned32Value", "cdecl")
    IedConnection_readUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readUnsigned32Value.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 974
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readTimestampValue", "cdecl"):
    IedConnection_readTimestampValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readTimestampValue", "cdecl")
    IedConnection_readTimestampValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(Timestamp)]
    IedConnection_readTimestampValue.restype = POINTER(Timestamp)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 989
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readQualityValue", "cdecl"):
    IedConnection_readQualityValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readQualityValue", "cdecl")
    IedConnection_readQualityValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readQualityValue.restype = Quality

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1001
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeBooleanValue", "cdecl"):
    IedConnection_writeBooleanValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeBooleanValue", "cdecl")
    IedConnection_writeBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_bool]
    IedConnection_writeBooleanValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1014
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeInt32Value", "cdecl"):
    IedConnection_writeInt32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeInt32Value", "cdecl")
    IedConnection_writeInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_int32]
    IedConnection_writeInt32Value.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1027
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeUnsigned32Value", "cdecl"):
    IedConnection_writeUnsigned32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeUnsigned32Value", "cdecl")
    IedConnection_writeUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_uint32]
    IedConnection_writeUnsigned32Value.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1040
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeFloatValue", "cdecl"):
    IedConnection_writeFloatValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeFloatValue", "cdecl")
    IedConnection_writeFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_float]
    IedConnection_writeFloatValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1044
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeVisibleStringValue", "cdecl"):
    IedConnection_writeVisibleStringValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeVisibleStringValue", "cdecl")
    IedConnection_writeVisibleStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, String]
    IedConnection_writeVisibleStringValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1048
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeOctetString", "cdecl"):
    IedConnection_writeOctetString = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeOctetString", "cdecl")
    IedConnection_writeOctetString.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(c_uint8), c_int]
    IedConnection_writeOctetString.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1097
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRCBValues", "cdecl"):
    IedConnection_getRCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRCBValues", "cdecl")
    IedConnection_getRCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock]
    IedConnection_getRCBValues.restype = ClientReportControlBlock

IedConnection_GetRCBValuesHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, ClientReportControlBlock)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1101

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1104
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRCBValuesAsync", "cdecl"):
    IedConnection_getRCBValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRCBValuesAsync", "cdecl")
    IedConnection_getRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock, IedConnection_GetRCBValuesHandler, POINTER(None)]
    IedConnection_getRCBValuesAsync.restype = c_uint32

enum_anon_44 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_NOT_INCLUDED = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_DATA_CHANGE = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_QUALITY_CHANGE = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_DATA_UPDATE = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_INTEGRITY = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_GI = 5# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

IEC61850_REASON_UNKNOWN = 6# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

ReasonForInclusion = enum_anon_44# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1129

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1212
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRCBValues", "cdecl"):
    IedConnection_setRCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRCBValues", "cdecl")
    IedConnection_setRCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, c_uint32, c_bool]
    IedConnection_setRCBValues.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1216
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRCBValuesAsync", "cdecl"):
    IedConnection_setRCBValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRCBValuesAsync", "cdecl")
    IedConnection_setRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, c_uint32, c_bool, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setRCBValuesAsync.restype = c_uint32

ReportCallbackFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None), ClientReport)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1225

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1247
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installReportHandler", "cdecl"):
    IedConnection_installReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installReportHandler", "cdecl")
    IedConnection_installReportHandler.argtypes = [IedConnection, String, String, ReportCallbackFunction, POINTER(None)]
    IedConnection_installReportHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1257
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_uninstallReportHandler", "cdecl"):
    IedConnection_uninstallReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_uninstallReportHandler", "cdecl")
    IedConnection_uninstallReportHandler.argtypes = [IedConnection, String]
    IedConnection_uninstallReportHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1271
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_triggerGIReport", "cdecl"):
    IedConnection_triggerGIReport = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_triggerGIReport", "cdecl")
    IedConnection_triggerGIReport.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_triggerGIReport.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1285
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataSetName", "cdecl"):
    ClientReport_getDataSetName = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataSetName", "cdecl")
    ClientReport_getDataSetName.argtypes = [ClientReport]
    ClientReport_getDataSetName.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1298
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataSetValues", "cdecl"):
    ClientReport_getDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataSetValues", "cdecl")
    ClientReport_getDataSetValues.argtypes = [ClientReport]
    ClientReport_getDataSetValues.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1307
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getRcbReference", "cdecl"):
    ClientReport_getRcbReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getRcbReference", "cdecl")
    ClientReport_getRcbReference.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRcbReference.restype = ReturnString
    else:
        ClientReport_getRcbReference.restype = String
        ClientReport_getRcbReference.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1316
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getRptId", "cdecl"):
    ClientReport_getRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getRptId", "cdecl")
    ClientReport_getRptId.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRptId.restype = ReturnString
    else:
        ClientReport_getRptId.restype = String
        ClientReport_getRptId.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1328
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getReasonForInclusion", "cdecl"):
    ClientReport_getReasonForInclusion = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getReasonForInclusion", "cdecl")
    ClientReport_getReasonForInclusion.argtypes = [ClientReport, c_int]
    ClientReport_getReasonForInclusion.restype = ReasonForInclusion

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1339
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getEntryId", "cdecl"):
    ClientReport_getEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getEntryId", "cdecl")
    ClientReport_getEntryId.argtypes = [ClientReport]
    ClientReport_getEntryId.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1350
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasTimestamp", "cdecl"):
    ClientReport_hasTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasTimestamp", "cdecl")
    ClientReport_hasTimestamp.argtypes = [ClientReport]
    ClientReport_hasTimestamp.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1360
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasSeqNum", "cdecl"):
    ClientReport_hasSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasSeqNum", "cdecl")
    ClientReport_hasSeqNum.argtypes = [ClientReport]
    ClientReport_hasSeqNum.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1372
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getSeqNum", "cdecl"):
    ClientReport_getSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getSeqNum", "cdecl")
    ClientReport_getSeqNum.argtypes = [ClientReport]
    ClientReport_getSeqNum.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1382
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasDataSetName", "cdecl"):
    ClientReport_hasDataSetName = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasDataSetName", "cdecl")
    ClientReport_hasDataSetName.argtypes = [ClientReport]
    ClientReport_hasDataSetName.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1392
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasReasonForInclusion", "cdecl"):
    ClientReport_hasReasonForInclusion = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasReasonForInclusion", "cdecl")
    ClientReport_hasReasonForInclusion.argtypes = [ClientReport]
    ClientReport_hasReasonForInclusion.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1402
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasConfRev", "cdecl"):
    ClientReport_hasConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasConfRev", "cdecl")
    ClientReport_hasConfRev.argtypes = [ClientReport]
    ClientReport_hasConfRev.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1414
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getConfRev", "cdecl"):
    ClientReport_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getConfRev", "cdecl")
    ClientReport_getConfRev.argtypes = [ClientReport]
    ClientReport_getConfRev.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1424
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasBufOvfl", "cdecl"):
    ClientReport_hasBufOvfl = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasBufOvfl", "cdecl")
    ClientReport_hasBufOvfl.argtypes = [ClientReport]
    ClientReport_hasBufOvfl.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1434
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getBufOvfl", "cdecl"):
    ClientReport_getBufOvfl = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getBufOvfl", "cdecl")
    ClientReport_getBufOvfl.argtypes = [ClientReport]
    ClientReport_getBufOvfl.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1444
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasDataReference", "cdecl"):
    ClientReport_hasDataReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasDataReference", "cdecl")
    ClientReport_hasDataReference.argtypes = [ClientReport]
    ClientReport_hasDataReference.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1459
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataReference", "cdecl"):
    ClientReport_getDataReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataReference", "cdecl")
    ClientReport_getDataReference.argtypes = [ClientReport, c_int]
    ClientReport_getDataReference.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1474
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getTimestamp", "cdecl"):
    ClientReport_getTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getTimestamp", "cdecl")
    ClientReport_getTimestamp.argtypes = [ClientReport]
    ClientReport_getTimestamp.restype = c_uint64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1484
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasSubSeqNum", "cdecl"):
    ClientReport_hasSubSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasSubSeqNum", "cdecl")
    ClientReport_hasSubSeqNum.argtypes = [ClientReport]
    ClientReport_hasSubSeqNum.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1497
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getSubSeqNum", "cdecl"):
    ClientReport_getSubSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getSubSeqNum", "cdecl")
    ClientReport_getSubSeqNum.argtypes = [ClientReport]
    ClientReport_getSubSeqNum.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1510
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getMoreSeqmentsFollow", "cdecl"):
    ClientReport_getMoreSeqmentsFollow = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getMoreSeqmentsFollow", "cdecl")
    ClientReport_getMoreSeqmentsFollow.argtypes = [ClientReport]
    ClientReport_getMoreSeqmentsFollow.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1519
if _libs["/usr/local/lib/libiec61850.so"].has("ReasonForInclusion_getValueAsString", "cdecl"):
    ReasonForInclusion_getValueAsString = _libs["/usr/local/lib/libiec61850.so"].get("ReasonForInclusion_getValueAsString", "cdecl")
    ReasonForInclusion_getValueAsString.argtypes = [ReasonForInclusion]
    if sizeof(c_int) == sizeof(c_void_p):
        ReasonForInclusion_getValueAsString.restype = ReturnString
    else:
        ReasonForInclusion_getValueAsString.restype = String
        ReasonForInclusion_getValueAsString.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1527
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_create", "cdecl"):
    ClientReportControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_create", "cdecl")
    ClientReportControlBlock_create.argtypes = [String]
    ClientReportControlBlock_create.restype = ClientReportControlBlock

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1530
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_destroy", "cdecl"):
    ClientReportControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_destroy", "cdecl")
    ClientReportControlBlock_destroy.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1532
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getObjectReference", "cdecl"):
    ClientReportControlBlock_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getObjectReference", "cdecl")
    ClientReportControlBlock_getObjectReference.argtypes = [ClientReportControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReportControlBlock_getObjectReference.restype = ReturnString
    else:
        ClientReportControlBlock_getObjectReference.restype = String
        ClientReportControlBlock_getObjectReference.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1536
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_isBuffered", "cdecl"):
    ClientReportControlBlock_isBuffered = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_isBuffered", "cdecl")
    ClientReportControlBlock_isBuffered.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_isBuffered.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1538
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getRptId", "cdecl"):
    ClientReportControlBlock_getRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getRptId", "cdecl")
    ClientReportControlBlock_getRptId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptId.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1542
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setRptId", "cdecl"):
    ClientReportControlBlock_setRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setRptId", "cdecl")
    ClientReportControlBlock_setRptId.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setRptId.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1545
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getRptEna", "cdecl"):
    ClientReportControlBlock_getRptEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getRptEna", "cdecl")
    ClientReportControlBlock_getRptEna.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptEna.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1548
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setRptEna", "cdecl"):
    ClientReportControlBlock_setRptEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setRptEna", "cdecl")
    ClientReportControlBlock_setRptEna.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setRptEna.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1551
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getResv", "cdecl"):
    ClientReportControlBlock_getResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getResv", "cdecl")
    ClientReportControlBlock_getResv.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResv.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1554
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setResv", "cdecl"):
    ClientReportControlBlock_setResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setResv", "cdecl")
    ClientReportControlBlock_setResv.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setResv.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1556
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getDataSetReference", "cdecl"):
    ClientReportControlBlock_getDataSetReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getDataSetReference", "cdecl")
    ClientReportControlBlock_getDataSetReference.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getDataSetReference.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1576
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setDataSetReference", "cdecl"):
    ClientReportControlBlock_setDataSetReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setDataSetReference", "cdecl")
    ClientReportControlBlock_setDataSetReference.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setDataSetReference.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1579
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getConfRev", "cdecl"):
    ClientReportControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getConfRev", "cdecl")
    ClientReportControlBlock_getConfRev.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getConfRev.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1588
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getOptFlds", "cdecl"):
    ClientReportControlBlock_getOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getOptFlds", "cdecl")
    ClientReportControlBlock_getOptFlds.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOptFlds.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1597
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setOptFlds", "cdecl"):
    ClientReportControlBlock_setOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setOptFlds", "cdecl")
    ClientReportControlBlock_setOptFlds.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setOptFlds.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1608
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getBufTm", "cdecl"):
    ClientReportControlBlock_getBufTm = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getBufTm", "cdecl")
    ClientReportControlBlock_getBufTm.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getBufTm.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1620
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setBufTm", "cdecl"):
    ClientReportControlBlock_setBufTm = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setBufTm", "cdecl")
    ClientReportControlBlock_setBufTm.argtypes = [ClientReportControlBlock, c_uint32]
    ClientReportControlBlock_setBufTm.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1623
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getSqNum", "cdecl"):
    ClientReportControlBlock_getSqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getSqNum", "cdecl")
    ClientReportControlBlock_getSqNum.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getSqNum.restype = c_uint16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1626
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getTrgOps", "cdecl"):
    ClientReportControlBlock_getTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getTrgOps", "cdecl")
    ClientReportControlBlock_getTrgOps.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getTrgOps.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1629
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setTrgOps", "cdecl"):
    ClientReportControlBlock_setTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setTrgOps", "cdecl")
    ClientReportControlBlock_setTrgOps.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setTrgOps.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1632
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getIntgPd", "cdecl"):
    ClientReportControlBlock_getIntgPd = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getIntgPd", "cdecl")
    ClientReportControlBlock_getIntgPd.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getIntgPd.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1635
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setIntgPd", "cdecl"):
    ClientReportControlBlock_setIntgPd = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setIntgPd", "cdecl")
    ClientReportControlBlock_setIntgPd.argtypes = [ClientReportControlBlock, c_uint32]
    ClientReportControlBlock_setIntgPd.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1638
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getGI", "cdecl"):
    ClientReportControlBlock_getGI = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getGI", "cdecl")
    ClientReportControlBlock_getGI.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getGI.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1641
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setGI", "cdecl"):
    ClientReportControlBlock_setGI = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setGI", "cdecl")
    ClientReportControlBlock_setGI.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setGI.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1644
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getPurgeBuf", "cdecl"):
    ClientReportControlBlock_getPurgeBuf = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getPurgeBuf", "cdecl")
    ClientReportControlBlock_getPurgeBuf.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getPurgeBuf.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1654
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setPurgeBuf", "cdecl"):
    ClientReportControlBlock_setPurgeBuf = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setPurgeBuf", "cdecl")
    ClientReportControlBlock_setPurgeBuf.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setPurgeBuf.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1662
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_hasResvTms", "cdecl"):
    ClientReportControlBlock_hasResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_hasResvTms", "cdecl")
    ClientReportControlBlock_hasResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_hasResvTms.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1665
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getResvTms", "cdecl"):
    ClientReportControlBlock_getResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getResvTms", "cdecl")
    ClientReportControlBlock_getResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResvTms.restype = c_int16

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1668
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setResvTms", "cdecl"):
    ClientReportControlBlock_setResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setResvTms", "cdecl")
    ClientReportControlBlock_setResvTms.argtypes = [ClientReportControlBlock, c_int16]
    ClientReportControlBlock_setResvTms.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1670
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getEntryId", "cdecl"):
    ClientReportControlBlock_getEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getEntryId", "cdecl")
    ClientReportControlBlock_getEntryId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryId.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1674
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setEntryId", "cdecl"):
    ClientReportControlBlock_setEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setEntryId", "cdecl")
    ClientReportControlBlock_setEntryId.argtypes = [ClientReportControlBlock, POINTER(MmsValue)]
    ClientReportControlBlock_setEntryId.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1677
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getEntryTime", "cdecl"):
    ClientReportControlBlock_getEntryTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getEntryTime", "cdecl")
    ClientReportControlBlock_getEntryTime.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryTime.restype = c_uint64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1679
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getOwner", "cdecl"):
    ClientReportControlBlock_getOwner = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getOwner", "cdecl")
    ClientReportControlBlock_getOwner.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOwner.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1713
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readDataSetValues", "cdecl"):
    IedConnection_readDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readDataSetValues", "cdecl")
    IedConnection_readDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet]
    IedConnection_readDataSetValues.restype = ClientDataSet

IedConnection_ReadDataSetHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, ClientDataSet)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1716

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1738
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readDataSetValuesAsync", "cdecl"):
    IedConnection_readDataSetValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readDataSetValuesAsync", "cdecl")
    IedConnection_readDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet, IedConnection_ReadDataSetHandler, POINTER(None)]
    IedConnection_readDataSetValuesAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1759
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createDataSet", "cdecl"):
    IedConnection_createDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createDataSet", "cdecl")
    IedConnection_createDataSet.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList]
    IedConnection_createDataSet.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1775
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteDataSet", "cdecl"):
    IedConnection_deleteDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteDataSet", "cdecl")
    IedConnection_deleteDataSet.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteDataSet.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1793
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataSetDirectory", "cdecl"):
    IedConnection_getDataSetDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataSetDirectory", "cdecl")
    IedConnection_getDataSetDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(c_bool)]
    IedConnection_getDataSetDirectory.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1811
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeDataSetValues", "cdecl"):
    IedConnection_writeDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeDataSetValues", "cdecl")
    IedConnection_writeDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, POINTER(LinkedList)]
    IedConnection_writeDataSetValues.restype = None

IedConnection_WriteDataSetHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, LinkedList)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1823

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1847
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeDataSetValuesAsync", "cdecl"):
    IedConnection_writeDataSetValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeDataSetValuesAsync", "cdecl")
    IedConnection_writeDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_WriteDataSetHandler, POINTER(None)]
    IedConnection_writeDataSetValuesAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1864
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_destroy", "cdecl"):
    ClientDataSet_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_destroy", "cdecl")
    ClientDataSet_destroy.argtypes = [ClientDataSet]
    ClientDataSet_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1880
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getValues", "cdecl"):
    ClientDataSet_getValues = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getValues", "cdecl")
    ClientDataSet_getValues.argtypes = [ClientDataSet]
    ClientDataSet_getValues.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1890
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getReference", "cdecl"):
    ClientDataSet_getReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getReference", "cdecl")
    ClientDataSet_getReference.argtypes = [ClientDataSet]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientDataSet_getReference.restype = ReturnString
    else:
        ClientDataSet_getReference.restype = String
        ClientDataSet_getReference.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1901
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getDataSetSize", "cdecl"):
    ClientDataSet_getDataSetSize = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getDataSetSize", "cdecl")
    ClientDataSet_getDataSetSize.argtypes = [ClientDataSet]
    ClientDataSet_getDataSetSize.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1915
class struct_sControlObjectClient(Structure):
    pass

ControlObjectClient = POINTER(struct_sControlObjectClient)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1915

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1934
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_create", "cdecl"):
    ControlObjectClient_create = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_create", "cdecl")
    ControlObjectClient_create.argtypes = [String, IedConnection]
    ControlObjectClient_create.restype = ControlObjectClient

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1949
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_createEx", "cdecl"):
    ControlObjectClient_createEx = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_createEx", "cdecl")
    ControlObjectClient_createEx.argtypes = [String, IedConnection, ControlModel, POINTER(MmsVariableSpecification)]
    ControlObjectClient_createEx.restype = ControlObjectClient

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1957
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_destroy", "cdecl"):
    ControlObjectClient_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_destroy", "cdecl")
    ControlObjectClient_destroy.argtypes = [ControlObjectClient]
    ControlObjectClient_destroy.restype = None

enum_anon_45 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1964

CONTROL_ACTION_TYPE_SELECT = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1964

CONTROL_ACTION_TYPE_OPERATE = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1964

CONTROL_ACTION_TYPE_CANCEL = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1964

ControlActionType = enum_anon_45# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1964

ControlObjectClient_ControlActionHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, ControlActionType, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1968

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1977
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getObjectReference", "cdecl"):
    ControlObjectClient_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getObjectReference", "cdecl")
    ControlObjectClient_getObjectReference.argtypes = [ControlObjectClient]
    ControlObjectClient_getObjectReference.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1988
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getControlModel", "cdecl"):
    ControlObjectClient_getControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getControlModel", "cdecl")
    ControlObjectClient_getControlModel.argtypes = [ControlObjectClient]
    ControlObjectClient_getControlModel.restype = ControlModel

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1999
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setControlModel", "cdecl"):
    ControlObjectClient_setControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setControlModel", "cdecl")
    ControlObjectClient_setControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_setControlModel.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2011
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_changeServerControlModel", "cdecl"):
    ControlObjectClient_changeServerControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_changeServerControlModel", "cdecl")
    ControlObjectClient_changeServerControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_changeServerControlModel.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2024
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getCtlValType", "cdecl"):
    ControlObjectClient_getCtlValType = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getCtlValType", "cdecl")
    ControlObjectClient_getCtlValType.argtypes = [ControlObjectClient]
    ControlObjectClient_getCtlValType.restype = MmsType

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2034
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getLastError", "cdecl"):
    ControlObjectClient_getLastError = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getLastError", "cdecl")
    ControlObjectClient_getLastError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastError.restype = IedClientError

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2047
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_operate", "cdecl"):
    ControlObjectClient_operate = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_operate", "cdecl")
    ControlObjectClient_operate.argtypes = [ControlObjectClient, POINTER(MmsValue), c_uint64]
    ControlObjectClient_operate.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2060
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_select", "cdecl"):
    ControlObjectClient_select = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_select", "cdecl")
    ControlObjectClient_select.argtypes = [ControlObjectClient]
    ControlObjectClient_select.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2074
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectWithValue", "cdecl"):
    ControlObjectClient_selectWithValue = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectWithValue", "cdecl")
    ControlObjectClient_selectWithValue.argtypes = [ControlObjectClient, POINTER(MmsValue)]
    ControlObjectClient_selectWithValue.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2087
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_cancel", "cdecl"):
    ControlObjectClient_cancel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_cancel", "cdecl")
    ControlObjectClient_cancel.argtypes = [ControlObjectClient]
    ControlObjectClient_cancel.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2104
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_operateAsync", "cdecl"):
    ControlObjectClient_operateAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_operateAsync", "cdecl")
    ControlObjectClient_operateAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), c_uint64, ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_operateAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2121
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectAsync", "cdecl"):
    ControlObjectClient_selectAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectAsync", "cdecl")
    ControlObjectClient_selectAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2138
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectWithValueAsync", "cdecl"):
    ControlObjectClient_selectWithValueAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectWithValueAsync", "cdecl")
    ControlObjectClient_selectWithValueAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectWithValueAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2155
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_cancelAsync", "cdecl"):
    ControlObjectClient_cancelAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_cancelAsync", "cdecl")
    ControlObjectClient_cancelAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_cancelAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2165
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getLastApplError", "cdecl"):
    ControlObjectClient_getLastApplError = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getLastApplError", "cdecl")
    ControlObjectClient_getLastApplError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastApplError.restype = LastApplError

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2177
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setTestMode", "cdecl"):
    ControlObjectClient_setTestMode = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setTestMode", "cdecl")
    ControlObjectClient_setTestMode.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setTestMode.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2190
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setOrigin", "cdecl"):
    ControlObjectClient_setOrigin = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setOrigin", "cdecl")
    ControlObjectClient_setOrigin.argtypes = [ControlObjectClient, String, c_int]
    ControlObjectClient_setOrigin.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2201
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_useConstantT", "cdecl"):
    ControlObjectClient_useConstantT = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_useConstantT", "cdecl")
    ControlObjectClient_useConstantT.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_useConstantT.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2207
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_enableInterlockCheck", "cdecl"):
    ControlObjectClient_enableInterlockCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_enableInterlockCheck", "cdecl")
    ControlObjectClient_enableInterlockCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableInterlockCheck.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2213
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_enableSynchroCheck", "cdecl"):
    ControlObjectClient_enableSynchroCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_enableSynchroCheck", "cdecl")
    ControlObjectClient_enableSynchroCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableSynchroCheck.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2222
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setInterlockCheck", "cdecl"):
    ControlObjectClient_setInterlockCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setInterlockCheck", "cdecl")
    ControlObjectClient_setInterlockCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setInterlockCheck.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2231
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setSynchroCheck", "cdecl"):
    ControlObjectClient_setSynchroCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setSynchroCheck", "cdecl")
    ControlObjectClient_setSynchroCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setSynchroCheck.restype = None

CommandTerminationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), ControlObjectClient)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2244

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2258
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setCommandTerminationHandler", "cdecl"):
    ControlObjectClient_setCommandTerminationHandler = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setCommandTerminationHandler", "cdecl")
    ControlObjectClient_setCommandTerminationHandler.argtypes = [ControlObjectClient, CommandTerminationHandler, POINTER(None)]
    ControlObjectClient_setCommandTerminationHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2284
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDeviceModelFromServer", "cdecl"):
    IedConnection_getDeviceModelFromServer = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDeviceModelFromServer", "cdecl")
    IedConnection_getDeviceModelFromServer.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getDeviceModelFromServer.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2300
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceList", "cdecl"):
    IedConnection_getLogicalDeviceList = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceList", "cdecl")
    IedConnection_getLogicalDeviceList.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getLogicalDeviceList.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2319
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getServerDirectory", "cdecl"):
    IedConnection_getServerDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getServerDirectory", "cdecl")
    IedConnection_getServerDirectory.argtypes = [IedConnection, POINTER(IedClientError), c_bool]
    IedConnection_getServerDirectory.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2337
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDirectory", "cdecl"):
    IedConnection_getLogicalDeviceDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDirectory", "cdecl")
    IedConnection_getLogicalDeviceDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDirectory.restype = LinkedList

enum_anon_46 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_DATA_OBJECT = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_DATA_SET = (ACSI_CLASS_DATA_OBJECT + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_BRCB = (ACSI_CLASS_DATA_SET + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_URCB = (ACSI_CLASS_BRCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_LCB = (ACSI_CLASS_URCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_LOG = (ACSI_CLASS_LCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_SGCB = (ACSI_CLASS_LOG + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_GoCB = (ACSI_CLASS_SGCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_GsCB = (ACSI_CLASS_GoCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_MSVCB = (ACSI_CLASS_GsCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSI_CLASS_USVCB = (ACSI_CLASS_MSVCB + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

ACSIClass = enum_anon_46# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2351

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2369
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalNodeVariables", "cdecl"):
    IedConnection_getLogicalNodeVariables = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalNodeVariables", "cdecl")
    IedConnection_getLogicalNodeVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalNodeVariables.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2389
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalNodeDirectory", "cdecl"):
    IedConnection_getLogicalNodeDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalNodeDirectory", "cdecl")
    IedConnection_getLogicalNodeDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, ACSIClass]
    IedConnection_getLogicalNodeDirectory.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2408
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectory", "cdecl"):
    IedConnection_getDataDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectory", "cdecl")
    IedConnection_getDataDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectory.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2427
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectoryFC", "cdecl"):
    IedConnection_getDataDirectoryFC = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectoryFC", "cdecl")
    IedConnection_getDataDirectoryFC.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectoryFC.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2449
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectoryByFC", "cdecl"):
    IedConnection_getDataDirectoryByFC = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectoryByFC", "cdecl")
    IedConnection_getDataDirectoryByFC.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getDataDirectoryByFC.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2466
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getVariableSpecification", "cdecl"):
    IedConnection_getVariableSpecification = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getVariableSpecification", "cdecl")
    IedConnection_getVariableSpecification.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getVariableSpecification.restype = POINTER(MmsVariableSpecification)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2483
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceVariables", "cdecl"):
    IedConnection_getLogicalDeviceVariables = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceVariables", "cdecl")
    IedConnection_getLogicalDeviceVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceVariables.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2498
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDataSets", "cdecl"):
    IedConnection_getLogicalDeviceDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDataSets", "cdecl")
    IedConnection_getLogicalDeviceDataSets.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDataSets.restype = LinkedList

IedConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, LinkedList, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2505

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2520
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getServerDirectoryAsync", "cdecl"):
    IedConnection_getServerDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getServerDirectoryAsync", "cdecl")
    IedConnection_getServerDirectoryAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getServerDirectoryAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2540
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceVariablesAsync", "cdecl"):
    IedConnection_getLogicalDeviceVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceVariablesAsync", "cdecl")
    IedConnection_getLogicalDeviceVariablesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceVariablesAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2560
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl"):
    IedConnection_getLogicalDeviceDataSetsAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl")
    IedConnection_getLogicalDeviceDataSetsAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceDataSetsAsync.restype = c_uint32

IedConnection_GetVariableSpecificationHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, POINTER(MmsVariableSpecification))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2565

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2579
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getVariableSpecificationAsync", "cdecl"):
    IedConnection_getVariableSpecificationAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getVariableSpecificationAsync", "cdecl")
    IedConnection_getVariableSpecificationAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_GetVariableSpecificationHandler, POINTER(None)]
    IedConnection_getVariableSpecificationAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2608
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogByTime", "cdecl"):
    IedConnection_queryLogByTime = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogByTime", "cdecl")
    IedConnection_queryLogByTime.argtypes = [IedConnection, POINTER(IedClientError), String, c_uint64, c_uint64, POINTER(c_bool)]
    IedConnection_queryLogByTime.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2629
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogAfter", "cdecl"):
    IedConnection_queryLogAfter = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogAfter", "cdecl")
    IedConnection_queryLogAfter.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), c_uint64, POINTER(c_bool)]
    IedConnection_queryLogAfter.restype = LinkedList

IedConnection_QueryLogHandler = CFUNCTYPE(UNCHECKED(None), c_uint32, POINTER(None), IedClientError, LinkedList, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2634

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2637
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogByTimeAsync", "cdecl"):
    IedConnection_queryLogByTimeAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogByTimeAsync", "cdecl")
    IedConnection_queryLogByTimeAsync.argtypes = [IedConnection, POINTER(IedClientError), String, c_uint64, c_uint64, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogByTimeAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2641
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogAfterAsync", "cdecl"):
    IedConnection_queryLogAfterAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogAfterAsync", "cdecl")
    IedConnection_queryLogAfterAsync.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), c_uint64, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogAfterAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2652
class struct_sFileDirectoryEntry(Structure):
    pass

FileDirectoryEntry = POINTER(struct_sFileDirectoryEntry)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2652

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2658
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_create", "cdecl"):
    FileDirectoryEntry_create = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_create", "cdecl")
    FileDirectoryEntry_create.argtypes = [String, c_uint32, c_uint64]
    FileDirectoryEntry_create.restype = FileDirectoryEntry

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2668
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_destroy", "cdecl"):
    FileDirectoryEntry_destroy = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_destroy", "cdecl")
    FileDirectoryEntry_destroy.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2677
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getFileName", "cdecl"):
    FileDirectoryEntry_getFileName = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getFileName", "cdecl")
    FileDirectoryEntry_getFileName.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileName.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2688
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getFileSize", "cdecl"):
    FileDirectoryEntry_getFileSize = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getFileSize", "cdecl")
    FileDirectoryEntry_getFileSize.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileSize.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2698
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getLastModified", "cdecl"):
    FileDirectoryEntry_getLastModified = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getLastModified", "cdecl")
    FileDirectoryEntry_getLastModified.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getLastModified.restype = c_uint64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2720
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectory", "cdecl"):
    IedConnection_getFileDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectory", "cdecl")
    IedConnection_getFileDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getFileDirectory.restype = LinkedList

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2751
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectoryEx", "cdecl"):
    IedConnection_getFileDirectoryEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectoryEx", "cdecl")
    IedConnection_getFileDirectoryEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, POINTER(c_bool)]
    IedConnection_getFileDirectoryEx.restype = LinkedList

IedConnection_FileDirectoryEntryHandler = CFUNCTYPE(UNCHECKED(c_bool), c_uint32, POINTER(None), IedClientError, String, c_uint32, c_uint64, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2779

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2801
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectoryAsyncEx", "cdecl"):
    IedConnection_getFileDirectoryAsyncEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectoryAsyncEx", "cdecl")
    IedConnection_getFileDirectoryAsyncEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_FileDirectoryEntryHandler, POINTER(None)]
    IedConnection_getFileDirectoryAsyncEx.restype = c_uint32

IedClientGetFileHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(c_uint8), c_uint32)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2819

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2833
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFile", "cdecl"):
    IedConnection_getFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFile", "cdecl")
    IedConnection_getFile.argtypes = [IedConnection, POINTER(IedClientError), String, IedClientGetFileHandler, POINTER(None)]
    IedConnection_getFile.restype = c_uint32

IedConnection_GetFileAsyncHandler = CFUNCTYPE(UNCHECKED(c_bool), c_uint32, POINTER(None), IedClientError, c_uint32, POINTER(c_uint8), c_uint32, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2854

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2875
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileAsync", "cdecl"):
    IedConnection_getFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileAsync", "cdecl")
    IedConnection_getFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GetFileAsyncHandler, POINTER(None)]
    IedConnection_getFileAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2889
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFilestoreBasepath", "cdecl"):
    IedConnection_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFilestoreBasepath", "cdecl")
    IedConnection_setFilestoreBasepath.argtypes = [IedConnection, String]
    IedConnection_setFilestoreBasepath.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2902
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFile", "cdecl"):
    IedConnection_setFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFile", "cdecl")
    IedConnection_setFile.argtypes = [IedConnection, POINTER(IedClientError), String, String]
    IedConnection_setFile.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2917
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFileAsync", "cdecl"):
    IedConnection_setFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFileAsync", "cdecl")
    IedConnection_setFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setFileAsync.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2930
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteFile", "cdecl"):
    IedConnection_deleteFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteFile", "cdecl")
    IedConnection_deleteFile.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteFile.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2944
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteFileAsync", "cdecl"):
    IedConnection_deleteFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteFileAsync", "cdecl")
    IedConnection_deleteFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_deleteFileAsync.restype = c_uint32

# /usr/local/include/libiec61850/mms_server.h: 44
class struct_sMmsServer(Structure):
    pass

MmsServer = POINTER(struct_sMmsServer)# /usr/local/include/libiec61850/mms_server.h: 44

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 191
class struct_sModelNode(Structure):
    pass

ModelNode = struct_sModelNode# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 46

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 217
class struct_sDataAttribute(Structure):
    pass

DataAttribute = struct_sDataAttribute# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 51

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 207
class struct_sDataObject(Structure):
    pass

DataObject = struct_sDataObject# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 56

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 199
class struct_sLogicalNode(Structure):
    pass

LogicalNode = struct_sLogicalNode# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 61

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 183
class struct_sLogicalDevice(Structure):
    pass

LogicalDevice = struct_sLogicalDevice# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 66

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 170
class struct_sIedModel(Structure):
    pass

IedModel = struct_sIedModel# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 71

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 246
class struct_sDataSet(Structure):
    pass

DataSet = struct_sDataSet# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 73

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 254
class struct_sReportControlBlock(Structure):
    pass

ReportControlBlock = struct_sReportControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 74

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 299
class struct_sSettingGroupControlBlock(Structure):
    pass

SettingGroupControlBlock = struct_sSettingGroupControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 79

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 313
class struct_sGSEControlBlock(Structure):
    pass

GSEControlBlock = struct_sGSEControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 81

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 326
class struct_sSVControlBlock(Structure):
    pass

SVControlBlock = struct_sSVControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 83

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 274
class struct_sLogControlBlock(Structure):
    pass

LogControlBlock = struct_sLogControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 85

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 291
class struct_sLog(Structure):
    pass

Log = struct_sLog# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 87

enum_anon_50 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_BOOLEAN = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT8 = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT16 = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT32 = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT64 = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT128 = 5# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT8U = 6# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT16U = 7# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT24U = 8# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_INT32U = 9# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_FLOAT32 = 10# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_FLOAT64 = 11# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_ENUMERATED = 12# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_OCTET_STRING_64 = 13# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_OCTET_STRING_6 = 14# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_OCTET_STRING_8 = 15# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_VISIBLE_STRING_32 = 16# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_VISIBLE_STRING_64 = 17# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_VISIBLE_STRING_65 = 18# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_VISIBLE_STRING_129 = 19# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_VISIBLE_STRING_255 = 20# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_UNICODE_STRING_255 = 21# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_TIMESTAMP = 22# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_QUALITY = 23# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_CHECK = 24# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_CODEDENUM = 25# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_GENERIC_BITSTRING = 26# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_CONSTRUCTED = 27# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_ENTRY_TIME = 28# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_PHYCOMADDR = 29# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_CURRENCY = 30# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_OPTFLDS = 31# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

IEC61850_TRGOPS = 32# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

DataAttributeType = enum_anon_50# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 161

enum_anon_51 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

LogicalDeviceModelType = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

LogicalNodeModelType = (LogicalDeviceModelType + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

DataObjectModelType = (LogicalNodeModelType + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

DataAttributeModelType = (DataObjectModelType + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

ModelNodeType = enum_anon_51# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 168

struct_sIedModel.__slots__ = [
    'name',
    'firstChild',
    'dataSets',
    'rcbs',
    'gseCBs',
    'svCBs',
    'sgcbs',
    'lcbs',
    'logs',
    'initializer',
]
struct_sIedModel._fields_ = [
    ('name', String),
    ('firstChild', POINTER(LogicalDevice)),
    ('dataSets', POINTER(DataSet)),
    ('rcbs', POINTER(ReportControlBlock)),
    ('gseCBs', POINTER(GSEControlBlock)),
    ('svCBs', POINTER(SVControlBlock)),
    ('sgcbs', POINTER(SettingGroupControlBlock)),
    ('lcbs', POINTER(LogControlBlock)),
    ('logs', POINTER(Log)),
    ('initializer', CFUNCTYPE(UNCHECKED(None), )),
]

struct_sLogicalDevice.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sLogicalDevice._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sModelNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sModelNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sLogicalNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sLogicalNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sDataObject.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
]
struct_sDataObject._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
]

struct_sDataAttribute.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
    'fc',
    'type',
    'triggerOptions',
    'mmsValue',
    'sAddr',
]
struct_sDataAttribute._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
    ('fc', FunctionalConstraint),
    ('type', DataAttributeType),
    ('triggerOptions', c_uint8),
    ('mmsValue', POINTER(MmsValue)),
    ('sAddr', c_uint32),
]

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 236
class struct_sDataSetEntry(Structure):
    pass

struct_sDataSetEntry.__slots__ = [
    'logicalDeviceName',
    'isLDNameDynamicallyAllocated',
    'variableName',
    'index',
    'componentName',
    'value',
    'sibling',
]
struct_sDataSetEntry._fields_ = [
    ('logicalDeviceName', String),
    ('isLDNameDynamicallyAllocated', c_bool),
    ('variableName', String),
    ('index', c_int),
    ('componentName', String),
    ('value', POINTER(MmsValue)),
    ('sibling', POINTER(struct_sDataSetEntry)),
]

DataSetEntry = struct_sDataSetEntry# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 244

struct_sDataSet.__slots__ = [
    'logicalDeviceName',
    'name',
    'elementCount',
    'fcdas',
    'sibling',
]
struct_sDataSet._fields_ = [
    ('logicalDeviceName', String),
    ('name', String),
    ('elementCount', c_int),
    ('fcdas', POINTER(DataSetEntry)),
    ('sibling', POINTER(DataSet)),
]

struct_sReportControlBlock.__slots__ = [
    'parent',
    'name',
    'rptId',
    'buffered',
    'dataSetName',
    'confRef',
    'trgOps',
    'options',
    'bufferTime',
    'intPeriod',
    'clientReservation',
    'sibling',
]
struct_sReportControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('rptId', String),
    ('buffered', c_bool),
    ('dataSetName', String),
    ('confRef', c_uint32),
    ('trgOps', c_uint8),
    ('options', c_uint8),
    ('bufferTime', c_uint32),
    ('intPeriod', c_uint32),
    ('clientReservation', c_uint8 * int(17)),
    ('sibling', POINTER(ReportControlBlock)),
]

struct_sLogControlBlock.__slots__ = [
    'parent',
    'name',
    'dataSetName',
    'logRef',
    'trgOps',
    'intPeriod',
    'logEna',
    'reasonCode',
    'sibling',
]
struct_sLogControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('dataSetName', String),
    ('logRef', String),
    ('trgOps', c_uint8),
    ('intPeriod', c_uint32),
    ('logEna', c_bool),
    ('reasonCode', c_bool),
    ('sibling', POINTER(LogControlBlock)),
]

struct_sLog.__slots__ = [
    'parent',
    'name',
    'sibling',
]
struct_sLog._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('sibling', POINTER(Log)),
]

struct_sSettingGroupControlBlock.__slots__ = [
    'parent',
    'actSG',
    'numOfSGs',
    'editSG',
    'cnfEdit',
    'timestamp',
    'resvTms',
    'sibling',
]
struct_sSettingGroupControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('actSG', c_uint8),
    ('numOfSGs', c_uint8),
    ('editSG', c_uint8),
    ('cnfEdit', c_bool),
    ('timestamp', c_uint64),
    ('resvTms', c_uint16),
    ('sibling', POINTER(SettingGroupControlBlock)),
]

struct_sGSEControlBlock.__slots__ = [
    'parent',
    'name',
    'appId',
    'dataSetName',
    'confRev',
    'fixedOffs',
    'address',
    'minTime',
    'maxTime',
    'sibling',
]
struct_sGSEControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('appId', String),
    ('dataSetName', String),
    ('confRev', c_uint32),
    ('fixedOffs', c_bool),
    ('address', POINTER(PhyComAddress)),
    ('minTime', c_int),
    ('maxTime', c_int),
    ('sibling', POINTER(GSEControlBlock)),
]

struct_sSVControlBlock.__slots__ = [
    'parent',
    'name',
    'svId',
    'dataSetName',
    'optFlds',
    'smpMod',
    'smpRate',
    'confRev',
    'dstAddress',
    'isUnicast',
    'noASDU',
    'sibling',
]
struct_sSVControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('svId', String),
    ('dataSetName', String),
    ('optFlds', c_uint8),
    ('smpMod', c_uint8),
    ('smpRate', c_uint16),
    ('confRev', c_uint32),
    ('dstAddress', POINTER(PhyComAddress)),
    ('isUnicast', c_bool),
    ('noASDU', c_int),
    ('sibling', POINTER(SVControlBlock)),
]

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 358
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChildCount", "cdecl"):
    ModelNode_getChildCount = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChildCount", "cdecl")
    ModelNode_getChildCount.argtypes = [POINTER(ModelNode)]
    ModelNode_getChildCount.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 368
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChild", "cdecl"):
    ModelNode_getChild = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChild", "cdecl")
    ModelNode_getChild.argtypes = [POINTER(ModelNode), String]
    ModelNode_getChild.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 384
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChildWithFc", "cdecl"):
    ModelNode_getChildWithFc = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChildWithFc", "cdecl")
    ModelNode_getChildWithFc.argtypes = [POINTER(ModelNode), String, FunctionalConstraint]
    ModelNode_getChildWithFc.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 396
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getObjectReference", "cdecl"):
    ModelNode_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getObjectReference", "cdecl")
    ModelNode_getObjectReference.argtypes = [POINTER(ModelNode), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ModelNode_getObjectReference.restype = ReturnString
    else:
        ModelNode_getObjectReference.restype = String
        ModelNode_getObjectReference.errcheck = ReturnString

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 407
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getType", "cdecl"):
    ModelNode_getType = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getType", "cdecl")
    ModelNode_getType.argtypes = [POINTER(ModelNode)]
    ModelNode_getType.restype = ModelNodeType

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 419
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setIedName", "cdecl"):
    IedModel_setIedName = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setIedName", "cdecl")
    IedModel_setIedName.argtypes = [POINTER(IedModel), String]
    IedModel_setIedName.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 433
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByObjectReference", "cdecl"):
    IedModel_getModelNodeByObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByObjectReference", "cdecl")
    IedModel_getModelNodeByObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByObjectReference.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 436
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getSVControlBlock", "cdecl"):
    IedModel_getSVControlBlock = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getSVControlBlock", "cdecl")
    IedModel_getSVControlBlock.argtypes = [POINTER(IedModel), POINTER(LogicalNode), String]
    IedModel_getSVControlBlock.restype = POINTER(SVControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 451
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByShortObjectReference", "cdecl"):
    IedModel_getModelNodeByShortObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByShortObjectReference", "cdecl")
    IedModel_getModelNodeByShortObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByShortObjectReference.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 465
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByShortAddress", "cdecl"):
    IedModel_getModelNodeByShortAddress = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByShortAddress", "cdecl")
    IedModel_getModelNodeByShortAddress.argtypes = [POINTER(IedModel), c_uint32]
    IedModel_getModelNodeByShortAddress.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 476
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDeviceByInst", "cdecl"):
    IedModel_getDeviceByInst = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDeviceByInst", "cdecl")
    IedModel_getDeviceByInst.argtypes = [POINTER(IedModel), String]
    IedModel_getDeviceByInst.restype = POINTER(LogicalDevice)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 487
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDeviceByIndex", "cdecl"):
    IedModel_getDeviceByIndex = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDeviceByIndex", "cdecl")
    IedModel_getDeviceByIndex.argtypes = [POINTER(IedModel), c_int]
    IedModel_getDeviceByIndex.restype = POINTER(LogicalDevice)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 499
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getLogicalNode", "cdecl"):
    LogicalDevice_getLogicalNode = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getLogicalNode", "cdecl")
    LogicalDevice_getLogicalNode.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getLogicalNode.restype = POINTER(LogicalNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 509
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getSettingGroupControlBlock", "cdecl"):
    LogicalDevice_getSettingGroupControlBlock = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getSettingGroupControlBlock", "cdecl")
    LogicalDevice_getSettingGroupControlBlock.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getSettingGroupControlBlock.restype = POINTER(SettingGroupControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 523
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setAttributeValuesToNull", "cdecl"):
    IedModel_setAttributeValuesToNull = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setAttributeValuesToNull", "cdecl")
    IedModel_setAttributeValuesToNull.argtypes = [POINTER(IedModel)]
    IedModel_setAttributeValuesToNull.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 533
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDevice", "cdecl"):
    IedModel_getDevice = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDevice", "cdecl")
    IedModel_getDevice.argtypes = [POINTER(IedModel), String]
    IedModel_getDevice.restype = POINTER(LogicalDevice)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 544
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_lookupDataSet", "cdecl"):
    IedModel_lookupDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_lookupDataSet", "cdecl")
    IedModel_lookupDataSet.argtypes = [POINTER(IedModel), String]
    IedModel_lookupDataSet.restype = POINTER(DataSet)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 555
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_lookupDataAttributeByMmsValue", "cdecl"):
    IedModel_lookupDataAttributeByMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_lookupDataAttributeByMmsValue", "cdecl")
    IedModel_lookupDataAttributeByMmsValue.argtypes = [POINTER(IedModel), POINTER(MmsValue)]
    IedModel_lookupDataAttributeByMmsValue.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 567
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getLogicalDeviceCount", "cdecl"):
    IedModel_getLogicalDeviceCount = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getLogicalDeviceCount", "cdecl")
    IedModel_getLogicalDeviceCount.argtypes = [POINTER(IedModel)]
    IedModel_getLogicalDeviceCount.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 570
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getLogicalNodeCount", "cdecl"):
    LogicalDevice_getLogicalNodeCount = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getLogicalNodeCount", "cdecl")
    LogicalDevice_getLogicalNodeCount.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getLogicalNodeCount.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 572
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getChildByMmsVariableName", "cdecl"):
    LogicalDevice_getChildByMmsVariableName = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getChildByMmsVariableName", "cdecl")
    LogicalDevice_getChildByMmsVariableName.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getChildByMmsVariableName.restype = POINTER(ModelNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 576
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_hasFCData", "cdecl"):
    LogicalNode_hasFCData = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_hasFCData", "cdecl")
    LogicalNode_hasFCData.argtypes = [POINTER(LogicalNode), FunctionalConstraint]
    LogicalNode_hasFCData.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 579
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasBufferedReports", "cdecl"):
        continue
    LogicalNode_hasBufferedReports = _lib.get("LogicalNode_hasBufferedReports", "cdecl")
    LogicalNode_hasBufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasBufferedReports.restype = c_bool
    break

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 582
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasUnbufferedReports", "cdecl"):
        continue
    LogicalNode_hasUnbufferedReports = _lib.get("LogicalNode_hasUnbufferedReports", "cdecl")
    LogicalNode_hasUnbufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasUnbufferedReports.restype = c_bool
    break

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 592
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_getDataSet", "cdecl"):
    LogicalNode_getDataSet = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_getDataSet", "cdecl")
    LogicalNode_getDataSet.argtypes = [POINTER(LogicalNode), String]
    LogicalNode_getDataSet.restype = POINTER(DataSet)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 596
if _libs["/usr/local/lib/libiec61850.so"].has("DataObject_hasFCData", "cdecl"):
    DataObject_hasFCData = _libs["/usr/local/lib/libiec61850.so"].get("DataObject_hasFCData", "cdecl")
    DataObject_hasFCData.argtypes = [POINTER(DataObject), FunctionalConstraint]
    DataObject_hasFCData.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 136
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_AnalogueValue_create", "cdecl"):
    CAC_AnalogueValue_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_AnalogueValue_create", "cdecl")
    CAC_AnalogueValue_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, c_uint8, c_bool]
    CAC_AnalogueValue_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 146
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_ValWithTrans_create", "cdecl"):
    CAC_ValWithTrans_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_ValWithTrans_create", "cdecl")
    CAC_ValWithTrans_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, c_uint8, c_bool]
    CAC_ValWithTrans_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 153
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Vector_create", "cdecl"):
    CAC_Vector_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Vector_create", "cdecl")
    CAC_Vector_create.argtypes = [String, POINTER(ModelNode), c_uint32, FunctionalConstraint, c_uint8]
    CAC_Vector_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 156
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Point_create", "cdecl"):
    CAC_Point_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Point_create", "cdecl")
    CAC_Point_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, c_uint8, c_bool]
    CAC_Point_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_ScaledValueConfig_create", "cdecl"):
    CAC_ScaledValueConfig_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_ScaledValueConfig_create", "cdecl")
    CAC_ScaledValueConfig_create.argtypes = [String, POINTER(ModelNode)]
    CAC_ScaledValueConfig_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 162
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Unit_create", "cdecl"):
    CAC_Unit_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Unit_create", "cdecl")
    CAC_Unit_create.argtypes = [String, POINTER(ModelNode), c_bool]
    CAC_Unit_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 165
for _lib in _libs.values():
    if not _lib.has("CDA_OperBoolean", "cdecl"):
        continue
    CDA_OperBoolean = _lib.get("CDA_OperBoolean", "cdecl")
    CDA_OperBoolean.argtypes = [POINTER(ModelNode), c_bool]
    CDA_OperBoolean.restype = POINTER(DataAttribute)
    break

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 172
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPS_create", "cdecl"):
    CDC_SPS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPS_create", "cdecl")
    CDC_SPS_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_SPS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 175
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPS_create", "cdecl"):
    CDC_DPS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPS_create", "cdecl")
    CDC_DPS_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_DPS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 178
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_INS_create", "cdecl"):
    CDC_INS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_INS_create", "cdecl")
    CDC_INS_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_INS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 181
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENS_create", "cdecl"):
    CDC_ENS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENS_create", "cdecl")
    CDC_ENS_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_ENS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 184
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BCR_create", "cdecl"):
    CDC_BCR_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BCR_create", "cdecl")
    CDC_BCR_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_BCR_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 187
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_VSS_create", "cdecl"):
    CDC_VSS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_VSS_create", "cdecl")
    CDC_VSS_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_VSS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 205
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SEC_create", "cdecl"):
    CDC_SEC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SEC_create", "cdecl")
    CDC_SEC_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_SEC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 225
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_MV_create", "cdecl"):
    CDC_MV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_MV_create", "cdecl")
    CDC_MV_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_bool]
    CDC_MV_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CMV_create", "cdecl"):
    CDC_CMV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CMV_create", "cdecl")
    CDC_CMV_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_CMV_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 253
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SAV_create", "cdecl"):
    CDC_SAV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SAV_create", "cdecl")
    CDC_SAV_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_bool]
    CDC_SAV_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 277
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_LPL_create", "cdecl"):
    CDC_LPL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_LPL_create", "cdecl")
    CDC_LPL_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_LPL_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPL_create", "cdecl"):
    CDC_DPL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPL_create", "cdecl")
    CDC_DPL_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_DPL_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 304
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_HST_create", "cdecl"):
    CDC_HST_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_HST_create", "cdecl")
    CDC_HST_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint16]
    CDC_HST_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 325
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ACD_create", "cdecl"):
    CDC_ACD_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ACD_create", "cdecl")
    CDC_ACD_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_ACD_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 331
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ACT_create", "cdecl"):
    CDC_ACT_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ACT_create", "cdecl")
    CDC_ACT_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_ACT_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 341
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPG_create", "cdecl"):
    CDC_SPG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPG_create", "cdecl")
    CDC_SPG_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_SPG_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 351
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_VSG_create", "cdecl"):
    CDC_VSG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_VSG_create", "cdecl")
    CDC_VSG_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_VSG_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 361
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENG_create", "cdecl"):
    CDC_ENG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENG_create", "cdecl")
    CDC_ENG_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_ENG_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 375
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ING_create", "cdecl"):
    CDC_ING_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ING_create", "cdecl")
    CDC_ING_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_ING_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 389
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ASG_create", "cdecl"):
    CDC_ASG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ASG_create", "cdecl")
    CDC_ASG_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_bool]
    CDC_ASG_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 398
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_WYE_create", "cdecl"):
    CDC_WYE_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_WYE_create", "cdecl")
    CDC_WYE_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_WYE_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 407
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DEL_create", "cdecl"):
    CDC_DEL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DEL_create", "cdecl")
    CDC_DEL_create.argtypes = [String, POINTER(ModelNode), c_uint32]
    CDC_DEL_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 419
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPC_create", "cdecl"):
    CDC_SPC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPC_create", "cdecl")
    CDC_SPC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32]
    CDC_SPC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 437
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPC_create", "cdecl"):
    CDC_DPC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPC_create", "cdecl")
    CDC_DPC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32]
    CDC_DPC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 459
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_INC_create", "cdecl"):
    CDC_INC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_INC_create", "cdecl")
    CDC_INC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32]
    CDC_INC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 477
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENC_create", "cdecl"):
    CDC_ENC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENC_create", "cdecl")
    CDC_ENC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32]
    CDC_ENC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 496
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BSC_create", "cdecl"):
    CDC_BSC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BSC_create", "cdecl")
    CDC_BSC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_bool]
    CDC_BSC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 515
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ISC_create", "cdecl"):
    CDC_ISC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ISC_create", "cdecl")
    CDC_ISC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_bool]
    CDC_ISC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 536
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_APC_create", "cdecl"):
    CDC_APC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_APC_create", "cdecl")
    CDC_APC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_bool]
    CDC_APC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 558
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BAC_create", "cdecl"):
    CDC_BAC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BAC_create", "cdecl")
    CDC_BAC_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_bool]
    CDC_BAC_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 606
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPV_create", "cdecl"):
    CDC_SPV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPV_create", "cdecl")
    CDC_SPV_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool]
    CDC_SPV_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 613
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_STV_create", "cdecl"):
    CDC_STV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_STV_create", "cdecl")
    CDC_STV_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool]
    CDC_STV_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 620
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CMD_create", "cdecl"):
    CDC_CMD_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CMD_create", "cdecl")
    CDC_CMD_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool, c_bool, c_bool]
    CDC_CMD_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 629
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ALM_create", "cdecl"):
    CDC_ALM_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ALM_create", "cdecl")
    CDC_ALM_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool]
    CDC_ALM_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 636
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CTE_create", "cdecl"):
    CDC_CTE_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CTE_create", "cdecl")
    CDC_CTE_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool]
    CDC_CTE_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 643
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_TMS_create", "cdecl"):
    CDC_TMS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_TMS_create", "cdecl")
    CDC_TMS_create.argtypes = [String, POINTER(ModelNode), c_uint32, c_uint32, c_uint32, c_bool]
    CDC_TMS_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 55
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_create", "cdecl"):
    IedModel_create = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_create", "cdecl")
    IedModel_create.argtypes = [String]
    IedModel_create.restype = POINTER(IedModel)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 70
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setIedNameForDynamicModel", "cdecl"):
    IedModel_setIedNameForDynamicModel = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setIedNameForDynamicModel", "cdecl")
    IedModel_setIedNameForDynamicModel.argtypes = [POINTER(IedModel), String]
    IedModel_setIedNameForDynamicModel.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_destroy", "cdecl"):
    IedModel_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_destroy", "cdecl")
    IedModel_destroy.argtypes = [POINTER(IedModel)]
    IedModel_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 92
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_create", "cdecl"):
    LogicalDevice_create = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_create", "cdecl")
    LogicalDevice_create.argtypes = [String, POINTER(IedModel)]
    LogicalDevice_create.restype = POINTER(LogicalDevice)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 104
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_create", "cdecl"):
    LogicalNode_create = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_create", "cdecl")
    LogicalNode_create.argtypes = [String, POINTER(LogicalDevice)]
    LogicalNode_create.restype = POINTER(LogicalNode)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 118
if _libs["/usr/local/lib/libiec61850.so"].has("DataObject_create", "cdecl"):
    DataObject_create = _libs["/usr/local/lib/libiec61850.so"].get("DataObject_create", "cdecl")
    DataObject_create.argtypes = [String, POINTER(ModelNode), c_int]
    DataObject_create.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 136
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_create", "cdecl"):
    DataAttribute_create = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_create", "cdecl")
    DataAttribute_create.argtypes = [String, POINTER(ModelNode), DataAttributeType, FunctionalConstraint, c_uint8, c_int, c_uint32]
    DataAttribute_create.restype = POINTER(DataAttribute)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_create", "cdecl"):
    ReportControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_create", "cdecl")
    ReportControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, c_bool, String, c_uint32, c_uint8, c_uint8, c_uint32, c_uint32]
    ReportControlBlock_create.restype = POINTER(ReportControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 173
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_setPreconfiguredClient", "cdecl"):
    ReportControlBlock_setPreconfiguredClient = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_setPreconfiguredClient", "cdecl")
    ReportControlBlock_setPreconfiguredClient.argtypes = [POINTER(ReportControlBlock), c_uint8, POINTER(c_uint8)]
    ReportControlBlock_setPreconfiguredClient.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 192
if _libs["/usr/local/lib/libiec61850.so"].has("LogControlBlock_create", "cdecl"):
    LogControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("LogControlBlock_create", "cdecl")
    LogControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, c_uint8, c_uint32, c_bool, c_bool]
    LogControlBlock_create.restype = POINTER(LogControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("Log_create", "cdecl"):
    Log_create = _libs["/usr/local/lib/libiec61850.so"].get("Log_create", "cdecl")
    Log_create.argtypes = [String, POINTER(LogicalNode)]
    Log_create.restype = POINTER(Log)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 218
if _libs["/usr/local/lib/libiec61850.so"].has("SettingGroupControlBlock_create", "cdecl"):
    SettingGroupControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("SettingGroupControlBlock_create", "cdecl")
    SettingGroupControlBlock_create.argtypes = [POINTER(LogicalNode), c_uint8, c_uint8]
    SettingGroupControlBlock_create.restype = POINTER(SettingGroupControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 237
if _libs["/usr/local/lib/libiec61850.so"].has("GSEControlBlock_create", "cdecl"):
    GSEControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("GSEControlBlock_create", "cdecl")
    GSEControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, c_uint32, c_bool, c_int, c_int]
    GSEControlBlock_create.restype = POINTER(GSEControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 257
if _libs["/usr/local/lib/libiec61850.so"].has("SVControlBlock_create", "cdecl"):
    SVControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("SVControlBlock_create", "cdecl")
    SVControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, c_uint32, c_uint8, c_uint16, c_uint8, c_bool]
    SVControlBlock_create.restype = POINTER(SVControlBlock)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 262
if _libs["/usr/local/lib/libiec61850.so"].has("SVControlBlock_addPhyComAddress", "cdecl"):
    SVControlBlock_addPhyComAddress = _libs["/usr/local/lib/libiec61850.so"].get("SVControlBlock_addPhyComAddress", "cdecl")
    SVControlBlock_addPhyComAddress.argtypes = [POINTER(SVControlBlock), POINTER(PhyComAddress)]
    SVControlBlock_addPhyComAddress.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 265
if _libs["/usr/local/lib/libiec61850.so"].has("GSEControlBlock_addPhyComAddress", "cdecl"):
    GSEControlBlock_addPhyComAddress = _libs["/usr/local/lib/libiec61850.so"].get("GSEControlBlock_addPhyComAddress", "cdecl")
    GSEControlBlock_addPhyComAddress.argtypes = [POINTER(GSEControlBlock), POINTER(PhyComAddress)]
    GSEControlBlock_addPhyComAddress.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 279
if _libs["/usr/local/lib/libiec61850.so"].has("PhyComAddress_create", "cdecl"):
    PhyComAddress_create = _libs["/usr/local/lib/libiec61850.so"].get("PhyComAddress_create", "cdecl")
    PhyComAddress_create.argtypes = [c_uint8, c_uint16, c_uint16, POINTER(c_uint8)]
    PhyComAddress_create.restype = POINTER(PhyComAddress)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 290
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_create", "cdecl"):
    DataSet_create = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_create", "cdecl")
    DataSet_create.argtypes = [String, POINTER(LogicalNode)]
    DataSet_create.restype = POINTER(DataSet)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_getSize", "cdecl"):
    DataSet_getSize = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_getSize", "cdecl")
    DataSet_getSize.argtypes = [POINTER(DataSet)]
    DataSet_getSize.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 303
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_getFirstEntry", "cdecl"):
    DataSet_getFirstEntry = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_getFirstEntry", "cdecl")
    DataSet_getFirstEntry.argtypes = [POINTER(DataSet)]
    DataSet_getFirstEntry.restype = POINTER(DataSetEntry)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 306
if _libs["/usr/local/lib/libiec61850.so"].has("DataSetEntry_getNext", "cdecl"):
    DataSetEntry_getNext = _libs["/usr/local/lib/libiec61850.so"].get("DataSetEntry_getNext", "cdecl")
    DataSetEntry_getNext.argtypes = [POINTER(DataSetEntry)]
    DataSetEntry_getNext.restype = POINTER(DataSetEntry)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_dynamic_model.h: 329
if _libs["/usr/local/lib/libiec61850.so"].has("DataSetEntry_create", "cdecl"):
    DataSetEntry_create = _libs["/usr/local/lib/libiec61850.so"].get("DataSetEntry_create", "cdecl")
    DataSetEntry_create.argtypes = [POINTER(DataSet), String, c_int, String]
    DataSetEntry_create.restype = POINTER(DataSetEntry)

FileHandle = POINTER(None)# /usr/local/include/libiec61850/hal_filesystem.h: 44

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_config_file_parser.h: 50
if _libs["/usr/local/lib/libiec61850.so"].has("ConfigFileParser_createModelFromConfigFileEx", "cdecl"):
    ConfigFileParser_createModelFromConfigFileEx = _libs["/usr/local/lib/libiec61850.so"].get("ConfigFileParser_createModelFromConfigFileEx", "cdecl")
    ConfigFileParser_createModelFromConfigFileEx.argtypes = [String]
    ConfigFileParser_createModelFromConfigFileEx.restype = POINTER(IedModel)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_config_file_parser.h: 53
if _libs["/usr/local/lib/libiec61850.so"].has("ConfigFileParser_createModelFromConfigFile", "cdecl"):
    ConfigFileParser_createModelFromConfigFile = _libs["/usr/local/lib/libiec61850.so"].get("ConfigFileParser_createModelFromConfigFile", "cdecl")
    ConfigFileParser_createModelFromConfigFile.argtypes = [FileHandle]
    ConfigFileParser_createModelFromConfigFile.restype = POINTER(IedModel)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 49
class struct_sIedServerConfig(Structure):
    pass

IedServerConfig = POINTER(struct_sIedServerConfig)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 47

struct_sIedServerConfig.__slots__ = [
    'reportBufferSize',
    'reportBufferSizeURCBs',
    'fileServiceBasepath',
    'enableFileService',
    'enableDynamicDataSetService',
    'maxAssociationSpecificDataSets',
    'maxDomainSpecificDataSets',
    'maxDataSetEntries',
    'enableLogService',
    'edition',
    'maxMmsConnections',
]
struct_sIedServerConfig._fields_ = [
    ('reportBufferSize', c_int),
    ('reportBufferSizeURCBs', c_int),
    ('fileServiceBasepath', String),
    ('enableFileService', c_bool),
    ('enableDynamicDataSetService', c_bool),
    ('maxAssociationSpecificDataSets', c_int),
    ('maxDomainSpecificDataSets', c_int),
    ('maxDataSetEntries', c_int),
    ('enableLogService', c_bool),
    ('edition', c_uint8),
    ('maxMmsConnections', c_int),
]

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_create", "cdecl"):
    IedServerConfig_create = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_create", "cdecl")
    IedServerConfig_create.argtypes = []
    IedServerConfig_create.restype = IedServerConfig

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 97
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_destroy", "cdecl"):
    IedServerConfig_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_destroy", "cdecl")
    IedServerConfig_destroy.argtypes = [IedServerConfig]
    IedServerConfig_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 105
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setEdition", "cdecl"):
    IedServerConfig_setEdition = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setEdition", "cdecl")
    IedServerConfig_setEdition.argtypes = [IedServerConfig, c_uint8]
    IedServerConfig_setEdition.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 113
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getEdition", "cdecl"):
    IedServerConfig_getEdition = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getEdition", "cdecl")
    IedServerConfig_getEdition.argtypes = [IedServerConfig]
    IedServerConfig_getEdition.restype = c_uint8

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 121
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setReportBufferSize", "cdecl"):
    IedServerConfig_setReportBufferSize = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setReportBufferSize", "cdecl")
    IedServerConfig_setReportBufferSize.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSize.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 129
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getReportBufferSize", "cdecl"):
    IedServerConfig_getReportBufferSize = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getReportBufferSize", "cdecl")
    IedServerConfig_getReportBufferSize.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSize.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 137
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_setReportBufferSizeForURCBs = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_setReportBufferSizeForURCBs.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSizeForURCBs.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 145
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_getReportBufferSizeForURCBs = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_getReportBufferSizeForURCBs.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSizeForURCBs.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 156
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxMmsConnections", "cdecl"):
    IedServerConfig_setMaxMmsConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxMmsConnections", "cdecl")
    IedServerConfig_setMaxMmsConnections.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxMmsConnections.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 164
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxMmsConnections", "cdecl"):
    IedServerConfig_getMaxMmsConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxMmsConnections", "cdecl")
    IedServerConfig_getMaxMmsConnections.argtypes = [IedServerConfig]
    IedServerConfig_getMaxMmsConnections.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 174
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setFileServiceBasePath", "cdecl"):
    IedServerConfig_setFileServiceBasePath = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setFileServiceBasePath", "cdecl")
    IedServerConfig_setFileServiceBasePath.argtypes = [IedServerConfig, String]
    IedServerConfig_setFileServiceBasePath.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 179
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getFileServiceBasePath", "cdecl"):
    IedServerConfig_getFileServiceBasePath = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getFileServiceBasePath", "cdecl")
    IedServerConfig_getFileServiceBasePath.argtypes = [IedServerConfig]
    IedServerConfig_getFileServiceBasePath.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 188
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableFileService", "cdecl"):
    IedServerConfig_enableFileService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableFileService", "cdecl")
    IedServerConfig_enableFileService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableFileService.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 196
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isFileServiceEnabled", "cdecl"):
    IedServerConfig_isFileServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isFileServiceEnabled", "cdecl")
    IedServerConfig_isFileServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isFileServiceEnabled.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableDynamicDataSetService", "cdecl"):
    IedServerConfig_enableDynamicDataSetService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableDynamicDataSetService", "cdecl")
    IedServerConfig_enableDynamicDataSetService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableDynamicDataSetService.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 212
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl"):
    IedServerConfig_isDynamicDataSetServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl")
    IedServerConfig_isDynamicDataSetServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isDynamicDataSetServiceEnabled.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 223
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxAssociationSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_setMaxAssociationSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxAssociationSpecificDataSets.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 231
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxAssociationSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_getMaxAssociationSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxAssociationSpecificDataSets.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 239
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxDomainSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_setMaxDomainSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDomainSpecificDataSets.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 247
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxDomainSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_getMaxDomainSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDomainSpecificDataSets.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 259
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxDataSetEntries", "cdecl"):
    IedServerConfig_setMaxDataSetEntries = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxDataSetEntries", "cdecl")
    IedServerConfig_setMaxDataSetEntries.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDataSetEntries.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 267
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxDatasSetEntries", "cdecl"):
    IedServerConfig_getMaxDatasSetEntries = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxDatasSetEntries", "cdecl")
    IedServerConfig_getMaxDatasSetEntries.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDatasSetEntries.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 275
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableLogService", "cdecl"):
    IedServerConfig_enableLogService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableLogService", "cdecl")
    IedServerConfig_enableLogService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableLogService.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 283
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isLogServiceEnabled", "cdecl"):
    IedServerConfig_isLogServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isLogServiceEnabled", "cdecl")
    IedServerConfig_isLogServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isLogServiceEnabled.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 288
class struct_sIedServer(Structure):
    pass

IedServer = POINTER(struct_sIedServer)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 288

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 293
class struct_sClientConnection(Structure):
    pass

ClientConnection = POINTER(struct_sClientConnection)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 293

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 310
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_create", "cdecl"):
    IedServer_create = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_create", "cdecl")
    IedServer_create.argtypes = [POINTER(IedModel)]
    IedServer_create.restype = IedServer

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 321
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_createWithTlsSupport", "cdecl"):
    IedServer_createWithTlsSupport = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_createWithTlsSupport", "cdecl")
    IedServer_createWithTlsSupport.argtypes = [POINTER(IedModel), TLSConfiguration]
    IedServer_createWithTlsSupport.restype = IedServer

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 331
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_createWithConfig", "cdecl"):
    IedServer_createWithConfig = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_createWithConfig", "cdecl")
    IedServer_createWithConfig.argtypes = [POINTER(IedModel), TLSConfiguration, IedServerConfig]
    IedServer_createWithConfig.restype = IedServer

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 339
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_destroy", "cdecl"):
    IedServer_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_destroy", "cdecl")
    IedServer_destroy.argtypes = [IedServer]
    IedServer_destroy.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 348
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setLocalIpAddress", "cdecl"):
    IedServer_setLocalIpAddress = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setLocalIpAddress", "cdecl")
    IedServer_setLocalIpAddress.argtypes = [IedServer, String]
    IedServer_setLocalIpAddress.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 361
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setServerIdentity", "cdecl"):
    IedServer_setServerIdentity = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setServerIdentity", "cdecl")
    IedServer_setServerIdentity.argtypes = [IedServer, String, String, String]
    IedServer_setServerIdentity.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 374
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setFilestoreBasepath", "cdecl"):
    IedServer_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setFilestoreBasepath", "cdecl")
    IedServer_setFilestoreBasepath.argtypes = [IedServer, String]
    IedServer_setFilestoreBasepath.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 383
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_start", "cdecl"):
    IedServer_start = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_start", "cdecl")
    IedServer_start.argtypes = [IedServer, c_int]
    IedServer_start.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 391
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_stop", "cdecl"):
    IedServer_stop = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_stop", "cdecl")
    IedServer_stop.argtypes = [IedServer]
    IedServer_stop.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 404
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_startThreadless", "cdecl"):
    IedServer_startThreadless = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_startThreadless", "cdecl")
    IedServer_startThreadless.argtypes = [IedServer, c_int]
    IedServer_startThreadless.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 420
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_waitReady", "cdecl"):
    IedServer_waitReady = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_waitReady", "cdecl")
    IedServer_waitReady.argtypes = [IedServer, c_uint]
    IedServer_waitReady.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 432
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_processIncomingData", "cdecl"):
    IedServer_processIncomingData = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_processIncomingData", "cdecl")
    IedServer_processIncomingData.argtypes = [IedServer]
    IedServer_processIncomingData.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 443
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_performPeriodicTasks", "cdecl"):
    IedServer_performPeriodicTasks = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_performPeriodicTasks", "cdecl")
    IedServer_performPeriodicTasks.argtypes = [IedServer]
    IedServer_performPeriodicTasks.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 451
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_stopThreadless", "cdecl"):
    IedServer_stopThreadless = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_stopThreadless", "cdecl")
    IedServer_stopThreadless.argtypes = [IedServer]
    IedServer_stopThreadless.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 460
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getDataModel", "cdecl"):
    IedServer_getDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getDataModel", "cdecl")
    IedServer_getDataModel.argtypes = [IedServer]
    IedServer_getDataModel.restype = POINTER(IedModel)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 471
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_isRunning", "cdecl"):
    IedServer_isRunning = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_isRunning", "cdecl")
    IedServer_isRunning.argtypes = [IedServer]
    IedServer_isRunning.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 481
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getNumberOfOpenConnections", "cdecl"):
    IedServer_getNumberOfOpenConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getNumberOfOpenConnections", "cdecl")
    IedServer_getNumberOfOpenConnections.argtypes = [IedServer]
    IedServer_getNumberOfOpenConnections.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 494
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getMmsServer", "cdecl"):
    IedServer_getMmsServer = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getMmsServer", "cdecl")
    IedServer_getMmsServer.argtypes = [IedServer]
    IedServer_getMmsServer.restype = MmsServer

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 509
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_enableGoosePublishing", "cdecl"):
    IedServer_enableGoosePublishing = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_enableGoosePublishing", "cdecl")
    IedServer_enableGoosePublishing.argtypes = [IedServer]
    IedServer_enableGoosePublishing.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 522
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_disableGoosePublishing", "cdecl"):
    IedServer_disableGoosePublishing = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_disableGoosePublishing", "cdecl")
    IedServer_disableGoosePublishing.argtypes = [IedServer]
    IedServer_disableGoosePublishing.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 537
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setGooseInterfaceId", "cdecl"):
    IedServer_setGooseInterfaceId = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setGooseInterfaceId", "cdecl")
    IedServer_setGooseInterfaceId.argtypes = [IedServer, String]
    IedServer_setGooseInterfaceId.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 553
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setGooseInterfaceIdEx", "cdecl"):
    IedServer_setGooseInterfaceIdEx = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setGooseInterfaceIdEx", "cdecl")
    IedServer_setGooseInterfaceIdEx.argtypes = [IedServer, POINTER(LogicalNode), String, String]
    IedServer_setGooseInterfaceIdEx.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 569
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_useGooseVlanTag", "cdecl"):
    IedServer_useGooseVlanTag = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_useGooseVlanTag", "cdecl")
    IedServer_useGooseVlanTag.argtypes = [IedServer, POINTER(LogicalNode), String, c_bool]
    IedServer_useGooseVlanTag.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 592
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setAuthenticator", "cdecl"):
    IedServer_setAuthenticator = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setAuthenticator", "cdecl")
    IedServer_setAuthenticator.argtypes = [IedServer, AcseAuthenticator, POINTER(None)]
    IedServer_setAuthenticator.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 605
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getPeerAddress", "cdecl"):
    ClientConnection_getPeerAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getPeerAddress", "cdecl")
    ClientConnection_getPeerAddress.argtypes = [ClientConnection]
    ClientConnection_getPeerAddress.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 617
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getLocalAddress", "cdecl"):
    ClientConnection_getLocalAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getLocalAddress", "cdecl")
    ClientConnection_getLocalAddress.argtypes = [ClientConnection]
    ClientConnection_getLocalAddress.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 630
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getSecurityToken", "cdecl"):
    ClientConnection_getSecurityToken = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getSecurityToken", "cdecl")
    ClientConnection_getSecurityToken.argtypes = [ClientConnection]
    ClientConnection_getSecurityToken.restype = POINTER(c_ubyte)
    ClientConnection_getSecurityToken.errcheck = lambda v,*a : cast(v, c_void_p)

IedConnectionIndicationHandler = CFUNCTYPE(UNCHECKED(None), IedServer, ClientConnection, c_bool, POINTER(None))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 642

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 652
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setConnectionIndicationHandler", "cdecl"):
    IedServer_setConnectionIndicationHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setConnectionIndicationHandler", "cdecl")
    IedServer_setConnectionIndicationHandler.argtypes = [IedServer, IedConnectionIndicationHandler, POINTER(None)]
    IedServer_setConnectionIndicationHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 678
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_lockDataModel", "cdecl"):
    IedServer_lockDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_lockDataModel", "cdecl")
    IedServer_lockDataModel.argtypes = [IedServer]
    IedServer_lockDataModel.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 689
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_unlockDataModel", "cdecl"):
    IedServer_unlockDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_unlockDataModel", "cdecl")
    IedServer_unlockDataModel.argtypes = [IedServer]
    IedServer_unlockDataModel.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 703
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getAttributeValue", "cdecl"):
    IedServer_getAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getAttributeValue", "cdecl")
    IedServer_getAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getAttributeValue.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 718
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getBooleanAttributeValue", "cdecl"):
    IedServer_getBooleanAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getBooleanAttributeValue", "cdecl")
    IedServer_getBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBooleanAttributeValue.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 732
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getInt32AttributeValue", "cdecl"):
    IedServer_getInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getInt32AttributeValue", "cdecl")
    IedServer_getInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt32AttributeValue.restype = c_int32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 746
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getInt64AttributeValue", "cdecl"):
    IedServer_getInt64AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getInt64AttributeValue", "cdecl")
    IedServer_getInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt64AttributeValue.restype = c_int64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 760
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getUInt32AttributeValue", "cdecl"):
    IedServer_getUInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getUInt32AttributeValue", "cdecl")
    IedServer_getUInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUInt32AttributeValue.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 774
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getFloatAttributeValue", "cdecl"):
    IedServer_getFloatAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getFloatAttributeValue", "cdecl")
    IedServer_getFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getFloatAttributeValue.restype = c_float

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 788
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getUTCTimeAttributeValue", "cdecl"):
    IedServer_getUTCTimeAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getUTCTimeAttributeValue", "cdecl")
    IedServer_getUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUTCTimeAttributeValue.restype = c_uint64

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 806
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getBitStringAttributeValue", "cdecl"):
    IedServer_getBitStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getBitStringAttributeValue", "cdecl")
    IedServer_getBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBitStringAttributeValue.restype = c_uint32

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 819
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getStringAttributeValue", "cdecl"):
    IedServer_getStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getStringAttributeValue", "cdecl")
    IedServer_getStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getStringAttributeValue.restype = c_char_p

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 838
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getFunctionalConstrainedData", "cdecl"):
    IedServer_getFunctionalConstrainedData = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getFunctionalConstrainedData", "cdecl")
    IedServer_getFunctionalConstrainedData.argtypes = [IedServer, POINTER(DataObject), FunctionalConstraint]
    IedServer_getFunctionalConstrainedData.restype = POINTER(MmsValue)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 858
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateAttributeValue", "cdecl"):
    IedServer_updateAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateAttributeValue", "cdecl")
    IedServer_updateAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(MmsValue)]
    IedServer_updateAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 873
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateFloatAttributeValue", "cdecl"):
    IedServer_updateFloatAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateFloatAttributeValue", "cdecl")
    IedServer_updateFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_float]
    IedServer_updateFloatAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 888
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateInt32AttributeValue", "cdecl"):
    IedServer_updateInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateInt32AttributeValue", "cdecl")
    IedServer_updateInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int32]
    IedServer_updateInt32AttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 903
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateDbposValue", "cdecl"):
    IedServer_updateDbposValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateDbposValue", "cdecl")
    IedServer_updateDbposValue.argtypes = [IedServer, POINTER(DataAttribute), Dbpos]
    IedServer_updateDbposValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 918
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateInt64AttributeValue", "cdecl"):
    IedServer_updateInt64AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateInt64AttributeValue", "cdecl")
    IedServer_updateInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int64]
    IedServer_updateInt64AttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 933
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateUnsignedAttributeValue", "cdecl"):
    IedServer_updateUnsignedAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateUnsignedAttributeValue", "cdecl")
    IedServer_updateUnsignedAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_uint32]
    IedServer_updateUnsignedAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 948
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateBitStringAttributeValue", "cdecl"):
    IedServer_updateBitStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateBitStringAttributeValue", "cdecl")
    IedServer_updateBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_uint32]
    IedServer_updateBitStringAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 963
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateBooleanAttributeValue", "cdecl"):
    IedServer_updateBooleanAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateBooleanAttributeValue", "cdecl")
    IedServer_updateBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_bool]
    IedServer_updateBooleanAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 978
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateVisibleStringAttributeValue", "cdecl"):
    IedServer_updateVisibleStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateVisibleStringAttributeValue", "cdecl")
    IedServer_updateVisibleStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), String]
    IedServer_updateVisibleStringAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 993
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateUTCTimeAttributeValue", "cdecl"):
    IedServer_updateUTCTimeAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateUTCTimeAttributeValue", "cdecl")
    IedServer_updateUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_uint64]
    IedServer_updateUTCTimeAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1008
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateTimestampAttributeValue", "cdecl"):
    IedServer_updateTimestampAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateTimestampAttributeValue", "cdecl")
    IedServer_updateTimestampAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(Timestamp)]
    IedServer_updateTimestampAttributeValue.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1025
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateQuality", "cdecl"):
    IedServer_updateQuality = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateQuality", "cdecl")
    IedServer_updateQuality.argtypes = [IedServer, POINTER(DataAttribute), Quality]
    IedServer_updateQuality.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1031
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setLogStorage", "cdecl"):
    IedServer_setLogStorage = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setLogStorage", "cdecl")
    IedServer_setLogStorage.argtypes = [IedServer, String, LogStorage]
    IedServer_setLogStorage.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1050
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_changeActiveSettingGroup", "cdecl"):
    IedServer_changeActiveSettingGroup = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_changeActiveSettingGroup", "cdecl")
    IedServer_changeActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock), c_uint8]
    IedServer_changeActiveSettingGroup.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1061
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getActiveSettingGroup", "cdecl"):
    IedServer_getActiveSettingGroup = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getActiveSettingGroup", "cdecl")
    IedServer_getActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock)]
    IedServer_getActiveSettingGroup.restype = c_uint8

ActiveSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), c_uint8, ClientConnection)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1078

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1090
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setActiveSettingGroupChangedHandler", "cdecl"):
    IedServer_setActiveSettingGroupChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setActiveSettingGroupChangedHandler", "cdecl")
    IedServer_setActiveSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), ActiveSettingGroupChangedHandler, POINTER(None)]
    IedServer_setActiveSettingGroupChangedHandler.restype = None

EditSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), c_uint8, ClientConnection)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1110

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1122
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setEditSettingGroupChangedHandler", "cdecl"):
    IedServer_setEditSettingGroupChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setEditSettingGroupChangedHandler", "cdecl")
    IedServer_setEditSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupChangedHandler, POINTER(None)]
    IedServer_setEditSettingGroupChangedHandler.restype = None

EditSettingGroupConfirmationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(SettingGroupControlBlock), c_uint8)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1134

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1146
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setEditSettingGroupConfirmationHandler", "cdecl"):
    IedServer_setEditSettingGroupConfirmationHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setEditSettingGroupConfirmationHandler", "cdecl")
    IedServer_setEditSettingGroupConfirmationHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupConfirmationHandler, POINTER(None)]
    IedServer_setEditSettingGroupConfirmationHandler.restype = None

enum_anon_52 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_ACCEPTED = (-1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_HARDWARE_FAULT = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_TEMPORARILY_UNAVAILABLE = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_OBJECT_ACCESS_DENIED = 3# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_OBJECT_UNDEFINED = 4# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CONTROL_VALUE_INVALID = 11# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

CheckHandlerResult = enum_anon_52# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1167

enum_anon_53 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1176

CONTROL_RESULT_FAILED = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1176

CONTROL_RESULT_OK = 1# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1176

CONTROL_RESULT_WAITING = 2# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1176

ControlHandlerResult = enum_anon_53# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1176

ControlAction = POINTER(None)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1178

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1187
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_setAddCause", "cdecl"):
    ControlAction_setAddCause = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_setAddCause", "cdecl")
    ControlAction_setAddCause.argtypes = [ControlAction, ControlAddCause]
    ControlAction_setAddCause.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1197
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getOrCat", "cdecl"):
    ControlAction_getOrCat = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getOrCat", "cdecl")
    ControlAction_getOrCat.argtypes = [ControlAction]
    ControlAction_getOrCat.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1206
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getOrIdent", "cdecl"):
    ControlAction_getOrIdent = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getOrIdent", "cdecl")
    ControlAction_getOrIdent.argtypes = [ControlAction, POINTER(c_int)]
    ControlAction_getOrIdent.restype = POINTER(c_uint8)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1217
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getCtlNum", "cdecl"):
    ControlAction_getCtlNum = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getCtlNum", "cdecl")
    ControlAction_getCtlNum.argtypes = [ControlAction]
    ControlAction_getCtlNum.restype = c_int

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1227
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_isSelect", "cdecl"):
    ControlAction_isSelect = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_isSelect", "cdecl")
    ControlAction_isSelect.argtypes = [ControlAction]
    ControlAction_isSelect.restype = c_bool

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1237
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getClientConnection", "cdecl"):
    ControlAction_getClientConnection = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getClientConnection", "cdecl")
    ControlAction_getClientConnection.argtypes = [ControlAction]
    ControlAction_getClientConnection.restype = ClientConnection

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1246
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getControlObject", "cdecl"):
    ControlAction_getControlObject = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getControlObject", "cdecl")
    ControlAction_getControlObject.argtypes = [ControlAction]
    ControlAction_getControlObject.restype = POINTER(DataObject)

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1257
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getControlTime", "cdecl"):
    ControlAction_getControlTime = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getControlTime", "cdecl")
    ControlAction_getControlTime.argtypes = [ControlAction]
    ControlAction_getControlTime.restype = c_uint64

ControlPerformCheckHandler = CFUNCTYPE(UNCHECKED(CheckHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1279

ControlWaitForExecutionHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1303

ControlHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1325

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1341
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setControlHandler", "cdecl"):
    IedServer_setControlHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setControlHandler", "cdecl")
    IedServer_setControlHandler.argtypes = [IedServer, POINTER(DataObject), ControlHandler, POINTER(None)]
    IedServer_setControlHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1358
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setPerformCheckHandler", "cdecl"):
    IedServer_setPerformCheckHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setPerformCheckHandler", "cdecl")
    IedServer_setPerformCheckHandler.argtypes = [IedServer, POINTER(DataObject), ControlPerformCheckHandler, POINTER(None)]
    IedServer_setPerformCheckHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1376
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setWaitForExecutionHandler", "cdecl"):
    IedServer_setWaitForExecutionHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setWaitForExecutionHandler", "cdecl")
    IedServer_setWaitForExecutionHandler.argtypes = [IedServer, POINTER(DataObject), ControlWaitForExecutionHandler, POINTER(None)]
    IedServer_setWaitForExecutionHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1389
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateCtlModel", "cdecl"):
    IedServer_updateCtlModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateCtlModel", "cdecl")
    IedServer_updateCtlModel.argtypes = [IedServer, POINTER(DataObject), ControlModel]
    IedServer_updateCtlModel.restype = None

SVCBEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(SVControlBlock), c_int, POINTER(None))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1412

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1423
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setSVCBHandler", "cdecl"):
    IedServer_setSVCBHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setSVCBHandler", "cdecl")
    IedServer_setSVCBHandler.argtypes = [IedServer, POINTER(SVControlBlock), SVCBEventHandler, POINTER(None)]
    IedServer_setSVCBHandler.restype = None

WriteAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(DataAttribute), POINTER(MmsValue), ClientConnection, POINTER(None))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1456

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1474
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_handleWriteAccess", "cdecl"):
    IedServer_handleWriteAccess = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_handleWriteAccess", "cdecl")
    IedServer_handleWriteAccess.argtypes = [IedServer, POINTER(DataAttribute), WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccess.restype = None

enum_anon_54 = c_int# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1480

ACCESS_POLICY_ALLOW = 0# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1480

ACCESS_POLICY_DENY = (ACCESS_POLICY_ALLOW + 1)# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1480

AccessPolicy = enum_anon_54# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1480

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1491
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setWriteAccessPolicy", "cdecl"):
    IedServer_setWriteAccessPolicy = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setWriteAccessPolicy", "cdecl")
    IedServer_setWriteAccessPolicy.argtypes = [IedServer, FunctionalConstraint, AccessPolicy]
    IedServer_setWriteAccessPolicy.restype = None

ReadAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(LogicalDevice), POINTER(LogicalNode), POINTER(DataObject), FunctionalConstraint, ClientConnection, POINTER(None))# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1510

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1522
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setReadAccessHandler", "cdecl"):
    IedServer_setReadAccessHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setReadAccessHandler", "cdecl")
    IedServer_setReadAccessHandler.argtypes = [IedServer, ReadAccessHandler, POINTER(None)]
    IedServer_setReadAccessHandler.restype = None

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 41
try:
    IEC_61850_EDITION_1 = 0
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 44
try:
    IEC_61850_EDITION_2 = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 47
try:
    IEC_61850_EDITION_2_1 = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 96
try:
    TRG_OPT_DATA_CHANGED = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 99
try:
    TRG_OPT_QUALITY_CHANGED = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 102
try:
    TRG_OPT_DATA_UPDATE = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 105
try:
    TRG_OPT_INTEGRITY = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 108
try:
    TRG_OPT_GI = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 111
try:
    TRG_OPT_TRANSIENT = 128
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 123
try:
    RPT_OPT_SEQ_NUM = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 126
try:
    RPT_OPT_TIME_STAMP = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 129
try:
    RPT_OPT_REASON_FOR_INCLUSION = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 132
try:
    RPT_OPT_DATA_SET = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 135
try:
    RPT_OPT_DATA_REFERENCE = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 138
try:
    RPT_OPT_BUFFER_OVERFLOW = 32
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 141
try:
    RPT_OPT_ENTRY_ID = 64
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 144
try:
    RPT_OPT_CONF_REV = 128
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 154
try:
    CONTROL_ORCAT_NOT_SUPPORTED = 0
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 157
try:
    CONTROL_ORCAT_BAY_CONTROL = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 160
try:
    CONTROL_ORCAT_STATION_CONTROL = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 163
try:
    CONTROL_ORCAT_REMOTE_CONTROL = 3
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 166
try:
    CONTROL_ORCAT_AUTOMATIC_BAY = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 169
try:
    CONTROL_ORCAT_AUTOMATIC_STATION = 5
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 172
try:
    CONTROL_ORCAT_AUTOMATIC_REMOTE = 6
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 175
try:
    CONTROL_ORCAT_MAINTENANCE = 7
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 178
try:
    CONTROL_ORCAT_PROCESS = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 317
try:
    QUALITY_VALIDITY_GOOD = 0
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 318
try:
    QUALITY_VALIDITY_INVALID = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 319
try:
    QUALITY_VALIDITY_RESERVED = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 320
try:
    QUALITY_VALIDITY_QUESTIONABLE = 3
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 322
try:
    QUALITY_DETAIL_OVERFLOW = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 323
try:
    QUALITY_DETAIL_OUT_OF_RANGE = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 324
try:
    QUALITY_DETAIL_BAD_REFERENCE = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 325
try:
    QUALITY_DETAIL_OSCILLATORY = 32
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 326
try:
    QUALITY_DETAIL_FAILURE = 64
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 327
try:
    QUALITY_DETAIL_OLD_DATA = 128
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 328
try:
    QUALITY_DETAIL_INCONSISTENT = 256
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 329
try:
    QUALITY_DETAIL_INACCURATE = 512
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 331
try:
    QUALITY_SOURCE_SUBSTITUTED = 1024
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 333
try:
    QUALITY_TEST = 2048
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 335
try:
    QUALITY_OPERATOR_BLOCKED = 4096
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_common.h: 337
try:
    QUALITY_DERIVED = 8192
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 489
try:
    IEC61850_SV_OPT_REFRESH_TIME = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 492
try:
    IEC61850_SV_OPT_SAMPLE_SYNC = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 495
try:
    IEC61850_SV_OPT_SAMPLE_RATE = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 498
try:
    IEC61850_SV_OPT_DATA_SET = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 501
try:
    IEC61850_SV_OPT_SECURITY = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 503
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_PERIOD = 0
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 505
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_SECOND = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 507
try:
    IEC61850_SV_SMPMOD_SECONDS_PER_SAMPLE = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 645
try:
    GOCB_ELEMENT_GO_ENA = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 648
try:
    GOCB_ELEMENT_GO_ID = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 651
try:
    GOCB_ELEMENT_DATSET = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 654
try:
    GOCB_ELEMENT_CONF_REV = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 657
try:
    GOCB_ELEMENT_NDS_COMM = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 660
try:
    GOCB_ELEMENT_DST_ADDRESS = 32
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 663
try:
    GOCB_ELEMENT_MIN_TIME = 64
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 666
try:
    GOCB_ELEMENT_MAX_TIME = 128
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 669
try:
    GOCB_ELEMENT_FIXED_OFFS = 256
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 672
try:
    GOCB_ELEMENT_ALL = 511
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1131
try:
    REASON_NOT_INCLUDED = IEC61850_REASON_NOT_INCLUDED
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1132
try:
    REASON_DATA_CHANGE = IEC61850_REASON_DATA_CHANGE
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1133
try:
    REASON_QUALITY_CHANGE = IEC61850_REASON_QUALITY_CHANGE
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1134
try:
    REASON_DATA_UPDATE = IEC61850_REASON_DATA_UPDATE
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1135
try:
    REASON_INTEGRITY = IEC61850_REASON_INTEGRITY
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1136
try:
    REASON_GI = IEC61850_REASON_GI
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1137
try:
    REASON_UNKNOWN = IEC61850_REASON_UNKNOWN
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1143
try:
    RCB_ELEMENT_RPT_ID = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1146
try:
    RCB_ELEMENT_RPT_ENA = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1149
try:
    RCB_ELEMENT_RESV = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1152
try:
    RCB_ELEMENT_DATSET = 8
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1155
try:
    RCB_ELEMENT_CONF_REV = 16
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1158
try:
    RCB_ELEMENT_OPT_FLDS = 32
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1161
try:
    RCB_ELEMENT_BUF_TM = 64
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1164
try:
    RCB_ELEMENT_SQ_NUM = 128
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1167
try:
    RCB_ELEMENT_TRG_OPS = 256
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1170
try:
    RCB_ELEMENT_INTG_PD = 512
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1173
try:
    RCB_ELEMENT_GI = 1024
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1176
try:
    RCB_ELEMENT_PURGE_BUF = 2048
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1179
try:
    RCB_ELEMENT_ENTRY_ID = 4096
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1182
try:
    RCB_ELEMENT_TIME_OF_ENTRY = 8192
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1185
try:
    RCB_ELEMENT_RESV_TMS = 16384
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1188
try:
    RCB_ELEMENT_OWNER = 32768
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 47
try:
    CDC_OPTION_PICS_SUBST = (1 << 0)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 48
try:
    CDC_OPTION_BLK_ENA = (1 << 1)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 51
try:
    CDC_OPTION_DESC = (1 << 2)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 54
try:
    CDC_OPTION_DESC_UNICODE = (1 << 3)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 57
try:
    CDC_OPTION_AC_DLNDA = (1 << 4)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 60
try:
    CDC_OPTION_AC_DLN = (1 << 5)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 63
try:
    CDC_OPTION_UNIT = (1 << 6)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 65
try:
    CDC_OPTION_FROZEN_VALUE = (1 << 7)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 67
try:
    CDC_OPTION_ADDR = (1 << 8)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 68
try:
    CDC_OPTION_ADDINFO = (1 << 9)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 70
try:
    CDC_OPTION_INST_MAG = (1 << 10)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 71
try:
    CDC_OPTION_RANGE = (1 << 11)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 73
try:
    CDC_OPTION_UNIT_MULTIPLIER = (1 << 12)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 75
try:
    CDC_OPTION_AC_SCAV = (1 << 13)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 77
try:
    CDC_OPTION_MIN = (1 << 14)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 78
try:
    CDC_OPTION_MAX = (1 << 15)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 80
try:
    CDC_OPTION_AC_CLC_O = (1 << 16)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 82
try:
    CDC_OPTION_RANGE_ANG = (1 << 17)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 84
try:
    CDC_OPTION_PHASE_A = (1 << 18)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 85
try:
    CDC_OPTION_PHASE_B = (1 << 19)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 86
try:
    CDC_OPTION_PHASE_C = (1 << 20)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 88
try:
    CDC_OPTION_PHASE_NEUT = (1 << 21)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 90
try:
    CDC_OPTION_PHASES_ABC = ((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 92
try:
    CDC_OPTION_PHASES_ALL = (((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C) | CDC_OPTION_PHASE_NEUT)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 94
try:
    CDC_OPTION_STEP_SIZE = (1 << 22)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 96
try:
    CDC_OPTION_ANGLE_REF = (1 << 23)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 99
try:
    CDC_OPTION_DPL_HWREV = (1 << 17)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 100
try:
    CDC_OPTION_DPL_SWREV = (1 << 18)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 101
try:
    CDC_OPTION_DPL_SERNUM = (1 << 19)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 102
try:
    CDC_OPTION_DPL_MODEL = (1 << 20)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 103
try:
    CDC_OPTION_DPL_LOCATION = (1 << 21)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 106
try:
    CDC_OPTION_AC_LN0_M = (1 << 24)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 107
try:
    CDC_OPTION_AC_LN0_EX = (1 << 25)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 108
try:
    CDC_OPTION_AC_DLD_M = (1 << 26)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 113
try:
    CDC_CTL_MODEL_NONE = 0
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 114
try:
    CDC_CTL_MODEL_DIRECT_NORMAL = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 115
try:
    CDC_CTL_MODEL_SBO_NORMAL = 2
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 116
try:
    CDC_CTL_MODEL_DIRECT_ENHANCED = 3
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 117
try:
    CDC_CTL_MODEL_SBO_ENHANCED = 4
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 119
try:
    CDC_CTL_MODEL_HAS_CANCEL = (1 << 4)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 120
try:
    CDC_CTL_MODEL_IS_TIME_ACTIVATED = (1 << 5)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 122
try:
    CDC_CTL_OPTION_ORIGIN = (1 << 6)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 123
try:
    CDC_CTL_OPTION_CTL_NUM = (1 << 7)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 124
try:
    CDC_CTL_OPTION_ST_SELD = (1 << 8)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 125
try:
    CDC_CTL_OPTION_OP_RCVD = (1 << 9)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 126
try:
    CDC_CTL_OPTION_OP_OK = (1 << 10)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 127
try:
    CDC_CTL_OPTION_T_OP_OK = (1 << 11)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 128
try:
    CDC_CTL_OPTION_SBO_TIMEOUT = (1 << 12)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 129
try:
    CDC_CTL_OPTION_SBO_CLASS = (1 << 13)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 130
try:
    CDC_CTL_OPTION_OPER_TIMEOUT = (1 << 14)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 562
try:
    CDC_OPTION_61400_MIN_MX_VAL = (1 << 10)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 565
try:
    CDC_OPTION_61400_MAX_MX_VAL = (1 << 11)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 568
try:
    CDC_OPTION_61400_TOT_AV_VAL = (1 << 12)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 571
try:
    CDC_OPTION_61400_SDV_VAL = (1 << 13)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 574
try:
    CDC_OPTION_61400_INC_RATE = (1 << 14)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 577
try:
    CDC_OPTION_61400_DEC_RATE = (1 << 15)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 580
try:
    CDC_OPTION_61400_SP_ACS = (1 << 16)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 583
try:
    CDC_OPTION_61400_CHA_PER_RS = (1 << 17)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 586
try:
    CDC_OPTION_61400_CM_ACS = (1 << 18)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 589
try:
    CDC_OPTION_61400_TM_TOT = (1 << 19)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 592
try:
    CDC_OPTION_61400_COUNTING_DAILY = (1 << 20)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 595
try:
    CDC_OPTION_61400_COUNTING_MONTHLY = (1 << 21)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 598
try:
    CDC_OPTION_61400_COUNTING_YEARLY = (1 << 22)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 601
try:
    CDC_OPTION_61400_COUNTING_TOTAL = (1 << 23)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_cdc.h: 604
try:
    CDC_OPTION_61400_COUNTING_ALL = (((CDC_OPTION_61400_COUNTING_DAILY | CDC_OPTION_61400_COUNTING_MONTHLY) | CDC_OPTION_61400_COUNTING_YEARLY) | CDC_OPTION_61400_COUNTING_TOTAL)
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1400
try:
    IEC61850_SVCB_EVENT_ENABLE = 1
except:
    pass

# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 1403
try:
    IEC61850_SVCB_EVENT_DISABLE = 0
except:
    pass

sMmsDomain = struct_sMmsDomain# /usr/local/include/libiec61850/mms_common.h: 137

sMmsAccessSpecifier = struct_sMmsAccessSpecifier# /usr/local/include/libiec61850/mms_common.h: 145

sMmsNamedVariableList = struct_sMmsNamedVariableList# /usr/local/include/libiec61850/mms_common.h: 155

sMmsVariableSpecification = struct_sMmsVariableSpecification# /usr/local/include/libiec61850/mms_types.h: 50

sMmsArray = struct_sMmsArray# /usr/local/include/libiec61850/mms_types.h: 55

sMmsStructure = struct_sMmsStructure# /usr/local/include/libiec61850/mms_types.h: 59

sMmsFloat = struct_sMmsFloat# /usr/local/include/libiec61850/mms_types.h: 66

uMmsTypeSpecification = union_uMmsTypeSpecification# /usr/local/include/libiec61850/mms_types.h: 53

sMmsValue = struct_sMmsValue# /usr/local/include/libiec61850/mms_value.h: 67

sLinkedList = struct_sLinkedList# /home/user/projects/fork/libiec61850/src/common/inc/linked_list.h: 44

sAcseAuthenticationParameter = struct_sAcseAuthenticationParameter# /usr/local/include/libiec61850/iso_connection_parameters.h: 60

sIsoConnectionParameters = struct_sIsoConnectionParameters# /usr/local/include/libiec61850/iso_connection_parameters.h: 137

sMmsConnectionParameters = struct_sMmsConnectionParameters# /usr/local/include/libiec61850/mms_client_connection.h: 54

sMmsConnection = struct_sMmsConnection# /usr/local/include/libiec61850/mms_client_connection.h: 75

sMmsJournalEntry = struct_sMmsJournalEntry# /usr/local/include/libiec61850/mms_client_connection.h: 1227

sMmsJournalVariable = struct_sMmsJournalVariable# /usr/local/include/libiec61850/mms_client_connection.h: 1233

sClientDataSet = struct_sClientDataSet# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 43

sClientReport = struct_sClientReport# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 46

sClientReportControlBlock = struct_sClientReportControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 49

sClientGooseControlBlock = struct_sClientGooseControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 52

sIedConnection = struct_sIedConnection# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 61

sClientSVControlBlock = struct_sClientSVControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 511

sControlObjectClient = struct_sControlObjectClient# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 1915

sFileDirectoryEntry = struct_sFileDirectoryEntry# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_client.h: 2652

sModelNode = struct_sModelNode# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 191

sDataAttribute = struct_sDataAttribute# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 217

sDataObject = struct_sDataObject# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 207

sLogicalNode = struct_sLogicalNode# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 199

sLogicalDevice = struct_sLogicalDevice# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 183

sIedModel = struct_sIedModel# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 170

sDataSet = struct_sDataSet# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 246

sReportControlBlock = struct_sReportControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 254

sSettingGroupControlBlock = struct_sSettingGroupControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 299

sGSEControlBlock = struct_sGSEControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 313

sSVControlBlock = struct_sSVControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 326

sLogControlBlock = struct_sLogControlBlock# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 274

sLog = struct_sLog# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 291

sDataSetEntry = struct_sDataSetEntry# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_model.h: 236

sIedServerConfig = struct_sIedServerConfig# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 49

sIedServer = struct_sIedServer# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 288

sClientConnection = struct_sClientConnection# /home/user/projects/fork/libiec61850/src/iec61850/inc/iec61850_server.h: 293

# No inserted files

# No prefix-stripping

