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

from procore_sdk.models.rfq_quote_attachments_inner import RFQQuoteAttachmentsInner

class TestRFQQuoteAttachmentsInner(unittest.TestCase):
    """RFQQuoteAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFQQuoteAttachmentsInner:
        """Test RFQQuoteAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFQQuoteAttachmentsInner`
        """
        model = RFQQuoteAttachmentsInner()
        if include_optional:
            return RFQQuoteAttachmentsInner(
                id = 56,
                name = 'filename.ext',
                url = 'https://storage.procore.com/v3/d/default/procore-files/1ZE258W9K804SAJJZX19JVAB3R?sig=e7a476ec0a46154d05e0d4a554fb2ea0904cb6604670f9247c54d7c56a84d0b6'
            )
        else:
            return RFQQuoteAttachmentsInner(
        )
        """

    def testRFQQuoteAttachmentsInner(self):
        """Test RFQQuoteAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
