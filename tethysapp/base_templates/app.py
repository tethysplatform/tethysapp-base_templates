from tethys_sdk.base import TethysAppBase, url_map_maker


class BaseTemplates(TethysAppBase):
    """
    Tethys app class for Base Templates.
    """

    name = 'Base Templates'
    index = 'base_templates:home'
    icon = 'base_templates/images/icon.gif'
    package = 'base_templates'
    root_url = 'base-templates'
    color = '#16a085'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='base-templates',
                controller='base_templates.controllers.home'
            ),
        )

        return url_maps