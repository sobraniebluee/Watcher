## Watcher

Is an util for watching changes in your file, and when they are, watcher re-compile file.

Now it is support to compile .py, .js, .mjs files

Usage:

``watcher {filepath}``

If you want add your interpreter you for yours file extensions you can edit ``src/config.py``:

```py 
    # ADD NEW KEY AS EXTENSION FILE AND AS VALUE PASS THE LIST WITH PATHS TO INTERPRETER
    INTERPRETER_PATHS = {
        'py': ['./venv/bin/python', '/usr/local/bin/python3'],
        'js': ['/usr/local/bin/node'],
        'mjs': ['/usr/local/bin/node'],
        # 'new_extension': ['/path/interpreter']
    }
```