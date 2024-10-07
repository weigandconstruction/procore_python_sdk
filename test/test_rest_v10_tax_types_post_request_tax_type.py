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

from procore_sdk.models.rest_v10_tax_types_post_request_tax_type import RestV10TaxTypesPostRequestTaxType

class TestRestV10TaxTypesPostRequestTaxType(unittest.TestCase):
    """RestV10TaxTypesPostRequestTaxType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10TaxTypesPostRequestTaxType:
        """Test RestV10TaxTypesPostRequestTaxType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10TaxTypesPostRequestTaxType`
        """
        model = RestV10TaxTypesPostRequestTaxType()
        if include_optional:
            return RestV10TaxTypesPostRequestTaxType(
                description = 'Goods and Services Tax',
                name = 'GST',
                origin_data = '{ parent_ids: [1,2] }',
                origin_id = '1VT-33778-013'
            )
        else:
            return RestV10TaxTypesPostRequestTaxType(
                name = 'GST',
        )
        """

    def testRestV10TaxTypesPostRequestTaxType(self):
        """Test RestV10TaxTypesPostRequestTaxType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
