class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""


class VersionNotFoundException(Exception):
    """Вызывается, когда парсер не может найти ни одной версии."""
