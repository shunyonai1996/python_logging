import logging

# 基本
# 標準主力にログを出力

# logging.debug('Detailed information, typically of interest only when diagnosing problems.')
# logging.info('Confirmation that things are working as expected.')
# logging.warning('An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.')
# logging.error('Due to a more serious problem, the software has not been able to perform some function.')
# logging.critical('A serious error, indicating that the program itself may be unable to continue running.')

# 特定のファイルに出力

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='./logs/example.log', encoding='utf-8', level=logging.DEBUG)
# logger.debug('This message should go to the log file')
# logger.info('So should this')
# logger.warning('And this, too')
# logger.error('And non-ASCII stuff, too, like Øresund and Malmö')


# 具体的な出力フォーマット
# 変数埋め込み
# logging.warning('%s 真ん中 %s', '最初', '最後')
# center = '真ん中（変数）'
# logging.warning('%s %s %s', '最初', center, '最後')

# 動的に出力内容を変える
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.DEBUG
#                     )
# logging.debug('debugのmessage')
# logging.info('infoのmessage')
# logging.warning('warningのmessage')