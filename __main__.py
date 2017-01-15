import sys
import argparse as AP
import logging as L
import VoiceHAB

Parser = AP.ArgumentParser()
Parser.add_argument('-l', '--log', default='ERROR')

Arguments = Parser.parse_args()

LoggingLevel = getattr(L, Arguments.log.upper(), None)

if not isinstance(LoggingLevel, int):
    print('Invalid log level: %s' % Arguments.log.upper())
    sys.exit(0)

L.basicConfig(format='[%(levelname)s] [%(module)s]: %(message)s', level=LoggingLevel)

try:
    VoiceHAB.init()
    VoiceHAB.Instance.InitializeModules()
    VoiceHAB.Instance.ListenForWakeUp()
except KeyboardInterrupt:
    L.debug('Exiting')
    sys.exit(0)
