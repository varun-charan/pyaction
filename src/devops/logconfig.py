import logging
import logging.config

def configure_logging(verbose=False):
    """
    configure the root logging
    :param verbose:
    :return:
    """
    level = logging.DEBUG if verbose else logging.INFO

    # plz use short names (8) for the loggers
    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                      '%(asctime)s %(name)-8s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': level}
        },
        root={
            'handlers': ['h'],
            'level': level,
        },
    )

    logging.config.dictConfig(logging_config)



