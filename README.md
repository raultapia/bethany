<div align="center" style="margin-bottom: 10px;">
<a href="https://github.com/raultapia/bethany">
<img src="https://raw.githubusercontent.com/raultapia/bethany/main/.github/assets/logo.png" alt="logo" width="400">
</a>
</div>

<p align="center">
A command line tool to list all BUG, TODO, HACK, NOTE, and FIXME keywords in your code.
</p>

## ⚙️ Installation
```bash
pip install bethany
```

## 🖥️ Usage
You can easily use `bethany` as follows:
```bash
bethany <filename>
```

For example, ``bethany tests/file1 tests/file2`` will return:

![example1](https://raw.githubusercontent.com/raultapia/bethany/main/.github/assets/example1.png)

## 🔩 Options
#### Continuous mode
Continuous mode is enabled using flag ``-c`` or ``--continuous``. Headers and separators are removed from the output in continuous mode.

For example, ``bethany -c tests/file1 tests/file2`` will return:

![example2](https://raw.githubusercontent.com/raultapia/bethany/main/.github/assets/example2.png)

## 📝 License

Distributed under the GPLv3 License. See `LICENSE` for more information.

## 📬 Contact

[Raul Tapia](https://github.com/raultapia) - raultapia@us.es
