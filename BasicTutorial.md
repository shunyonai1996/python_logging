# PythonのLoggingについてまとめた（基本編）

## Loggingとは
Python標準のログ機能のモジュール。
標準搭載だけど、ログレベルを制御できたり、出力するメッセージや出力先を柔軟に変更できて便利です。
公式ドキュメントを読みながら、実際に手を動かしたものをGitHubにあげてます。
pythonの実行環境がある方であれば、`basic_logging.py`のコメントアウトを解除して、
`python basic_logging.py`
を実行すると簡単にLoggingの動作確認ができます。

[logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)

## 基本
### 標準出力にログを出力
```python
import logging

logging.debug('Detailed information, typically of interest only when diagnosing problems.')
logging.info('Confirmation that things are working as expected.')
logging.warning('An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.')
logging.error('Due to a more serious problem, the software has not been able to perform some function.')
logging.critical('A serious error, indicating that the program itself may be unable to continue running.')
```
出力
```bash
$ python basic_logging.py
WARNING:root:An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR:root:Due to a more serious problem, the software has not been able to perform some function.
CRITICAL:root:A serious error, indicating that the program itself may be unable to continue running.
```

### 特定のファイルに出力
```python
import logging

logger = logging.getLogger(__name__)
# 以下で出力先やログレベルを制御
logging.basicConfig(filename='./logs/example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
```
example.logに出力
```example.log
DEBUG:__main__:This message should go to the log file
INFO:__main__:So should this
WARNING:__main__:And this, too
ERROR:__main__:And non-ASCII stuff, too, like Øresund and Malmö
```
※補足：
`basicConfig()`は1度しか読み込まれません。
途中から別の設定を定義しようとしても、その定義は無効化されます。
既存のハンドラ削除してから再度定義し直すことは可能ですが、ここでは触れません。

## 具体的な出力フォーマット
### 変数埋め込み
```python
import logging

variable = '真ん中（変数）'
logging.warning('%s variable %s', '最初', '最後')
```

標準出力
```bash
$ python basic_logging.py
WARNING:root:最初 真ん中 最後
WARNING:root:最初 真ん中（変数） 最後
```
※`%s`はプレースホルダー。Loggingが古いモジュールのため、`str.format()`などの関数に対応していない（対応させる方法もあるが、ここでは割愛）。

### 動的に出力内容を変える
Loggingがあらかじめ用意している属性を設定可能。

公式に詳しい属性が書いてます。気になる方は参考にしてください。
[LogRecord attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)

```python
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG
                    )
logging.debug('debugのmessage')
logging.info('infoのmessage')
logging.warning('warningのmessage')
```
標準出力
```bash
$ python basic_logging.py
2025-04-26 16:54:19:DEBUG:debugのmessage
2025-04-26 16:54:19:INFO:infoのmessage
2025-04-26 16:54:19:WARNING:warningのmessage
```