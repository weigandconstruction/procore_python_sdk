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

from procore_sdk.models.default1_designated_reviewer import Default1DesignatedReviewer

class TestDefault1DesignatedReviewer(unittest.TestCase):
    """Default1DesignatedReviewer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Default1DesignatedReviewer:
        """Test Default1DesignatedReviewer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Default1DesignatedReviewer`
        """
        model = Default1DesignatedReviewer()
        if include_optional:
            return Default1DesignatedReviewer(
                id = 161072,
                name = 'Carl the Contractor'
            )
        else:
            return Default1DesignatedReviewer(
        )
        """

    def testDefault1DesignatedReviewer(self):
        """Test Default1DesignatedReviewer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
