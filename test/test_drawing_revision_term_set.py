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

from procore_sdk.models.drawing_revision_term_set import DrawingRevisionTermSet

class TestDrawingRevisionTermSet(unittest.TestCase):
    """DrawingRevisionTermSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DrawingRevisionTermSet:
        """Test DrawingRevisionTermSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DrawingRevisionTermSet`
        """
        model = DrawingRevisionTermSet()
        if include_optional:
            return DrawingRevisionTermSet(
                drawing_revision_id = 2,
                updated_at = '2015-03-19T12:00Z',
                terms = {
                    'key' : {"foo":[{"x":10,"y":10,"height":10,"width":10,"index":1},{"x":20,"y":20,"height":10,"width":10,"index":2}],"bar":[{"x":30,"y":30,"height":10,"width":10,"index":3}]}
                    }
            )
        else:
            return DrawingRevisionTermSet(
        )
        """

    def testDrawingRevisionTermSet(self):
        """Test DrawingRevisionTermSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
