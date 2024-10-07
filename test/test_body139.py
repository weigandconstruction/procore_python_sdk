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

from procore_sdk.models.body139 import Body139

class TestBody139(unittest.TestCase):
    """Body139 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body139:
        """Test Body139
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body139`
        """
        model = Body139()
        if include_optional:
            return Body139(
                project_id = 326,
                view = 'compact',
                bim_geometry_file_bundle = procore_sdk.models.body_139_bim_geometry_file_bundle.Body_139_bim_geometry_file_bundle(
                    bim_model_revision_id = 1984, 
                    cell_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3P', 
                    node_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3Q', 
                    mesh_node_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3R', 
                    mesh_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3S', )
            )
        else:
            return Body139(
                project_id = 326,
                bim_geometry_file_bundle = procore_sdk.models.body_139_bim_geometry_file_bundle.Body_139_bim_geometry_file_bundle(
                    bim_model_revision_id = 1984, 
                    cell_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3P', 
                    node_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3Q', 
                    mesh_node_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3R', 
                    mesh_upload_uuid = '1ZE258W9K804SAJJZX19JVAB3S', ),
        )
        """

    def testBody139(self):
        """Test Body139"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
