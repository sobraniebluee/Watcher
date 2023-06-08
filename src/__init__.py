import sys
import time
import subprocess
import os
import threading
from src.colors import Clrs
from src.config import INTERPRETER_PATHS


class Watcher:
    def __init__(self, filename, callback, params=None):
        self._prev_stamp = 0
        self.filename = filename
        self.callback = callback
        self.params = params or []

    def look_changes(self):
        curr_stamp = os.stat(self.filename).st_mtime
        if curr_stamp != self._prev_stamp:
            self.callback(*self.params)
            self._prev_stamp = curr_stamp

    def watch(self):
        print(Clrs.green("Start watch..."))
        print(Clrs.green("Enter 'reload' in cli and file will be reload!"))
        time.sleep(0.5)
        threading.Thread(target=self.check_stdin, daemon=True).start()

        while True:
            self.look_changes()
            time.sleep(1)

    def check_stdin(self):
        while True:
            time.sleep(0.5)
            stdin = input()
            if stdin == "reload":
                self.callback(*self.params)


class BaseCompilerException(Exception):
    message: str

    def __init__(self):
        super().__init__(self.message)


class NotSupportedFileExtension(BaseCompilerException):
    message = "Sorry, this extension doesn't support!"


class NotFoundInterpreter(BaseCompilerException):
    message = "Sorry, we don't found interpreter for this file extension!"


class Compiler:
    interpreter: str

    def __init__(self, filepath):
        self.filepath = filepath
        self.interpreter = self.get_interpreter_path()

    def compile_file(self):
        print(Clrs.green(f"Reload file changes [ {self.filepath} ]"))
        time.sleep(0.3)
        response_cmd = subprocess.run([self.interpreter, self.filepath],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        stdout_text = response_cmd.stdout.decode('utf-8').strip()
        stderr_text = response_cmd.stderr.decode('utf-8').strip()

        if stdout_text:
            print(stdout_text)
        if stderr_text:
            print(stderr_text)

    def get_interpreter_path(self) -> str:
        extension = self.filepath.split('.')[-1]
        if extension in INTERPRETER_PATHS:
            return self.search_py_compiler(extension)
        raise NotSupportedFileExtension

    @staticmethod
    def search_py_compiler(ext) -> str:
        for paths in INTERPRETER_PATHS[ext]:
            if os.path.exists(paths):
                print(Clrs.warn(f"Compiler: {paths}"))
                return paths
        raise NotFoundInterpreter


def main():
    try:
        filepath = os.path.abspath(sys.argv[1])

        if not os.path.isfile(filepath):
            exit("Please enter existing filepath!")
        compiler = Compiler(filepath)

        watcher = Watcher(filename=filepath,
                          callback=compiler.compile_file)
        watcher.watch()
    except KeyboardInterrupt:
        exit(Clrs.warn("\nBye Bye"))
    except IndexError:
        exit("Please enter filepath:"
             " watcher {filepath}")
    except Exception as e:
        exit(e)
