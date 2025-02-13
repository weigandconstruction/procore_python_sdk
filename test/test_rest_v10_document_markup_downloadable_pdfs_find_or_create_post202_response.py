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

from procore_sdk.models.rest_v10_document_markup_downloadable_pdfs_find_or_create_post202_response import RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response

class TestRestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response(unittest.TestCase):
    """RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response:
        """Test RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response`
        """
        model = RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response()
        if include_optional:
            return RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response(
                id = 42,
                error_message = '',
                status = 'processing',
                url = ''
            )
        else:
            return RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response(
        )
        """

    def testRestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response(self):
        """Test RestV10DocumentMarkupDownloadablePdfsFindOrCreatePost202Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
