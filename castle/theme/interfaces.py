from zope.interface import Interface


class ICustomTheme(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    """


class IUtils(Interface):

    def get_folder_section():
        pass