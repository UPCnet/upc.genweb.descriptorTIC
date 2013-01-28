from zope.interface import Interface

from zope.browsermenu.interfaces import IBrowserMenu
from zope.browsermenu.interfaces import IBrowserSubMenuItem


class IServeiTIC(Interface):
    """A Servei Content Type
    """


class IFaq(Interface):
    """A faq Content Type
    """


class IUnitatTIC(Interface):
    """A faq Content Type
    """


class IFamiliaTIC(Interface):
    """A faq Content Type
    """


class IFaqContainerTIC(Interface):
    """A faq Content Type
    """


class ICarpetaTIC(Interface):
    """A faq Content Type
    """


class IConfigperiodeSubMenuItem(IBrowserSubMenuItem):
    """The menu item linking to the Configperiode menu.
    """


class IConfigperiodeMenu(IBrowserMenu):
    """The Configperiode menu.
    """
