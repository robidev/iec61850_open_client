r"""Wrapper for hal_base.h

Generated with:
/home/user/iec61850_open_gateway/.venv/bin/ctypesgen -l lib60870.so -I ../lib60870/lib60870-C/src/hal/inc ../lib60870/lib60870-C/src/hal/inc/hal_base.h ../lib60870/lib60870-C/src/hal/inc/hal_serial.h ../lib60870/lib60870-C/src/hal/inc/hal_socket.h ../lib60870/lib60870-C/src/hal/inc/hal_thread.h ../lib60870/lib60870-C/src/hal/inc/hal_time.h ../lib60870/lib60870-C/src/hal/inc/lib_memory.h ../lib60870/lib60870-C/src/hal/inc/platform_endian.h ../lib60870/lib60870-C/src/hal/inc/tls_ciphers.h ../lib60870/lib60870-C/src/hal/inc/tls_config.h ../lib60870/lib60870-C/src/hal/inc/tls_socket.h -I ../lib60870/lib60870-C/src/inc/api ../lib60870/lib60870-C/src/inc/api/cs101_information_objects.h ../lib60870/lib60870-C/src/inc/api/cs101_master.h ../lib60870/lib60870-C/src/inc/api/cs101_slave.h ../lib60870/lib60870-C/src/inc/api/cs104_connection.h ../lib60870/lib60870-C/src/inc/api/cs104_slave.h ../lib60870/lib60870-C/src/inc/api/iec60870_common.h ../lib60870/lib60870-C/src/inc/api/iec60870_master.h ../lib60870/lib60870-C/src/inc/api/iec60870_slave.h ../lib60870/lib60870-C/src/inc/api/link_layer_parameters.h -o _lib60870.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
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


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

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
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
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
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


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

"""
Load libraries - appropriately for all our supported platforms
"""
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

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
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
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
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

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
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

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

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
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
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
            "SHLIB_PATH",  # HP-UX
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
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
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
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

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
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libiec60870.so"] = load_library("libiec60870.so")

# 1 libraries
# End libraries

# No modules

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

uint8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 27

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39
class struct_sSerialPort(Structure):
    pass

SerialPort = POINTER(struct_sSerialPort)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

enum_anon_18 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_NONE = 0# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_ARGUMENT = 1# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_INVALID_BAUDRATE = 2# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_OPEN_FAILED = 3# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SERIAL_PORT_ERROR_UNKNOWN = 99# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

SerialPortError = enum_anon_18# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 47

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 61
for _lib in _libs.values():
    if not _lib.has("SerialPort_create", "cdecl"):
        continue
    SerialPort_create = _lib.get("SerialPort_create", "cdecl")
    SerialPort_create.argtypes = [String, c_int, uint8_t, c_char, uint8_t]
    SerialPort_create.restype = SerialPort
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 67
for _lib in _libs.values():
    if not _lib.has("SerialPort_destroy", "cdecl"):
        continue
    SerialPort_destroy = _lib.get("SerialPort_destroy", "cdecl")
    SerialPort_destroy.argtypes = [SerialPort]
    SerialPort_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 75
for _lib in _libs.values():
    if not _lib.has("SerialPort_open", "cdecl"):
        continue
    SerialPort_open = _lib.get("SerialPort_open", "cdecl")
    SerialPort_open.argtypes = [SerialPort]
    SerialPort_open.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 81
for _lib in _libs.values():
    if not _lib.has("SerialPort_close", "cdecl"):
        continue
    SerialPort_close = _lib.get("SerialPort_close", "cdecl")
    SerialPort_close.argtypes = [SerialPort]
    SerialPort_close.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 89
for _lib in _libs.values():
    if not _lib.has("SerialPort_getBaudRate", "cdecl"):
        continue
    SerialPort_getBaudRate = _lib.get("SerialPort_getBaudRate", "cdecl")
    SerialPort_getBaudRate.argtypes = [SerialPort]
    SerialPort_getBaudRate.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 97
for _lib in _libs.values():
    if not _lib.has("SerialPort_setTimeout", "cdecl"):
        continue
    SerialPort_setTimeout = _lib.get("SerialPort_setTimeout", "cdecl")
    SerialPort_setTimeout.argtypes = [SerialPort, c_int]
    SerialPort_setTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 103
for _lib in _libs.values():
    if not _lib.has("SerialPort_discardInBuffer", "cdecl"):
        continue
    SerialPort_discardInBuffer = _lib.get("SerialPort_discardInBuffer", "cdecl")
    SerialPort_discardInBuffer.argtypes = [SerialPort]
    SerialPort_discardInBuffer.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 111
for _lib in _libs.values():
    if not _lib.has("SerialPort_readByte", "cdecl"):
        continue
    SerialPort_readByte = _lib.get("SerialPort_readByte", "cdecl")
    SerialPort_readByte.argtypes = [SerialPort]
    SerialPort_readByte.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 123
for _lib in _libs.values():
    if not _lib.has("SerialPort_write", "cdecl"):
        continue
    SerialPort_write = _lib.get("SerialPort_write", "cdecl")
    SerialPort_write.argtypes = [SerialPort, POINTER(uint8_t), c_int, c_int]
    SerialPort_write.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 129
for _lib in _libs.values():
    if not _lib.has("SerialPort_getLastError", "cdecl"):
        continue
    SerialPort_getLastError = _lib.get("SerialPort_getLastError", "cdecl")
    SerialPort_getLastError.argtypes = [SerialPort]
    SerialPort_getLastError.restype = SerialPortError
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44
class struct_sServerSocket(Structure):
    pass

ServerSocket = POINTER(struct_sServerSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46
class struct_sUdpSocket(Structure):
    pass

UdpSocket = POINTER(struct_sUdpSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49
class struct_sSocket(Structure):
    pass

Socket = POINTER(struct_sSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52
class struct_sHandleSet(Structure):
    pass

HandleSet = POINTER(struct_sHandleSet)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

enum_anon_19 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTING = 0# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_FAILED = 1# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SOCKET_STATE_CONNECTED = 2# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

SocketState = enum_anon_19# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 60

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 69
for _lib in _libs.values():
    if not _lib.has("Handleset_new", "cdecl"):
        continue
    Handleset_new = _lib.get("Handleset_new", "cdecl")
    Handleset_new.argtypes = []
    Handleset_new.restype = HandleSet
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 75
for _lib in _libs.values():
    if not _lib.has("Handleset_reset", "cdecl"):
        continue
    Handleset_reset = _lib.get("Handleset_reset", "cdecl")
    Handleset_reset.argtypes = [HandleSet]
    Handleset_reset.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 84
for _lib in _libs.values():
    if not _lib.has("Handleset_addSocket", "cdecl"):
        continue
    Handleset_addSocket = _lib.get("Handleset_addSocket", "cdecl")
    Handleset_addSocket.argtypes = [HandleSet, Socket]
    Handleset_addSocket.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 90
for _lib in _libs.values():
    if not _lib.has("Handleset_removeSocket", "cdecl"):
        continue
    Handleset_removeSocket = _lib.get("Handleset_removeSocket", "cdecl")
    Handleset_removeSocket.argtypes = [HandleSet, Socket]
    Handleset_removeSocket.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 108
for _lib in _libs.values():
    if not _lib.has("Handleset_waitReady", "cdecl"):
        continue
    Handleset_waitReady = _lib.get("Handleset_waitReady", "cdecl")
    Handleset_waitReady.argtypes = [HandleSet, c_uint]
    Handleset_waitReady.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 116
for _lib in _libs.values():
    if not _lib.has("Handleset_destroy", "cdecl"):
        continue
    Handleset_destroy = _lib.get("Handleset_destroy", "cdecl")
    Handleset_destroy.argtypes = [HandleSet]
    Handleset_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 129
for _lib in _libs.values():
    if not _lib.has("TcpServerSocket_create", "cdecl"):
        continue
    TcpServerSocket_create = _lib.get("TcpServerSocket_create", "cdecl")
    TcpServerSocket_create.argtypes = [String, c_int]
    TcpServerSocket_create.restype = ServerSocket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 137
for _lib in _libs.values():
    if not _lib.has("UdpSocket_create", "cdecl"):
        continue
    UdpSocket_create = _lib.get("UdpSocket_create", "cdecl")
    UdpSocket_create.argtypes = []
    UdpSocket_create.restype = UdpSocket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 145
for _lib in _libs.values():
    if not _lib.has("UdpSocket_createIpV6", "cdecl"):
        continue
    UdpSocket_createIpV6 = _lib.get("UdpSocket_createIpV6", "cdecl")
    UdpSocket_createIpV6.argtypes = []
    UdpSocket_createIpV6.restype = UdpSocket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 156
for _lib in _libs.values():
    if not _lib.has("UdpSocket_addGroupMembership", "cdecl"):
        continue
    UdpSocket_addGroupMembership = _lib.get("UdpSocket_addGroupMembership", "cdecl")
    UdpSocket_addGroupMembership.argtypes = [UdpSocket, String]
    UdpSocket_addGroupMembership.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 167
for _lib in _libs.values():
    if not _lib.has("UdpSocket_setMulticastTtl", "cdecl"):
        continue
    UdpSocket_setMulticastTtl = _lib.get("UdpSocket_setMulticastTtl", "cdecl")
    UdpSocket_setMulticastTtl.argtypes = [UdpSocket, c_int]
    UdpSocket_setMulticastTtl.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 170
for _lib in _libs.values():
    if not _lib.has("UdpSocket_bind", "cdecl"):
        continue
    UdpSocket_bind = _lib.get("UdpSocket_bind", "cdecl")
    UdpSocket_bind.argtypes = [UdpSocket, String, c_int]
    UdpSocket_bind.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 173
for _lib in _libs.values():
    if not _lib.has("UdpSocket_sendTo", "cdecl"):
        continue
    UdpSocket_sendTo = _lib.get("UdpSocket_sendTo", "cdecl")
    UdpSocket_sendTo.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_sendTo.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 187
for _lib in _libs.values():
    if not _lib.has("UdpSocket_receiveFrom", "cdecl"):
        continue
    UdpSocket_receiveFrom = _lib.get("UdpSocket_receiveFrom", "cdecl")
    UdpSocket_receiveFrom.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_receiveFrom.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 191
for _lib in _libs.values():
    if not _lib.has("ServerSocket_listen", "cdecl"):
        continue
    ServerSocket_listen = _lib.get("ServerSocket_listen", "cdecl")
    ServerSocket_listen.argtypes = [ServerSocket]
    ServerSocket_listen.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 208
for _lib in _libs.values():
    if not _lib.has("ServerSocket_accept", "cdecl"):
        continue
    ServerSocket_accept = _lib.get("ServerSocket_accept", "cdecl")
    ServerSocket_accept.argtypes = [ServerSocket]
    ServerSocket_accept.restype = Socket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 221
for _lib in _libs.values():
    if not _lib.has("Socket_activateTcpKeepAlive", "cdecl"):
        continue
    Socket_activateTcpKeepAlive = _lib.get("Socket_activateTcpKeepAlive", "cdecl")
    Socket_activateTcpKeepAlive.argtypes = [Socket, c_int, c_int, c_int]
    Socket_activateTcpKeepAlive.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 233
for _lib in _libs.values():
    if not _lib.has("ServerSocket_setBacklog", "cdecl"):
        continue
    ServerSocket_setBacklog = _lib.get("ServerSocket_setBacklog", "cdecl")
    ServerSocket_setBacklog.argtypes = [ServerSocket, c_int]
    ServerSocket_setBacklog.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 245
for _lib in _libs.values():
    if not _lib.has("ServerSocket_destroy", "cdecl"):
        continue
    ServerSocket_destroy = _lib.get("ServerSocket_destroy", "cdecl")
    ServerSocket_destroy.argtypes = [ServerSocket]
    ServerSocket_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 255
for _lib in _libs.values():
    if not _lib.has("TcpSocket_create", "cdecl"):
        continue
    TcpSocket_create = _lib.get("TcpSocket_create", "cdecl")
    TcpSocket_create.argtypes = []
    TcpSocket_create.restype = Socket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 264
for _lib in _libs.values():
    if not _lib.has("Socket_setConnectTimeout", "cdecl"):
        continue
    Socket_setConnectTimeout = _lib.get("Socket_setConnectTimeout", "cdecl")
    Socket_setConnectTimeout.argtypes = [Socket, uint32_t]
    Socket_setConnectTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 278
for _lib in _libs.values():
    if not _lib.has("Socket_bind", "cdecl"):
        continue
    Socket_bind = _lib.get("Socket_bind", "cdecl")
    Socket_bind.argtypes = [Socket, String, c_int]
    Socket_bind.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 299
for _lib in _libs.values():
    if not _lib.has("Socket_connect", "cdecl"):
        continue
    Socket_connect = _lib.get("Socket_connect", "cdecl")
    Socket_connect.argtypes = [Socket, String, c_int]
    Socket_connect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 302
for _lib in _libs.values():
    if not _lib.has("Socket_connectAsync", "cdecl"):
        continue
    Socket_connectAsync = _lib.get("Socket_connectAsync", "cdecl")
    Socket_connectAsync.argtypes = [Socket, String, c_int]
    Socket_connectAsync.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 305
for _lib in _libs.values():
    if not _lib.has("Socket_checkAsyncConnectState", "cdecl"):
        continue
    Socket_checkAsyncConnectState = _lib.get("Socket_checkAsyncConnectState", "cdecl")
    Socket_checkAsyncConnectState.argtypes = [Socket]
    Socket_checkAsyncConnectState.restype = SocketState
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 324
for _lib in _libs.values():
    if not _lib.has("Socket_read", "cdecl"):
        continue
    Socket_read = _lib.get("Socket_read", "cdecl")
    Socket_read.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_read.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 336
for _lib in _libs.values():
    if not _lib.has("Socket_write", "cdecl"):
        continue
    Socket_write = _lib.get("Socket_write", "cdecl")
    Socket_write.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_write.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 338
for _lib in _libs.values():
    if not _lib.has("Socket_getLocalAddress", "cdecl"):
        continue
    Socket_getLocalAddress = _lib.get("Socket_getLocalAddress", "cdecl")
    Socket_getLocalAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getLocalAddress.restype = ReturnString
    else:
        Socket_getLocalAddress.restype = String
        Socket_getLocalAddress.errcheck = ReturnString
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 352
for _lib in _libs.values():
    if not _lib.has("Socket_getPeerAddress", "cdecl"):
        continue
    Socket_getPeerAddress = _lib.get("Socket_getPeerAddress", "cdecl")
    Socket_getPeerAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddress.restype = ReturnString
    else:
        Socket_getPeerAddress.restype = String
        Socket_getPeerAddress.errcheck = ReturnString
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 369
for _lib in _libs.values():
    if not _lib.has("Socket_getPeerAddressStatic", "cdecl"):
        continue
    Socket_getPeerAddressStatic = _lib.get("Socket_getPeerAddressStatic", "cdecl")
    Socket_getPeerAddressStatic.argtypes = [Socket, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddressStatic.restype = ReturnString
    else:
        Socket_getPeerAddressStatic.restype = String
        Socket_getPeerAddressStatic.errcheck = ReturnString
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 383
for _lib in _libs.values():
    if not _lib.has("Socket_destroy", "cdecl"):
        continue
    Socket_destroy = _lib.get("Socket_destroy", "cdecl")
    Socket_destroy.argtypes = [Socket]
    Socket_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38
class struct_sThread(Structure):
    pass

Thread = POINTER(struct_sThread)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

Semaphore = POINTER(None)# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 41

ThreadExecutionFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None))# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 44

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 56
for _lib in _libs.values():
    if not _lib.has("Thread_create", "cdecl"):
        continue
    Thread_create = _lib.get("Thread_create", "cdecl")
    Thread_create.argtypes = [ThreadExecutionFunction, POINTER(None), c_bool]
    Thread_create.restype = Thread
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 67
for _lib in _libs.values():
    if not _lib.has("Thread_start", "cdecl"):
        continue
    Thread_start = _lib.get("Thread_start", "cdecl")
    Thread_start.argtypes = [Thread]
    Thread_start.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 75
for _lib in _libs.values():
    if not _lib.has("Thread_destroy", "cdecl"):
        continue
    Thread_destroy = _lib.get("Thread_destroy", "cdecl")
    Thread_destroy.argtypes = [Thread]
    Thread_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 81
for _lib in _libs.values():
    if not _lib.has("Thread_sleep", "cdecl"):
        continue
    Thread_sleep = _lib.get("Thread_sleep", "cdecl")
    Thread_sleep.argtypes = [c_int]
    Thread_sleep.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 84
for _lib in _libs.values():
    if not _lib.has("Semaphore_create", "cdecl"):
        continue
    Semaphore_create = _lib.get("Semaphore_create", "cdecl")
    Semaphore_create.argtypes = [c_int]
    Semaphore_create.restype = Semaphore
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 88
for _lib in _libs.values():
    if not _lib.has("Semaphore_wait", "cdecl"):
        continue
    Semaphore_wait = _lib.get("Semaphore_wait", "cdecl")
    Semaphore_wait.argtypes = [Semaphore]
    Semaphore_wait.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 91
for _lib in _libs.values():
    if not _lib.has("Semaphore_post", "cdecl"):
        continue
    Semaphore_post = _lib.get("Semaphore_post", "cdecl")
    Semaphore_post.argtypes = [Semaphore]
    Semaphore_post.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 94
for _lib in _libs.values():
    if not _lib.has("Semaphore_destroy", "cdecl"):
        continue
    Semaphore_destroy = _lib.get("Semaphore_destroy", "cdecl")
    Semaphore_destroy.argtypes = [Semaphore]
    Semaphore_destroy.restype = None
    break

nsSinceEpoch = uint64_t# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 35

msSinceEpoch = uint64_t# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 36

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 47
for _lib in _libs.values():
    if not _lib.has("Hal_getTimeInMs", "cdecl"):
        continue
    Hal_getTimeInMs = _lib.get("Hal_getTimeInMs", "cdecl")
    Hal_getTimeInMs.argtypes = []
    Hal_getTimeInMs.restype = msSinceEpoch
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 58
for _lib in _libs.values():
    if not _lib.has("Hal_getTimeInNs", "cdecl"):
        continue
    Hal_getTimeInNs = _lib.get("Hal_getTimeInNs", "cdecl")
    Hal_getTimeInNs.argtypes = []
    Hal_getTimeInNs.restype = nsSinceEpoch
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 69
for _lib in _libs.values():
    if not _lib.has("Hal_setTimeInNs", "cdecl"):
        continue
    Hal_setTimeInNs = _lib.get("Hal_setTimeInNs", "cdecl")
    Hal_setTimeInNs.argtypes = [nsSinceEpoch]
    Hal_setTimeInNs.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 77
for _lib in _libs.values():
    if not _lib.has("Hal_getMonotonicTimeInMs", "cdecl"):
        continue
    Hal_getMonotonicTimeInMs = _lib.get("Hal_getMonotonicTimeInMs", "cdecl")
    Hal_getMonotonicTimeInMs.argtypes = []
    Hal_getMonotonicTimeInMs.restype = msSinceEpoch
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/hal_time.h: 85
for _lib in _libs.values():
    if not _lib.has("Hal_getMonotonicTimeInNs", "cdecl"):
        continue
    Hal_getMonotonicTimeInNs = _lib.get("Hal_getMonotonicTimeInNs", "cdecl")
    Hal_getMonotonicTimeInNs.argtypes = []
    Hal_getMonotonicTimeInNs.restype = nsSinceEpoch
    break

MemoryExceptionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 32

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 35
for _lib in _libs.values():
    if not _lib.has("Memory_installExceptionHandler", "cdecl"):
        continue
    Memory_installExceptionHandler = _lib.get("Memory_installExceptionHandler", "cdecl")
    Memory_installExceptionHandler.argtypes = [MemoryExceptionHandler, POINTER(None)]
    Memory_installExceptionHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 37
for _lib in _libs.values():
    if not _lib.has("Memory_malloc", "cdecl"):
        continue
    Memory_malloc = _lib.get("Memory_malloc", "cdecl")
    Memory_malloc.argtypes = [c_size_t]
    Memory_malloc.restype = POINTER(c_ubyte)
    Memory_malloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 40
for _lib in _libs.values():
    if not _lib.has("Memory_calloc", "cdecl"):
        continue
    Memory_calloc = _lib.get("Memory_calloc", "cdecl")
    Memory_calloc.argtypes = [c_size_t, c_size_t]
    Memory_calloc.restype = POINTER(c_ubyte)
    Memory_calloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 43
for _lib in _libs.values():
    if not _lib.has("Memory_realloc", "cdecl"):
        continue
    Memory_realloc = _lib.get("Memory_realloc", "cdecl")
    Memory_realloc.argtypes = [POINTER(None), c_size_t]
    Memory_realloc.restype = POINTER(c_ubyte)
    Memory_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 47
for _lib in _libs.values():
    if not _lib.has("Memory_free", "cdecl"):
        continue
    Memory_free = _lib.get("Memory_free", "cdecl")
    Memory_free.argtypes = [POINTER(None)]
    Memory_free.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 48
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_create", "cdecl"):
        continue
    TLSConfiguration_create = _lib.get("TLSConfiguration_create", "cdecl")
    TLSConfiguration_create.argtypes = []
    TLSConfiguration_create.restype = TLSConfiguration
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 52
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setClientMode", "cdecl"):
        continue
    TLSConfiguration_setClientMode = _lib.get("TLSConfiguration_setClientMode", "cdecl")
    TLSConfiguration_setClientMode.argtypes = [TLSConfiguration]
    TLSConfiguration_setClientMode.restype = None
    break

enum_anon_20 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_NOT_SELECTED = 0# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_SSL_3_0 = 3# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_0 = 4# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_1 = 5# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_2 = 6# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLS_VERSION_TLS_1_3 = 7# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

TLSConfigVersion = enum_anon_20# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 61

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 70
for _lib in _libs.values():
    if not _lib.has("TLSConfigVersion_toString", "cdecl"):
        continue
    TLSConfigVersion_toString = _lib.get("TLSConfigVersion_toString", "cdecl")
    TLSConfigVersion_toString.argtypes = [TLSConfigVersion]
    TLSConfigVersion_toString.restype = c_char_p
    break

enum_anon_21 = c_int# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INFO = 0# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_WARNING = 1# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLS_SEC_EVT_INCIDENT = 2# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

TLSEventLevel = enum_anon_21# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 77

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 100
class struct_sTLSConnection(Structure):
    pass

TLSConnection = POINTER(struct_sTLSConnection)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 100

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 110
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerAddress", "cdecl"):
        continue
    TLSConnection_getPeerAddress = _lib.get("TLSConnection_getPeerAddress", "cdecl")
    TLSConnection_getPeerAddress.argtypes = [TLSConnection, String]
    if sizeof(c_int) == sizeof(c_void_p):
        TLSConnection_getPeerAddress.restype = ReturnString
    else:
        TLSConnection_getPeerAddress.restype = String
        TLSConnection_getPeerAddress.errcheck = ReturnString
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 121
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerCertificate", "cdecl"):
        continue
    TLSConnection_getPeerCertificate = _lib.get("TLSConnection_getPeerCertificate", "cdecl")
    TLSConnection_getPeerCertificate.argtypes = [TLSConnection, POINTER(c_int)]
    TLSConnection_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 132
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getTLSVersion", "cdecl"):
        continue
    TLSConnection_getTLSVersion = _lib.get("TLSConnection_getTLSVersion", "cdecl")
    TLSConnection_getTLSVersion.argtypes = [TLSConnection]
    TLSConnection_getTLSVersion.restype = TLSConfigVersion
    break

TLSConfiguration_EventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), TLSEventLevel, c_int, String, TLSConnection)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 134

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 143
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setEventHandler", "cdecl"):
        continue
    TLSConfiguration_setEventHandler = _lib.get("TLSConfiguration_setEventHandler", "cdecl")
    TLSConfiguration_setEventHandler.argtypes = [TLSConfiguration, TLSConfiguration_EventHandler, POINTER(None)]
    TLSConfiguration_setEventHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 154
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_enableSessionResumption", "cdecl"):
        continue
    TLSConfiguration_enableSessionResumption = _lib.get("TLSConfiguration_enableSessionResumption", "cdecl")
    TLSConfiguration_enableSessionResumption.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_enableSessionResumption.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 162
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setSessionResumptionInterval", "cdecl"):
        continue
    TLSConfiguration_setSessionResumptionInterval = _lib.get("TLSConfiguration_setSessionResumptionInterval", "cdecl")
    TLSConfiguration_setSessionResumptionInterval.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setSessionResumptionInterval.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 170
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setChainValidation", "cdecl"):
        continue
    TLSConfiguration_setChainValidation = _lib.get("TLSConfiguration_setChainValidation", "cdecl")
    TLSConfiguration_setChainValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setChainValidation.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 178
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setTimeValidation", "cdecl"):
        continue
    TLSConfiguration_setTimeValidation = _lib.get("TLSConfiguration_setTimeValidation", "cdecl")
    TLSConfiguration_setTimeValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setTimeValidation.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 189
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl"):
        continue
    TLSConfiguration_setAllowOnlyKnownCertificates = _lib.get("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl")
    TLSConfiguration_setAllowOnlyKnownCertificates.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setAllowOnlyKnownCertificates.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 200
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificate", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificate = _lib.get("TLSConfiguration_setOwnCertificate", "cdecl")
    TLSConfiguration_setOwnCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_setOwnCertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 210
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificateFromFile = _lib.get("TLSConfiguration_setOwnCertificateFromFile", "cdecl")
    TLSConfiguration_setOwnCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_setOwnCertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 222
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKey", "cdecl"):
        continue
    TLSConfiguration_setOwnKey = _lib.get("TLSConfiguration_setOwnKey", "cdecl")
    TLSConfiguration_setOwnKey.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int, String]
    TLSConfiguration_setOwnKey.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 233
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKeyFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnKeyFromFile = _lib.get("TLSConfiguration_setOwnKeyFromFile", "cdecl")
    TLSConfiguration_setOwnKeyFromFile.argtypes = [TLSConfiguration, String, String]
    TLSConfiguration_setOwnKeyFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 243
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificate", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificate = _lib.get("TLSConfiguration_addAllowedCertificate", "cdecl")
    TLSConfiguration_addAllowedCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addAllowedCertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 252
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificateFromFile = _lib.get("TLSConfiguration_addAllowedCertificateFromFile", "cdecl")
    TLSConfiguration_addAllowedCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addAllowedCertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 262
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificate", "cdecl"):
        continue
    TLSConfiguration_addCACertificate = _lib.get("TLSConfiguration_addCACertificate", "cdecl")
    TLSConfiguration_addCACertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCACertificate.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 271
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addCACertificateFromFile = _lib.get("TLSConfiguration_addCACertificateFromFile", "cdecl")
    TLSConfiguration_addCACertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCACertificateFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 281
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setRenegotiationTime", "cdecl"):
        continue
    TLSConfiguration_setRenegotiationTime = _lib.get("TLSConfiguration_setRenegotiationTime", "cdecl")
    TLSConfiguration_setRenegotiationTime.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setRenegotiationTime.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 287
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMinTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMinTlsVersion = _lib.get("TLSConfiguration_setMinTlsVersion", "cdecl")
    TLSConfiguration_setMinTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMinTlsVersion.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 293
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMaxTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMaxTlsVersion = _lib.get("TLSConfiguration_setMaxTlsVersion", "cdecl")
    TLSConfiguration_setMaxTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMaxTlsVersion.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 303
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRL", "cdecl"):
        continue
    TLSConfiguration_addCRL = _lib.get("TLSConfiguration_addCRL", "cdecl")
    TLSConfiguration_addCRL.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCRL.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 312
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRLFromFile", "cdecl"):
        continue
    TLSConfiguration_addCRLFromFile = _lib.get("TLSConfiguration_addCRLFromFile", "cdecl")
    TLSConfiguration_addCRLFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCRLFromFile.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 318
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_resetCRL", "cdecl"):
        continue
    TLSConfiguration_resetCRL = _lib.get("TLSConfiguration_resetCRL", "cdecl")
    TLSConfiguration_resetCRL.argtypes = [TLSConfiguration]
    TLSConfiguration_resetCRL.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 327
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCipherSuite", "cdecl"):
        continue
    TLSConfiguration_addCipherSuite = _lib.get("TLSConfiguration_addCipherSuite", "cdecl")
    TLSConfiguration_addCipherSuite.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_addCipherSuite.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 335
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_clearCipherSuiteList", "cdecl"):
        continue
    TLSConfiguration_clearCipherSuiteList = _lib.get("TLSConfiguration_clearCipherSuiteList", "cdecl")
    TLSConfiguration_clearCipherSuiteList.argtypes = [TLSConfiguration]
    TLSConfiguration_clearCipherSuiteList.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 343
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_destroy", "cdecl"):
        continue
    TLSConfiguration_destroy = _lib.get("TLSConfiguration_destroy", "cdecl")
    TLSConfiguration_destroy.argtypes = [TLSConfiguration]
    TLSConfiguration_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48
class struct_sTLSSocket(Structure):
    pass

TLSSocket = POINTER(struct_sTLSSocket)# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 63
for _lib in _libs.values():
    if not _lib.has("TLSSocket_create", "cdecl"):
        continue
    TLSSocket_create = _lib.get("TLSSocket_create", "cdecl")
    TLSSocket_create.argtypes = [Socket, TLSConfiguration, c_bool]
    TLSSocket_create.restype = TLSSocket
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 69
for _lib in _libs.values():
    if not _lib.has("TLSSocket_performHandshake", "cdecl"):
        continue
    TLSSocket_performHandshake = _lib.get("TLSSocket_performHandshake", "cdecl")
    TLSSocket_performHandshake.argtypes = [TLSSocket]
    TLSSocket_performHandshake.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 78
for _lib in _libs.values():
    if not _lib.has("TLSSocket_getPeerCertificate", "cdecl"):
        continue
    TLSSocket_getPeerCertificate = _lib.get("TLSSocket_getPeerCertificate", "cdecl")
    TLSSocket_getPeerCertificate.argtypes = [TLSSocket, POINTER(c_int)]
    TLSSocket_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 94
for _lib in _libs.values():
    if not _lib.has("TLSSocket_read", "cdecl"):
        continue
    TLSSocket_read = _lib.get("TLSSocket_read", "cdecl")
    TLSSocket_read.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_read.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 106
for _lib in _libs.values():
    if not _lib.has("TLSSocket_write", "cdecl"):
        continue
    TLSSocket_write = _lib.get("TLSSocket_write", "cdecl")
    TLSSocket_write.argtypes = [TLSSocket, POINTER(uint8_t), c_int]
    TLSSocket_write.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 112
for _lib in _libs.values():
    if not _lib.has("TLSSocket_close", "cdecl"):
        continue
    TLSSocket_close = _lib.get("TLSSocket_close", "cdecl")
    TLSSocket_close.argtypes = [TLSSocket]
    TLSSocket_close.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'major',
    'minor',
    'patch',
]
struct_anon_22._fields_ = [
    ('major', c_int),
    ('minor', c_int),
    ('patch', c_int),
]

Lib60870VersionInfo = struct_anon_22# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 59

enum_anon_23 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_BALANCED = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LINK_LAYER_UNBALANCED = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

IEC60870_LinkLayerMode = enum_anon_23# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 67

enum_anon_24 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_IDLE = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_ERROR = (LL_STATE_IDLE + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_BUSY = (LL_STATE_ERROR + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LL_STATE_AVAILABLE = (LL_STATE_BUSY + 1)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

LinkLayerState = enum_anon_24# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 82

IEC60870_LinkLayerStateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int, LinkLayerState)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 91

IEC60870_RawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t), c_int, c_bool)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 105

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112
class struct_sCS101_AppLayerParameters(Structure):
    pass

CS101_AppLayerParameters = POINTER(struct_sCS101_AppLayerParameters)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 110

struct_sCS101_AppLayerParameters.__slots__ = [
    'sizeOfTypeId',
    'sizeOfVSQ',
    'sizeOfCOT',
    'originatorAddress',
    'sizeOfCA',
    'sizeOfIOA',
    'maxSizeOfASDU',
]
struct_sCS101_AppLayerParameters._fields_ = [
    ('sizeOfTypeId', c_int),
    ('sizeOfVSQ', c_int),
    ('sizeOfCOT', c_int),
    ('originatorAddress', c_int),
    ('sizeOfCA', c_int),
    ('sizeOfIOA', c_int),
    ('maxSizeOfASDU', c_int),
]

enum_anon_25 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_NA_1 = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_TA_1 = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_NA_1 = 3# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_TA_1 = 4# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_NA_1 = 5# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_TA_1 = 6# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_NA_1 = 7# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_TA_1 = 8# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NA_1 = 9# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TA_1 = 10# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NB_1 = 11# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TB_1 = 12# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_NC_1 = 13# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TC_1 = 14# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_NA_1 = 15# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_TA_1 = 16# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TA_1 = 17# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TB_1 = 18# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TC_1 = 19# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_PS_NA_1 = 20# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_ND_1 = 21# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_SP_TB_1 = 30# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_DP_TB_1 = 31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ST_TB_1 = 32# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_BO_TB_1 = 33# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TD_1 = 34# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TE_1 = 35# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_ME_TF_1 = 36# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_IT_TB_1 = 37# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TD_1 = 38# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TE_1 = 39# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EP_TF_1 = 40# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_IT_TC_1 = 41# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SC_NA_1 = 45# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_DC_NA_1 = 46# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RC_NA_1 = 47# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NA_1 = 48# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NB_1 = 49# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_NC_1 = 50# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_BO_NA_1 = 51# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SC_TA_1 = 58# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_DC_TA_1 = 59# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RC_TA_1 = 60# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TA_1 = 61# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TB_1 = 62# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_SE_TC_1 = 63# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_BO_TA_1 = 64# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

M_EI_NA_1 = 70# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_CH_NA_1 = 81# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_RP_NA_1 = 82# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_AR_NA_1 = 83# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KR_NA_1 = 84# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KS_NA_1 = 85# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_KC_NA_1 = 86# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_ER_NA_1 = 87# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_US_NA_1 = 90# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UQ_NA_1 = 91# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UR_NA_1 = 92# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UK_NA_1 = 93# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UA_NA_1 = 94# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

S_UC_NA_1 = 95# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_IC_NA_1 = 100# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CI_NA_1 = 101# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RD_NA_1 = 102# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CS_NA_1 = 103# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_TS_NA_1 = 104# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_RP_NA_1 = 105# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_CD_NA_1 = 106# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

C_TS_TA_1 = 107# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NA_1 = 110# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NB_1 = 111# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_ME_NC_1 = 112# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

P_AC_NA_1 = 113# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_FR_NA_1 = 120# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SR_NA_1 = 121# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SC_NA_1 = 122# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_LS_NA_1 = 123# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_AF_NA_1 = 124# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SG_NA_1 = 125# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_DR_TA_1 = 126# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

F_SC_NB_1 = 127# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

IEC60870_5_TypeID = enum_anon_25# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 207

TypeID = IEC60870_5_TypeID# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 209

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211
class struct_sInformationObject(Structure):
    pass

InformationObject = POINTER(struct_sInformationObject)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216
class struct_sCS101_ASDU(Structure):
    pass

CS101_ASDU = POINTER(struct_sCS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 225
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'parameters',
    'asdu',
    'asduHeaderLength',
    'payload',
    'payloadSize',
    'encodedData',
]
struct_anon_26._fields_ = [
    ('parameters', CS101_AppLayerParameters),
    ('asdu', POINTER(uint8_t)),
    ('asduHeaderLength', c_int),
    ('payload', POINTER(uint8_t)),
    ('payloadSize', c_int),
    ('encodedData', uint8_t * int(256)),
]

sCS101_StaticASDU = struct_anon_26# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 225

CS101_StaticASDU = POINTER(sCS101_StaticASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 227

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 231
class struct_sCP16Time2a(Structure):
    pass

CP16Time2a = POINTER(struct_sCP16Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 229

struct_sCP16Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP16Time2a._fields_ = [
    ('encodedValue', uint8_t * int(2)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 237
class struct_sCP24Time2a(Structure):
    pass

CP24Time2a = POINTER(struct_sCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 235

struct_sCP24Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP24Time2a._fields_ = [
    ('encodedValue', uint8_t * int(3)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 246
class struct_sCP32Time2a(Structure):
    pass

CP32Time2a = POINTER(struct_sCP32Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 241

struct_sCP32Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP32Time2a._fields_ = [
    ('encodedValue', uint8_t * int(4)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 255
class struct_sCP56Time2a(Structure):
    pass

CP56Time2a = POINTER(struct_sCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 253

struct_sCP56Time2a.__slots__ = [
    'encodedValue',
]
struct_sCP56Time2a._fields_ = [
    ('encodedValue', uint8_t * int(7)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 264
class struct_sBinaryCounterReading(Structure):
    pass

BinaryCounterReading = POINTER(struct_sBinaryCounterReading)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 262

struct_sBinaryCounterReading.__slots__ = [
    'encodedValue',
]
struct_sBinaryCounterReading._fields_ = [
    ('encodedValue', uint8_t * int(5)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 273
class struct_sCS104_APCIParameters(Structure):
    pass

CS104_APCIParameters = POINTER(struct_sCS104_APCIParameters)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 271

struct_sCS104_APCIParameters.__slots__ = [
    'k',
    'w',
    't0',
    't1',
    't2',
    't3',
]
struct_sCS104_APCIParameters._fields_ = [
    ('k', c_int),
    ('w', c_int),
    ('t0', c_int),
    ('t1', c_int),
    ('t2', c_int),
    ('t3', c_int),
]

enum_anon_27 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_PERIODIC = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_BACKGROUND_SCAN = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_SPONTANEOUS = 3# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INITIALIZED = 4# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUEST = 5# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION = 6# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION_CON = 7# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_DEACTIVATION = 8# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_DEACTIVATION_CON = 9# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_ACTIVATION_TERMINATION = 10# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_RETURN_INFO_REMOTE = 11# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_RETURN_INFO_LOCAL = 12# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_FILE_TRANSFER = 13# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_AUTHENTICATION = 14# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_MAINTENANCE_OF_AUTH_SESSION_KEY = 15# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_MAINTENANCE_OF_USER_ROLE_AND_UPDATE_KEY = 16# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_STATION = 20# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_1 = 21# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_2 = 22# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_3 = 23# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_4 = 24# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_5 = 25# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_6 = 26# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_7 = 27# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_8 = 28# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_9 = 29# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_10 = 30# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_11 = 31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_12 = 32# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_13 = 33# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_14 = 34# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_15 = 35# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_INTERROGATED_BY_GROUP_16 = 36# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GENERAL_COUNTER = 37# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_1_COUNTER = 38# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_2_COUNTER = 39# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_3_COUNTER = 40# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_REQUESTED_BY_GROUP_4_COUNTER = 41# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_TYPE_ID = 44# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_COT = 45# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_CA = 46# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_COT_UNKNOWN_IOA = 47# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

CS101_CauseOfTransmission = enum_anon_27# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 327

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 329
for _lib in _libs.values():
    if not _lib.has("CS101_CauseOfTransmission_toString", "cdecl"):
        continue
    CS101_CauseOfTransmission_toString = _lib.get("CS101_CauseOfTransmission_toString", "cdecl")
    CS101_CauseOfTransmission_toString.argtypes = [CS101_CauseOfTransmission]
    CS101_CauseOfTransmission_toString.restype = c_char_p
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 333
for _lib in _libs.values():
    if not _lib.has("Lib60870_enableDebugOutput", "cdecl"):
        continue
    Lib60870_enableDebugOutput = _lib.get("Lib60870_enableDebugOutput", "cdecl")
    Lib60870_enableDebugOutput.argtypes = [c_bool]
    Lib60870_enableDebugOutput.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 336
for _lib in _libs.values():
    if not _lib.has("Lib60870_getLibraryVersionInfo", "cdecl"):
        continue
    Lib60870_getLibraryVersionInfo = _lib.get("Lib60870_getLibraryVersionInfo", "cdecl")
    Lib60870_getLibraryVersionInfo.argtypes = []
    Lib60870_getLibraryVersionInfo.restype = Lib60870VersionInfo
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 342
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_isTest", "cdecl"):
        continue
    CS101_ASDU_isTest = _lib.get("CS101_ASDU_isTest", "cdecl")
    CS101_ASDU_isTest.argtypes = [CS101_ASDU]
    CS101_ASDU_isTest.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 348
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setTest", "cdecl"):
        continue
    CS101_ASDU_setTest = _lib.get("CS101_ASDU_setTest", "cdecl")
    CS101_ASDU_setTest.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setTest.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 354
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_isNegative", "cdecl"):
        continue
    CS101_ASDU_isNegative = _lib.get("CS101_ASDU_isNegative", "cdecl")
    CS101_ASDU_isNegative.argtypes = [CS101_ASDU]
    CS101_ASDU_isNegative.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 360
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setNegative", "cdecl"):
        continue
    CS101_ASDU_setNegative = _lib.get("CS101_ASDU_setNegative", "cdecl")
    CS101_ASDU_setNegative.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setNegative.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 366
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getOA", "cdecl"):
        continue
    CS101_ASDU_getOA = _lib.get("CS101_ASDU_getOA", "cdecl")
    CS101_ASDU_getOA.argtypes = [CS101_ASDU]
    CS101_ASDU_getOA.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 372
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getCOT", "cdecl"):
        continue
    CS101_ASDU_getCOT = _lib.get("CS101_ASDU_getCOT", "cdecl")
    CS101_ASDU_getCOT.argtypes = [CS101_ASDU]
    CS101_ASDU_getCOT.restype = CS101_CauseOfTransmission
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 378
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setCOT", "cdecl"):
        continue
    CS101_ASDU_setCOT = _lib.get("CS101_ASDU_setCOT", "cdecl")
    CS101_ASDU_setCOT.argtypes = [CS101_ASDU, CS101_CauseOfTransmission]
    CS101_ASDU_setCOT.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 384
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getCA", "cdecl"):
        continue
    CS101_ASDU_getCA = _lib.get("CS101_ASDU_getCA", "cdecl")
    CS101_ASDU_getCA.argtypes = [CS101_ASDU]
    CS101_ASDU_getCA.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 392
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setCA", "cdecl"):
        continue
    CS101_ASDU_setCA = _lib.get("CS101_ASDU_setCA", "cdecl")
    CS101_ASDU_setCA.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setCA.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 401
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getTypeID", "cdecl"):
        continue
    CS101_ASDU_getTypeID = _lib.get("CS101_ASDU_getTypeID", "cdecl")
    CS101_ASDU_getTypeID.argtypes = [CS101_ASDU]
    CS101_ASDU_getTypeID.restype = IEC60870_5_TypeID
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 413
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setTypeID", "cdecl"):
        continue
    CS101_ASDU_setTypeID = _lib.get("CS101_ASDU_setTypeID", "cdecl")
    CS101_ASDU_setTypeID.argtypes = [CS101_ASDU, IEC60870_5_TypeID]
    CS101_ASDU_setTypeID.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 424
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_isSequence", "cdecl"):
        continue
    CS101_ASDU_isSequence = _lib.get("CS101_ASDU_isSequence", "cdecl")
    CS101_ASDU_isSequence.argtypes = [CS101_ASDU]
    CS101_ASDU_isSequence.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 435
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setSequence", "cdecl"):
        continue
    CS101_ASDU_setSequence = _lib.get("CS101_ASDU_setSequence", "cdecl")
    CS101_ASDU_setSequence.argtypes = [CS101_ASDU, c_bool]
    CS101_ASDU_setSequence.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 443
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getNumberOfElements", "cdecl"):
        continue
    CS101_ASDU_getNumberOfElements = _lib.get("CS101_ASDU_getNumberOfElements", "cdecl")
    CS101_ASDU_getNumberOfElements.argtypes = [CS101_ASDU]
    CS101_ASDU_getNumberOfElements.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 455
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_setNumberOfElements", "cdecl"):
        continue
    CS101_ASDU_setNumberOfElements = _lib.get("CS101_ASDU_setNumberOfElements", "cdecl")
    CS101_ASDU_setNumberOfElements.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_setNumberOfElements.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 465
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getElement", "cdecl"):
        continue
    CS101_ASDU_getElement = _lib.get("CS101_ASDU_getElement", "cdecl")
    CS101_ASDU_getElement.argtypes = [CS101_ASDU, c_int]
    CS101_ASDU_getElement.restype = InformationObject
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 476
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getElementEx", "cdecl"):
        continue
    CS101_ASDU_getElementEx = _lib.get("CS101_ASDU_getElementEx", "cdecl")
    CS101_ASDU_getElementEx.argtypes = [CS101_ASDU, InformationObject, c_int]
    CS101_ASDU_getElementEx.restype = InformationObject
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 492
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_create", "cdecl"):
        continue
    CS101_ASDU_create = _lib.get("CS101_ASDU_create", "cdecl")
    CS101_ASDU_create.argtypes = [CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_create.restype = CS101_ASDU
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 507
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_createFromBuffer", "cdecl"):
        continue
    CS101_ASDU_createFromBuffer = _lib.get("CS101_ASDU_createFromBuffer", "cdecl")
    CS101_ASDU_createFromBuffer.argtypes = [CS101_AppLayerParameters, POINTER(uint8_t), c_int]
    CS101_ASDU_createFromBuffer.restype = CS101_ASDU
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 526
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_initializeStatic", "cdecl"):
        continue
    CS101_ASDU_initializeStatic = _lib.get("CS101_ASDU_initializeStatic", "cdecl")
    CS101_ASDU_initializeStatic.argtypes = [CS101_StaticASDU, CS101_AppLayerParameters, c_bool, CS101_CauseOfTransmission, c_int, c_int, c_bool, c_bool]
    CS101_ASDU_initializeStatic.restype = CS101_ASDU
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 538
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_clone", "cdecl"):
        continue
    CS101_ASDU_clone = _lib.get("CS101_ASDU_clone", "cdecl")
    CS101_ASDU_clone.argtypes = [CS101_ASDU, CS101_StaticASDU]
    CS101_ASDU_clone.restype = CS101_ASDU
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 547
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getPayload", "cdecl"):
        continue
    CS101_ASDU_getPayload = _lib.get("CS101_ASDU_getPayload", "cdecl")
    CS101_ASDU_getPayload.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayload.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 563
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_addPayload", "cdecl"):
        continue
    CS101_ASDU_addPayload = _lib.get("CS101_ASDU_addPayload", "cdecl")
    CS101_ASDU_addPayload.argtypes = [CS101_ASDU, POINTER(uint8_t), c_int]
    CS101_ASDU_addPayload.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 573
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_getPayloadSize", "cdecl"):
        continue
    CS101_ASDU_getPayloadSize = _lib.get("CS101_ASDU_getPayloadSize", "cdecl")
    CS101_ASDU_getPayloadSize.argtypes = [CS101_ASDU]
    CS101_ASDU_getPayloadSize.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 579
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_destroy", "cdecl"):
        continue
    CS101_ASDU_destroy = _lib.get("CS101_ASDU_destroy", "cdecl")
    CS101_ASDU_destroy.argtypes = [CS101_ASDU]
    CS101_ASDU_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 592
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_addInformationObject", "cdecl"):
        continue
    CS101_ASDU_addInformationObject = _lib.get("CS101_ASDU_addInformationObject", "cdecl")
    CS101_ASDU_addInformationObject.argtypes = [CS101_ASDU, InformationObject]
    CS101_ASDU_addInformationObject.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 600
for _lib in _libs.values():
    if not _lib.has("CS101_ASDU_removeAllElements", "cdecl"):
        continue
    CS101_ASDU_removeAllElements = _lib.get("CS101_ASDU_removeAllElements", "cdecl")
    CS101_ASDU_removeAllElements.argtypes = [CS101_ASDU]
    CS101_ASDU_removeAllElements.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 606
for _lib in _libs.values():
    if not _lib.has("CP16Time2a_getEplapsedTimeInMs", "cdecl"):
        continue
    CP16Time2a_getEplapsedTimeInMs = _lib.get("CP16Time2a_getEplapsedTimeInMs", "cdecl")
    CP16Time2a_getEplapsedTimeInMs.argtypes = [CP16Time2a]
    CP16Time2a_getEplapsedTimeInMs.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 612
for _lib in _libs.values():
    if not _lib.has("CP16Time2a_setEplapsedTimeInMs", "cdecl"):
        continue
    CP16Time2a_setEplapsedTimeInMs = _lib.get("CP16Time2a_setEplapsedTimeInMs", "cdecl")
    CP16Time2a_setEplapsedTimeInMs.argtypes = [CP16Time2a, c_int]
    CP16Time2a_setEplapsedTimeInMs.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 618
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_getMillisecond", "cdecl"):
        continue
    CP24Time2a_getMillisecond = _lib.get("CP24Time2a_getMillisecond", "cdecl")
    CP24Time2a_getMillisecond.argtypes = [CP24Time2a]
    CP24Time2a_getMillisecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 624
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_setMillisecond", "cdecl"):
        continue
    CP24Time2a_setMillisecond = _lib.get("CP24Time2a_setMillisecond", "cdecl")
    CP24Time2a_setMillisecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMillisecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 630
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_getSecond", "cdecl"):
        continue
    CP24Time2a_getSecond = _lib.get("CP24Time2a_getSecond", "cdecl")
    CP24Time2a_getSecond.argtypes = [CP24Time2a]
    CP24Time2a_getSecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 636
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_setSecond", "cdecl"):
        continue
    CP24Time2a_setSecond = _lib.get("CP24Time2a_setSecond", "cdecl")
    CP24Time2a_setSecond.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setSecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 642
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_getMinute", "cdecl"):
        continue
    CP24Time2a_getMinute = _lib.get("CP24Time2a_getMinute", "cdecl")
    CP24Time2a_getMinute.argtypes = [CP24Time2a]
    CP24Time2a_getMinute.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 648
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_setMinute", "cdecl"):
        continue
    CP24Time2a_setMinute = _lib.get("CP24Time2a_setMinute", "cdecl")
    CP24Time2a_setMinute.argtypes = [CP24Time2a, c_int]
    CP24Time2a_setMinute.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 654
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_isInvalid", "cdecl"):
        continue
    CP24Time2a_isInvalid = _lib.get("CP24Time2a_isInvalid", "cdecl")
    CP24Time2a_isInvalid.argtypes = [CP24Time2a]
    CP24Time2a_isInvalid.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 660
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_setInvalid", "cdecl"):
        continue
    CP24Time2a_setInvalid = _lib.get("CP24Time2a_setInvalid", "cdecl")
    CP24Time2a_setInvalid.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setInvalid.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 666
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_isSubstituted", "cdecl"):
        continue
    CP24Time2a_isSubstituted = _lib.get("CP24Time2a_isSubstituted", "cdecl")
    CP24Time2a_isSubstituted.argtypes = [CP24Time2a]
    CP24Time2a_isSubstituted.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 672
for _lib in _libs.values():
    if not _lib.has("CP24Time2a_setSubstituted", "cdecl"):
        continue
    CP24Time2a_setSubstituted = _lib.get("CP24Time2a_setSubstituted", "cdecl")
    CP24Time2a_setSubstituted.argtypes = [CP24Time2a, c_bool]
    CP24Time2a_setSubstituted.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 678
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_createFromMsTimestamp", "cdecl"):
        continue
    CP56Time2a_createFromMsTimestamp = _lib.get("CP56Time2a_createFromMsTimestamp", "cdecl")
    CP56Time2a_createFromMsTimestamp.argtypes = [CP56Time2a, uint64_t]
    CP56Time2a_createFromMsTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 682
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_create", "cdecl"):
        continue
    CP32Time2a_create = _lib.get("CP32Time2a_create", "cdecl")
    CP32Time2a_create.argtypes = [CP32Time2a]
    CP32Time2a_create.restype = CP32Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 685
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setFromMsTimestamp", "cdecl"):
        continue
    CP32Time2a_setFromMsTimestamp = _lib.get("CP32Time2a_setFromMsTimestamp", "cdecl")
    CP32Time2a_setFromMsTimestamp.argtypes = [CP32Time2a, uint64_t]
    CP32Time2a_setFromMsTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 688
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_getMillisecond", "cdecl"):
        continue
    CP32Time2a_getMillisecond = _lib.get("CP32Time2a_getMillisecond", "cdecl")
    CP32Time2a_getMillisecond.argtypes = [CP32Time2a]
    CP32Time2a_getMillisecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 691
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setMillisecond", "cdecl"):
        continue
    CP32Time2a_setMillisecond = _lib.get("CP32Time2a_setMillisecond", "cdecl")
    CP32Time2a_setMillisecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMillisecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 694
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_getSecond", "cdecl"):
        continue
    CP32Time2a_getSecond = _lib.get("CP32Time2a_getSecond", "cdecl")
    CP32Time2a_getSecond.argtypes = [CP32Time2a]
    CP32Time2a_getSecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 697
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setSecond", "cdecl"):
        continue
    CP32Time2a_setSecond = _lib.get("CP32Time2a_setSecond", "cdecl")
    CP32Time2a_setSecond.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setSecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 700
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_getMinute", "cdecl"):
        continue
    CP32Time2a_getMinute = _lib.get("CP32Time2a_getMinute", "cdecl")
    CP32Time2a_getMinute.argtypes = [CP32Time2a]
    CP32Time2a_getMinute.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 704
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setMinute", "cdecl"):
        continue
    CP32Time2a_setMinute = _lib.get("CP32Time2a_setMinute", "cdecl")
    CP32Time2a_setMinute.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setMinute.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 707
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_isInvalid", "cdecl"):
        continue
    CP32Time2a_isInvalid = _lib.get("CP32Time2a_isInvalid", "cdecl")
    CP32Time2a_isInvalid.argtypes = [CP32Time2a]
    CP32Time2a_isInvalid.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 710
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setInvalid", "cdecl"):
        continue
    CP32Time2a_setInvalid = _lib.get("CP32Time2a_setInvalid", "cdecl")
    CP32Time2a_setInvalid.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setInvalid.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 713
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_isSubstituted", "cdecl"):
        continue
    CP32Time2a_isSubstituted = _lib.get("CP32Time2a_isSubstituted", "cdecl")
    CP32Time2a_isSubstituted.argtypes = [CP32Time2a]
    CP32Time2a_isSubstituted.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 716
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setSubstituted", "cdecl"):
        continue
    CP32Time2a_setSubstituted = _lib.get("CP32Time2a_setSubstituted", "cdecl")
    CP32Time2a_setSubstituted.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSubstituted.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 719
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_getHour", "cdecl"):
        continue
    CP32Time2a_getHour = _lib.get("CP32Time2a_getHour", "cdecl")
    CP32Time2a_getHour.argtypes = [CP32Time2a]
    CP32Time2a_getHour.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 722
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setHour", "cdecl"):
        continue
    CP32Time2a_setHour = _lib.get("CP32Time2a_setHour", "cdecl")
    CP32Time2a_setHour.argtypes = [CP32Time2a, c_int]
    CP32Time2a_setHour.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 725
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_isSummerTime", "cdecl"):
        continue
    CP32Time2a_isSummerTime = _lib.get("CP32Time2a_isSummerTime", "cdecl")
    CP32Time2a_isSummerTime.argtypes = [CP32Time2a]
    CP32Time2a_isSummerTime.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 728
for _lib in _libs.values():
    if not _lib.has("CP32Time2a_setSummerTime", "cdecl"):
        continue
    CP32Time2a_setSummerTime = _lib.get("CP32Time2a_setSummerTime", "cdecl")
    CP32Time2a_setSummerTime.argtypes = [CP32Time2a, c_bool]
    CP32Time2a_setSummerTime.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 734
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setFromMsTimestamp", "cdecl"):
        continue
    CP56Time2a_setFromMsTimestamp = _lib.get("CP56Time2a_setFromMsTimestamp", "cdecl")
    CP56Time2a_setFromMsTimestamp.argtypes = [CP56Time2a, uint64_t]
    CP56Time2a_setFromMsTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 740
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_toMsTimestamp", "cdecl"):
        continue
    CP56Time2a_toMsTimestamp = _lib.get("CP56Time2a_toMsTimestamp", "cdecl")
    CP56Time2a_toMsTimestamp.argtypes = [CP56Time2a]
    CP56Time2a_toMsTimestamp.restype = uint64_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 746
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getMillisecond", "cdecl"):
        continue
    CP56Time2a_getMillisecond = _lib.get("CP56Time2a_getMillisecond", "cdecl")
    CP56Time2a_getMillisecond.argtypes = [CP56Time2a]
    CP56Time2a_getMillisecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 752
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setMillisecond", "cdecl"):
        continue
    CP56Time2a_setMillisecond = _lib.get("CP56Time2a_setMillisecond", "cdecl")
    CP56Time2a_setMillisecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMillisecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 755
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getSecond", "cdecl"):
        continue
    CP56Time2a_getSecond = _lib.get("CP56Time2a_getSecond", "cdecl")
    CP56Time2a_getSecond.argtypes = [CP56Time2a]
    CP56Time2a_getSecond.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 758
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setSecond", "cdecl"):
        continue
    CP56Time2a_setSecond = _lib.get("CP56Time2a_setSecond", "cdecl")
    CP56Time2a_setSecond.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setSecond.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 761
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getMinute", "cdecl"):
        continue
    CP56Time2a_getMinute = _lib.get("CP56Time2a_getMinute", "cdecl")
    CP56Time2a_getMinute.argtypes = [CP56Time2a]
    CP56Time2a_getMinute.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 764
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setMinute", "cdecl"):
        continue
    CP56Time2a_setMinute = _lib.get("CP56Time2a_setMinute", "cdecl")
    CP56Time2a_setMinute.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMinute.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 767
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getHour", "cdecl"):
        continue
    CP56Time2a_getHour = _lib.get("CP56Time2a_getHour", "cdecl")
    CP56Time2a_getHour.argtypes = [CP56Time2a]
    CP56Time2a_getHour.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 770
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setHour", "cdecl"):
        continue
    CP56Time2a_setHour = _lib.get("CP56Time2a_setHour", "cdecl")
    CP56Time2a_setHour.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setHour.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 773
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getDayOfWeek", "cdecl"):
        continue
    CP56Time2a_getDayOfWeek = _lib.get("CP56Time2a_getDayOfWeek", "cdecl")
    CP56Time2a_getDayOfWeek.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfWeek.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 776
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setDayOfWeek", "cdecl"):
        continue
    CP56Time2a_setDayOfWeek = _lib.get("CP56Time2a_setDayOfWeek", "cdecl")
    CP56Time2a_setDayOfWeek.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfWeek.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 779
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getDayOfMonth", "cdecl"):
        continue
    CP56Time2a_getDayOfMonth = _lib.get("CP56Time2a_getDayOfMonth", "cdecl")
    CP56Time2a_getDayOfMonth.argtypes = [CP56Time2a]
    CP56Time2a_getDayOfMonth.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 782
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setDayOfMonth", "cdecl"):
        continue
    CP56Time2a_setDayOfMonth = _lib.get("CP56Time2a_setDayOfMonth", "cdecl")
    CP56Time2a_setDayOfMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setDayOfMonth.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 790
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getMonth", "cdecl"):
        continue
    CP56Time2a_getMonth = _lib.get("CP56Time2a_getMonth", "cdecl")
    CP56Time2a_getMonth.argtypes = [CP56Time2a]
    CP56Time2a_getMonth.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 798
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setMonth", "cdecl"):
        continue
    CP56Time2a_setMonth = _lib.get("CP56Time2a_setMonth", "cdecl")
    CP56Time2a_setMonth.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setMonth.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 806
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_getYear", "cdecl"):
        continue
    CP56Time2a_getYear = _lib.get("CP56Time2a_getYear", "cdecl")
    CP56Time2a_getYear.argtypes = [CP56Time2a]
    CP56Time2a_getYear.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 814
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setYear", "cdecl"):
        continue
    CP56Time2a_setYear = _lib.get("CP56Time2a_setYear", "cdecl")
    CP56Time2a_setYear.argtypes = [CP56Time2a, c_int]
    CP56Time2a_setYear.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 817
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_isSummerTime", "cdecl"):
        continue
    CP56Time2a_isSummerTime = _lib.get("CP56Time2a_isSummerTime", "cdecl")
    CP56Time2a_isSummerTime.argtypes = [CP56Time2a]
    CP56Time2a_isSummerTime.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 820
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setSummerTime", "cdecl"):
        continue
    CP56Time2a_setSummerTime = _lib.get("CP56Time2a_setSummerTime", "cdecl")
    CP56Time2a_setSummerTime.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSummerTime.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 823
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_isInvalid", "cdecl"):
        continue
    CP56Time2a_isInvalid = _lib.get("CP56Time2a_isInvalid", "cdecl")
    CP56Time2a_isInvalid.argtypes = [CP56Time2a]
    CP56Time2a_isInvalid.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 826
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setInvalid", "cdecl"):
        continue
    CP56Time2a_setInvalid = _lib.get("CP56Time2a_setInvalid", "cdecl")
    CP56Time2a_setInvalid.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setInvalid.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 829
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_isSubstituted", "cdecl"):
        continue
    CP56Time2a_isSubstituted = _lib.get("CP56Time2a_isSubstituted", "cdecl")
    CP56Time2a_isSubstituted.argtypes = [CP56Time2a]
    CP56Time2a_isSubstituted.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 832
for _lib in _libs.values():
    if not _lib.has("CP56Time2a_setSubstituted", "cdecl"):
        continue
    CP56Time2a_setSubstituted = _lib.get("CP56Time2a_setSubstituted", "cdecl")
    CP56Time2a_setSubstituted.argtypes = [CP56Time2a, c_bool]
    CP56Time2a_setSubstituted.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 835
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_create", "cdecl"):
        continue
    BinaryCounterReading_create = _lib.get("BinaryCounterReading_create", "cdecl")
    BinaryCounterReading_create.argtypes = [BinaryCounterReading, c_int32, c_int, c_bool, c_bool, c_bool]
    BinaryCounterReading_create.restype = BinaryCounterReading
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 839
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_destroy", "cdecl"):
        continue
    BinaryCounterReading_destroy = _lib.get("BinaryCounterReading_destroy", "cdecl")
    BinaryCounterReading_destroy.argtypes = [BinaryCounterReading]
    BinaryCounterReading_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 842
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_getValue", "cdecl"):
        continue
    BinaryCounterReading_getValue = _lib.get("BinaryCounterReading_getValue", "cdecl")
    BinaryCounterReading_getValue.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getValue.restype = c_int32
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 845
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_setValue", "cdecl"):
        continue
    BinaryCounterReading_setValue = _lib.get("BinaryCounterReading_setValue", "cdecl")
    BinaryCounterReading_setValue.argtypes = [BinaryCounterReading, c_int32]
    BinaryCounterReading_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 848
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_getSequenceNumber", "cdecl"):
        continue
    BinaryCounterReading_getSequenceNumber = _lib.get("BinaryCounterReading_getSequenceNumber", "cdecl")
    BinaryCounterReading_getSequenceNumber.argtypes = [BinaryCounterReading]
    BinaryCounterReading_getSequenceNumber.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 851
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_hasCarry", "cdecl"):
        continue
    BinaryCounterReading_hasCarry = _lib.get("BinaryCounterReading_hasCarry", "cdecl")
    BinaryCounterReading_hasCarry.argtypes = [BinaryCounterReading]
    BinaryCounterReading_hasCarry.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 854
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_isAdjusted", "cdecl"):
        continue
    BinaryCounterReading_isAdjusted = _lib.get("BinaryCounterReading_isAdjusted", "cdecl")
    BinaryCounterReading_isAdjusted.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isAdjusted.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 857
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_isInvalid", "cdecl"):
        continue
    BinaryCounterReading_isInvalid = _lib.get("BinaryCounterReading_isInvalid", "cdecl")
    BinaryCounterReading_isInvalid.argtypes = [BinaryCounterReading]
    BinaryCounterReading_isInvalid.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 860
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_setSequenceNumber", "cdecl"):
        continue
    BinaryCounterReading_setSequenceNumber = _lib.get("BinaryCounterReading_setSequenceNumber", "cdecl")
    BinaryCounterReading_setSequenceNumber.argtypes = [BinaryCounterReading, c_int]
    BinaryCounterReading_setSequenceNumber.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 863
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_setCarry", "cdecl"):
        continue
    BinaryCounterReading_setCarry = _lib.get("BinaryCounterReading_setCarry", "cdecl")
    BinaryCounterReading_setCarry.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setCarry.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 866
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_setAdjusted", "cdecl"):
        continue
    BinaryCounterReading_setAdjusted = _lib.get("BinaryCounterReading_setAdjusted", "cdecl")
    BinaryCounterReading_setAdjusted.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setAdjusted.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 869
for _lib in _libs.values():
    if not _lib.has("BinaryCounterReading_setInvalid", "cdecl"):
        continue
    BinaryCounterReading_setInvalid = _lib.get("BinaryCounterReading_setInvalid", "cdecl")
    BinaryCounterReading_setInvalid.argtypes = [BinaryCounterReading, c_bool]
    BinaryCounterReading_setInvalid.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 875
class struct_sFrame(Structure):
    pass

Frame = POINTER(struct_sFrame)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 875

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 878
for _lib in _libs.values():
    if not _lib.has("Frame_destroy", "cdecl"):
        continue
    Frame_destroy = _lib.get("Frame_destroy", "cdecl")
    Frame_destroy.argtypes = [Frame]
    Frame_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 881
for _lib in _libs.values():
    if not _lib.has("Frame_resetFrame", "cdecl"):
        continue
    Frame_resetFrame = _lib.get("Frame_resetFrame", "cdecl")
    Frame_resetFrame.argtypes = [Frame]
    Frame_resetFrame.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 884
for _lib in _libs.values():
    if not _lib.has("Frame_setNextByte", "cdecl"):
        continue
    Frame_setNextByte = _lib.get("Frame_setNextByte", "cdecl")
    Frame_setNextByte.argtypes = [Frame, uint8_t]
    Frame_setNextByte.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 887
for _lib in _libs.values():
    if not _lib.has("Frame_appendBytes", "cdecl"):
        continue
    Frame_appendBytes = _lib.get("Frame_appendBytes", "cdecl")
    Frame_appendBytes.argtypes = [Frame, POINTER(uint8_t), c_int]
    Frame_appendBytes.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 890
for _lib in _libs.values():
    if not _lib.has("Frame_getMsgSize", "cdecl"):
        continue
    Frame_getMsgSize = _lib.get("Frame_getMsgSize", "cdecl")
    Frame_getMsgSize.argtypes = [Frame]
    Frame_getMsgSize.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 892
for _lib in _libs.values():
    if not _lib.has("Frame_getBuffer", "cdecl"):
        continue
    Frame_getBuffer = _lib.get("Frame_getBuffer", "cdecl")
    Frame_getBuffer.argtypes = [Frame]
    Frame_getBuffer.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 896
for _lib in _libs.values():
    if not _lib.has("Frame_getSpaceLeft", "cdecl"):
        continue
    Frame_getSpaceLeft = _lib.get("Frame_getSpaceLeft", "cdecl")
    Frame_getSpaceLeft.argtypes = [Frame]
    Frame_getSpaceLeft.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 43
for _lib in _libs.values():
    if not _lib.has("TypeID_toString", "cdecl"):
        continue
    TypeID_toString = _lib.get("TypeID_toString", "cdecl")
    TypeID_toString.argtypes = [TypeID]
    TypeID_toString.restype = c_char_p
    break

QualityDescriptor = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 46

QualityDescriptorP = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 51

StartEvent = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 65

OutputCircuitInfo = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 80

QualifierOfParameterMV = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 99

CauseOfInitialization = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 111

QualifierOfCommand = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 120

SelectAndCallQualifier = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 131

QualifierOfInterrogation = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 146

QualifierOfCIC = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 185

QualifierOfRPC = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 201

QualifierOfParameterActivation = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 211

SetpointCommandQualifier = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 219

enum_anon_28 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_INTERMEDIATE = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_OFF = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_ON = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

IEC60870_DOUBLE_POINT_INDETERMINATE = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

DoublePointValue = enum_anon_28# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 226

enum_anon_29 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_INDETERMINATE_0 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_OFF = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_ON = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

IEC60870_EVENTSTATE_INDETERMINATE_3 = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

EventState = enum_anon_29# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 233

enum_anon_30 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_INVALID_0 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_LOWER = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_HIGHER = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

IEC60870_STEP_INVALID_3 = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

StepCommandValue = enum_anon_30# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 243

tSingleEvent = uint8_t# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 245

SingleEvent = POINTER(tSingleEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 247

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 250
for _lib in _libs.values():
    if not _lib.has("SingleEvent_setEventState", "cdecl"):
        continue
    SingleEvent_setEventState = _lib.get("SingleEvent_setEventState", "cdecl")
    SingleEvent_setEventState.argtypes = [SingleEvent, EventState]
    SingleEvent_setEventState.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 253
for _lib in _libs.values():
    if not _lib.has("SingleEvent_getEventState", "cdecl"):
        continue
    SingleEvent_getEventState = _lib.get("SingleEvent_getEventState", "cdecl")
    SingleEvent_getEventState.argtypes = [SingleEvent]
    SingleEvent_getEventState.restype = EventState
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 256
for _lib in _libs.values():
    if not _lib.has("SingleEvent_setQDP", "cdecl"):
        continue
    SingleEvent_setQDP = _lib.get("SingleEvent_setQDP", "cdecl")
    SingleEvent_setQDP.argtypes = [SingleEvent, QualityDescriptorP]
    SingleEvent_setQDP.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 259
for _lib in _libs.values():
    if not _lib.has("SingleEvent_getQDP", "cdecl"):
        continue
    SingleEvent_getQDP = _lib.get("SingleEvent_getQDP", "cdecl")
    SingleEvent_getQDP.argtypes = [SingleEvent]
    SingleEvent_getQDP.restype = QualityDescriptorP
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 266
class struct_sStatusAndStatusChangeDetection(Structure):
    pass

tStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 262

StatusAndStatusChangeDetection = POINTER(tStatusAndStatusChangeDetection)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 264

struct_sStatusAndStatusChangeDetection.__slots__ = [
    'encodedValue',
]
struct_sStatusAndStatusChangeDetection._fields_ = [
    ('encodedValue', uint8_t * int(4)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 271
for _lib in _libs.values():
    if not _lib.has("StatusAndStatusChangeDetection_getSTn", "cdecl"):
        continue
    StatusAndStatusChangeDetection_getSTn = _lib.get("StatusAndStatusChangeDetection_getSTn", "cdecl")
    StatusAndStatusChangeDetection_getSTn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getSTn.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 274
for _lib in _libs.values():
    if not _lib.has("StatusAndStatusChangeDetection_getCDn", "cdecl"):
        continue
    StatusAndStatusChangeDetection_getCDn = _lib.get("StatusAndStatusChangeDetection_getCDn", "cdecl")
    StatusAndStatusChangeDetection_getCDn.argtypes = [StatusAndStatusChangeDetection]
    StatusAndStatusChangeDetection_getCDn.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 277
for _lib in _libs.values():
    if not _lib.has("StatusAndStatusChangeDetection_setSTn", "cdecl"):
        continue
    StatusAndStatusChangeDetection_setSTn = _lib.get("StatusAndStatusChangeDetection_setSTn", "cdecl")
    StatusAndStatusChangeDetection_setSTn.argtypes = [StatusAndStatusChangeDetection, uint16_t]
    StatusAndStatusChangeDetection_setSTn.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 280
for _lib in _libs.values():
    if not _lib.has("StatusAndStatusChangeDetection_getST", "cdecl"):
        continue
    StatusAndStatusChangeDetection_getST = _lib.get("StatusAndStatusChangeDetection_getST", "cdecl")
    StatusAndStatusChangeDetection_getST.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getST.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 283
for _lib in _libs.values():
    if not _lib.has("StatusAndStatusChangeDetection_getCD", "cdecl"):
        continue
    StatusAndStatusChangeDetection_getCD = _lib.get("StatusAndStatusChangeDetection_getCD", "cdecl")
    StatusAndStatusChangeDetection_getCD.argtypes = [StatusAndStatusChangeDetection, c_int]
    StatusAndStatusChangeDetection_getCD.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 286
for _lib in _libs.values():
    if not _lib.has("NormalizedValue_fromScaled", "cdecl"):
        continue
    NormalizedValue_fromScaled = _lib.get("NormalizedValue_fromScaled", "cdecl")
    NormalizedValue_fromScaled.argtypes = [c_int]
    NormalizedValue_fromScaled.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 289
for _lib in _libs.values():
    if not _lib.has("NormalizedValue_toScaled", "cdecl"):
        continue
    NormalizedValue_toScaled = _lib.get("NormalizedValue_toScaled", "cdecl")
    NormalizedValue_toScaled.argtypes = [c_float]
    NormalizedValue_toScaled.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 301
for _lib in _libs.values():
    if not _lib.has("InformationObject_getMaxSizeInMemory", "cdecl"):
        continue
    InformationObject_getMaxSizeInMemory = _lib.get("InformationObject_getMaxSizeInMemory", "cdecl")
    InformationObject_getMaxSizeInMemory.argtypes = []
    InformationObject_getMaxSizeInMemory.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 304
for _lib in _libs.values():
    if not _lib.has("InformationObject_getObjectAddress", "cdecl"):
        continue
    InformationObject_getObjectAddress = _lib.get("InformationObject_getObjectAddress", "cdecl")
    InformationObject_getObjectAddress.argtypes = [InformationObject]
    InformationObject_getObjectAddress.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 307
for _lib in _libs.values():
    if not _lib.has("InformationObject_getType", "cdecl"):
        continue
    InformationObject_getType = _lib.get("InformationObject_getType", "cdecl")
    InformationObject_getType.argtypes = [InformationObject]
    InformationObject_getType.restype = TypeID
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 317
for _lib in _libs.values():
    if not _lib.has("InformationObject_destroy", "cdecl"):
        continue
    InformationObject_destroy = _lib.get("InformationObject_destroy", "cdecl")
    InformationObject_destroy.argtypes = [InformationObject]
    InformationObject_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323
class struct_sSinglePointInformation(Structure):
    pass

SinglePointInformation = POINTER(struct_sSinglePointInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 326
for _lib in _libs.values():
    if not _lib.has("SinglePointInformation_create", "cdecl"):
        continue
    SinglePointInformation_create = _lib.get("SinglePointInformation_create", "cdecl")
    SinglePointInformation_create.argtypes = [SinglePointInformation, c_int, c_bool, QualityDescriptor]
    SinglePointInformation_create.restype = SinglePointInformation
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 330
for _lib in _libs.values():
    if not _lib.has("SinglePointInformation_getValue", "cdecl"):
        continue
    SinglePointInformation_getValue = _lib.get("SinglePointInformation_getValue", "cdecl")
    SinglePointInformation_getValue.argtypes = [SinglePointInformation]
    SinglePointInformation_getValue.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 333
for _lib in _libs.values():
    if not _lib.has("SinglePointInformation_getQuality", "cdecl"):
        continue
    SinglePointInformation_getQuality = _lib.get("SinglePointInformation_getQuality", "cdecl")
    SinglePointInformation_getQuality.argtypes = [SinglePointInformation]
    SinglePointInformation_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 336
for _lib in _libs.values():
    if not _lib.has("SinglePointInformation_destroy", "cdecl"):
        continue
    SinglePointInformation_destroy = _lib.get("SinglePointInformation_destroy", "cdecl")
    SinglePointInformation_destroy.argtypes = [SinglePointInformation]
    SinglePointInformation_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342
class struct_sSinglePointWithCP24Time2a(Structure):
    pass

SinglePointWithCP24Time2a = POINTER(struct_sSinglePointWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 345
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP24Time2a_create", "cdecl"):
        continue
    SinglePointWithCP24Time2a_create = _lib.get("SinglePointWithCP24Time2a_create", "cdecl")
    SinglePointWithCP24Time2a_create.argtypes = [SinglePointWithCP24Time2a, c_int, c_bool, QualityDescriptor, CP24Time2a]
    SinglePointWithCP24Time2a_create.restype = SinglePointWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 349
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP24Time2a_destroy", "cdecl"):
        continue
    SinglePointWithCP24Time2a_destroy = _lib.get("SinglePointWithCP24Time2a_destroy", "cdecl")
    SinglePointWithCP24Time2a_destroy.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 352
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    SinglePointWithCP24Time2a_getTimestamp = _lib.get("SinglePointWithCP24Time2a_getTimestamp", "cdecl")
    SinglePointWithCP24Time2a_getTimestamp.argtypes = [SinglePointWithCP24Time2a]
    SinglePointWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358
class struct_sSinglePointWithCP56Time2a(Structure):
    pass

SinglePointWithCP56Time2a = POINTER(struct_sSinglePointWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 361
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP56Time2a_create", "cdecl"):
        continue
    SinglePointWithCP56Time2a_create = _lib.get("SinglePointWithCP56Time2a_create", "cdecl")
    SinglePointWithCP56Time2a_create.argtypes = [SinglePointWithCP56Time2a, c_int, c_bool, QualityDescriptor, CP56Time2a]
    SinglePointWithCP56Time2a_create.restype = SinglePointWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 365
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP56Time2a_destroy", "cdecl"):
        continue
    SinglePointWithCP56Time2a_destroy = _lib.get("SinglePointWithCP56Time2a_destroy", "cdecl")
    SinglePointWithCP56Time2a_destroy.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 368
for _lib in _libs.values():
    if not _lib.has("SinglePointWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    SinglePointWithCP56Time2a_getTimestamp = _lib.get("SinglePointWithCP56Time2a_getTimestamp", "cdecl")
    SinglePointWithCP56Time2a_getTimestamp.argtypes = [SinglePointWithCP56Time2a]
    SinglePointWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375
class struct_sDoublePointInformation(Structure):
    pass

DoublePointInformation = POINTER(struct_sDoublePointInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 378
for _lib in _libs.values():
    if not _lib.has("DoublePointInformation_destroy", "cdecl"):
        continue
    DoublePointInformation_destroy = _lib.get("DoublePointInformation_destroy", "cdecl")
    DoublePointInformation_destroy.argtypes = [DoublePointInformation]
    DoublePointInformation_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 381
for _lib in _libs.values():
    if not _lib.has("DoublePointInformation_create", "cdecl"):
        continue
    DoublePointInformation_create = _lib.get("DoublePointInformation_create", "cdecl")
    DoublePointInformation_create.argtypes = [DoublePointInformation, c_int, DoublePointValue, QualityDescriptor]
    DoublePointInformation_create.restype = DoublePointInformation
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 385
for _lib in _libs.values():
    if not _lib.has("DoublePointInformation_getValue", "cdecl"):
        continue
    DoublePointInformation_getValue = _lib.get("DoublePointInformation_getValue", "cdecl")
    DoublePointInformation_getValue.argtypes = [DoublePointInformation]
    DoublePointInformation_getValue.restype = DoublePointValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 388
for _lib in _libs.values():
    if not _lib.has("DoublePointInformation_getQuality", "cdecl"):
        continue
    DoublePointInformation_getQuality = _lib.get("DoublePointInformation_getQuality", "cdecl")
    DoublePointInformation_getQuality.argtypes = [DoublePointInformation]
    DoublePointInformation_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394
class struct_sDoublePointWithCP24Time2a(Structure):
    pass

DoublePointWithCP24Time2a = POINTER(struct_sDoublePointWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 397
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP24Time2a_destroy", "cdecl"):
        continue
    DoublePointWithCP24Time2a_destroy = _lib.get("DoublePointWithCP24Time2a_destroy", "cdecl")
    DoublePointWithCP24Time2a_destroy.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 400
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP24Time2a_create", "cdecl"):
        continue
    DoublePointWithCP24Time2a_create = _lib.get("DoublePointWithCP24Time2a_create", "cdecl")
    DoublePointWithCP24Time2a_create.argtypes = [DoublePointWithCP24Time2a, c_int, DoublePointValue, QualityDescriptor, CP24Time2a]
    DoublePointWithCP24Time2a_create.restype = DoublePointWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 404
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    DoublePointWithCP24Time2a_getTimestamp = _lib.get("DoublePointWithCP24Time2a_getTimestamp", "cdecl")
    DoublePointWithCP24Time2a_getTimestamp.argtypes = [DoublePointWithCP24Time2a]
    DoublePointWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410
class struct_sDoublePointWithCP56Time2a(Structure):
    pass

DoublePointWithCP56Time2a = POINTER(struct_sDoublePointWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 413
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP56Time2a_create", "cdecl"):
        continue
    DoublePointWithCP56Time2a_create = _lib.get("DoublePointWithCP56Time2a_create", "cdecl")
    DoublePointWithCP56Time2a_create.argtypes = [DoublePointWithCP56Time2a, c_int, DoublePointValue, QualityDescriptor, CP56Time2a]
    DoublePointWithCP56Time2a_create.restype = DoublePointWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 417
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP56Time2a_destroy", "cdecl"):
        continue
    DoublePointWithCP56Time2a_destroy = _lib.get("DoublePointWithCP56Time2a_destroy", "cdecl")
    DoublePointWithCP56Time2a_destroy.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 420
for _lib in _libs.values():
    if not _lib.has("DoublePointWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    DoublePointWithCP56Time2a_getTimestamp = _lib.get("DoublePointWithCP56Time2a_getTimestamp", "cdecl")
    DoublePointWithCP56Time2a_getTimestamp.argtypes = [DoublePointWithCP56Time2a]
    DoublePointWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426
class struct_sStepPositionInformation(Structure):
    pass

StepPositionInformation = POINTER(struct_sStepPositionInformation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 440
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_create", "cdecl"):
        continue
    StepPositionInformation_create = _lib.get("StepPositionInformation_create", "cdecl")
    StepPositionInformation_create.argtypes = [StepPositionInformation, c_int, c_int, c_bool, QualityDescriptor]
    StepPositionInformation_create.restype = StepPositionInformation
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 444
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_destroy", "cdecl"):
        continue
    StepPositionInformation_destroy = _lib.get("StepPositionInformation_destroy", "cdecl")
    StepPositionInformation_destroy.argtypes = [StepPositionInformation]
    StepPositionInformation_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 447
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_getObjectAddress", "cdecl"):
        continue
    StepPositionInformation_getObjectAddress = _lib.get("StepPositionInformation_getObjectAddress", "cdecl")
    StepPositionInformation_getObjectAddress.argtypes = [StepPositionInformation]
    StepPositionInformation_getObjectAddress.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 453
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_getValue", "cdecl"):
        continue
    StepPositionInformation_getValue = _lib.get("StepPositionInformation_getValue", "cdecl")
    StepPositionInformation_getValue.argtypes = [StepPositionInformation]
    StepPositionInformation_getValue.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 456
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_isTransient", "cdecl"):
        continue
    StepPositionInformation_isTransient = _lib.get("StepPositionInformation_isTransient", "cdecl")
    StepPositionInformation_isTransient.argtypes = [StepPositionInformation]
    StepPositionInformation_isTransient.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 459
for _lib in _libs.values():
    if not _lib.has("StepPositionInformation_getQuality", "cdecl"):
        continue
    StepPositionInformation_getQuality = _lib.get("StepPositionInformation_getQuality", "cdecl")
    StepPositionInformation_getQuality.argtypes = [StepPositionInformation]
    StepPositionInformation_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465
class struct_sStepPositionWithCP24Time2a(Structure):
    pass

StepPositionWithCP24Time2a = POINTER(struct_sStepPositionWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 468
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP24Time2a_destroy", "cdecl"):
        continue
    StepPositionWithCP24Time2a_destroy = _lib.get("StepPositionWithCP24Time2a_destroy", "cdecl")
    StepPositionWithCP24Time2a_destroy.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 471
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP24Time2a_create", "cdecl"):
        continue
    StepPositionWithCP24Time2a_create = _lib.get("StepPositionWithCP24Time2a_create", "cdecl")
    StepPositionWithCP24Time2a_create.argtypes = [StepPositionWithCP24Time2a, c_int, c_int, c_bool, QualityDescriptor, CP24Time2a]
    StepPositionWithCP24Time2a_create.restype = StepPositionWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 475
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    StepPositionWithCP24Time2a_getTimestamp = _lib.get("StepPositionWithCP24Time2a_getTimestamp", "cdecl")
    StepPositionWithCP24Time2a_getTimestamp.argtypes = [StepPositionWithCP24Time2a]
    StepPositionWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482
class struct_sStepPositionWithCP56Time2a(Structure):
    pass

StepPositionWithCP56Time2a = POINTER(struct_sStepPositionWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 485
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP56Time2a_destroy", "cdecl"):
        continue
    StepPositionWithCP56Time2a_destroy = _lib.get("StepPositionWithCP56Time2a_destroy", "cdecl")
    StepPositionWithCP56Time2a_destroy.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 488
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP56Time2a_create", "cdecl"):
        continue
    StepPositionWithCP56Time2a_create = _lib.get("StepPositionWithCP56Time2a_create", "cdecl")
    StepPositionWithCP56Time2a_create.argtypes = [StepPositionWithCP56Time2a, c_int, c_int, c_bool, QualityDescriptor, CP56Time2a]
    StepPositionWithCP56Time2a_create.restype = StepPositionWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 492
for _lib in _libs.values():
    if not _lib.has("StepPositionWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    StepPositionWithCP56Time2a_getTimestamp = _lib.get("StepPositionWithCP56Time2a_getTimestamp", "cdecl")
    StepPositionWithCP56Time2a_getTimestamp.argtypes = [StepPositionWithCP56Time2a]
    StepPositionWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498
class struct_sBitString32(Structure):
    pass

BitString32 = POINTER(struct_sBitString32)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 501
for _lib in _libs.values():
    if not _lib.has("BitString32_destroy", "cdecl"):
        continue
    BitString32_destroy = _lib.get("BitString32_destroy", "cdecl")
    BitString32_destroy.argtypes = [BitString32]
    BitString32_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 504
for _lib in _libs.values():
    if not _lib.has("BitString32_create", "cdecl"):
        continue
    BitString32_create = _lib.get("BitString32_create", "cdecl")
    BitString32_create.argtypes = [BitString32, c_int, uint32_t]
    BitString32_create.restype = BitString32
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 507
for _lib in _libs.values():
    if not _lib.has("BitString32_createEx", "cdecl"):
        continue
    BitString32_createEx = _lib.get("BitString32_createEx", "cdecl")
    BitString32_createEx.argtypes = [BitString32, c_int, uint32_t, QualityDescriptor]
    BitString32_createEx.restype = BitString32
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 510
for _lib in _libs.values():
    if not _lib.has("BitString32_getValue", "cdecl"):
        continue
    BitString32_getValue = _lib.get("BitString32_getValue", "cdecl")
    BitString32_getValue.argtypes = [BitString32]
    BitString32_getValue.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 513
for _lib in _libs.values():
    if not _lib.has("BitString32_getQuality", "cdecl"):
        continue
    BitString32_getQuality = _lib.get("BitString32_getQuality", "cdecl")
    BitString32_getQuality.argtypes = [BitString32]
    BitString32_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519
class struct_sBitstring32WithCP24Time2a(Structure):
    pass

Bitstring32WithCP24Time2a = POINTER(struct_sBitstring32WithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 522
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP24Time2a_destroy", "cdecl"):
        continue
    Bitstring32WithCP24Time2a_destroy = _lib.get("Bitstring32WithCP24Time2a_destroy", "cdecl")
    Bitstring32WithCP24Time2a_destroy.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 525
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP24Time2a_create", "cdecl"):
        continue
    Bitstring32WithCP24Time2a_create = _lib.get("Bitstring32WithCP24Time2a_create", "cdecl")
    Bitstring32WithCP24Time2a_create.argtypes = [Bitstring32WithCP24Time2a, c_int, uint32_t, CP24Time2a]
    Bitstring32WithCP24Time2a_create.restype = Bitstring32WithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 528
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP24Time2a_createEx", "cdecl"):
        continue
    Bitstring32WithCP24Time2a_createEx = _lib.get("Bitstring32WithCP24Time2a_createEx", "cdecl")
    Bitstring32WithCP24Time2a_createEx.argtypes = [Bitstring32WithCP24Time2a, c_int, uint32_t, QualityDescriptor, CP24Time2a]
    Bitstring32WithCP24Time2a_createEx.restype = Bitstring32WithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 531
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP24Time2a_getTimestamp", "cdecl"):
        continue
    Bitstring32WithCP24Time2a_getTimestamp = _lib.get("Bitstring32WithCP24Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP24Time2a_getTimestamp.argtypes = [Bitstring32WithCP24Time2a]
    Bitstring32WithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537
class struct_sBitstring32WithCP56Time2a(Structure):
    pass

Bitstring32WithCP56Time2a = POINTER(struct_sBitstring32WithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 540
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP56Time2a_destroy", "cdecl"):
        continue
    Bitstring32WithCP56Time2a_destroy = _lib.get("Bitstring32WithCP56Time2a_destroy", "cdecl")
    Bitstring32WithCP56Time2a_destroy.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 543
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP56Time2a_create", "cdecl"):
        continue
    Bitstring32WithCP56Time2a_create = _lib.get("Bitstring32WithCP56Time2a_create", "cdecl")
    Bitstring32WithCP56Time2a_create.argtypes = [Bitstring32WithCP56Time2a, c_int, uint32_t, CP56Time2a]
    Bitstring32WithCP56Time2a_create.restype = Bitstring32WithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 546
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP56Time2a_createEx", "cdecl"):
        continue
    Bitstring32WithCP56Time2a_createEx = _lib.get("Bitstring32WithCP56Time2a_createEx", "cdecl")
    Bitstring32WithCP56Time2a_createEx.argtypes = [Bitstring32WithCP56Time2a, c_int, uint32_t, QualityDescriptor, CP56Time2a]
    Bitstring32WithCP56Time2a_createEx.restype = Bitstring32WithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 549
for _lib in _libs.values():
    if not _lib.has("Bitstring32WithCP56Time2a_getTimestamp", "cdecl"):
        continue
    Bitstring32WithCP56Time2a_getTimestamp = _lib.get("Bitstring32WithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32WithCP56Time2a_getTimestamp.argtypes = [Bitstring32WithCP56Time2a]
    Bitstring32WithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555
class struct_sMeasuredValueNormalizedWithoutQuality(Structure):
    pass

MeasuredValueNormalizedWithoutQuality = POINTER(struct_sMeasuredValueNormalizedWithoutQuality)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 558
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl"):
        continue
    MeasuredValueNormalizedWithoutQuality_destroy = _lib.get("MeasuredValueNormalizedWithoutQuality_destroy", "cdecl")
    MeasuredValueNormalizedWithoutQuality_destroy.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 561
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithoutQuality_create", "cdecl"):
        continue
    MeasuredValueNormalizedWithoutQuality_create = _lib.get("MeasuredValueNormalizedWithoutQuality_create", "cdecl")
    MeasuredValueNormalizedWithoutQuality_create.argtypes = [MeasuredValueNormalizedWithoutQuality, c_int, c_float]
    MeasuredValueNormalizedWithoutQuality_create.restype = MeasuredValueNormalizedWithoutQuality
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 564
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl"):
        continue
    MeasuredValueNormalizedWithoutQuality_getValue = _lib.get("MeasuredValueNormalizedWithoutQuality_getValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_getValue.argtypes = [MeasuredValueNormalizedWithoutQuality]
    MeasuredValueNormalizedWithoutQuality_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 567
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl"):
        continue
    MeasuredValueNormalizedWithoutQuality_setValue = _lib.get("MeasuredValueNormalizedWithoutQuality_setValue", "cdecl")
    MeasuredValueNormalizedWithoutQuality_setValue.argtypes = [MeasuredValueNormalizedWithoutQuality, c_float]
    MeasuredValueNormalizedWithoutQuality_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573
class struct_sMeasuredValueNormalized(Structure):
    pass

MeasuredValueNormalized = POINTER(struct_sMeasuredValueNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 576
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalized_destroy", "cdecl"):
        continue
    MeasuredValueNormalized_destroy = _lib.get("MeasuredValueNormalized_destroy", "cdecl")
    MeasuredValueNormalized_destroy.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 579
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalized_create", "cdecl"):
        continue
    MeasuredValueNormalized_create = _lib.get("MeasuredValueNormalized_create", "cdecl")
    MeasuredValueNormalized_create.argtypes = [MeasuredValueNormalized, c_int, c_float, QualityDescriptor]
    MeasuredValueNormalized_create.restype = MeasuredValueNormalized
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 582
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalized_getValue", "cdecl"):
        continue
    MeasuredValueNormalized_getValue = _lib.get("MeasuredValueNormalized_getValue", "cdecl")
    MeasuredValueNormalized_getValue.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 585
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalized_setValue", "cdecl"):
        continue
    MeasuredValueNormalized_setValue = _lib.get("MeasuredValueNormalized_setValue", "cdecl")
    MeasuredValueNormalized_setValue.argtypes = [MeasuredValueNormalized, c_float]
    MeasuredValueNormalized_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 588
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalized_getQuality", "cdecl"):
        continue
    MeasuredValueNormalized_getQuality = _lib.get("MeasuredValueNormalized_getQuality", "cdecl")
    MeasuredValueNormalized_getQuality.argtypes = [MeasuredValueNormalized]
    MeasuredValueNormalized_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594
class struct_sMeasuredValueNormalizedWithCP24Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP24Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 597
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP24Time2a_destroy = _lib.get("MeasuredValueNormalizedWithCP24Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 600
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP24Time2a_create = _lib.get("MeasuredValueNormalizedWithCP24Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_create.argtypes = [MeasuredValueNormalizedWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_create.restype = MeasuredValueNormalizedWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 604
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp = _lib.get("MeasuredValueNormalizedWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 607
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp = _lib.get("MeasuredValueNormalizedWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP24Time2a, CP24Time2a]
    MeasuredValueNormalizedWithCP24Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613
class struct_sMeasuredValueNormalizedWithCP56Time2a(Structure):
    pass

MeasuredValueNormalizedWithCP56Time2a = POINTER(struct_sMeasuredValueNormalizedWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 616
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP56Time2a_destroy = _lib.get("MeasuredValueNormalizedWithCP56Time2a_destroy", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_destroy.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 619
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP56Time2a_create = _lib.get("MeasuredValueNormalizedWithCP56Time2a_create", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_create.argtypes = [MeasuredValueNormalizedWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_create.restype = MeasuredValueNormalizedWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 623
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp = _lib.get("MeasuredValueNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 626
for _lib in _libs.values():
    if not _lib.has("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp = _lib.get("MeasuredValueNormalizedWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueNormalizedWithCP56Time2a, CP56Time2a]
    MeasuredValueNormalizedWithCP56Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633
class struct_sMeasuredValueScaled(Structure):
    pass

MeasuredValueScaled = POINTER(struct_sMeasuredValueScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 646
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_create", "cdecl"):
        continue
    MeasuredValueScaled_create = _lib.get("MeasuredValueScaled_create", "cdecl")
    MeasuredValueScaled_create.argtypes = [MeasuredValueScaled, c_int, c_int, QualityDescriptor]
    MeasuredValueScaled_create.restype = MeasuredValueScaled
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 649
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_destroy", "cdecl"):
        continue
    MeasuredValueScaled_destroy = _lib.get("MeasuredValueScaled_destroy", "cdecl")
    MeasuredValueScaled_destroy.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 652
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_getValue", "cdecl"):
        continue
    MeasuredValueScaled_getValue = _lib.get("MeasuredValueScaled_getValue", "cdecl")
    MeasuredValueScaled_getValue.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getValue.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 655
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_setValue", "cdecl"):
        continue
    MeasuredValueScaled_setValue = _lib.get("MeasuredValueScaled_setValue", "cdecl")
    MeasuredValueScaled_setValue.argtypes = [MeasuredValueScaled, c_int]
    MeasuredValueScaled_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 658
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_getQuality", "cdecl"):
        continue
    MeasuredValueScaled_getQuality = _lib.get("MeasuredValueScaled_getQuality", "cdecl")
    MeasuredValueScaled_getQuality.argtypes = [MeasuredValueScaled]
    MeasuredValueScaled_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 661
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaled_setQuality", "cdecl"):
        continue
    MeasuredValueScaled_setQuality = _lib.get("MeasuredValueScaled_setQuality", "cdecl")
    MeasuredValueScaled_setQuality.argtypes = [MeasuredValueScaled, QualityDescriptor]
    MeasuredValueScaled_setQuality.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667
class struct_sMeasuredValueScaledWithCP24Time2a(Structure):
    pass

MeasuredValueScaledWithCP24Time2a = POINTER(struct_sMeasuredValueScaledWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 670
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl"):
        continue
    MeasuredValueScaledWithCP24Time2a_destroy = _lib.get("MeasuredValueScaledWithCP24Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP24Time2a_destroy.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 673
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP24Time2a_create", "cdecl"):
        continue
    MeasuredValueScaledWithCP24Time2a_create = _lib.get("MeasuredValueScaledWithCP24Time2a_create", "cdecl")
    MeasuredValueScaledWithCP24Time2a_create.argtypes = [MeasuredValueScaledWithCP24Time2a, c_int, c_int, QualityDescriptor, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_create.restype = MeasuredValueScaledWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 677
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueScaledWithCP24Time2a_getTimestamp = _lib.get("MeasuredValueScaledWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a]
    MeasuredValueScaledWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 680
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueScaledWithCP24Time2a_setTimestamp = _lib.get("MeasuredValueScaledWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP24Time2a, CP24Time2a]
    MeasuredValueScaledWithCP24Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686
class struct_sMeasuredValueScaledWithCP56Time2a(Structure):
    pass

MeasuredValueScaledWithCP56Time2a = POINTER(struct_sMeasuredValueScaledWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 689
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl"):
        continue
    MeasuredValueScaledWithCP56Time2a_destroy = _lib.get("MeasuredValueScaledWithCP56Time2a_destroy", "cdecl")
    MeasuredValueScaledWithCP56Time2a_destroy.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 692
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP56Time2a_create", "cdecl"):
        continue
    MeasuredValueScaledWithCP56Time2a_create = _lib.get("MeasuredValueScaledWithCP56Time2a_create", "cdecl")
    MeasuredValueScaledWithCP56Time2a_create.argtypes = [MeasuredValueScaledWithCP56Time2a, c_int, c_int, QualityDescriptor, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_create.restype = MeasuredValueScaledWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 696
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueScaledWithCP56Time2a_getTimestamp = _lib.get("MeasuredValueScaledWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a]
    MeasuredValueScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 699
for _lib in _libs.values():
    if not _lib.has("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueScaledWithCP56Time2a_setTimestamp = _lib.get("MeasuredValueScaledWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueScaledWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueScaledWithCP56Time2a, CP56Time2a]
    MeasuredValueScaledWithCP56Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705
class struct_sMeasuredValueShort(Structure):
    pass

MeasuredValueShort = POINTER(struct_sMeasuredValueShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 708
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShort_destroy", "cdecl"):
        continue
    MeasuredValueShort_destroy = _lib.get("MeasuredValueShort_destroy", "cdecl")
    MeasuredValueShort_destroy.argtypes = [MeasuredValueShort]
    MeasuredValueShort_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 711
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShort_create", "cdecl"):
        continue
    MeasuredValueShort_create = _lib.get("MeasuredValueShort_create", "cdecl")
    MeasuredValueShort_create.argtypes = [MeasuredValueShort, c_int, c_float, QualityDescriptor]
    MeasuredValueShort_create.restype = MeasuredValueShort
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 714
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShort_getValue", "cdecl"):
        continue
    MeasuredValueShort_getValue = _lib.get("MeasuredValueShort_getValue", "cdecl")
    MeasuredValueShort_getValue.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 717
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShort_setValue", "cdecl"):
        continue
    MeasuredValueShort_setValue = _lib.get("MeasuredValueShort_setValue", "cdecl")
    MeasuredValueShort_setValue.argtypes = [MeasuredValueShort, c_float]
    MeasuredValueShort_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 720
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShort_getQuality", "cdecl"):
        continue
    MeasuredValueShort_getQuality = _lib.get("MeasuredValueShort_getQuality", "cdecl")
    MeasuredValueShort_getQuality.argtypes = [MeasuredValueShort]
    MeasuredValueShort_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726
class struct_sMeasuredValueShortWithCP24Time2a(Structure):
    pass

MeasuredValueShortWithCP24Time2a = POINTER(struct_sMeasuredValueShortWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 729
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP24Time2a_destroy", "cdecl"):
        continue
    MeasuredValueShortWithCP24Time2a_destroy = _lib.get("MeasuredValueShortWithCP24Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP24Time2a_destroy.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 732
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP24Time2a_create", "cdecl"):
        continue
    MeasuredValueShortWithCP24Time2a_create = _lib.get("MeasuredValueShortWithCP24Time2a_create", "cdecl")
    MeasuredValueShortWithCP24Time2a_create.argtypes = [MeasuredValueShortWithCP24Time2a, c_int, c_float, QualityDescriptor, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_create.restype = MeasuredValueShortWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 736
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueShortWithCP24Time2a_getTimestamp = _lib.get("MeasuredValueShortWithCP24Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a]
    MeasuredValueShortWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 739
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueShortWithCP24Time2a_setTimestamp = _lib.get("MeasuredValueShortWithCP24Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP24Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP24Time2a, CP24Time2a]
    MeasuredValueShortWithCP24Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746
class struct_sMeasuredValueShortWithCP56Time2a(Structure):
    pass

MeasuredValueShortWithCP56Time2a = POINTER(struct_sMeasuredValueShortWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 749
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP56Time2a_destroy", "cdecl"):
        continue
    MeasuredValueShortWithCP56Time2a_destroy = _lib.get("MeasuredValueShortWithCP56Time2a_destroy", "cdecl")
    MeasuredValueShortWithCP56Time2a_destroy.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 752
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP56Time2a_create", "cdecl"):
        continue
    MeasuredValueShortWithCP56Time2a_create = _lib.get("MeasuredValueShortWithCP56Time2a_create", "cdecl")
    MeasuredValueShortWithCP56Time2a_create.argtypes = [MeasuredValueShortWithCP56Time2a, c_int, c_float, QualityDescriptor, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_create.restype = MeasuredValueShortWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 756
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    MeasuredValueShortWithCP56Time2a_getTimestamp = _lib.get("MeasuredValueShortWithCP56Time2a_getTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_getTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a]
    MeasuredValueShortWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 759
for _lib in _libs.values():
    if not _lib.has("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl"):
        continue
    MeasuredValueShortWithCP56Time2a_setTimestamp = _lib.get("MeasuredValueShortWithCP56Time2a_setTimestamp", "cdecl")
    MeasuredValueShortWithCP56Time2a_setTimestamp.argtypes = [MeasuredValueShortWithCP56Time2a, CP56Time2a]
    MeasuredValueShortWithCP56Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766
class struct_sIntegratedTotals(Structure):
    pass

IntegratedTotals = POINTER(struct_sIntegratedTotals)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 769
for _lib in _libs.values():
    if not _lib.has("IntegratedTotals_destroy", "cdecl"):
        continue
    IntegratedTotals_destroy = _lib.get("IntegratedTotals_destroy", "cdecl")
    IntegratedTotals_destroy.argtypes = [IntegratedTotals]
    IntegratedTotals_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 783
for _lib in _libs.values():
    if not _lib.has("IntegratedTotals_create", "cdecl"):
        continue
    IntegratedTotals_create = _lib.get("IntegratedTotals_create", "cdecl")
    IntegratedTotals_create.argtypes = [IntegratedTotals, c_int, BinaryCounterReading]
    IntegratedTotals_create.restype = IntegratedTotals
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 786
for _lib in _libs.values():
    if not _lib.has("IntegratedTotals_getBCR", "cdecl"):
        continue
    IntegratedTotals_getBCR = _lib.get("IntegratedTotals_getBCR", "cdecl")
    IntegratedTotals_getBCR.argtypes = [IntegratedTotals]
    IntegratedTotals_getBCR.restype = BinaryCounterReading
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 789
for _lib in _libs.values():
    if not _lib.has("IntegratedTotals_setBCR", "cdecl"):
        continue
    IntegratedTotals_setBCR = _lib.get("IntegratedTotals_setBCR", "cdecl")
    IntegratedTotals_setBCR.argtypes = [IntegratedTotals, BinaryCounterReading]
    IntegratedTotals_setBCR.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795
class struct_sIntegratedTotalsWithCP24Time2a(Structure):
    pass

IntegratedTotalsWithCP24Time2a = POINTER(struct_sIntegratedTotalsWithCP24Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 810
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP24Time2a_create", "cdecl"):
        continue
    IntegratedTotalsWithCP24Time2a_create = _lib.get("IntegratedTotalsWithCP24Time2a_create", "cdecl")
    IntegratedTotalsWithCP24Time2a_create.argtypes = [IntegratedTotalsWithCP24Time2a, c_int, BinaryCounterReading, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_create.restype = IntegratedTotalsWithCP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 814
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP24Time2a_destroy", "cdecl"):
        continue
    IntegratedTotalsWithCP24Time2a_destroy = _lib.get("IntegratedTotalsWithCP24Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP24Time2a_destroy.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 817
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl"):
        continue
    IntegratedTotalsWithCP24Time2a_getTimestamp = _lib.get("IntegratedTotalsWithCP24Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a]
    IntegratedTotalsWithCP24Time2a_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 820
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl"):
        continue
    IntegratedTotalsWithCP24Time2a_setTimestamp = _lib.get("IntegratedTotalsWithCP24Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP24Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP24Time2a, CP24Time2a]
    IntegratedTotalsWithCP24Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827
class struct_sIntegratedTotalsWithCP56Time2a(Structure):
    pass

IntegratedTotalsWithCP56Time2a = POINTER(struct_sIntegratedTotalsWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 842
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP56Time2a_create", "cdecl"):
        continue
    IntegratedTotalsWithCP56Time2a_create = _lib.get("IntegratedTotalsWithCP56Time2a_create", "cdecl")
    IntegratedTotalsWithCP56Time2a_create.argtypes = [IntegratedTotalsWithCP56Time2a, c_int, BinaryCounterReading, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_create.restype = IntegratedTotalsWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 846
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP56Time2a_destroy", "cdecl"):
        continue
    IntegratedTotalsWithCP56Time2a_destroy = _lib.get("IntegratedTotalsWithCP56Time2a_destroy", "cdecl")
    IntegratedTotalsWithCP56Time2a_destroy.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 849
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    IntegratedTotalsWithCP56Time2a_getTimestamp = _lib.get("IntegratedTotalsWithCP56Time2a_getTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_getTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a]
    IntegratedTotalsWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 852
for _lib in _libs.values():
    if not _lib.has("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl"):
        continue
    IntegratedTotalsWithCP56Time2a_setTimestamp = _lib.get("IntegratedTotalsWithCP56Time2a_setTimestamp", "cdecl")
    IntegratedTotalsWithCP56Time2a_setTimestamp.argtypes = [IntegratedTotalsWithCP56Time2a, CP56Time2a]
    IntegratedTotalsWithCP56Time2a_setTimestamp.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859
class struct_sEventOfProtectionEquipment(Structure):
    pass

EventOfProtectionEquipment = POINTER(struct_sEventOfProtectionEquipment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 862
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipment_destroy", "cdecl"):
        continue
    EventOfProtectionEquipment_destroy = _lib.get("EventOfProtectionEquipment_destroy", "cdecl")
    EventOfProtectionEquipment_destroy.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 865
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipment_create", "cdecl"):
        continue
    EventOfProtectionEquipment_create = _lib.get("EventOfProtectionEquipment_create", "cdecl")
    EventOfProtectionEquipment_create.argtypes = [EventOfProtectionEquipment, c_int, SingleEvent, CP16Time2a, CP24Time2a]
    EventOfProtectionEquipment_create.restype = EventOfProtectionEquipment
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 869
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipment_getEvent", "cdecl"):
        continue
    EventOfProtectionEquipment_getEvent = _lib.get("EventOfProtectionEquipment_getEvent", "cdecl")
    EventOfProtectionEquipment_getEvent.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getEvent.restype = SingleEvent
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 872
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipment_getElapsedTime", "cdecl"):
        continue
    EventOfProtectionEquipment_getElapsedTime = _lib.get("EventOfProtectionEquipment_getElapsedTime", "cdecl")
    EventOfProtectionEquipment_getElapsedTime.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getElapsedTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 875
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipment_getTimestamp", "cdecl"):
        continue
    EventOfProtectionEquipment_getTimestamp = _lib.get("EventOfProtectionEquipment_getTimestamp", "cdecl")
    EventOfProtectionEquipment_getTimestamp.argtypes = [EventOfProtectionEquipment]
    EventOfProtectionEquipment_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 881
class struct_sPackedStartEventsOfProtectionEquipment(Structure):
    pass

PackedStartEventsOfProtectionEquipment = POINTER(struct_sPackedStartEventsOfProtectionEquipment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 881

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 884
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_create", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_create = _lib.get("PackedStartEventsOfProtectionEquipment_create", "cdecl")
    PackedStartEventsOfProtectionEquipment_create.argtypes = [PackedStartEventsOfProtectionEquipment, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedStartEventsOfProtectionEquipment_create.restype = PackedStartEventsOfProtectionEquipment
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 888
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_destroy", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_destroy = _lib.get("PackedStartEventsOfProtectionEquipment_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipment_destroy.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 891
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_getEvent = _lib.get("PackedStartEventsOfProtectionEquipment_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipment_getEvent.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getEvent.restype = StartEvent
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 894
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_getQuality = _lib.get("PackedStartEventsOfProtectionEquipment_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipment_getQuality.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getQuality.restype = QualityDescriptorP
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 897
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_getElapsedTime = _lib.get("PackedStartEventsOfProtectionEquipment_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipment_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getElapsedTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 900
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipment_getTimestamp = _lib.get("PackedStartEventsOfProtectionEquipment_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipment_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipment]
    PackedStartEventsOfProtectionEquipment_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 906
class struct_sPackedOutputCircuitInfo(Structure):
    pass

PackedOutputCircuitInfo = POINTER(struct_sPackedOutputCircuitInfo)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 906

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 909
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_destroy", "cdecl"):
        continue
    PackedOutputCircuitInfo_destroy = _lib.get("PackedOutputCircuitInfo_destroy", "cdecl")
    PackedOutputCircuitInfo_destroy.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 912
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_create", "cdecl"):
        continue
    PackedOutputCircuitInfo_create = _lib.get("PackedOutputCircuitInfo_create", "cdecl")
    PackedOutputCircuitInfo_create.argtypes = [PackedOutputCircuitInfo, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP24Time2a]
    PackedOutputCircuitInfo_create.restype = PackedOutputCircuitInfo
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 916
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_getOCI", "cdecl"):
        continue
    PackedOutputCircuitInfo_getOCI = _lib.get("PackedOutputCircuitInfo_getOCI", "cdecl")
    PackedOutputCircuitInfo_getOCI.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOCI.restype = OutputCircuitInfo
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 919
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_getQuality", "cdecl"):
        continue
    PackedOutputCircuitInfo_getQuality = _lib.get("PackedOutputCircuitInfo_getQuality", "cdecl")
    PackedOutputCircuitInfo_getQuality.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getQuality.restype = QualityDescriptorP
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 922
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_getOperatingTime", "cdecl"):
        continue
    PackedOutputCircuitInfo_getOperatingTime = _lib.get("PackedOutputCircuitInfo_getOperatingTime", "cdecl")
    PackedOutputCircuitInfo_getOperatingTime.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getOperatingTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 925
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfo_getTimestamp", "cdecl"):
        continue
    PackedOutputCircuitInfo_getTimestamp = _lib.get("PackedOutputCircuitInfo_getTimestamp", "cdecl")
    PackedOutputCircuitInfo_getTimestamp.argtypes = [PackedOutputCircuitInfo]
    PackedOutputCircuitInfo_getTimestamp.restype = CP24Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 931
class struct_sPackedSinglePointWithSCD(Structure):
    pass

PackedSinglePointWithSCD = POINTER(struct_sPackedSinglePointWithSCD)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 931

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 934
for _lib in _libs.values():
    if not _lib.has("PackedSinglePointWithSCD_destroy", "cdecl"):
        continue
    PackedSinglePointWithSCD_destroy = _lib.get("PackedSinglePointWithSCD_destroy", "cdecl")
    PackedSinglePointWithSCD_destroy.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 937
for _lib in _libs.values():
    if not _lib.has("PackedSinglePointWithSCD_create", "cdecl"):
        continue
    PackedSinglePointWithSCD_create = _lib.get("PackedSinglePointWithSCD_create", "cdecl")
    PackedSinglePointWithSCD_create.argtypes = [PackedSinglePointWithSCD, c_int, StatusAndStatusChangeDetection, QualityDescriptor]
    PackedSinglePointWithSCD_create.restype = PackedSinglePointWithSCD
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 941
for _lib in _libs.values():
    if not _lib.has("PackedSinglePointWithSCD_getQuality", "cdecl"):
        continue
    PackedSinglePointWithSCD_getQuality = _lib.get("PackedSinglePointWithSCD_getQuality", "cdecl")
    PackedSinglePointWithSCD_getQuality.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getQuality.restype = QualityDescriptor
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 944
for _lib in _libs.values():
    if not _lib.has("PackedSinglePointWithSCD_getSCD", "cdecl"):
        continue
    PackedSinglePointWithSCD_getSCD = _lib.get("PackedSinglePointWithSCD_getSCD", "cdecl")
    PackedSinglePointWithSCD_getSCD.argtypes = [PackedSinglePointWithSCD]
    PackedSinglePointWithSCD_getSCD.restype = StatusAndStatusChangeDetection
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 951
class struct_sSingleCommand(Structure):
    pass

SingleCommand = POINTER(struct_sSingleCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 951

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 965
for _lib in _libs.values():
    if not _lib.has("SingleCommand_create", "cdecl"):
        continue
    SingleCommand_create = _lib.get("SingleCommand_create", "cdecl")
    SingleCommand_create.argtypes = [SingleCommand, c_int, c_bool, c_bool, c_int]
    SingleCommand_create.restype = SingleCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 968
for _lib in _libs.values():
    if not _lib.has("SingleCommand_destroy", "cdecl"):
        continue
    SingleCommand_destroy = _lib.get("SingleCommand_destroy", "cdecl")
    SingleCommand_destroy.argtypes = [SingleCommand]
    SingleCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 976
for _lib in _libs.values():
    if not _lib.has("SingleCommand_getQU", "cdecl"):
        continue
    SingleCommand_getQU = _lib.get("SingleCommand_getQU", "cdecl")
    SingleCommand_getQU.argtypes = [SingleCommand]
    SingleCommand_getQU.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 982
for _lib in _libs.values():
    if not _lib.has("SingleCommand_getState", "cdecl"):
        continue
    SingleCommand_getState = _lib.get("SingleCommand_getState", "cdecl")
    SingleCommand_getState.argtypes = [SingleCommand]
    SingleCommand_getState.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 990
for _lib in _libs.values():
    if not _lib.has("SingleCommand_isSelect", "cdecl"):
        continue
    SingleCommand_isSelect = _lib.get("SingleCommand_isSelect", "cdecl")
    SingleCommand_isSelect.argtypes = [SingleCommand]
    SingleCommand_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 996
class struct_sSingleCommandWithCP56Time2a(Structure):
    pass

SingleCommandWithCP56Time2a = POINTER(struct_sSingleCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 996

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 999
for _lib in _libs.values():
    if not _lib.has("SingleCommandWithCP56Time2a_destroy", "cdecl"):
        continue
    SingleCommandWithCP56Time2a_destroy = _lib.get("SingleCommandWithCP56Time2a_destroy", "cdecl")
    SingleCommandWithCP56Time2a_destroy.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1014
for _lib in _libs.values():
    if not _lib.has("SingleCommandWithCP56Time2a_create", "cdecl"):
        continue
    SingleCommandWithCP56Time2a_create = _lib.get("SingleCommandWithCP56Time2a_create", "cdecl")
    SingleCommandWithCP56Time2a_create.argtypes = [SingleCommandWithCP56Time2a, c_int, c_bool, c_bool, c_int, CP56Time2a]
    SingleCommandWithCP56Time2a_create.restype = SingleCommandWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1025
for _lib in _libs.values():
    if not _lib.has("SingleCommandWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    SingleCommandWithCP56Time2a_getTimestamp = _lib.get("SingleCommandWithCP56Time2a_getTimestamp", "cdecl")
    SingleCommandWithCP56Time2a_getTimestamp.argtypes = [SingleCommandWithCP56Time2a]
    SingleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1031
class struct_sDoubleCommand(Structure):
    pass

DoubleCommand = POINTER(struct_sDoubleCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1031

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1034
for _lib in _libs.values():
    if not _lib.has("DoubleCommand_destroy", "cdecl"):
        continue
    DoubleCommand_destroy = _lib.get("DoubleCommand_destroy", "cdecl")
    DoubleCommand_destroy.argtypes = [DoubleCommand]
    DoubleCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1048
for _lib in _libs.values():
    if not _lib.has("DoubleCommand_create", "cdecl"):
        continue
    DoubleCommand_create = _lib.get("DoubleCommand_create", "cdecl")
    DoubleCommand_create.argtypes = [DoubleCommand, c_int, c_int, c_bool, c_int]
    DoubleCommand_create.restype = DoubleCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1056
for _lib in _libs.values():
    if not _lib.has("DoubleCommand_getQU", "cdecl"):
        continue
    DoubleCommand_getQU = _lib.get("DoubleCommand_getQU", "cdecl")
    DoubleCommand_getQU.argtypes = [DoubleCommand]
    DoubleCommand_getQU.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1064
for _lib in _libs.values():
    if not _lib.has("DoubleCommand_getState", "cdecl"):
        continue
    DoubleCommand_getState = _lib.get("DoubleCommand_getState", "cdecl")
    DoubleCommand_getState.argtypes = [DoubleCommand]
    DoubleCommand_getState.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1072
for _lib in _libs.values():
    if not _lib.has("DoubleCommand_isSelect", "cdecl"):
        continue
    DoubleCommand_isSelect = _lib.get("DoubleCommand_isSelect", "cdecl")
    DoubleCommand_isSelect.argtypes = [DoubleCommand]
    DoubleCommand_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1078
class struct_sStepCommand(Structure):
    pass

StepCommand = POINTER(struct_sStepCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1078

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1081
for _lib in _libs.values():
    if not _lib.has("StepCommand_destroy", "cdecl"):
        continue
    StepCommand_destroy = _lib.get("StepCommand_destroy", "cdecl")
    StepCommand_destroy.argtypes = [StepCommand]
    StepCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1084
for _lib in _libs.values():
    if not _lib.has("StepCommand_create", "cdecl"):
        continue
    StepCommand_create = _lib.get("StepCommand_create", "cdecl")
    StepCommand_create.argtypes = [StepCommand, c_int, StepCommandValue, c_bool, c_int]
    StepCommand_create.restype = StepCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1092
for _lib in _libs.values():
    if not _lib.has("StepCommand_getQU", "cdecl"):
        continue
    StepCommand_getQU = _lib.get("StepCommand_getQU", "cdecl")
    StepCommand_getQU.argtypes = [StepCommand]
    StepCommand_getQU.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1095
for _lib in _libs.values():
    if not _lib.has("StepCommand_getState", "cdecl"):
        continue
    StepCommand_getState = _lib.get("StepCommand_getState", "cdecl")
    StepCommand_getState.argtypes = [StepCommand]
    StepCommand_getState.restype = StepCommandValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1103
for _lib in _libs.values():
    if not _lib.has("StepCommand_isSelect", "cdecl"):
        continue
    StepCommand_isSelect = _lib.get("StepCommand_isSelect", "cdecl")
    StepCommand_isSelect.argtypes = [StepCommand]
    StepCommand_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1109
class struct_sSetpointCommandNormalized(Structure):
    pass

SetpointCommandNormalized = POINTER(struct_sSetpointCommandNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1109

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1112
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalized_destroy", "cdecl"):
        continue
    SetpointCommandNormalized_destroy = _lib.get("SetpointCommandNormalized_destroy", "cdecl")
    SetpointCommandNormalized_destroy.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1126
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalized_create", "cdecl"):
        continue
    SetpointCommandNormalized_create = _lib.get("SetpointCommandNormalized_create", "cdecl")
    SetpointCommandNormalized_create.argtypes = [SetpointCommandNormalized, c_int, c_float, c_bool, c_int]
    SetpointCommandNormalized_create.restype = SetpointCommandNormalized
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1129
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalized_getValue", "cdecl"):
        continue
    SetpointCommandNormalized_getValue = _lib.get("SetpointCommandNormalized_getValue", "cdecl")
    SetpointCommandNormalized_getValue.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1132
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalized_getQL", "cdecl"):
        continue
    SetpointCommandNormalized_getQL = _lib.get("SetpointCommandNormalized_getQL", "cdecl")
    SetpointCommandNormalized_getQL.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1140
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalized_isSelect", "cdecl"):
        continue
    SetpointCommandNormalized_isSelect = _lib.get("SetpointCommandNormalized_isSelect", "cdecl")
    SetpointCommandNormalized_isSelect.argtypes = [SetpointCommandNormalized]
    SetpointCommandNormalized_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1146
class struct_sSetpointCommandScaled(Structure):
    pass

SetpointCommandScaled = POINTER(struct_sSetpointCommandScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1146

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1149
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaled_destroy", "cdecl"):
        continue
    SetpointCommandScaled_destroy = _lib.get("SetpointCommandScaled_destroy", "cdecl")
    SetpointCommandScaled_destroy.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1163
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaled_create", "cdecl"):
        continue
    SetpointCommandScaled_create = _lib.get("SetpointCommandScaled_create", "cdecl")
    SetpointCommandScaled_create.argtypes = [SetpointCommandScaled, c_int, c_int, c_bool, c_int]
    SetpointCommandScaled_create.restype = SetpointCommandScaled
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1166
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaled_getValue", "cdecl"):
        continue
    SetpointCommandScaled_getValue = _lib.get("SetpointCommandScaled_getValue", "cdecl")
    SetpointCommandScaled_getValue.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getValue.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1169
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaled_getQL", "cdecl"):
        continue
    SetpointCommandScaled_getQL = _lib.get("SetpointCommandScaled_getQL", "cdecl")
    SetpointCommandScaled_getQL.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1177
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaled_isSelect", "cdecl"):
        continue
    SetpointCommandScaled_isSelect = _lib.get("SetpointCommandScaled_isSelect", "cdecl")
    SetpointCommandScaled_isSelect.argtypes = [SetpointCommandScaled]
    SetpointCommandScaled_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1183
class struct_sSetpointCommandShort(Structure):
    pass

SetpointCommandShort = POINTER(struct_sSetpointCommandShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1183

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1186
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShort_destroy", "cdecl"):
        continue
    SetpointCommandShort_destroy = _lib.get("SetpointCommandShort_destroy", "cdecl")
    SetpointCommandShort_destroy.argtypes = [SetpointCommandShort]
    SetpointCommandShort_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1200
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShort_create", "cdecl"):
        continue
    SetpointCommandShort_create = _lib.get("SetpointCommandShort_create", "cdecl")
    SetpointCommandShort_create.argtypes = [SetpointCommandShort, c_int, c_float, c_bool, c_int]
    SetpointCommandShort_create.restype = SetpointCommandShort
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1203
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShort_getValue", "cdecl"):
        continue
    SetpointCommandShort_getValue = _lib.get("SetpointCommandShort_getValue", "cdecl")
    SetpointCommandShort_getValue.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1206
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShort_getQL", "cdecl"):
        continue
    SetpointCommandShort_getQL = _lib.get("SetpointCommandShort_getQL", "cdecl")
    SetpointCommandShort_getQL.argtypes = [SetpointCommandShort]
    SetpointCommandShort_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1214
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShort_isSelect", "cdecl"):
        continue
    SetpointCommandShort_isSelect = _lib.get("SetpointCommandShort_isSelect", "cdecl")
    SetpointCommandShort_isSelect.argtypes = [SetpointCommandShort]
    SetpointCommandShort_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1220
class struct_sBitstring32Command(Structure):
    pass

Bitstring32Command = POINTER(struct_sBitstring32Command)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1220

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1223
for _lib in _libs.values():
    if not _lib.has("Bitstring32Command_create", "cdecl"):
        continue
    Bitstring32Command_create = _lib.get("Bitstring32Command_create", "cdecl")
    Bitstring32Command_create.argtypes = [Bitstring32Command, c_int, uint32_t]
    Bitstring32Command_create.restype = Bitstring32Command
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1226
for _lib in _libs.values():
    if not _lib.has("Bitstring32Command_destroy", "cdecl"):
        continue
    Bitstring32Command_destroy = _lib.get("Bitstring32Command_destroy", "cdecl")
    Bitstring32Command_destroy.argtypes = [Bitstring32Command]
    Bitstring32Command_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1229
for _lib in _libs.values():
    if not _lib.has("Bitstring32Command_getValue", "cdecl"):
        continue
    Bitstring32Command_getValue = _lib.get("Bitstring32Command_getValue", "cdecl")
    Bitstring32Command_getValue.argtypes = [Bitstring32Command]
    Bitstring32Command_getValue.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1235
class struct_sInterrogationCommand(Structure):
    pass

InterrogationCommand = POINTER(struct_sInterrogationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1235

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1238
for _lib in _libs.values():
    if not _lib.has("InterrogationCommand_create", "cdecl"):
        continue
    InterrogationCommand_create = _lib.get("InterrogationCommand_create", "cdecl")
    InterrogationCommand_create.argtypes = [InterrogationCommand, c_int, uint8_t]
    InterrogationCommand_create.restype = InterrogationCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1241
for _lib in _libs.values():
    if not _lib.has("InterrogationCommand_destroy", "cdecl"):
        continue
    InterrogationCommand_destroy = _lib.get("InterrogationCommand_destroy", "cdecl")
    InterrogationCommand_destroy.argtypes = [InterrogationCommand]
    InterrogationCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1244
for _lib in _libs.values():
    if not _lib.has("InterrogationCommand_getQOI", "cdecl"):
        continue
    InterrogationCommand_getQOI = _lib.get("InterrogationCommand_getQOI", "cdecl")
    InterrogationCommand_getQOI.argtypes = [InterrogationCommand]
    InterrogationCommand_getQOI.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1250
class struct_sReadCommand(Structure):
    pass

ReadCommand = POINTER(struct_sReadCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1250

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1253
for _lib in _libs.values():
    if not _lib.has("ReadCommand_create", "cdecl"):
        continue
    ReadCommand_create = _lib.get("ReadCommand_create", "cdecl")
    ReadCommand_create.argtypes = [ReadCommand, c_int]
    ReadCommand_create.restype = ReadCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1256
for _lib in _libs.values():
    if not _lib.has("ReadCommand_destroy", "cdecl"):
        continue
    ReadCommand_destroy = _lib.get("ReadCommand_destroy", "cdecl")
    ReadCommand_destroy.argtypes = [ReadCommand]
    ReadCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1262
class struct_sClockSynchronizationCommand(Structure):
    pass

ClockSynchronizationCommand = POINTER(struct_sClockSynchronizationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1262

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1265
for _lib in _libs.values():
    if not _lib.has("ClockSynchronizationCommand_create", "cdecl"):
        continue
    ClockSynchronizationCommand_create = _lib.get("ClockSynchronizationCommand_create", "cdecl")
    ClockSynchronizationCommand_create.argtypes = [ClockSynchronizationCommand, c_int, CP56Time2a]
    ClockSynchronizationCommand_create.restype = ClockSynchronizationCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1268
for _lib in _libs.values():
    if not _lib.has("ClockSynchronizationCommand_destroy", "cdecl"):
        continue
    ClockSynchronizationCommand_destroy = _lib.get("ClockSynchronizationCommand_destroy", "cdecl")
    ClockSynchronizationCommand_destroy.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1271
for _lib in _libs.values():
    if not _lib.has("ClockSynchronizationCommand_getTime", "cdecl"):
        continue
    ClockSynchronizationCommand_getTime = _lib.get("ClockSynchronizationCommand_getTime", "cdecl")
    ClockSynchronizationCommand_getTime.argtypes = [ClockSynchronizationCommand]
    ClockSynchronizationCommand_getTime.restype = CP56Time2a
    break

ParameterNormalizedValue = POINTER(struct_sMeasuredValueNormalized)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1277

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1280
for _lib in _libs.values():
    if not _lib.has("ParameterNormalizedValue_destroy", "cdecl"):
        continue
    ParameterNormalizedValue_destroy = _lib.get("ParameterNormalizedValue_destroy", "cdecl")
    ParameterNormalizedValue_destroy.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1305
for _lib in _libs.values():
    if not _lib.has("ParameterNormalizedValue_create", "cdecl"):
        continue
    ParameterNormalizedValue_create = _lib.get("ParameterNormalizedValue_create", "cdecl")
    ParameterNormalizedValue_create.argtypes = [ParameterNormalizedValue, c_int, c_float, QualifierOfParameterMV]
    ParameterNormalizedValue_create.restype = ParameterNormalizedValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1308
for _lib in _libs.values():
    if not _lib.has("ParameterNormalizedValue_getValue", "cdecl"):
        continue
    ParameterNormalizedValue_getValue = _lib.get("ParameterNormalizedValue_getValue", "cdecl")
    ParameterNormalizedValue_getValue.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1311
for _lib in _libs.values():
    if not _lib.has("ParameterNormalizedValue_setValue", "cdecl"):
        continue
    ParameterNormalizedValue_setValue = _lib.get("ParameterNormalizedValue_setValue", "cdecl")
    ParameterNormalizedValue_setValue.argtypes = [ParameterNormalizedValue, c_float]
    ParameterNormalizedValue_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1319
for _lib in _libs.values():
    if not _lib.has("ParameterNormalizedValue_getQPM", "cdecl"):
        continue
    ParameterNormalizedValue_getQPM = _lib.get("ParameterNormalizedValue_getQPM", "cdecl")
    ParameterNormalizedValue_getQPM.argtypes = [ParameterNormalizedValue]
    ParameterNormalizedValue_getQPM.restype = QualifierOfParameterMV
    break

ParameterScaledValue = POINTER(struct_sMeasuredValueScaled)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1325

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1328
for _lib in _libs.values():
    if not _lib.has("ParameterScaledValue_destroy", "cdecl"):
        continue
    ParameterScaledValue_destroy = _lib.get("ParameterScaledValue_destroy", "cdecl")
    ParameterScaledValue_destroy.argtypes = [ParameterScaledValue]
    ParameterScaledValue_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1353
for _lib in _libs.values():
    if not _lib.has("ParameterScaledValue_create", "cdecl"):
        continue
    ParameterScaledValue_create = _lib.get("ParameterScaledValue_create", "cdecl")
    ParameterScaledValue_create.argtypes = [ParameterScaledValue, c_int, c_int, QualifierOfParameterMV]
    ParameterScaledValue_create.restype = ParameterScaledValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1356
for _lib in _libs.values():
    if not _lib.has("ParameterScaledValue_getValue", "cdecl"):
        continue
    ParameterScaledValue_getValue = _lib.get("ParameterScaledValue_getValue", "cdecl")
    ParameterScaledValue_getValue.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getValue.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1359
for _lib in _libs.values():
    if not _lib.has("ParameterScaledValue_setValue", "cdecl"):
        continue
    ParameterScaledValue_setValue = _lib.get("ParameterScaledValue_setValue", "cdecl")
    ParameterScaledValue_setValue.argtypes = [ParameterScaledValue, c_int]
    ParameterScaledValue_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1367
for _lib in _libs.values():
    if not _lib.has("ParameterScaledValue_getQPM", "cdecl"):
        continue
    ParameterScaledValue_getQPM = _lib.get("ParameterScaledValue_getQPM", "cdecl")
    ParameterScaledValue_getQPM.argtypes = [ParameterScaledValue]
    ParameterScaledValue_getQPM.restype = QualifierOfParameterMV
    break

ParameterFloatValue = POINTER(struct_sMeasuredValueShort)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1373

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1376
for _lib in _libs.values():
    if not _lib.has("ParameterFloatValue_destroy", "cdecl"):
        continue
    ParameterFloatValue_destroy = _lib.get("ParameterFloatValue_destroy", "cdecl")
    ParameterFloatValue_destroy.argtypes = [ParameterFloatValue]
    ParameterFloatValue_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1401
for _lib in _libs.values():
    if not _lib.has("ParameterFloatValue_create", "cdecl"):
        continue
    ParameterFloatValue_create = _lib.get("ParameterFloatValue_create", "cdecl")
    ParameterFloatValue_create.argtypes = [ParameterFloatValue, c_int, c_float, QualifierOfParameterMV]
    ParameterFloatValue_create.restype = ParameterFloatValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1404
for _lib in _libs.values():
    if not _lib.has("ParameterFloatValue_getValue", "cdecl"):
        continue
    ParameterFloatValue_getValue = _lib.get("ParameterFloatValue_getValue", "cdecl")
    ParameterFloatValue_getValue.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1407
for _lib in _libs.values():
    if not _lib.has("ParameterFloatValue_setValue", "cdecl"):
        continue
    ParameterFloatValue_setValue = _lib.get("ParameterFloatValue_setValue", "cdecl")
    ParameterFloatValue_setValue.argtypes = [ParameterFloatValue, c_float]
    ParameterFloatValue_setValue.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1415
for _lib in _libs.values():
    if not _lib.has("ParameterFloatValue_getQPM", "cdecl"):
        continue
    ParameterFloatValue_getQPM = _lib.get("ParameterFloatValue_getQPM", "cdecl")
    ParameterFloatValue_getQPM.argtypes = [ParameterFloatValue]
    ParameterFloatValue_getQPM.restype = QualifierOfParameterMV
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1421
class struct_sParameterActivation(Structure):
    pass

ParameterActivation = POINTER(struct_sParameterActivation)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1421

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1424
for _lib in _libs.values():
    if not _lib.has("ParameterActivation_destroy", "cdecl"):
        continue
    ParameterActivation_destroy = _lib.get("ParameterActivation_destroy", "cdecl")
    ParameterActivation_destroy.argtypes = [ParameterActivation]
    ParameterActivation_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1436
for _lib in _libs.values():
    if not _lib.has("ParameterActivation_create", "cdecl"):
        continue
    ParameterActivation_create = _lib.get("ParameterActivation_create", "cdecl")
    ParameterActivation_create.argtypes = [ParameterActivation, c_int, QualifierOfParameterActivation]
    ParameterActivation_create.restype = ParameterActivation
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1444
for _lib in _libs.values():
    if not _lib.has("ParameterActivation_getQuality", "cdecl"):
        continue
    ParameterActivation_getQuality = _lib.get("ParameterActivation_getQuality", "cdecl")
    ParameterActivation_getQuality.argtypes = [ParameterActivation]
    ParameterActivation_getQuality.restype = QualifierOfParameterActivation
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1450
class struct_sEventOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

EventOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sEventOfProtectionEquipmentWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1450

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1453
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
        continue
    EventOfProtectionEquipmentWithCP56Time2a_destroy = _lib.get("EventOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1456
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
        continue
    EventOfProtectionEquipmentWithCP56Time2a_create = _lib.get("EventOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_create.argtypes = [EventOfProtectionEquipmentWithCP56Time2a, c_int, SingleEvent, CP16Time2a, CP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_create.restype = EventOfProtectionEquipmentWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1460
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
        continue
    EventOfProtectionEquipmentWithCP56Time2a_getEvent = _lib.get("EventOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getEvent.restype = SingleEvent
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1463
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
        continue
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _lib.get("EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1466
for _lib in _libs.values():
    if not _lib.has("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp = _lib.get("EventOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [EventOfProtectionEquipmentWithCP56Time2a]
    EventOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1472
class struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a(Structure):
    pass

PackedStartEventsOfProtectionEquipmentWithCP56Time2a = POINTER(struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1472

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1475
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1478
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a, c_int, StartEvent, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_create.restype = PackedStartEventsOfProtectionEquipmentWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1482
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getEvent.restype = StartEvent
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1485
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getQuality.restype = QualityDescriptorP
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1488
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getElapsedTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1491
for _lib in _libs.values():
    if not _lib.has("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp = _lib.get("PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp", "cdecl")
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.argtypes = [PackedStartEventsOfProtectionEquipmentWithCP56Time2a]
    PackedStartEventsOfProtectionEquipmentWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1497
class struct_sPackedOutputCircuitInfoWithCP56Time2a(Structure):
    pass

PackedOutputCircuitInfoWithCP56Time2a = POINTER(struct_sPackedOutputCircuitInfoWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1497

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1500
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_destroy = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_destroy", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_destroy.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1503
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_create = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_create", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_create.argtypes = [PackedOutputCircuitInfoWithCP56Time2a, c_int, OutputCircuitInfo, QualityDescriptorP, CP16Time2a, CP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_create.restype = PackedOutputCircuitInfoWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1507
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_getOCI = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_getOCI", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOCI.restype = OutputCircuitInfo
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1510
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_getQuality = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_getQuality", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getQuality.restype = QualityDescriptorP
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1513
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getOperatingTime.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1516
for _lib in _libs.values():
    if not _lib.has("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp = _lib.get("PackedOutputCircuitInfoWithCP56Time2a_getTimestamp", "cdecl")
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.argtypes = [PackedOutputCircuitInfoWithCP56Time2a]
    PackedOutputCircuitInfoWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1522
class struct_sDoubleCommandWithCP56Time2a(Structure):
    pass

DoubleCommandWithCP56Time2a = POINTER(struct_sDoubleCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1522

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1525
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_destroy", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_destroy = _lib.get("DoubleCommandWithCP56Time2a_destroy", "cdecl")
    DoubleCommandWithCP56Time2a_destroy.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1528
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_create", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_create = _lib.get("DoubleCommandWithCP56Time2a_create", "cdecl")
    DoubleCommandWithCP56Time2a_create.argtypes = [DoubleCommandWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    DoubleCommandWithCP56Time2a_create.restype = DoubleCommandWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1531
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_getQU", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_getQU = _lib.get("DoubleCommandWithCP56Time2a_getQU", "cdecl")
    DoubleCommandWithCP56Time2a_getQU.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getQU.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1534
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_getState", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_getState = _lib.get("DoubleCommandWithCP56Time2a_getState", "cdecl")
    DoubleCommandWithCP56Time2a_getState.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getState.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1537
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_isSelect", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_isSelect = _lib.get("DoubleCommandWithCP56Time2a_isSelect", "cdecl")
    DoubleCommandWithCP56Time2a_isSelect.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1540
for _lib in _libs.values():
    if not _lib.has("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    DoubleCommandWithCP56Time2a_getTimestamp = _lib.get("DoubleCommandWithCP56Time2a_getTimestamp", "cdecl")
    DoubleCommandWithCP56Time2a_getTimestamp.argtypes = [DoubleCommandWithCP56Time2a]
    DoubleCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1546
class struct_sStepCommandWithCP56Time2a(Structure):
    pass

StepCommandWithCP56Time2a = POINTER(struct_sStepCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1546

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1549
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_destroy", "cdecl"):
        continue
    StepCommandWithCP56Time2a_destroy = _lib.get("StepCommandWithCP56Time2a_destroy", "cdecl")
    StepCommandWithCP56Time2a_destroy.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1552
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_create", "cdecl"):
        continue
    StepCommandWithCP56Time2a_create = _lib.get("StepCommandWithCP56Time2a_create", "cdecl")
    StepCommandWithCP56Time2a_create.argtypes = [StepCommandWithCP56Time2a, c_int, StepCommandValue, c_bool, c_int, CP56Time2a]
    StepCommandWithCP56Time2a_create.restype = StepCommandWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1555
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_getQU", "cdecl"):
        continue
    StepCommandWithCP56Time2a_getQU = _lib.get("StepCommandWithCP56Time2a_getQU", "cdecl")
    StepCommandWithCP56Time2a_getQU.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getQU.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1558
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_getState", "cdecl"):
        continue
    StepCommandWithCP56Time2a_getState = _lib.get("StepCommandWithCP56Time2a_getState", "cdecl")
    StepCommandWithCP56Time2a_getState.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getState.restype = StepCommandValue
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1561
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_isSelect", "cdecl"):
        continue
    StepCommandWithCP56Time2a_isSelect = _lib.get("StepCommandWithCP56Time2a_isSelect", "cdecl")
    StepCommandWithCP56Time2a_isSelect.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1564
for _lib in _libs.values():
    if not _lib.has("StepCommandWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    StepCommandWithCP56Time2a_getTimestamp = _lib.get("StepCommandWithCP56Time2a_getTimestamp", "cdecl")
    StepCommandWithCP56Time2a_getTimestamp.argtypes = [StepCommandWithCP56Time2a]
    StepCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1570
class struct_sSetpointCommandNormalizedWithCP56Time2a(Structure):
    pass

SetpointCommandNormalizedWithCP56Time2a = POINTER(struct_sSetpointCommandNormalizedWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1570

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1573
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_destroy = _lib.get("SetpointCommandNormalizedWithCP56Time2a_destroy", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_destroy.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1576
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_create = _lib.get("SetpointCommandNormalizedWithCP56Time2a_create", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_create.argtypes = [SetpointCommandNormalizedWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_create.restype = SetpointCommandNormalizedWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1579
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_getValue = _lib.get("SetpointCommandNormalizedWithCP56Time2a_getValue", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getValue.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1582
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_getQL = _lib.get("SetpointCommandNormalizedWithCP56Time2a_getQL", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getQL.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1585
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_isSelect = _lib.get("SetpointCommandNormalizedWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_isSelect.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1588
for _lib in _libs.values():
    if not _lib.has("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp = _lib.get("SetpointCommandNormalizedWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandNormalizedWithCP56Time2a]
    SetpointCommandNormalizedWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1594
class struct_sSetpointCommandScaledWithCP56Time2a(Structure):
    pass

SetpointCommandScaledWithCP56Time2a = POINTER(struct_sSetpointCommandScaledWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1594

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1597
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_destroy = _lib.get("SetpointCommandScaledWithCP56Time2a_destroy", "cdecl")
    SetpointCommandScaledWithCP56Time2a_destroy.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1600
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_create", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_create = _lib.get("SetpointCommandScaledWithCP56Time2a_create", "cdecl")
    SetpointCommandScaledWithCP56Time2a_create.argtypes = [SetpointCommandScaledWithCP56Time2a, c_int, c_int, c_bool, c_int, CP56Time2a]
    SetpointCommandScaledWithCP56Time2a_create.restype = SetpointCommandScaledWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1603
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_getValue = _lib.get("SetpointCommandScaledWithCP56Time2a_getValue", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getValue.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getValue.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1606
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_getQL = _lib.get("SetpointCommandScaledWithCP56Time2a_getQL", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getQL.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1609
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_isSelect = _lib.get("SetpointCommandScaledWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandScaledWithCP56Time2a_isSelect.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1612
for _lib in _libs.values():
    if not _lib.has("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    SetpointCommandScaledWithCP56Time2a_getTimestamp = _lib.get("SetpointCommandScaledWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandScaledWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandScaledWithCP56Time2a]
    SetpointCommandScaledWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1618
class struct_sSetpointCommandShortWithCP56Time2a(Structure):
    pass

SetpointCommandShortWithCP56Time2a = POINTER(struct_sSetpointCommandShortWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1618

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1621
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_destroy", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_destroy = _lib.get("SetpointCommandShortWithCP56Time2a_destroy", "cdecl")
    SetpointCommandShortWithCP56Time2a_destroy.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1624
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_create", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_create = _lib.get("SetpointCommandShortWithCP56Time2a_create", "cdecl")
    SetpointCommandShortWithCP56Time2a_create.argtypes = [SetpointCommandShortWithCP56Time2a, c_int, c_float, c_bool, c_int, CP56Time2a]
    SetpointCommandShortWithCP56Time2a_create.restype = SetpointCommandShortWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1627
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_getValue", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_getValue = _lib.get("SetpointCommandShortWithCP56Time2a_getValue", "cdecl")
    SetpointCommandShortWithCP56Time2a_getValue.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getValue.restype = c_float
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1630
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_getQL", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_getQL = _lib.get("SetpointCommandShortWithCP56Time2a_getQL", "cdecl")
    SetpointCommandShortWithCP56Time2a_getQL.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getQL.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1633
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_isSelect = _lib.get("SetpointCommandShortWithCP56Time2a_isSelect", "cdecl")
    SetpointCommandShortWithCP56Time2a_isSelect.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_isSelect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1636
for _lib in _libs.values():
    if not _lib.has("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    SetpointCommandShortWithCP56Time2a_getTimestamp = _lib.get("SetpointCommandShortWithCP56Time2a_getTimestamp", "cdecl")
    SetpointCommandShortWithCP56Time2a_getTimestamp.argtypes = [SetpointCommandShortWithCP56Time2a]
    SetpointCommandShortWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1642
class struct_sBitstring32CommandWithCP56Time2a(Structure):
    pass

Bitstring32CommandWithCP56Time2a = POINTER(struct_sBitstring32CommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1642

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1645
for _lib in _libs.values():
    if not _lib.has("Bitstring32CommandWithCP56Time2a_create", "cdecl"):
        continue
    Bitstring32CommandWithCP56Time2a_create = _lib.get("Bitstring32CommandWithCP56Time2a_create", "cdecl")
    Bitstring32CommandWithCP56Time2a_create.argtypes = [Bitstring32CommandWithCP56Time2a, c_int, uint32_t, CP56Time2a]
    Bitstring32CommandWithCP56Time2a_create.restype = Bitstring32CommandWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1648
for _lib in _libs.values():
    if not _lib.has("Bitstring32CommandWithCP56Time2a_destroy", "cdecl"):
        continue
    Bitstring32CommandWithCP56Time2a_destroy = _lib.get("Bitstring32CommandWithCP56Time2a_destroy", "cdecl")
    Bitstring32CommandWithCP56Time2a_destroy.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1651
for _lib in _libs.values():
    if not _lib.has("Bitstring32CommandWithCP56Time2a_getValue", "cdecl"):
        continue
    Bitstring32CommandWithCP56Time2a_getValue = _lib.get("Bitstring32CommandWithCP56Time2a_getValue", "cdecl")
    Bitstring32CommandWithCP56Time2a_getValue.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getValue.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1654
for _lib in _libs.values():
    if not _lib.has("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    Bitstring32CommandWithCP56Time2a_getTimestamp = _lib.get("Bitstring32CommandWithCP56Time2a_getTimestamp", "cdecl")
    Bitstring32CommandWithCP56Time2a_getTimestamp.argtypes = [Bitstring32CommandWithCP56Time2a]
    Bitstring32CommandWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1661
class struct_sCounterInterrogationCommand(Structure):
    pass

CounterInterrogationCommand = POINTER(struct_sCounterInterrogationCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1661

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1664
for _lib in _libs.values():
    if not _lib.has("CounterInterrogationCommand_create", "cdecl"):
        continue
    CounterInterrogationCommand_create = _lib.get("CounterInterrogationCommand_create", "cdecl")
    CounterInterrogationCommand_create.argtypes = [CounterInterrogationCommand, c_int, QualifierOfCIC]
    CounterInterrogationCommand_create.restype = CounterInterrogationCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1667
for _lib in _libs.values():
    if not _lib.has("CounterInterrogationCommand_destroy", "cdecl"):
        continue
    CounterInterrogationCommand_destroy = _lib.get("CounterInterrogationCommand_destroy", "cdecl")
    CounterInterrogationCommand_destroy.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1670
for _lib in _libs.values():
    if not _lib.has("CounterInterrogationCommand_getQCC", "cdecl"):
        continue
    CounterInterrogationCommand_getQCC = _lib.get("CounterInterrogationCommand_getQCC", "cdecl")
    CounterInterrogationCommand_getQCC.argtypes = [CounterInterrogationCommand]
    CounterInterrogationCommand_getQCC.restype = QualifierOfCIC
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1676
class struct_sTestCommand(Structure):
    pass

TestCommand = POINTER(struct_sTestCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1676

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1679
for _lib in _libs.values():
    if not _lib.has("TestCommand_create", "cdecl"):
        continue
    TestCommand_create = _lib.get("TestCommand_create", "cdecl")
    TestCommand_create.argtypes = [TestCommand]
    TestCommand_create.restype = TestCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1682
for _lib in _libs.values():
    if not _lib.has("TestCommand_destroy", "cdecl"):
        continue
    TestCommand_destroy = _lib.get("TestCommand_destroy", "cdecl")
    TestCommand_destroy.argtypes = [TestCommand]
    TestCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1685
for _lib in _libs.values():
    if not _lib.has("TestCommand_isValid", "cdecl"):
        continue
    TestCommand_isValid = _lib.get("TestCommand_isValid", "cdecl")
    TestCommand_isValid.argtypes = [TestCommand]
    TestCommand_isValid.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1691
class struct_sTestCommandWithCP56Time2a(Structure):
    pass

TestCommandWithCP56Time2a = POINTER(struct_sTestCommandWithCP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1691

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1703
for _lib in _libs.values():
    if not _lib.has("TestCommandWithCP56Time2a_create", "cdecl"):
        continue
    TestCommandWithCP56Time2a_create = _lib.get("TestCommandWithCP56Time2a_create", "cdecl")
    TestCommandWithCP56Time2a_create.argtypes = [TestCommandWithCP56Time2a, uint16_t, CP56Time2a]
    TestCommandWithCP56Time2a_create.restype = TestCommandWithCP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1706
for _lib in _libs.values():
    if not _lib.has("TestCommandWithCP56Time2a_destroy", "cdecl"):
        continue
    TestCommandWithCP56Time2a_destroy = _lib.get("TestCommandWithCP56Time2a_destroy", "cdecl")
    TestCommandWithCP56Time2a_destroy.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1709
for _lib in _libs.values():
    if not _lib.has("TestCommandWithCP56Time2a_getCounter", "cdecl"):
        continue
    TestCommandWithCP56Time2a_getCounter = _lib.get("TestCommandWithCP56Time2a_getCounter", "cdecl")
    TestCommandWithCP56Time2a_getCounter.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getCounter.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1712
for _lib in _libs.values():
    if not _lib.has("TestCommandWithCP56Time2a_getTimestamp", "cdecl"):
        continue
    TestCommandWithCP56Time2a_getTimestamp = _lib.get("TestCommandWithCP56Time2a_getTimestamp", "cdecl")
    TestCommandWithCP56Time2a_getTimestamp.argtypes = [TestCommandWithCP56Time2a]
    TestCommandWithCP56Time2a_getTimestamp.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1718
class struct_sResetProcessCommand(Structure):
    pass

ResetProcessCommand = POINTER(struct_sResetProcessCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1718

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1721
for _lib in _libs.values():
    if not _lib.has("ResetProcessCommand_create", "cdecl"):
        continue
    ResetProcessCommand_create = _lib.get("ResetProcessCommand_create", "cdecl")
    ResetProcessCommand_create.argtypes = [ResetProcessCommand, c_int, QualifierOfRPC]
    ResetProcessCommand_create.restype = ResetProcessCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1724
for _lib in _libs.values():
    if not _lib.has("ResetProcessCommand_destroy", "cdecl"):
        continue
    ResetProcessCommand_destroy = _lib.get("ResetProcessCommand_destroy", "cdecl")
    ResetProcessCommand_destroy.argtypes = [ResetProcessCommand]
    ResetProcessCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1727
for _lib in _libs.values():
    if not _lib.has("ResetProcessCommand_getQRP", "cdecl"):
        continue
    ResetProcessCommand_getQRP = _lib.get("ResetProcessCommand_getQRP", "cdecl")
    ResetProcessCommand_getQRP.argtypes = [ResetProcessCommand]
    ResetProcessCommand_getQRP.restype = QualifierOfRPC
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1733
class struct_sDelayAcquisitionCommand(Structure):
    pass

DelayAcquisitionCommand = POINTER(struct_sDelayAcquisitionCommand)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1733

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1736
for _lib in _libs.values():
    if not _lib.has("DelayAcquisitionCommand_create", "cdecl"):
        continue
    DelayAcquisitionCommand_create = _lib.get("DelayAcquisitionCommand_create", "cdecl")
    DelayAcquisitionCommand_create.argtypes = [DelayAcquisitionCommand, c_int, CP16Time2a]
    DelayAcquisitionCommand_create.restype = DelayAcquisitionCommand
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1739
for _lib in _libs.values():
    if not _lib.has("DelayAcquisitionCommand_destroy", "cdecl"):
        continue
    DelayAcquisitionCommand_destroy = _lib.get("DelayAcquisitionCommand_destroy", "cdecl")
    DelayAcquisitionCommand_destroy.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1742
for _lib in _libs.values():
    if not _lib.has("DelayAcquisitionCommand_getDelay", "cdecl"):
        continue
    DelayAcquisitionCommand_getDelay = _lib.get("DelayAcquisitionCommand_getDelay", "cdecl")
    DelayAcquisitionCommand_getDelay.argtypes = [DelayAcquisitionCommand]
    DelayAcquisitionCommand_getDelay.restype = CP16Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1748
class struct_sEndOfInitialization(Structure):
    pass

EndOfInitialization = POINTER(struct_sEndOfInitialization)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1748

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1751
for _lib in _libs.values():
    if not _lib.has("EndOfInitialization_create", "cdecl"):
        continue
    EndOfInitialization_create = _lib.get("EndOfInitialization_create", "cdecl")
    EndOfInitialization_create.argtypes = [EndOfInitialization, uint8_t]
    EndOfInitialization_create.restype = EndOfInitialization
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1754
for _lib in _libs.values():
    if not _lib.has("EndOfInitialization_destroy", "cdecl"):
        continue
    EndOfInitialization_destroy = _lib.get("EndOfInitialization_destroy", "cdecl")
    EndOfInitialization_destroy.argtypes = [EndOfInitialization]
    EndOfInitialization_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1757
for _lib in _libs.values():
    if not _lib.has("EndOfInitialization_getCOI", "cdecl"):
        continue
    EndOfInitialization_getCOI = _lib.get("EndOfInitialization_getCOI", "cdecl")
    EndOfInitialization_getCOI.argtypes = [EndOfInitialization]
    EndOfInitialization_getCOI.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1889
class struct_sFileReady(Structure):
    pass

FileReady = POINTER(struct_sFileReady)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1889

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1903
for _lib in _libs.values():
    if not _lib.has("FileReady_create", "cdecl"):
        continue
    FileReady_create = _lib.get("FileReady_create", "cdecl")
    FileReady_create.argtypes = [FileReady, c_int, uint16_t, uint32_t, c_bool]
    FileReady_create.restype = FileReady
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1906
for _lib in _libs.values():
    if not _lib.has("FileReady_getFRQ", "cdecl"):
        continue
    FileReady_getFRQ = _lib.get("FileReady_getFRQ", "cdecl")
    FileReady_getFRQ.argtypes = [FileReady]
    FileReady_getFRQ.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1909
for _lib in _libs.values():
    if not _lib.has("FileReady_setFRQ", "cdecl"):
        continue
    FileReady_setFRQ = _lib.get("FileReady_setFRQ", "cdecl")
    FileReady_setFRQ.argtypes = [FileReady, uint8_t]
    FileReady_setFRQ.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1912
for _lib in _libs.values():
    if not _lib.has("FileReady_isPositive", "cdecl"):
        continue
    FileReady_isPositive = _lib.get("FileReady_isPositive", "cdecl")
    FileReady_isPositive.argtypes = [FileReady]
    FileReady_isPositive.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1915
for _lib in _libs.values():
    if not _lib.has("FileReady_getNOF", "cdecl"):
        continue
    FileReady_getNOF = _lib.get("FileReady_getNOF", "cdecl")
    FileReady_getNOF.argtypes = [FileReady]
    FileReady_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1918
for _lib in _libs.values():
    if not _lib.has("FileReady_getLengthOfFile", "cdecl"):
        continue
    FileReady_getLengthOfFile = _lib.get("FileReady_getLengthOfFile", "cdecl")
    FileReady_getLengthOfFile.argtypes = [FileReady]
    FileReady_getLengthOfFile.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1921
for _lib in _libs.values():
    if not _lib.has("FileReady_destroy", "cdecl"):
        continue
    FileReady_destroy = _lib.get("FileReady_destroy", "cdecl")
    FileReady_destroy.argtypes = [FileReady]
    FileReady_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1927
class struct_sSectionReady(Structure):
    pass

SectionReady = POINTER(struct_sSectionReady)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1927

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1930
for _lib in _libs.values():
    if not _lib.has("SectionReady_create", "cdecl"):
        continue
    SectionReady_create = _lib.get("SectionReady_create", "cdecl")
    SectionReady_create.argtypes = [SectionReady, c_int, uint16_t, uint8_t, uint32_t, c_bool]
    SectionReady_create.restype = SectionReady
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1934
for _lib in _libs.values():
    if not _lib.has("SectionReady_isNotReady", "cdecl"):
        continue
    SectionReady_isNotReady = _lib.get("SectionReady_isNotReady", "cdecl")
    SectionReady_isNotReady.argtypes = [SectionReady]
    SectionReady_isNotReady.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1937
for _lib in _libs.values():
    if not _lib.has("SectionReady_getSRQ", "cdecl"):
        continue
    SectionReady_getSRQ = _lib.get("SectionReady_getSRQ", "cdecl")
    SectionReady_getSRQ.argtypes = [SectionReady]
    SectionReady_getSRQ.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1940
for _lib in _libs.values():
    if not _lib.has("SectionReady_setSRQ", "cdecl"):
        continue
    SectionReady_setSRQ = _lib.get("SectionReady_setSRQ", "cdecl")
    SectionReady_setSRQ.argtypes = [SectionReady, uint8_t]
    SectionReady_setSRQ.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1943
for _lib in _libs.values():
    if not _lib.has("SectionReady_getNOF", "cdecl"):
        continue
    SectionReady_getNOF = _lib.get("SectionReady_getNOF", "cdecl")
    SectionReady_getNOF.argtypes = [SectionReady]
    SectionReady_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1946
for _lib in _libs.values():
    if not _lib.has("SectionReady_getNameOfSection", "cdecl"):
        continue
    SectionReady_getNameOfSection = _lib.get("SectionReady_getNameOfSection", "cdecl")
    SectionReady_getNameOfSection.argtypes = [SectionReady]
    SectionReady_getNameOfSection.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1949
for _lib in _libs.values():
    if not _lib.has("SectionReady_getLengthOfSection", "cdecl"):
        continue
    SectionReady_getLengthOfSection = _lib.get("SectionReady_getLengthOfSection", "cdecl")
    SectionReady_getLengthOfSection.argtypes = [SectionReady]
    SectionReady_getLengthOfSection.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1952
for _lib in _libs.values():
    if not _lib.has("SectionReady_destroy", "cdecl"):
        continue
    SectionReady_destroy = _lib.get("SectionReady_destroy", "cdecl")
    SectionReady_destroy.argtypes = [SectionReady]
    SectionReady_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1959
class struct_sFileCallOrSelect(Structure):
    pass

FileCallOrSelect = POINTER(struct_sFileCallOrSelect)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1959

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1962
for _lib in _libs.values():
    if not _lib.has("FileCallOrSelect_create", "cdecl"):
        continue
    FileCallOrSelect_create = _lib.get("FileCallOrSelect_create", "cdecl")
    FileCallOrSelect_create.argtypes = [FileCallOrSelect, c_int, uint16_t, uint8_t, uint8_t]
    FileCallOrSelect_create.restype = FileCallOrSelect
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1965
for _lib in _libs.values():
    if not _lib.has("FileCallOrSelect_getNOF", "cdecl"):
        continue
    FileCallOrSelect_getNOF = _lib.get("FileCallOrSelect_getNOF", "cdecl")
    FileCallOrSelect_getNOF.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1968
for _lib in _libs.values():
    if not _lib.has("FileCallOrSelect_getNameOfSection", "cdecl"):
        continue
    FileCallOrSelect_getNameOfSection = _lib.get("FileCallOrSelect_getNameOfSection", "cdecl")
    FileCallOrSelect_getNameOfSection.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getNameOfSection.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1971
for _lib in _libs.values():
    if not _lib.has("FileCallOrSelect_getSCQ", "cdecl"):
        continue
    FileCallOrSelect_getSCQ = _lib.get("FileCallOrSelect_getSCQ", "cdecl")
    FileCallOrSelect_getSCQ.argtypes = [FileCallOrSelect]
    FileCallOrSelect_getSCQ.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1974
for _lib in _libs.values():
    if not _lib.has("FileCallOrSelect_destroy", "cdecl"):
        continue
    FileCallOrSelect_destroy = _lib.get("FileCallOrSelect_destroy", "cdecl")
    FileCallOrSelect_destroy.argtypes = [FileCallOrSelect]
    FileCallOrSelect_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1980
class struct_sFileLastSegmentOrSection(Structure):
    pass

FileLastSegmentOrSection = POINTER(struct_sFileLastSegmentOrSection)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1980

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1983
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_create", "cdecl"):
        continue
    FileLastSegmentOrSection_create = _lib.get("FileLastSegmentOrSection_create", "cdecl")
    FileLastSegmentOrSection_create.argtypes = [FileLastSegmentOrSection, c_int, uint16_t, uint8_t, uint8_t, uint8_t]
    FileLastSegmentOrSection_create.restype = FileLastSegmentOrSection
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1986
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_getNOF", "cdecl"):
        continue
    FileLastSegmentOrSection_getNOF = _lib.get("FileLastSegmentOrSection_getNOF", "cdecl")
    FileLastSegmentOrSection_getNOF.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1989
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_getNameOfSection", "cdecl"):
        continue
    FileLastSegmentOrSection_getNameOfSection = _lib.get("FileLastSegmentOrSection_getNameOfSection", "cdecl")
    FileLastSegmentOrSection_getNameOfSection.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getNameOfSection.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1992
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_getLSQ", "cdecl"):
        continue
    FileLastSegmentOrSection_getLSQ = _lib.get("FileLastSegmentOrSection_getLSQ", "cdecl")
    FileLastSegmentOrSection_getLSQ.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getLSQ.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1995
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_getCHS", "cdecl"):
        continue
    FileLastSegmentOrSection_getCHS = _lib.get("FileLastSegmentOrSection_getCHS", "cdecl")
    FileLastSegmentOrSection_getCHS.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_getCHS.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1998
for _lib in _libs.values():
    if not _lib.has("FileLastSegmentOrSection_destroy", "cdecl"):
        continue
    FileLastSegmentOrSection_destroy = _lib.get("FileLastSegmentOrSection_destroy", "cdecl")
    FileLastSegmentOrSection_destroy.argtypes = [FileLastSegmentOrSection]
    FileLastSegmentOrSection_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2004
class struct_sFileACK(Structure):
    pass

FileACK = POINTER(struct_sFileACK)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2004

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2007
for _lib in _libs.values():
    if not _lib.has("FileACK_create", "cdecl"):
        continue
    FileACK_create = _lib.get("FileACK_create", "cdecl")
    FileACK_create.argtypes = [FileACK, c_int, uint16_t, uint8_t, uint8_t]
    FileACK_create.restype = FileACK
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2010
for _lib in _libs.values():
    if not _lib.has("FileACK_getNOF", "cdecl"):
        continue
    FileACK_getNOF = _lib.get("FileACK_getNOF", "cdecl")
    FileACK_getNOF.argtypes = [FileACK]
    FileACK_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2013
for _lib in _libs.values():
    if not _lib.has("FileACK_getNameOfSection", "cdecl"):
        continue
    FileACK_getNameOfSection = _lib.get("FileACK_getNameOfSection", "cdecl")
    FileACK_getNameOfSection.argtypes = [FileACK]
    FileACK_getNameOfSection.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2016
for _lib in _libs.values():
    if not _lib.has("FileACK_getAFQ", "cdecl"):
        continue
    FileACK_getAFQ = _lib.get("FileACK_getAFQ", "cdecl")
    FileACK_getAFQ.argtypes = [FileACK]
    FileACK_getAFQ.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2019
for _lib in _libs.values():
    if not _lib.has("FileACK_destroy", "cdecl"):
        continue
    FileACK_destroy = _lib.get("FileACK_destroy", "cdecl")
    FileACK_destroy.argtypes = [FileACK]
    FileACK_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2025
class struct_sFileSegment(Structure):
    pass

FileSegment = POINTER(struct_sFileSegment)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2025

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2028
for _lib in _libs.values():
    if not _lib.has("FileSegment_create", "cdecl"):
        continue
    FileSegment_create = _lib.get("FileSegment_create", "cdecl")
    FileSegment_create.argtypes = [FileSegment, c_int, uint16_t, uint8_t, POINTER(uint8_t), uint8_t]
    FileSegment_create.restype = FileSegment
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2031
for _lib in _libs.values():
    if not _lib.has("FileSegment_getNOF", "cdecl"):
        continue
    FileSegment_getNOF = _lib.get("FileSegment_getNOF", "cdecl")
    FileSegment_getNOF.argtypes = [FileSegment]
    FileSegment_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2034
for _lib in _libs.values():
    if not _lib.has("FileSegment_getNameOfSection", "cdecl"):
        continue
    FileSegment_getNameOfSection = _lib.get("FileSegment_getNameOfSection", "cdecl")
    FileSegment_getNameOfSection.argtypes = [FileSegment]
    FileSegment_getNameOfSection.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2037
for _lib in _libs.values():
    if not _lib.has("FileSegment_getLengthOfSegment", "cdecl"):
        continue
    FileSegment_getLengthOfSegment = _lib.get("FileSegment_getLengthOfSegment", "cdecl")
    FileSegment_getLengthOfSegment.argtypes = [FileSegment]
    FileSegment_getLengthOfSegment.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2039
for _lib in _libs.values():
    if not _lib.has("FileSegment_getSegmentData", "cdecl"):
        continue
    FileSegment_getSegmentData = _lib.get("FileSegment_getSegmentData", "cdecl")
    FileSegment_getSegmentData.argtypes = [FileSegment]
    FileSegment_getSegmentData.restype = POINTER(uint8_t)
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2043
for _lib in _libs.values():
    if not _lib.has("FileSegment_GetMaxDataSize", "cdecl"):
        continue
    FileSegment_GetMaxDataSize = _lib.get("FileSegment_GetMaxDataSize", "cdecl")
    FileSegment_GetMaxDataSize.argtypes = [CS101_AppLayerParameters]
    FileSegment_GetMaxDataSize.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2046
for _lib in _libs.values():
    if not _lib.has("FileSegment_destroy", "cdecl"):
        continue
    FileSegment_destroy = _lib.get("FileSegment_destroy", "cdecl")
    FileSegment_destroy.argtypes = [FileSegment]
    FileSegment_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2052
class struct_sFileDirectory(Structure):
    pass

FileDirectory = POINTER(struct_sFileDirectory)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2052

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2055
for _lib in _libs.values():
    if not _lib.has("FileDirectory_create", "cdecl"):
        continue
    FileDirectory_create = _lib.get("FileDirectory_create", "cdecl")
    FileDirectory_create.argtypes = [FileDirectory, c_int, uint16_t, uint32_t, uint8_t, CP56Time2a]
    FileDirectory_create.restype = FileDirectory
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2058
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getNOF", "cdecl"):
        continue
    FileDirectory_getNOF = _lib.get("FileDirectory_getNOF", "cdecl")
    FileDirectory_getNOF.argtypes = [FileDirectory]
    FileDirectory_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2061
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getSOF", "cdecl"):
        continue
    FileDirectory_getSOF = _lib.get("FileDirectory_getSOF", "cdecl")
    FileDirectory_getSOF.argtypes = [FileDirectory]
    FileDirectory_getSOF.restype = uint8_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2064
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getSTATUS", "cdecl"):
        continue
    FileDirectory_getSTATUS = _lib.get("FileDirectory_getSTATUS", "cdecl")
    FileDirectory_getSTATUS.argtypes = [FileDirectory]
    FileDirectory_getSTATUS.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2067
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getLFD", "cdecl"):
        continue
    FileDirectory_getLFD = _lib.get("FileDirectory_getLFD", "cdecl")
    FileDirectory_getLFD.argtypes = [FileDirectory]
    FileDirectory_getLFD.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2070
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getFOR", "cdecl"):
        continue
    FileDirectory_getFOR = _lib.get("FileDirectory_getFOR", "cdecl")
    FileDirectory_getFOR.argtypes = [FileDirectory]
    FileDirectory_getFOR.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2073
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getFA", "cdecl"):
        continue
    FileDirectory_getFA = _lib.get("FileDirectory_getFA", "cdecl")
    FileDirectory_getFA.argtypes = [FileDirectory]
    FileDirectory_getFA.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2076
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getLengthOfFile", "cdecl"):
        continue
    FileDirectory_getLengthOfFile = _lib.get("FileDirectory_getLengthOfFile", "cdecl")
    FileDirectory_getLengthOfFile.argtypes = [FileDirectory]
    FileDirectory_getLengthOfFile.restype = uint32_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2079
for _lib in _libs.values():
    if not _lib.has("FileDirectory_getCreationTime", "cdecl"):
        continue
    FileDirectory_getCreationTime = _lib.get("FileDirectory_getCreationTime", "cdecl")
    FileDirectory_getCreationTime.argtypes = [FileDirectory]
    FileDirectory_getCreationTime.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2082
for _lib in _libs.values():
    if not _lib.has("FileDirectory_destroy", "cdecl"):
        continue
    FileDirectory_destroy = _lib.get("FileDirectory_destroy", "cdecl")
    FileDirectory_destroy.argtypes = [FileDirectory]
    FileDirectory_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2088
class struct_sQueryLog(Structure):
    pass

QueryLog = POINTER(struct_sQueryLog)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2088

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2091
for _lib in _libs.values():
    if not _lib.has("QueryLog_create", "cdecl"):
        continue
    QueryLog_create = _lib.get("QueryLog_create", "cdecl")
    QueryLog_create.argtypes = [QueryLog, c_int, uint16_t, CP56Time2a, CP56Time2a]
    QueryLog_create.restype = QueryLog
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2094
for _lib in _libs.values():
    if not _lib.has("QueryLog_getNOF", "cdecl"):
        continue
    QueryLog_getNOF = _lib.get("QueryLog_getNOF", "cdecl")
    QueryLog_getNOF.argtypes = [QueryLog]
    QueryLog_getNOF.restype = uint16_t
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2097
for _lib in _libs.values():
    if not _lib.has("QueryLog_getRangeStartTime", "cdecl"):
        continue
    QueryLog_getRangeStartTime = _lib.get("QueryLog_getRangeStartTime", "cdecl")
    QueryLog_getRangeStartTime.argtypes = [QueryLog]
    QueryLog_getRangeStartTime.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2101
for _lib in _libs.values():
    if not _lib.has("QueryLog_getRangeStopTime", "cdecl"):
        continue
    QueryLog_getRangeStopTime = _lib.get("QueryLog_getRangeStopTime", "cdecl")
    QueryLog_getRangeStopTime.argtypes = [QueryLog]
    QueryLog_getRangeStopTime.restype = CP56Time2a
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2104
for _lib in _libs.values():
    if not _lib.has("QueryLog_destroy", "cdecl"):
        continue
    QueryLog_destroy = _lib.get("QueryLog_destroy", "cdecl")
    QueryLog_destroy.argtypes = [QueryLog]
    QueryLog_destroy.restype = None
    break

CS101_ASDUReceivedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), c_int, CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_master.h: 53

# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42
class struct_sLinkLayerParameters(Structure):
    pass

LinkLayerParameters = POINTER(struct_sLinkLayerParameters)# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 40

struct_sLinkLayerParameters.__slots__ = [
    'addressLength',
    'timeoutForAck',
    'timeoutRepeat',
    'useSingleCharACK',
    'timeoutLinkState',
]
struct_sLinkLayerParameters._fields_ = [
    ('addressLength', c_int),
    ('timeoutForAck', c_int),
    ('timeoutRepeat', c_int),
    ('useSingleCharACK', c_bool),
    ('timeoutLinkState', c_int),
]

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55
class struct_sCS101_Master(Structure):
    pass

CS101_Master = POINTER(struct_sCS101_Master)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 68
for _lib in _libs.values():
    if not _lib.has("CS101_Master_create", "cdecl"):
        continue
    CS101_Master_create = _lib.get("CS101_Master_create", "cdecl")
    CS101_Master_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Master_create.restype = CS101_Master
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 82
for _lib in _libs.values():
    if not _lib.has("CS101_Master_createEx", "cdecl"):
        continue
    CS101_Master_createEx = _lib.get("CS101_Master_createEx", "cdecl")
    CS101_Master_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int]
    CS101_Master_createEx.restype = CS101_Master
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 92
for _lib in _libs.values():
    if not _lib.has("CS101_Master_run", "cdecl"):
        continue
    CS101_Master_run = _lib.get("CS101_Master_run", "cdecl")
    CS101_Master_run.argtypes = [CS101_Master]
    CS101_Master_run.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 104
for _lib in _libs.values():
    if not _lib.has("CS101_Master_start", "cdecl"):
        continue
    CS101_Master_start = _lib.get("CS101_Master_start", "cdecl")
    CS101_Master_start.argtypes = [CS101_Master]
    CS101_Master_start.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 112
for _lib in _libs.values():
    if not _lib.has("CS101_Master_stop", "cdecl"):
        continue
    CS101_Master_stop = _lib.get("CS101_Master_stop", "cdecl")
    CS101_Master_stop.argtypes = [CS101_Master]
    CS101_Master_stop.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 124
for _lib in _libs.values():
    if not _lib.has("CS101_Master_addSlave", "cdecl"):
        continue
    CS101_Master_addSlave = _lib.get("CS101_Master_addSlave", "cdecl")
    CS101_Master_addSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_addSlave.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 138
for _lib in _libs.values():
    if not _lib.has("CS101_Master_pollSingleSlave", "cdecl"):
        continue
    CS101_Master_pollSingleSlave = _lib.get("CS101_Master_pollSingleSlave", "cdecl")
    CS101_Master_pollSingleSlave.argtypes = [CS101_Master, c_int]
    CS101_Master_pollSingleSlave.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 144
for _lib in _libs.values():
    if not _lib.has("CS101_Master_destroy", "cdecl"):
        continue
    CS101_Master_destroy = _lib.get("CS101_Master_destroy", "cdecl")
    CS101_Master_destroy.argtypes = [CS101_Master]
    CS101_Master_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 155
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setDIR", "cdecl"):
        continue
    CS101_Master_setDIR = _lib.get("CS101_Master_setDIR", "cdecl")
    CS101_Master_setDIR.argtypes = [CS101_Master, c_bool]
    CS101_Master_setDIR.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 163
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setOwnAddress", "cdecl"):
        continue
    CS101_Master_setOwnAddress = _lib.get("CS101_Master_setOwnAddress", "cdecl")
    CS101_Master_setOwnAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_setOwnAddress.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 175
for _lib in _libs.values():
    if not _lib.has("CS101_Master_useSlaveAddress", "cdecl"):
        continue
    CS101_Master_useSlaveAddress = _lib.get("CS101_Master_useSlaveAddress", "cdecl")
    CS101_Master_useSlaveAddress.argtypes = [CS101_Master, c_int]
    CS101_Master_useSlaveAddress.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 185
for _lib in _libs.values():
    if not _lib.has("CS101_Master_getAppLayerParameters", "cdecl"):
        continue
    CS101_Master_getAppLayerParameters = _lib.get("CS101_Master_getAppLayerParameters", "cdecl")
    CS101_Master_getAppLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getAppLayerParameters.restype = CS101_AppLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 193
for _lib in _libs.values():
    if not _lib.has("CS101_Master_getLinkLayerParameters", "cdecl"):
        continue
    CS101_Master_getLinkLayerParameters = _lib.get("CS101_Master_getLinkLayerParameters", "cdecl")
    CS101_Master_getLinkLayerParameters.argtypes = [CS101_Master]
    CS101_Master_getLinkLayerParameters.restype = LinkLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 206
for _lib in _libs.values():
    if not _lib.has("CS101_Master_isChannelReady", "cdecl"):
        continue
    CS101_Master_isChannelReady = _lib.get("CS101_Master_isChannelReady", "cdecl")
    CS101_Master_isChannelReady.argtypes = [CS101_Master, c_int]
    CS101_Master_isChannelReady.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 215
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendLinkLayerTestFunction", "cdecl"):
        continue
    CS101_Master_sendLinkLayerTestFunction = _lib.get("CS101_Master_sendLinkLayerTestFunction", "cdecl")
    CS101_Master_sendLinkLayerTestFunction.argtypes = [CS101_Master]
    CS101_Master_sendLinkLayerTestFunction.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 225
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendInterrogationCommand", "cdecl"):
        continue
    CS101_Master_sendInterrogationCommand = _lib.get("CS101_Master_sendInterrogationCommand", "cdecl")
    CS101_Master_sendInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS101_Master_sendInterrogationCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 235
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendCounterInterrogationCommand", "cdecl"):
        continue
    CS101_Master_sendCounterInterrogationCommand = _lib.get("CS101_Master_sendCounterInterrogationCommand", "cdecl")
    CS101_Master_sendCounterInterrogationCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, uint8_t]
    CS101_Master_sendCounterInterrogationCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 247
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendReadCommand", "cdecl"):
        continue
    CS101_Master_sendReadCommand = _lib.get("CS101_Master_sendReadCommand", "cdecl")
    CS101_Master_sendReadCommand.argtypes = [CS101_Master, c_int, c_int]
    CS101_Master_sendReadCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 256
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendClockSyncCommand", "cdecl"):
        continue
    CS101_Master_sendClockSyncCommand = _lib.get("CS101_Master_sendClockSyncCommand", "cdecl")
    CS101_Master_sendClockSyncCommand.argtypes = [CS101_Master, c_int, CP56Time2a]
    CS101_Master_sendClockSyncCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 266
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendTestCommand", "cdecl"):
        continue
    CS101_Master_sendTestCommand = _lib.get("CS101_Master_sendTestCommand", "cdecl")
    CS101_Master_sendTestCommand.argtypes = [CS101_Master, c_int]
    CS101_Master_sendTestCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 277
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendProcessCommand", "cdecl"):
        continue
    CS101_Master_sendProcessCommand = _lib.get("CS101_Master_sendProcessCommand", "cdecl")
    CS101_Master_sendProcessCommand.argtypes = [CS101_Master, CS101_CauseOfTransmission, c_int, InformationObject]
    CS101_Master_sendProcessCommand.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 293
for _lib in _libs.values():
    if not _lib.has("CS101_Master_sendASDU", "cdecl"):
        continue
    CS101_Master_sendASDU = _lib.get("CS101_Master_sendASDU", "cdecl")
    CS101_Master_sendASDU.argtypes = [CS101_Master, CS101_ASDU]
    CS101_Master_sendASDU.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 302
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setASDUReceivedHandler", "cdecl"):
        continue
    CS101_Master_setASDUReceivedHandler = _lib.get("CS101_Master_setASDUReceivedHandler", "cdecl")
    CS101_Master_setASDUReceivedHandler.argtypes = [CS101_Master, CS101_ASDUReceivedHandler, POINTER(None)]
    CS101_Master_setASDUReceivedHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 308
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setLinkLayerStateChanged", "cdecl"):
        continue
    CS101_Master_setLinkLayerStateChanged = _lib.get("CS101_Master_setLinkLayerStateChanged", "cdecl")
    CS101_Master_setLinkLayerStateChanged.argtypes = [CS101_Master, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Master_setLinkLayerStateChanged.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 317
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setRawMessageHandler", "cdecl"):
        continue
    CS101_Master_setRawMessageHandler = _lib.get("CS101_Master_setRawMessageHandler", "cdecl")
    CS101_Master_setRawMessageHandler.argtypes = [CS101_Master, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Master_setRawMessageHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 328
for _lib in _libs.values():
    if not _lib.has("CS101_Master_setIdleTimeout", "cdecl"):
        continue
    CS101_Master_setIdleTimeout = _lib.get("CS101_Master_setIdleTimeout", "cdecl")
    CS101_Master_setIdleTimeout.argtypes = [CS101_Master, c_int]
    CS101_Master_setIdleTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 65
class struct_sIMasterConnection(Structure):
    pass

IMasterConnection = POINTER(struct_sIMasterConnection)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 63

struct_sIMasterConnection.__slots__ = [
    'isReady',
    'sendASDU',
    'sendACT_CON',
    'sendACT_TERM',
    'close',
    'getPeerAddress',
    'getApplicationLayerParameters',
    'object',
]
struct_sIMasterConnection._fields_ = [
    ('isReady', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection)),
    ('sendASDU', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU)),
    ('sendACT_CON', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU, c_bool)),
    ('sendACT_TERM', CFUNCTYPE(UNCHECKED(c_bool), IMasterConnection, CS101_ASDU)),
    ('close', CFUNCTYPE(UNCHECKED(None), IMasterConnection)),
    ('getPeerAddress', CFUNCTYPE(UNCHECKED(c_int), IMasterConnection, String, c_int)),
    ('getApplicationLayerParameters', CFUNCTYPE(UNCHECKED(CS101_AppLayerParameters), IMasterConnection)),
    ('object', POINTER(None)),
]

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 90
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_isReady", "cdecl"):
        continue
    IMasterConnection_isReady = _lib.get("IMasterConnection_isReady", "cdecl")
    IMasterConnection_isReady.argtypes = [IMasterConnection]
    IMasterConnection_isReady.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 103
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_sendASDU", "cdecl"):
        continue
    IMasterConnection_sendASDU = _lib.get("IMasterConnection_sendASDU", "cdecl")
    IMasterConnection_sendASDU.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendASDU.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 116
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_sendACT_CON", "cdecl"):
        continue
    IMasterConnection_sendACT_CON = _lib.get("IMasterConnection_sendACT_CON", "cdecl")
    IMasterConnection_sendACT_CON.argtypes = [IMasterConnection, CS101_ASDU, c_bool]
    IMasterConnection_sendACT_CON.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 128
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_sendACT_TERM", "cdecl"):
        continue
    IMasterConnection_sendACT_TERM = _lib.get("IMasterConnection_sendACT_TERM", "cdecl")
    IMasterConnection_sendACT_TERM.argtypes = [IMasterConnection, CS101_ASDU]
    IMasterConnection_sendACT_TERM.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 139
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_getPeerAddress", "cdecl"):
        continue
    IMasterConnection_getPeerAddress = _lib.get("IMasterConnection_getPeerAddress", "cdecl")
    IMasterConnection_getPeerAddress.argtypes = [IMasterConnection, String, c_int]
    IMasterConnection_getPeerAddress.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 147
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_close", "cdecl"):
        continue
    IMasterConnection_close = _lib.get("IMasterConnection_close", "cdecl")
    IMasterConnection_close.argtypes = [IMasterConnection]
    IMasterConnection_close.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 153
for _lib in _libs.values():
    if not _lib.has("IMasterConnection_getApplicationLayerParameters", "cdecl"):
        continue
    IMasterConnection_getApplicationLayerParameters = _lib.get("IMasterConnection_getApplicationLayerParameters", "cdecl")
    IMasterConnection_getApplicationLayerParameters.argtypes = [IMasterConnection]
    IMasterConnection_getApplicationLayerParameters.restype = CS101_AppLayerParameters
    break

enum_anon_31 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_NOT_HANDLED = 0# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_HANDLED = 1# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_PLUGIN_RESULT_INVALID_ASDU = 2# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

CS101_SlavePlugin_Result = enum_anon_31# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 171

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 178
class struct_sCS101_SlavePlugin(Structure):
    pass

CS101_SlavePlugin = POINTER(struct_sCS101_SlavePlugin)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 176

struct_sCS101_SlavePlugin.__slots__ = [
    'handleAsdu',
    'runTask',
    'parameter',
]
struct_sCS101_SlavePlugin._fields_ = [
    ('handleAsdu', CFUNCTYPE(UNCHECKED(CS101_SlavePlugin_Result), POINTER(None), IMasterConnection, CS101_ASDU)),
    ('runTask', CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection)),
    ('parameter', POINTER(None)),
]

CS101_ResetCUHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 203

CS101_InterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, uint8_t)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 208

CS101_CounterInterrogationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, QualifierOfCIC)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 213

CS101_ReadHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, c_int)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 218

CS101_ClockSynchronizationHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP56Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 233

CS101_ResetProcessHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, uint8_t)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 238

CS101_DelayAcquisitionHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU, CP16Time2a)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 243

CS101_ASDUHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), IMasterConnection, CS101_ASDU)# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 248

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59
class struct_sCS101_Slave(Structure):
    pass

CS101_Slave = POINTER(struct_sCS101_Slave)# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 75
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_create", "cdecl"):
        continue
    CS101_Slave_create = _lib.get("CS101_Slave_create", "cdecl")
    CS101_Slave_create.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode]
    CS101_Slave_create.restype = CS101_Slave
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 92
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_createEx", "cdecl"):
        continue
    CS101_Slave_createEx = _lib.get("CS101_Slave_createEx", "cdecl")
    CS101_Slave_createEx.argtypes = [SerialPort, LinkLayerParameters, CS101_AppLayerParameters, IEC60870_LinkLayerMode, c_int, c_int]
    CS101_Slave_createEx.restype = CS101_Slave
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 101
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_destroy", "cdecl"):
        continue
    CS101_Slave_destroy = _lib.get("CS101_Slave_destroy", "cdecl")
    CS101_Slave_destroy.argtypes = [CS101_Slave]
    CS101_Slave_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 112
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setDIR", "cdecl"):
        continue
    CS101_Slave_setDIR = _lib.get("CS101_Slave_setDIR", "cdecl")
    CS101_Slave_setDIR.argtypes = [CS101_Slave, c_bool]
    CS101_Slave_setDIR.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 120
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_addPlugin", "cdecl"):
        continue
    CS101_Slave_addPlugin = _lib.get("CS101_Slave_addPlugin", "cdecl")
    CS101_Slave_addPlugin.argtypes = [CS101_Slave, CS101_SlavePlugin]
    CS101_Slave_addPlugin.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 131
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setIdleTimeout", "cdecl"):
        continue
    CS101_Slave_setIdleTimeout = _lib.get("CS101_Slave_setIdleTimeout", "cdecl")
    CS101_Slave_setIdleTimeout.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setIdleTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 137
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setLinkLayerStateChanged", "cdecl"):
        continue
    CS101_Slave_setLinkLayerStateChanged = _lib.get("CS101_Slave_setLinkLayerStateChanged", "cdecl")
    CS101_Slave_setLinkLayerStateChanged.argtypes = [CS101_Slave, IEC60870_LinkLayerStateChangedHandler, POINTER(None)]
    CS101_Slave_setLinkLayerStateChanged.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 147
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setLinkLayerAddress", "cdecl"):
        continue
    CS101_Slave_setLinkLayerAddress = _lib.get("CS101_Slave_setLinkLayerAddress", "cdecl")
    CS101_Slave_setLinkLayerAddress.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddress.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 156
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl"):
        continue
    CS101_Slave_setLinkLayerAddressOtherStation = _lib.get("CS101_Slave_setLinkLayerAddressOtherStation", "cdecl")
    CS101_Slave_setLinkLayerAddressOtherStation.argtypes = [CS101_Slave, c_int]
    CS101_Slave_setLinkLayerAddressOtherStation.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 166
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_isClass1QueueFull", "cdecl"):
        continue
    CS101_Slave_isClass1QueueFull = _lib.get("CS101_Slave_isClass1QueueFull", "cdecl")
    CS101_Slave_isClass1QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass1QueueFull.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 175
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_enqueueUserDataClass1", "cdecl"):
        continue
    CS101_Slave_enqueueUserDataClass1 = _lib.get("CS101_Slave_enqueueUserDataClass1", "cdecl")
    CS101_Slave_enqueueUserDataClass1.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass1.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 185
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_isClass2QueueFull", "cdecl"):
        continue
    CS101_Slave_isClass2QueueFull = _lib.get("CS101_Slave_isClass2QueueFull", "cdecl")
    CS101_Slave_isClass2QueueFull.argtypes = [CS101_Slave]
    CS101_Slave_isClass2QueueFull.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 194
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_enqueueUserDataClass2", "cdecl"):
        continue
    CS101_Slave_enqueueUserDataClass2 = _lib.get("CS101_Slave_enqueueUserDataClass2", "cdecl")
    CS101_Slave_enqueueUserDataClass2.argtypes = [CS101_Slave, CS101_ASDU]
    CS101_Slave_enqueueUserDataClass2.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 202
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_flushQueues", "cdecl"):
        continue
    CS101_Slave_flushQueues = _lib.get("CS101_Slave_flushQueues", "cdecl")
    CS101_Slave_flushQueues.argtypes = [CS101_Slave]
    CS101_Slave_flushQueues.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 213
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_run", "cdecl"):
        continue
    CS101_Slave_run = _lib.get("CS101_Slave_run", "cdecl")
    CS101_Slave_run.argtypes = [CS101_Slave]
    CS101_Slave_run.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 225
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_start", "cdecl"):
        continue
    CS101_Slave_start = _lib.get("CS101_Slave_start", "cdecl")
    CS101_Slave_start.argtypes = [CS101_Slave]
    CS101_Slave_start.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 233
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_stop", "cdecl"):
        continue
    CS101_Slave_stop = _lib.get("CS101_Slave_stop", "cdecl")
    CS101_Slave_stop.argtypes = [CS101_Slave]
    CS101_Slave_stop.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 243
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_getAppLayerParameters", "cdecl"):
        continue
    CS101_Slave_getAppLayerParameters = _lib.get("CS101_Slave_getAppLayerParameters", "cdecl")
    CS101_Slave_getAppLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 253
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_getLinkLayerParameters", "cdecl"):
        continue
    CS101_Slave_getLinkLayerParameters = _lib.get("CS101_Slave_getLinkLayerParameters", "cdecl")
    CS101_Slave_getLinkLayerParameters.argtypes = [CS101_Slave]
    CS101_Slave_getLinkLayerParameters.restype = LinkLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 262
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setResetCUHandler", "cdecl"):
        continue
    CS101_Slave_setResetCUHandler = _lib.get("CS101_Slave_setResetCUHandler", "cdecl")
    CS101_Slave_setResetCUHandler.argtypes = [CS101_Slave, CS101_ResetCUHandler, POINTER(None)]
    CS101_Slave_setResetCUHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 271
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setInterrogationHandler", "cdecl"):
        continue
    CS101_Slave_setInterrogationHandler = _lib.get("CS101_Slave_setInterrogationHandler", "cdecl")
    CS101_Slave_setInterrogationHandler.argtypes = [CS101_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS101_Slave_setInterrogationHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 280
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setCounterInterrogationHandler", "cdecl"):
        continue
    CS101_Slave_setCounterInterrogationHandler = _lib.get("CS101_Slave_setCounterInterrogationHandler", "cdecl")
    CS101_Slave_setCounterInterrogationHandler.argtypes = [CS101_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS101_Slave_setCounterInterrogationHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 289
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setReadHandler", "cdecl"):
        continue
    CS101_Slave_setReadHandler = _lib.get("CS101_Slave_setReadHandler", "cdecl")
    CS101_Slave_setReadHandler.argtypes = [CS101_Slave, CS101_ReadHandler, POINTER(None)]
    CS101_Slave_setReadHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 298
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setClockSyncHandler", "cdecl"):
        continue
    CS101_Slave_setClockSyncHandler = _lib.get("CS101_Slave_setClockSyncHandler", "cdecl")
    CS101_Slave_setClockSyncHandler.argtypes = [CS101_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS101_Slave_setClockSyncHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 307
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setResetProcessHandler", "cdecl"):
        continue
    CS101_Slave_setResetProcessHandler = _lib.get("CS101_Slave_setResetProcessHandler", "cdecl")
    CS101_Slave_setResetProcessHandler.argtypes = [CS101_Slave, CS101_ResetProcessHandler, POINTER(None)]
    CS101_Slave_setResetProcessHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 316
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setDelayAcquisitionHandler", "cdecl"):
        continue
    CS101_Slave_setDelayAcquisitionHandler = _lib.get("CS101_Slave_setDelayAcquisitionHandler", "cdecl")
    CS101_Slave_setDelayAcquisitionHandler.argtypes = [CS101_Slave, CS101_DelayAcquisitionHandler, POINTER(None)]
    CS101_Slave_setDelayAcquisitionHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 328
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setASDUHandler", "cdecl"):
        continue
    CS101_Slave_setASDUHandler = _lib.get("CS101_Slave_setASDUHandler", "cdecl")
    CS101_Slave_setASDUHandler.argtypes = [CS101_Slave, CS101_ASDUHandler, POINTER(None)]
    CS101_Slave_setASDUHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 337
for _lib in _libs.values():
    if not _lib.has("CS101_Slave_setRawMessageHandler", "cdecl"):
        continue
    CS101_Slave_setRawMessageHandler = _lib.get("CS101_Slave_setRawMessageHandler", "cdecl")
    CS101_Slave_setRawMessageHandler.argtypes = [CS101_Slave, IEC60870_RawMessageHandler, POINTER(None)]
    CS101_Slave_setRawMessageHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52
class struct_sCS104_Connection(Structure):
    pass

CS104_Connection = POINTER(struct_sCS104_Connection)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 63
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_create", "cdecl"):
        continue
    CS104_Connection_create = _lib.get("CS104_Connection_create", "cdecl")
    CS104_Connection_create.argtypes = [String, c_int]
    CS104_Connection_create.restype = CS104_Connection
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 75
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_createSecure", "cdecl"):
        continue
    CS104_Connection_createSecure = _lib.get("CS104_Connection_createSecure", "cdecl")
    CS104_Connection_createSecure.argtypes = [String, c_int, TLSConfiguration]
    CS104_Connection_createSecure.restype = CS104_Connection
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 88
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setLocalAddress", "cdecl"):
        continue
    CS104_Connection_setLocalAddress = _lib.get("CS104_Connection_setLocalAddress", "cdecl")
    CS104_Connection_setLocalAddress.argtypes = [CS104_Connection, String, c_int]
    CS104_Connection_setLocalAddress.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 101
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setAPCIParameters", "cdecl"):
        continue
    CS104_Connection_setAPCIParameters = _lib.get("CS104_Connection_setAPCIParameters", "cdecl")
    CS104_Connection_setAPCIParameters.argtypes = [CS104_Connection, CS104_APCIParameters]
    CS104_Connection_setAPCIParameters.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 107
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_getAPCIParameters", "cdecl"):
        continue
    CS104_Connection_getAPCIParameters = _lib.get("CS104_Connection_getAPCIParameters", "cdecl")
    CS104_Connection_getAPCIParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAPCIParameters.restype = CS104_APCIParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 120
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setAppLayerParameters", "cdecl"):
        continue
    CS104_Connection_setAppLayerParameters = _lib.get("CS104_Connection_setAppLayerParameters", "cdecl")
    CS104_Connection_setAppLayerParameters.argtypes = [CS104_Connection, CS101_AppLayerParameters]
    CS104_Connection_setAppLayerParameters.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 132
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_getAppLayerParameters", "cdecl"):
        continue
    CS104_Connection_getAppLayerParameters = _lib.get("CS104_Connection_getAppLayerParameters", "cdecl")
    CS104_Connection_getAppLayerParameters.argtypes = [CS104_Connection]
    CS104_Connection_getAppLayerParameters.restype = CS101_AppLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 143
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setConnectTimeout", "cdecl"):
        continue
    CS104_Connection_setConnectTimeout = _lib.get("CS104_Connection_setConnectTimeout", "cdecl")
    CS104_Connection_setConnectTimeout.argtypes = [CS104_Connection, c_int]
    CS104_Connection_setConnectTimeout.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 153
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_connectAsync", "cdecl"):
        continue
    CS104_Connection_connectAsync = _lib.get("CS104_Connection_connectAsync", "cdecl")
    CS104_Connection_connectAsync.argtypes = [CS104_Connection]
    CS104_Connection_connectAsync.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 165
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_connect", "cdecl"):
        continue
    CS104_Connection_connect = _lib.get("CS104_Connection_connect", "cdecl")
    CS104_Connection_connect.argtypes = [CS104_Connection]
    CS104_Connection_connect.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 174
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendStartDT", "cdecl"):
        continue
    CS104_Connection_sendStartDT = _lib.get("CS104_Connection_sendStartDT", "cdecl")
    CS104_Connection_sendStartDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStartDT.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 180
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendStopDT", "cdecl"):
        continue
    CS104_Connection_sendStopDT = _lib.get("CS104_Connection_sendStopDT", "cdecl")
    CS104_Connection_sendStopDT.argtypes = [CS104_Connection]
    CS104_Connection_sendStopDT.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 190
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_isTransmitBufferFull", "cdecl"):
        continue
    CS104_Connection_isTransmitBufferFull = _lib.get("CS104_Connection_isTransmitBufferFull", "cdecl")
    CS104_Connection_isTransmitBufferFull.argtypes = [CS104_Connection]
    CS104_Connection_isTransmitBufferFull.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 202
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendInterrogationCommand", "cdecl"):
        continue
    CS104_Connection_sendInterrogationCommand = _lib.get("CS104_Connection_sendInterrogationCommand", "cdecl")
    CS104_Connection_sendInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, QualifierOfInterrogation]
    CS104_Connection_sendInterrogationCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 214
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendCounterInterrogationCommand", "cdecl"):
        continue
    CS104_Connection_sendCounterInterrogationCommand = _lib.get("CS104_Connection_sendCounterInterrogationCommand", "cdecl")
    CS104_Connection_sendCounterInterrogationCommand.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, uint8_t]
    CS104_Connection_sendCounterInterrogationCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 228
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendReadCommand", "cdecl"):
        continue
    CS104_Connection_sendReadCommand = _lib.get("CS104_Connection_sendReadCommand", "cdecl")
    CS104_Connection_sendReadCommand.argtypes = [CS104_Connection, c_int, c_int]
    CS104_Connection_sendReadCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 239
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendClockSyncCommand", "cdecl"):
        continue
    CS104_Connection_sendClockSyncCommand = _lib.get("CS104_Connection_sendClockSyncCommand", "cdecl")
    CS104_Connection_sendClockSyncCommand.argtypes = [CS104_Connection, c_int, CP56Time2a]
    CS104_Connection_sendClockSyncCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 251
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendTestCommand", "cdecl"):
        continue
    CS104_Connection_sendTestCommand = _lib.get("CS104_Connection_sendTestCommand", "cdecl")
    CS104_Connection_sendTestCommand.argtypes = [CS104_Connection, c_int]
    CS104_Connection_sendTestCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 263
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendTestCommandWithTimestamp", "cdecl"):
        continue
    CS104_Connection_sendTestCommandWithTimestamp = _lib.get("CS104_Connection_sendTestCommandWithTimestamp", "cdecl")
    CS104_Connection_sendTestCommandWithTimestamp.argtypes = [CS104_Connection, c_int, uint16_t, CP56Time2a]
    CS104_Connection_sendTestCommandWithTimestamp.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 278
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendProcessCommand", "cdecl"):
        continue
    CS104_Connection_sendProcessCommand = _lib.get("CS104_Connection_sendProcessCommand", "cdecl")
    CS104_Connection_sendProcessCommand.argtypes = [CS104_Connection, TypeID, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommand.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 291
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendProcessCommandEx", "cdecl"):
        continue
    CS104_Connection_sendProcessCommandEx = _lib.get("CS104_Connection_sendProcessCommandEx", "cdecl")
    CS104_Connection_sendProcessCommandEx.argtypes = [CS104_Connection, CS101_CauseOfTransmission, c_int, InformationObject]
    CS104_Connection_sendProcessCommandEx.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 302
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendASDU", "cdecl"):
        continue
    CS104_Connection_sendASDU = _lib.get("CS104_Connection_sendASDU", "cdecl")
    CS104_Connection_sendASDU.argtypes = [CS104_Connection, CS101_ASDU]
    CS104_Connection_sendASDU.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 311
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setASDUReceivedHandler", "cdecl"):
        continue
    CS104_Connection_setASDUReceivedHandler = _lib.get("CS104_Connection_setASDUReceivedHandler", "cdecl")
    CS104_Connection_setASDUReceivedHandler.argtypes = [CS104_Connection, CS101_ASDUReceivedHandler, POINTER(None)]
    CS104_Connection_setASDUReceivedHandler.restype = None
    break

enum_anon_32 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_CONNECTION_OPENED = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_CONNECTION_CLOSED = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_CONNECTION_STARTDT_CON_RECEIVED = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_CONNECTION_STOPDT_CON_RECEIVED = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_CONNECTION_FAILED = 4# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_ConnectionEvent = enum_anon_32# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 319

CS104_ConnectionHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), CS104_Connection, CS104_ConnectionEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 331

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 340
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setConnectionHandler", "cdecl"):
        continue
    CS104_Connection_setConnectionHandler = _lib.get("CS104_Connection_setConnectionHandler", "cdecl")
    CS104_Connection_setConnectionHandler.argtypes = [CS104_Connection, CS104_ConnectionHandler, POINTER(None)]
    CS104_Connection_setConnectionHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 350
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_setRawMessageHandler", "cdecl"):
        continue
    CS104_Connection_setRawMessageHandler = _lib.get("CS104_Connection_setRawMessageHandler", "cdecl")
    CS104_Connection_setRawMessageHandler.argtypes = [CS104_Connection, IEC60870_RawMessageHandler, POINTER(None)]
    CS104_Connection_setRawMessageHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 356
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_close", "cdecl"):
        continue
    CS104_Connection_close = _lib.get("CS104_Connection_close", "cdecl")
    CS104_Connection_close.argtypes = [CS104_Connection]
    CS104_Connection_close.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 362
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_destroy", "cdecl"):
        continue
    CS104_Connection_destroy = _lib.get("CS104_Connection_destroy", "cdecl")
    CS104_Connection_destroy.argtypes = [CS104_Connection]
    CS104_Connection_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 375
for _lib in _libs.values():
    if not _lib.has("CS104_Connection_sendMessage", "cdecl"):
        continue
    CS104_Connection_sendMessage = _lib.get("CS104_Connection_sendMessage", "cdecl")
    CS104_Connection_sendMessage.argtypes = [CS104_Connection, POINTER(uint8_t), c_int]
    CS104_Connection_sendMessage.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50
class struct_sCS104_Slave(Structure):
    pass

CS104_Slave = POINTER(struct_sCS104_Slave)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50

enum_anon_33 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_SINGLE_REDUNDANCY_GROUP = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP = (CS104_MODE_SINGLE_REDUNDANCY_GROUP + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_MODE_MULTIPLE_REDUNDANCY_GROUPS = (CS104_MODE_CONNECTION_IS_REDUNDANCY_GROUP + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

CS104_ServerMode = enum_anon_33# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 56

enum_anon_34 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

IP_ADDRESS_TYPE_IPV4 = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

IP_ADDRESS_TYPE_IPV6 = (IP_ADDRESS_TYPE_IPV4 + 1)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

eCS104_IPAddressType = enum_anon_34# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 62

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64
class struct_sCS104_RedundancyGroup(Structure):
    pass

CS104_RedundancyGroup = POINTER(struct_sCS104_RedundancyGroup)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64

CS104_ConnectionRequestHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), String)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 74

enum_anon_35 = c_int# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_CONNECTION_OPENED = 0# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_CONNECTION_CLOSED = 1# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_ACTIVATED = 2# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_CON_EVENT_DEACTIVATED = 3# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_PeerConnectionEvent = enum_anon_35# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 81

CS104_ConnectionEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, CS104_PeerConnectionEvent)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 91

CS104_SlaveRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IMasterConnection, POINTER(uint8_t), c_int, c_bool)# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 106

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 118
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_create", "cdecl"):
        continue
    CS104_Slave_create = _lib.get("CS104_Slave_create", "cdecl")
    CS104_Slave_create.argtypes = [c_int, c_int]
    CS104_Slave_create.restype = CS104_Slave
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 130
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_createSecure", "cdecl"):
        continue
    CS104_Slave_createSecure = _lib.get("CS104_Slave_createSecure", "cdecl")
    CS104_Slave_createSecure.argtypes = [c_int, c_int, TLSConfiguration]
    CS104_Slave_createSecure.restype = CS104_Slave
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 133
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_addPlugin", "cdecl"):
        continue
    CS104_Slave_addPlugin = _lib.get("CS104_Slave_addPlugin", "cdecl")
    CS104_Slave_addPlugin.argtypes = [CS104_Slave, CS101_SlavePlugin]
    CS104_Slave_addPlugin.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 143
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setLocalAddress", "cdecl"):
        continue
    CS104_Slave_setLocalAddress = _lib.get("CS104_Slave_setLocalAddress", "cdecl")
    CS104_Slave_setLocalAddress.argtypes = [CS104_Slave, String]
    CS104_Slave_setLocalAddress.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 152
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setLocalPort", "cdecl"):
        continue
    CS104_Slave_setLocalPort = _lib.get("CS104_Slave_setLocalPort", "cdecl")
    CS104_Slave_setLocalPort.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setLocalPort.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 160
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_getOpenConnections", "cdecl"):
        continue
    CS104_Slave_getOpenConnections = _lib.get("CS104_Slave_getOpenConnections", "cdecl")
    CS104_Slave_getOpenConnections.argtypes = [CS104_Slave]
    CS104_Slave_getOpenConnections.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 171
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setMaxOpenConnections", "cdecl"):
        continue
    CS104_Slave_setMaxOpenConnections = _lib.get("CS104_Slave_setMaxOpenConnections", "cdecl")
    CS104_Slave_setMaxOpenConnections.argtypes = [CS104_Slave, c_int]
    CS104_Slave_setMaxOpenConnections.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 180
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setServerMode", "cdecl"):
        continue
    CS104_Slave_setServerMode = _lib.get("CS104_Slave_setServerMode", "cdecl")
    CS104_Slave_setServerMode.argtypes = [CS104_Slave, CS104_ServerMode]
    CS104_Slave_setServerMode.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 194
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setConnectionRequestHandler", "cdecl"):
        continue
    CS104_Slave_setConnectionRequestHandler = _lib.get("CS104_Slave_setConnectionRequestHandler", "cdecl")
    CS104_Slave_setConnectionRequestHandler.argtypes = [CS104_Slave, CS104_ConnectionRequestHandler, POINTER(None)]
    CS104_Slave_setConnectionRequestHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 207
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setConnectionEventHandler", "cdecl"):
        continue
    CS104_Slave_setConnectionEventHandler = _lib.get("CS104_Slave_setConnectionEventHandler", "cdecl")
    CS104_Slave_setConnectionEventHandler.argtypes = [CS104_Slave, CS104_ConnectionEventHandler, POINTER(None)]
    CS104_Slave_setConnectionEventHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 210
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setInterrogationHandler", "cdecl"):
        continue
    CS104_Slave_setInterrogationHandler = _lib.get("CS104_Slave_setInterrogationHandler", "cdecl")
    CS104_Slave_setInterrogationHandler.argtypes = [CS104_Slave, CS101_InterrogationHandler, POINTER(None)]
    CS104_Slave_setInterrogationHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 213
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setCounterInterrogationHandler", "cdecl"):
        continue
    CS104_Slave_setCounterInterrogationHandler = _lib.get("CS104_Slave_setCounterInterrogationHandler", "cdecl")
    CS104_Slave_setCounterInterrogationHandler.argtypes = [CS104_Slave, CS101_CounterInterrogationHandler, POINTER(None)]
    CS104_Slave_setCounterInterrogationHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 219
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setReadHandler", "cdecl"):
        continue
    CS104_Slave_setReadHandler = _lib.get("CS104_Slave_setReadHandler", "cdecl")
    CS104_Slave_setReadHandler.argtypes = [CS104_Slave, CS101_ReadHandler, POINTER(None)]
    CS104_Slave_setReadHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 222
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setASDUHandler", "cdecl"):
        continue
    CS104_Slave_setASDUHandler = _lib.get("CS104_Slave_setASDUHandler", "cdecl")
    CS104_Slave_setASDUHandler.argtypes = [CS104_Slave, CS101_ASDUHandler, POINTER(None)]
    CS104_Slave_setASDUHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 225
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setClockSyncHandler", "cdecl"):
        continue
    CS104_Slave_setClockSyncHandler = _lib.get("CS104_Slave_setClockSyncHandler", "cdecl")
    CS104_Slave_setClockSyncHandler.argtypes = [CS104_Slave, CS101_ClockSynchronizationHandler, POINTER(None)]
    CS104_Slave_setClockSyncHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 234
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_setRawMessageHandler", "cdecl"):
        continue
    CS104_Slave_setRawMessageHandler = _lib.get("CS104_Slave_setRawMessageHandler", "cdecl")
    CS104_Slave_setRawMessageHandler.argtypes = [CS104_Slave, CS104_SlaveRawMessageHandler, POINTER(None)]
    CS104_Slave_setRawMessageHandler.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 240
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_getConnectionParameters", "cdecl"):
        continue
    CS104_Slave_getConnectionParameters = _lib.get("CS104_Slave_getConnectionParameters", "cdecl")
    CS104_Slave_getConnectionParameters.argtypes = [CS104_Slave]
    CS104_Slave_getConnectionParameters.restype = CS104_APCIParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 246
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_getAppLayerParameters", "cdecl"):
        continue
    CS104_Slave_getAppLayerParameters = _lib.get("CS104_Slave_getAppLayerParameters", "cdecl")
    CS104_Slave_getAppLayerParameters.argtypes = [CS104_Slave]
    CS104_Slave_getAppLayerParameters.restype = CS101_AppLayerParameters
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 257
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_start", "cdecl"):
        continue
    CS104_Slave_start = _lib.get("CS104_Slave_start", "cdecl")
    CS104_Slave_start.argtypes = [CS104_Slave]
    CS104_Slave_start.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 267
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_isRunning", "cdecl"):
        continue
    CS104_Slave_isRunning = _lib.get("CS104_Slave_isRunning", "cdecl")
    CS104_Slave_isRunning.argtypes = [CS104_Slave]
    CS104_Slave_isRunning.restype = c_bool
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 276
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_stop", "cdecl"):
        continue
    CS104_Slave_stop = _lib.get("CS104_Slave_stop", "cdecl")
    CS104_Slave_stop.argtypes = [CS104_Slave]
    CS104_Slave_stop.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 286
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_startThreadless", "cdecl"):
        continue
    CS104_Slave_startThreadless = _lib.get("CS104_Slave_startThreadless", "cdecl")
    CS104_Slave_startThreadless.argtypes = [CS104_Slave]
    CS104_Slave_startThreadless.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 295
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_stopThreadless", "cdecl"):
        continue
    CS104_Slave_stopThreadless = _lib.get("CS104_Slave_stopThreadless", "cdecl")
    CS104_Slave_stopThreadless.argtypes = [CS104_Slave]
    CS104_Slave_stopThreadless.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 306
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_tick", "cdecl"):
        continue
    CS104_Slave_tick = _lib.get("CS104_Slave_tick", "cdecl")
    CS104_Slave_tick.argtypes = [CS104_Slave]
    CS104_Slave_tick.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 318
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_getNumberOfQueueEntries", "cdecl"):
        continue
    CS104_Slave_getNumberOfQueueEntries = _lib.get("CS104_Slave_getNumberOfQueueEntries", "cdecl")
    CS104_Slave_getNumberOfQueueEntries.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_getNumberOfQueueEntries.restype = c_int
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 326
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_enqueueASDU", "cdecl"):
        continue
    CS104_Slave_enqueueASDU = _lib.get("CS104_Slave_enqueueASDU", "cdecl")
    CS104_Slave_enqueueASDU.argtypes = [CS104_Slave, CS101_ASDU]
    CS104_Slave_enqueueASDU.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 339
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_addRedundancyGroup", "cdecl"):
        continue
    CS104_Slave_addRedundancyGroup = _lib.get("CS104_Slave_addRedundancyGroup", "cdecl")
    CS104_Slave_addRedundancyGroup.argtypes = [CS104_Slave, CS104_RedundancyGroup]
    CS104_Slave_addRedundancyGroup.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 345
for _lib in _libs.values():
    if not _lib.has("CS104_Slave_destroy", "cdecl"):
        continue
    CS104_Slave_destroy = _lib.get("CS104_Slave_destroy", "cdecl")
    CS104_Slave_destroy.argtypes = [CS104_Slave]
    CS104_Slave_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 354
for _lib in _libs.values():
    if not _lib.has("CS104_RedundancyGroup_create", "cdecl"):
        continue
    CS104_RedundancyGroup_create = _lib.get("CS104_RedundancyGroup_create", "cdecl")
    CS104_RedundancyGroup_create.argtypes = [String]
    CS104_RedundancyGroup_create.restype = CS104_RedundancyGroup
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 362
for _lib in _libs.values():
    if not _lib.has("CS104_RedundancyGroup_addAllowedClient", "cdecl"):
        continue
    CS104_RedundancyGroup_addAllowedClient = _lib.get("CS104_RedundancyGroup_addAllowedClient", "cdecl")
    CS104_RedundancyGroup_addAllowedClient.argtypes = [CS104_RedundancyGroup, String]
    CS104_RedundancyGroup_addAllowedClient.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 371
for _lib in _libs.values():
    if not _lib.has("CS104_RedundancyGroup_addAllowedClientEx", "cdecl"):
        continue
    CS104_RedundancyGroup_addAllowedClientEx = _lib.get("CS104_RedundancyGroup_addAllowedClientEx", "cdecl")
    CS104_RedundancyGroup_addAllowedClientEx.argtypes = [CS104_RedundancyGroup, POINTER(uint8_t), eCS104_IPAddressType]
    CS104_RedundancyGroup_addAllowedClientEx.restype = None
    break

# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 381
for _lib in _libs.values():
    if not _lib.has("CS104_RedundancyGroup_destroy", "cdecl"):
        continue
    CS104_RedundancyGroup_destroy = _lib.get("CS104_RedundancyGroup_destroy", "cdecl")
    CS104_RedundancyGroup_destroy.argtypes = [CS104_RedundancyGroup]
    CS104_RedundancyGroup_destroy.restype = None
    break

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 15
def CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 16
def MALLOC(size):
    return (Memory_malloc (size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 17
def REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 18
def FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 20
def GLOBAL_CALLOC(nmemb, size):
    return (Memory_calloc (nmemb, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 21
def GLOBAL_MALLOC(size):
    return (Memory_malloc (size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 22
def GLOBAL_REALLOC(oldptr, size):
    return (Memory_realloc (oldptr, size))

# /home/user/lib60870/lib60870-C/src/hal/inc/lib_memory.h: 23
def GLOBAL_FREEMEM(ptr):
    return (Memory_free (ptr))

# /home/user/lib60870/lib60870-C/src/hal/inc/platform_endian.h: 34
try:
    ORDER_LITTLE_ENDIAN = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 8
try:
    TLS_NULL_WITH_NULL_NULL = 0x0000
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 9
try:
    TLS_RSA_WITH_NULL_MD5 = 0x0001
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 10
try:
    TLS_RSA_WITH_NULL_SHA = 0x0002
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 11
try:
    TLS_RSA_EXPORT_WITH_RC4_40_MD5 = 0x0003
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 12
try:
    TLS_RSA_WITH_RC4_128_MD5 = 0x0004
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 13
try:
    TLS_RSA_WITH_RC4_128_SHA = 0x0005
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 14
try:
    TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 = 0x0006
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 15
try:
    TLS_RSA_WITH_IDEA_CBC_SHA = 0x0007
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 16
try:
    TLS_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0008
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 17
try:
    TLS_RSA_WITH_DES_CBC_SHA = 0x0009
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 18
try:
    TLS_RSA_WITH_3DES_EDE_CBC_SHA = 0x000A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 19
try:
    TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x000B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 20
try:
    TLS_DH_DSS_WITH_DES_CBC_SHA = 0x000C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 21
try:
    TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA = 0x000D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 22
try:
    TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x000E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 23
try:
    TLS_DH_RSA_WITH_DES_CBC_SHA = 0x000F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 24
try:
    TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA = 0x0010
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 25
try:
    TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA = 0x0011
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 26
try:
    TLS_DHE_DSS_WITH_DES_CBC_SHA = 0x0012
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 27
try:
    TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA = 0x0013
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 28
try:
    TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA = 0x0014
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 29
try:
    TLS_DHE_RSA_WITH_DES_CBC_SHA = 0x0015
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 30
try:
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA = 0x0016
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 31
try:
    TLS_DH_anon_EXPORT_WITH_RC4_40_MD5 = 0x0017
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 32
try:
    TLS_DH_anon_WITH_RC4_128_MD5 = 0x0018
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 33
try:
    TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA = 0x0019
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 34
try:
    TLS_DH_anon_WITH_DES_CBC_SHA = 0x001A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 35
try:
    TLS_DH_anon_WITH_3DES_EDE_CBC_SHA = 0x001B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 36
try:
    TLS_RSA_WITH_AES_128_CBC_SHA = 0x002F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 37
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA = 0x0030
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 38
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA = 0x0031
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 39
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA = 0x0032
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 40
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 0x0033
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 41
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA = 0x0034
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 42
try:
    TLS_RSA_WITH_AES_256_CBC_SHA = 0x0035
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 43
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA = 0x0036
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 44
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA = 0x0037
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 45
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA = 0x0038
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 46
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 0x0039
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 47
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA = 0x003A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 48
try:
    TLS_RSA_WITH_NULL_SHA256 = 0x003B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 49
try:
    TLS_RSA_WITH_AES_128_CBC_SHA256 = 0x003C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 50
try:
    TLS_RSA_WITH_AES_256_CBC_SHA256 = 0x003D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 51
try:
    TLS_DH_DSS_WITH_AES_128_CBC_SHA256 = 0x003E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 52
try:
    TLS_DH_RSA_WITH_AES_128_CBC_SHA256 = 0x003F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 53
try:
    TLS_DHE_DSS_WITH_AES_128_CBC_SHA256 = 0x0040
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 54
try:
    TLS_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0041
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 55
try:
    TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0042
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 56
try:
    TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0043
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 57
try:
    TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA = 0x0044
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 58
try:
    TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA = 0x0045
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 59
try:
    TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA = 0x0046
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 60
try:
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 = 0x0067
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 61
try:
    TLS_DH_DSS_WITH_AES_256_CBC_SHA256 = 0x0068
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 62
try:
    TLS_DH_RSA_WITH_AES_256_CBC_SHA256 = 0x0069
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 63
try:
    TLS_DHE_DSS_WITH_AES_256_CBC_SHA256 = 0x006A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 64
try:
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 = 0x006B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 65
try:
    TLS_DH_anon_WITH_AES_128_CBC_SHA256 = 0x006C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 66
try:
    TLS_DH_anon_WITH_AES_256_CBC_SHA256 = 0x006D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 67
try:
    TLS_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0084
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 68
try:
    TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0085
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 69
try:
    TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0086
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 70
try:
    TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA = 0x0087
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 71
try:
    TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA = 0x0088
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 72
try:
    TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA = 0x0089
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 73
try:
    TLS_RSA_WITH_SEED_CBC_SHA = 0x0096
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 74
try:
    TLS_DH_DSS_WITH_SEED_CBC_SHA = 0x0097
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 75
try:
    TLS_DH_RSA_WITH_SEED_CBC_SHA = 0x0098
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 76
try:
    TLS_DHE_DSS_WITH_SEED_CBC_SHA = 0x0099
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 77
try:
    TLS_DHE_RSA_WITH_SEED_CBC_SHA = 0x009A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 78
try:
    TLS_DH_anon_WITH_SEED_CBC_SHA = 0x009B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 79
try:
    TLS_RSA_WITH_AES_128_GCM_SHA256 = 0x009C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 80
try:
    TLS_RSA_WITH_AES_256_GCM_SHA384 = 0x009D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 81
try:
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 = 0x009E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 82
try:
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 = 0x009F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 83
try:
    TLS_DH_RSA_WITH_AES_128_GCM_SHA256 = 0x00A0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 84
try:
    TLS_DH_RSA_WITH_AES_256_GCM_SHA384 = 0x00A1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 85
try:
    TLS_DHE_DSS_WITH_AES_128_GCM_SHA256 = 0x00A2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 86
try:
    TLS_DHE_DSS_WITH_AES_256_GCM_SHA384 = 0x00A3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 87
try:
    TLS_DH_DSS_WITH_AES_128_GCM_SHA256 = 0x00A4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 88
try:
    TLS_DH_DSS_WITH_AES_256_GCM_SHA384 = 0x00A5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 89
try:
    TLS_DH_anon_WITH_AES_128_GCM_SHA256 = 0x00A6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 90
try:
    TLS_DH_anon_WITH_AES_256_GCM_SHA384 = 0x00A7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 91
try:
    TLS_PSK_WITH_AES_128_CBC_SHA = 0x008C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 92
try:
    TLS_PSK_WITH_AES_256_CBC_SHA = 0x008D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 93
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA = 0x008E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 94
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA = 0x008F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 95
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA = 0x0090
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 96
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA = 0x0091
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 97
try:
    TLS_PSK_WITH_AES_128_CBC_SHA256 = 0x00AE
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 98
try:
    TLS_PSK_WITH_AES_256_CBC_SHA384 = 0x00AF
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 99
try:
    TLS_DHE_PSK_WITH_AES_128_CBC_SHA256 = 0x00B0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 100
try:
    TLS_DHE_PSK_WITH_AES_256_CBC_SHA384 = 0x00B1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 101
try:
    TLS_RSA_PSK_WITH_AES_128_CBC_SHA256 = 0x00B2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 102
try:
    TLS_RSA_PSK_WITH_AES_256_CBC_SHA384 = 0x00B3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 103
try:
    TLS_PSK_WITH_NULL_SHA = 0x002C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 104
try:
    TLS_DHE_PSK_WITH_NULL_SHA = 0x002D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 105
try:
    TLS_RSA_PSK_WITH_NULL_SHA = 0x002E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 106
try:
    TLS_PSK_WITH_NULL_SHA256 = 0x00B4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 107
try:
    TLS_PSK_WITH_NULL_SHA384 = 0x00B5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 108
try:
    TLS_DHE_PSK_WITH_NULL_SHA256 = 0x00B6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 109
try:
    TLS_DHE_PSK_WITH_NULL_SHA384 = 0x00B7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 110
try:
    TLS_RSA_PSK_WITH_NULL_SHA256 = 0x00B8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 111
try:
    TLS_RSA_PSK_WITH_NULL_SHA384 = 0x00B9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 112
try:
    TLS_ECDH_ECDSA_WITH_NULL_SHA = 0xC001
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 113
try:
    TLS_ECDH_ECDSA_WITH_RC4_128_SHA = 0xC002
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 114
try:
    TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC003
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 115
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA = 0xC004
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 116
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA = 0xC005
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 117
try:
    TLS_ECDHE_ECDSA_WITH_NULL_SHA = 0xC006
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 118
try:
    TLS_ECDHE_ECDSA_WITH_RC4_128_SHA = 0xC007
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 119
try:
    TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA = 0xC008
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 120
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 0xC009
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 121
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 0xC00A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 122
try:
    TLS_ECDH_RSA_WITH_NULL_SHA = 0xC00B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 123
try:
    TLS_ECDH_RSA_WITH_RC4_128_SHA = 0xC00C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 124
try:
    TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA = 0xC00D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 125
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA = 0xC00E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 126
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA = 0xC00F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 127
try:
    TLS_ECDHE_RSA_WITH_NULL_SHA = 0xC010
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 128
try:
    TLS_ECDHE_RSA_WITH_RC4_128_SHA = 0xC011
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 129
try:
    TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA = 0xC012
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 130
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 0xC013
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 131
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 0xC014
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 132
try:
    TLS_ECDH_anon_WITH_NULL_SHA = 0xC015
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 133
try:
    TLS_ECDH_anon_WITH_RC4_128_SHA = 0xC016
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 134
try:
    TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA = 0xC017
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 135
try:
    TLS_ECDH_anon_WITH_AES_128_CBC_SHA = 0xC018
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 136
try:
    TLS_ECDH_anon_WITH_AES_256_CBC_SHA = 0xC019
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 137
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC023
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 138
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC024
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 139
try:
    TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256 = 0xC025
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 140
try:
    TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384 = 0xC026
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 141
try:
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 = 0xC027
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 142
try:
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 = 0xC028
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 143
try:
    TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256 = 0xC029
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 144
try:
    TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384 = 0xC02A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 145
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 146
try:
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 147
try:
    TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256 = 0xC02D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 148
try:
    TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 = 0xC02E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 149
try:
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0xC02F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 150
try:
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = 0xC030
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 151
try:
    TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256 = 0xC031
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 152
try:
    TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384 = 0xC032
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 153
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA = 0xC035
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 154
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA = 0xC036
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 155
try:
    TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256 = 0xC037
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 156
try:
    TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384 = 0xC038
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 157
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA = 0xC039
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 158
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA256 = 0xC03A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 159
try:
    TLS_ECDHE_PSK_WITH_NULL_SHA384 = 0xC03B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 160
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC072
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 161
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC073
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 162
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC074
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 163
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC075
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 164
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC076
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 165
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC077
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 166
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 0xC078
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 167
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384 = 0xC079
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 168
try:
    TLS_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC03C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 169
try:
    TLS_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC03D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 170
try:
    TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC03E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 171
try:
    TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC03F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 172
try:
    TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC040
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 173
try:
    TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC041
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 174
try:
    TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256 = 0xC042
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 175
try:
    TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384 = 0xC043
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 176
try:
    TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC044
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 177
try:
    TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC045
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 178
try:
    TLS_DH_anon_WITH_ARIA_128_CBC_SHA256 = 0xC046
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 179
try:
    TLS_DH_anon_WITH_ARIA_256_CBC_SHA384 = 0xC047
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 180
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC048
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 181
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC049
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 182
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256 = 0xC04A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 183
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384 = 0xC04B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 184
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 185
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 186
try:
    TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256 = 0xC04E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 187
try:
    TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384 = 0xC04F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 188
try:
    TLS_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC050
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 189
try:
    TLS_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC051
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 190
try:
    TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC052
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 191
try:
    TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC053
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 192
try:
    TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC054
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 193
try:
    TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC055
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 194
try:
    TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC056
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 195
try:
    TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC057
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 196
try:
    TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256 = 0xC058
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 197
try:
    TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384 = 0xC059
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 198
try:
    TLS_DH_anon_WITH_ARIA_128_GCM_SHA256 = 0xC05A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 199
try:
    TLS_DH_anon_WITH_ARIA_256_GCM_SHA384 = 0xC05B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 200
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 201
try:
    TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 202
try:
    TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256 = 0xC05E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 203
try:
    TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384 = 0xC05F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 204
try:
    TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC060
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 205
try:
    TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC061
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 206
try:
    TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256 = 0xC062
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 207
try:
    TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384 = 0xC063
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 208
try:
    TLS_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC064
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 209
try:
    TLS_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC065
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 210
try:
    TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC066
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 211
try:
    TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC067
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 212
try:
    TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC068
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 213
try:
    TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC069
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 214
try:
    TLS_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 215
try:
    TLS_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 216
try:
    TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 217
try:
    TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 218
try:
    TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256 = 0xC06E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 219
try:
    TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384 = 0xC06F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 220
try:
    TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256 = 0xC070
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 221
try:
    TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384 = 0xC071
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 222
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC076
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 223
try:
    TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC077
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 224
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC078
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 225
try:
    TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC079
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 226
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07A
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 227
try:
    TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07B
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 228
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 229
try:
    TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 230
try:
    TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC07E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 231
try:
    TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC07F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 232
try:
    TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC080
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 233
try:
    TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC081
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 234
try:
    TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC082
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 235
try:
    TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC083
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 236
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_128_GCM_SHA256 = 0xC084
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 237
try:
    TLS_ECDHE_PSK_WITH_CAMELLIA_256_GCM_SHA384 = 0xC085
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 238
try:
    TLS_RSA_WITH_AES_128_CCM = 0xC09C
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 239
try:
    TLS_RSA_WITH_AES_256_CCM = 0xC09D
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 240
try:
    TLS_DHE_RSA_WITH_AES_128_CCM = 0xC09E
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 241
try:
    TLS_DHE_RSA_WITH_AES_256_CCM = 0xC09F
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 242
try:
    TLS_RSA_WITH_AES_128_CCM_8 = 0xC0A0
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 243
try:
    TLS_RSA_WITH_AES_256_CCM_8 = 0xC0A1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 244
try:
    TLS_DHE_RSA_WITH_AES_128_CCM_8 = 0xC0A2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 245
try:
    TLS_DHE_RSA_WITH_AES_256_CCM_8 = 0xC0A3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 246
try:
    TLS_PSK_WITH_AES_128_CCM = 0xC0A4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 247
try:
    TLS_PSK_WITH_AES_256_CCM = 0xC0A5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 248
try:
    TLS_DHE_PSK_WITH_AES_128_CCM = 0xC0A6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 249
try:
    TLS_DHE_PSK_WITH_AES_256_CCM = 0xC0A7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 250
try:
    TLS_PSK_WITH_AES_128_CCM_8 = 0xC0A8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 251
try:
    TLS_PSK_WITH_AES_256_CCM_8 = 0xC0A9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 252
try:
    TLS_PSK_DHE_WITH_AES_128_CCM_8 = 0xC0AA
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 253
try:
    TLS_PSK_DHE_WITH_AES_256_CCM_8 = 0xC0AB
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_ciphers.h: 254
try:
    TLS_ECDHE_ECDSA_WITH_AES_128_CCM = 0xC0AC
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 79
try:
    TLS_EVENT_CODE_ALM_ALGO_NOT_SUPPORTED = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 80
try:
    TLS_EVENT_CODE_ALM_UNSECURE_COMMUNICATION = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 81
try:
    TLS_EVENT_CODE_ALM_CERT_UNAVAILABLE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 82
try:
    TLS_EVENT_CODE_ALM_BAD_CERT = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 83
try:
    TLS_EVENT_CODE_ALM_CERT_SIZE_EXCEEDED = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 84
try:
    TLS_EVENT_CODE_ALM_CERT_VALIDATION_FAILED = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 85
try:
    TLS_EVENT_CODE_ALM_CERT_REQUIRED = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 86
try:
    TLS_EVENT_CODE_ALM_HANDSHAKE_FAILED_UNKNOWN_REASON = 8
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 87
try:
    TLS_EVENT_CODE_WRN_INSECURE_TLS_VERSION = 9
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 88
try:
    TLS_EVENT_CODE_INF_SESSION_RENEGOTIATION = 10
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 89
try:
    TLS_EVENT_CODE_ALM_CERT_EXPIRED = 11
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 90
try:
    TLS_EVENT_CODE_ALM_CERT_REVOKED = 12
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 91
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_CONFIGURED = 13
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 92
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_TRUSTED = 14
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 93
try:
    TLS_EVENT_CODE_ALM_NO_CIPHER = 15
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 94
try:
    TLS_EVENT_CODE_INF_SESSION_ESTABLISHED = 16
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 95
try:
    TLS_EVENT_CODE_WRN_CERT_EXPIRED = 17
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 96
try:
    TLS_EVENT_CODE_WRN_CERT_NOT_YET_VALID = 18
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 97
try:
    TLS_EVENT_CODE_WRN_CRL_EXPIRED = 19
except:
    pass

# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 98
try:
    TLS_EVENT_CODE_WRN_CRL_NOT_YET_VALID = 20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 45
try:
    IEC_60870_5_104_DEFAULT_PORT = 2404
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 46
try:
    IEC_60870_5_104_DEFAULT_TLS_PORT = 19998
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 48
try:
    LIB60870_VERSION_MAJOR = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 49
try:
    LIB60870_VERSION_MINOR = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 50
try:
    LIB60870_VERSION_PATCH = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 53
try:
    IEC60870_QUALITY_GOOD = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 54
try:
    IEC60870_QUALITY_OVERFLOW = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 55
try:
    IEC60870_QUALITY_RESERVED = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 56
try:
    IEC60870_QUALITY_ELAPSED_TIME_INVALID = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 57
try:
    IEC60870_QUALITY_BLOCKED = 0x10
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 58
try:
    IEC60870_QUALITY_SUBSTITUTED = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 59
try:
    IEC60870_QUALITY_NON_TOPICAL = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 60
try:
    IEC60870_QUALITY_INVALID = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 67
try:
    IEC60870_START_EVENT_NONE = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 68
try:
    IEC60870_START_EVENT_GS = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 69
try:
    IEC60870_START_EVENT_SL1 = 0x02
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 70
try:
    IEC60870_START_EVENT_SL2 = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 71
try:
    IEC60870_START_EVENT_SL3 = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 72
try:
    IEC60870_START_EVENT_SIE = 0x10
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 73
try:
    IEC60870_START_EVENT_SRD = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 74
try:
    IEC60870_START_EVENT_RES1 = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 75
try:
    IEC60870_START_EVENT_RES2 = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 82
try:
    IEC60870_OUTPUT_CI_GC = 0x01
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 83
try:
    IEC60870_OUTPUT_CI_CL1 = 0x02
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 84
try:
    IEC60870_OUTPUT_CI_CL2 = 0x04
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 85
try:
    IEC60870_OUTPUT_CI_CL3 = 0x08
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 101
try:
    IEC60870_QPM_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 102
try:
    IEC60870_QPM_THRESHOLD_VALUE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 103
try:
    IEC60870_QPM_SMOOTHING_FACTOR = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 104
try:
    IEC60870_QPM_LOW_LIMIT_FOR_TRANSMISSION = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 105
try:
    IEC60870_QPM_HIGH_LIMIT_FOR_TRANSMISSION = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 113
try:
    IEC60870_COI_LOCAL_SWITCH_ON = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 114
try:
    IEC60870_COI_LOCAL_MANUAL_RESET = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 115
try:
    IEC60870_COI_REMOTE_RESET = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 122
try:
    IEC60870_QOC_NO_ADDITIONAL_DEFINITION = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 123
try:
    IEC60870_QOC_SHORT_PULSE_DURATION = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 124
try:
    IEC60870_QOC_LONG_PULSE_DURATION = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 125
try:
    IEC60870_QOC_PERSISTANT_OUTPUT = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 133
try:
    IEC60870_SCQ_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 134
try:
    IEC60870_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 135
try:
    IEC60870_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 136
try:
    IEC60870_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 137
try:
    IEC60870_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 138
try:
    IEC60870_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 139
try:
    IEC60870_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 140
try:
    IEC60870_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 148
try:
    IEC60870_QOI_STATION = 20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 149
try:
    IEC60870_QOI_GROUP_1 = 21
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 150
try:
    IEC60870_QOI_GROUP_2 = 22
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 151
try:
    IEC60870_QOI_GROUP_3 = 23
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 152
try:
    IEC60870_QOI_GROUP_4 = 24
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 153
try:
    IEC60870_QOI_GROUP_5 = 25
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 154
try:
    IEC60870_QOI_GROUP_6 = 26
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 155
try:
    IEC60870_QOI_GROUP_7 = 27
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 156
try:
    IEC60870_QOI_GROUP_8 = 28
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 157
try:
    IEC60870_QOI_GROUP_9 = 29
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 158
try:
    IEC60870_QOI_GROUP_10 = 30
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 159
try:
    IEC60870_QOI_GROUP_11 = 31
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 160
try:
    IEC60870_QOI_GROUP_12 = 32
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 161
try:
    IEC60870_QOI_GROUP_13 = 33
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 162
try:
    IEC60870_QOI_GROUP_14 = 34
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 163
try:
    IEC60870_QOI_GROUP_15 = 35
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 164
try:
    IEC60870_QOI_GROUP_16 = 36
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 187
try:
    IEC60870_QCC_RQT_GROUP_1 = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 188
try:
    IEC60870_QCC_RQT_GROUP_2 = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 189
try:
    IEC60870_QCC_RQT_GROUP_3 = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 190
try:
    IEC60870_QCC_RQT_GROUP_4 = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 191
try:
    IEC60870_QCC_RQT_GENERAL = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 193
try:
    IEC60870_QCC_FRZ_READ = 0x00
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 194
try:
    IEC60870_QCC_FRZ_FREEZE_WITHOUT_RESET = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 195
try:
    IEC60870_QCC_FRZ_FREEZE_WITH_RESET = 0x80
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 196
try:
    IEC60870_QCC_FRZ_COUNTER_RESET = 0xc0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 203
try:
    IEC60870_QRP_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 204
try:
    IEC60870_QRP_GENERAL_RESET = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 205
try:
    IEC60870_QRP_RESET_PENDING_INFO_WITH_TIME_TAG = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 213
try:
    IEC60870_QPA_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 214
try:
    IEC60870_QPA_DE_ACT_PREV_LOADED_PARAMETER = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 215
try:
    IEC60870_QPA_DE_ACT_OBJECT_PARAMETER = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 216
try:
    IEC60870_QPA_DE_ACT_OBJECT_TRANSMISSION = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1771
try:
    CS101_NOF_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1772
try:
    CS101_NOF_TRANSPARENT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1773
try:
    CS101_NOF_DISTURBANCE_DATA = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1774
try:
    CS101_NOF_SEQUENCES_OF_EVENTS = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1775
try:
    CS101_NOF_SEQUENCES_OF_ANALOGUE_VALUES = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1787
try:
    CS101_SCQ_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1788
try:
    CS101_SCQ_SELECT_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1789
try:
    CS101_SCQ_REQUEST_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1790
try:
    CS101_SCQ_DEACTIVATE_FILE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1791
try:
    CS101_SCQ_DELETE_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1792
try:
    CS101_SCQ_SELECT_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1793
try:
    CS101_SCQ_REQUEST_SECTION = 6
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1794
try:
    CS101_SCQ_DEACTIVATE_SECTION = 7
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1807
try:
    CS101_LSQ_FILE_TRANSFER_WITHOUT_DEACT = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1808
try:
    CS101_LSQ_FILE_TRANSFER_WITH_DEACT = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1809
try:
    CS101_LSQ_SECTION_TRANSFER_WITHOUT_DEACT = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1810
try:
    CS101_LSQ_SECTION_TRANSFER_WITH_DEACT = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1823
try:
    CS101_AFQ_NOT_USED = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1826
try:
    CS101_AFQ_POS_ACK_FILE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1829
try:
    CS101_AFQ_NEG_ACK_FILE = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1832
try:
    CS101_AFQ_POS_ACK_SECTION = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1835
try:
    CS101_AFQ_NEG_ACK_SECTION = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1848
try:
    CS101_FILE_ERROR_DEFAULT = 0
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1851
try:
    CS101_FILE_ERROR_REQ_MEMORY_NOT_AVAILABLE = 1
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1854
try:
    CS101_FILE_ERROR_CHECKSUM_FAILED = 2
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1857
try:
    CS101_FILE_ERROR_UNEXPECTED_COMM_SERVICE = 3
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1860
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_FILE = 4
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1863
try:
    CS101_FILE_ERROR_UNEXPECTED_NAME_OF_SECTION = 5
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1876
try:
    CS101_SOF_STATUS = 0x1f
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1879
try:
    CS101_SOF_LFD = 0x20
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1882
try:
    CS101_SOF_FOR = 0x40
except:
    pass

# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1885
try:
    CS101_SOF_FA = 0x80
except:
    pass

sSerialPort = struct_sSerialPort# /home/user/lib60870/lib60870-C/src/hal/inc/hal_serial.h: 39

sServerSocket = struct_sServerSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 44

sUdpSocket = struct_sUdpSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 46

sSocket = struct_sSocket# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 49

sHandleSet = struct_sHandleSet# /home/user/lib60870/lib60870-C/src/hal/inc/hal_socket.h: 52

sThread = struct_sThread# /home/user/lib60870/lib60870-C/src/hal/inc/hal_thread.h: 38

sTLSConfiguration = struct_sTLSConfiguration# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 38

sTLSConnection = struct_sTLSConnection# /home/user/lib60870/lib60870-C/src/hal/inc/tls_config.h: 100

sTLSSocket = struct_sTLSSocket# /home/user/lib60870/lib60870-C/src/hal/inc/tls_socket.h: 48

sCS101_AppLayerParameters = struct_sCS101_AppLayerParameters# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 112

sInformationObject = struct_sInformationObject# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 211

sCS101_ASDU = struct_sCS101_ASDU# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 216

sCP16Time2a = struct_sCP16Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 231

sCP24Time2a = struct_sCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 237

sCP32Time2a = struct_sCP32Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 246

sCP56Time2a = struct_sCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 255

sBinaryCounterReading = struct_sBinaryCounterReading# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 264

sCS104_APCIParameters = struct_sCS104_APCIParameters# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 273

sFrame = struct_sFrame# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_common.h: 875

sStatusAndStatusChangeDetection = struct_sStatusAndStatusChangeDetection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 266

sSinglePointInformation = struct_sSinglePointInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 323

sSinglePointWithCP24Time2a = struct_sSinglePointWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 342

sSinglePointWithCP56Time2a = struct_sSinglePointWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 358

sDoublePointInformation = struct_sDoublePointInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 375

sDoublePointWithCP24Time2a = struct_sDoublePointWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 394

sDoublePointWithCP56Time2a = struct_sDoublePointWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 410

sStepPositionInformation = struct_sStepPositionInformation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 426

sStepPositionWithCP24Time2a = struct_sStepPositionWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 465

sStepPositionWithCP56Time2a = struct_sStepPositionWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 482

sBitString32 = struct_sBitString32# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 498

sBitstring32WithCP24Time2a = struct_sBitstring32WithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 519

sBitstring32WithCP56Time2a = struct_sBitstring32WithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 537

sMeasuredValueNormalizedWithoutQuality = struct_sMeasuredValueNormalizedWithoutQuality# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 555

sMeasuredValueNormalized = struct_sMeasuredValueNormalized# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 573

sMeasuredValueNormalizedWithCP24Time2a = struct_sMeasuredValueNormalizedWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 594

sMeasuredValueNormalizedWithCP56Time2a = struct_sMeasuredValueNormalizedWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 613

sMeasuredValueScaled = struct_sMeasuredValueScaled# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 633

sMeasuredValueScaledWithCP24Time2a = struct_sMeasuredValueScaledWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 667

sMeasuredValueScaledWithCP56Time2a = struct_sMeasuredValueScaledWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 686

sMeasuredValueShort = struct_sMeasuredValueShort# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 705

sMeasuredValueShortWithCP24Time2a = struct_sMeasuredValueShortWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 726

sMeasuredValueShortWithCP56Time2a = struct_sMeasuredValueShortWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 746

sIntegratedTotals = struct_sIntegratedTotals# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 766

sIntegratedTotalsWithCP24Time2a = struct_sIntegratedTotalsWithCP24Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 795

sIntegratedTotalsWithCP56Time2a = struct_sIntegratedTotalsWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 827

sEventOfProtectionEquipment = struct_sEventOfProtectionEquipment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 859

sPackedStartEventsOfProtectionEquipment = struct_sPackedStartEventsOfProtectionEquipment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 881

sPackedOutputCircuitInfo = struct_sPackedOutputCircuitInfo# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 906

sPackedSinglePointWithSCD = struct_sPackedSinglePointWithSCD# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 931

sSingleCommand = struct_sSingleCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 951

sSingleCommandWithCP56Time2a = struct_sSingleCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 996

sDoubleCommand = struct_sDoubleCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1031

sStepCommand = struct_sStepCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1078

sSetpointCommandNormalized = struct_sSetpointCommandNormalized# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1109

sSetpointCommandScaled = struct_sSetpointCommandScaled# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1146

sSetpointCommandShort = struct_sSetpointCommandShort# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1183

sBitstring32Command = struct_sBitstring32Command# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1220

sInterrogationCommand = struct_sInterrogationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1235

sReadCommand = struct_sReadCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1250

sClockSynchronizationCommand = struct_sClockSynchronizationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1262

sParameterActivation = struct_sParameterActivation# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1421

sEventOfProtectionEquipmentWithCP56Time2a = struct_sEventOfProtectionEquipmentWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1450

sPackedStartEventsOfProtectionEquipmentWithCP56Time2a = struct_sPackedStartEventsOfProtectionEquipmentWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1472

sPackedOutputCircuitInfoWithCP56Time2a = struct_sPackedOutputCircuitInfoWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1497

sDoubleCommandWithCP56Time2a = struct_sDoubleCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1522

sStepCommandWithCP56Time2a = struct_sStepCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1546

sSetpointCommandNormalizedWithCP56Time2a = struct_sSetpointCommandNormalizedWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1570

sSetpointCommandScaledWithCP56Time2a = struct_sSetpointCommandScaledWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1594

sSetpointCommandShortWithCP56Time2a = struct_sSetpointCommandShortWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1618

sBitstring32CommandWithCP56Time2a = struct_sBitstring32CommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1642

sCounterInterrogationCommand = struct_sCounterInterrogationCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1661

sTestCommand = struct_sTestCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1676

sTestCommandWithCP56Time2a = struct_sTestCommandWithCP56Time2a# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1691

sResetProcessCommand = struct_sResetProcessCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1718

sDelayAcquisitionCommand = struct_sDelayAcquisitionCommand# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1733

sEndOfInitialization = struct_sEndOfInitialization# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1748

sFileReady = struct_sFileReady# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1889

sSectionReady = struct_sSectionReady# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1927

sFileCallOrSelect = struct_sFileCallOrSelect# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1959

sFileLastSegmentOrSection = struct_sFileLastSegmentOrSection# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 1980

sFileACK = struct_sFileACK# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2004

sFileSegment = struct_sFileSegment# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2025

sFileDirectory = struct_sFileDirectory# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2052

sQueryLog = struct_sQueryLog# /home/user/lib60870/lib60870-C/src/inc/api/cs101_information_objects.h: 2088

sLinkLayerParameters = struct_sLinkLayerParameters# /home/user/lib60870/lib60870-C/src/inc/api/link_layer_parameters.h: 42

sCS101_Master = struct_sCS101_Master# /home/user/lib60870/lib60870-C/src/inc/api/cs101_master.h: 55

sIMasterConnection = struct_sIMasterConnection# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 65

sCS101_SlavePlugin = struct_sCS101_SlavePlugin# /home/user/lib60870/lib60870-C/src/inc/api/iec60870_slave.h: 178

sCS101_Slave = struct_sCS101_Slave# /home/user/lib60870/lib60870-C/src/inc/api/cs101_slave.h: 59

sCS104_Connection = struct_sCS104_Connection# /home/user/lib60870/lib60870-C/src/inc/api/cs104_connection.h: 52

sCS104_Slave = struct_sCS104_Slave# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 50

sCS104_RedundancyGroup = struct_sCS104_RedundancyGroup# /home/user/lib60870/lib60870-C/src/inc/api/cs104_slave.h: 64

# No inserted files

# No prefix-stripping

