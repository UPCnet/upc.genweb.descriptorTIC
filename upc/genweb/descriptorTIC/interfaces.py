from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from upc.genweb.descriptorTIC import descriptorticMessageFactory as _

# -*- extra stuff goes here -*-

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
