# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from procore_sdk.models.rest_v10_projects_project_id_drawing_revisions_drawing_revision_id_drawing_tiles_get200_response import RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response

class TestRestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response(unittest.TestCase):
    """RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response:
        """Test RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response`
        """
        model = RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response()
        if include_optional:
            return RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response(
                max_zoom_level = 2,
                tile_size = [750,750],
                zip_url = 'https://streaming.procore.com/download?uuid=03bb9d61702ce533caef169d4370b98f7f7e407f71a0af72f8a593de469aae92',
                tiles = [
                    procore_sdk.models.drawing_tile.DrawingTile(
                        id = 402785892, 
                        x = 8, 
                        y = 6, 
                        z = 2, 
                        url = 'deprecated', )
                    ]
            )
        else:
            return RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response(
        )
        """

    def testRestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response(self):
        """Test RestV10ProjectsProjectIdDrawingRevisionsDrawingRevisionIdDrawingTilesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
