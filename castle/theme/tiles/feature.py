from castle.cms.widgets import ImageRelatedItemsFieldWidget
from castle.cms.widgets import VideoRelatedItemsFieldWidget
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives as form
from plone.supermodel import model
from plone.tiles.interfaces import IPersistentTile
from zope import schema
from zope.component import getMultiAdapter
from zope.component.hooks import getSite
from zope.globalrequest import getRequest
from zope.interface import implements
from zope.interface import Invalid
from zope.interface import invariant
from castle.cms.tiles.video import VideoTile


class FeatureTile(VideoTile):
    implements(IPersistentTile)

    def getTitle(self):
        icon_obj = self.get_icon()
        if icon_obj is not None:
            return icon_obj.Title
        else:
            if self.data.get('title') is not None:
                return self.data.get('title')
            else:
                return ''

    def get_icon_path(self):
        icon_obj = self.get_icon()
        if icon_obj is None:
            if self.data.get('icon_link') is not None:
                return self.data.get('icon_link')
            else:
                return ''

        return '%s/@@images/image/thumb' % icon_obj.absolute_url()

    def get_icon(self):
        icon = self.data.get('icon')
        if not icon:
            return
        return self.utils.get_object(self.data['icon'][0])

class IFeatureTileSchema(model.Schema):
    title = schema.TextLine(
        title=u'Title'
    )

    form.widget(icon=ImageRelatedItemsFieldWidget)
    icon = schema.List(
        title=u"Icon",
        description=u"Icon that shows up above title",
        required=False,
        default=[],
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.Catalog'
        )
    )

    icon_link = schema.TextLine(
        title=u'Icon link',
        required=False,
        description=u'Link to an external icon image'
    )

    @invariant
    def validate_icon(data):
        if data.icon and len(data.icon) != 1:
            raise Invalid("Must select 1 icon")
        if data.icon:
            utils = getMultiAdapter((getSite(), getRequest()),
                                    name="castle-utils")
            obj = utils.get_object(data.icon[0])
            if not obj or obj.portal_type != 'Image':
                raise Invalid('Must provide icon file')

    form.widget(text=RichTextFieldWidget)
    text = RichText(
        title=u'Text',
        default_mime_type='text/html',
        output_mime_type='text/html',
        allowed_mime_types=('text/html',),
        required=True
    )

    form.widget(video=VideoRelatedItemsFieldWidget)
    video = schema.List(
        title=u"Video file",
        description=u"Reference video file on the site.",
        required=False,
        default=[],
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.Catalog'
        )
    )

    youtube_url = schema.TextLine(
        title=u'YouTube url',
        description=u'Or provide a YouTube url',
        required=False)

    @invariant
    def validate_video(data):
        if data.video and len(data.video) != 1:
            raise Invalid("Must select 1 video")
        if data.video and data.youtube_url:
            raise Invalid("You can not select both a video and a youtube url")
        if data.video:
            utils = getMultiAdapter((getSite(), getRequest()),
                                    name="castle-utils")
            obj = utils.get_object(data.video[0])
            if not obj or obj.portal_type != 'Video':
                raise Invalid('Must provide video')
