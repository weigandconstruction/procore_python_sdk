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

from procore_sdk.models.rest_v10_tax_codes_id_patch_request_tax_code import RestV10TaxCodesIdPatchRequestTaxCode

class TestRestV10TaxCodesIdPatchRequestTaxCode(unittest.TestCase):
    """RestV10TaxCodesIdPatchRequestTaxCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10TaxCodesIdPatchRequestTaxCode:
        """Test RestV10TaxCodesIdPatchRequestTaxCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10TaxCodesIdPatchRequestTaxCode`
        """
        model = RestV10TaxCodesIdPatchRequestTaxCode()
        if include_optional:
            return RestV10TaxCodesIdPatchRequestTaxCode(
                code = 'GST@10%',
                description = 'Goods and Services Tax',
                origin_data = '{ parent_ids: [1,2] }',
                origin_id = '1VT-33778-013',
                rate1 = 10,
                archived = False
            )
        else:
            return RestV10TaxCodesIdPatchRequestTaxCode(
        )
        """

    def testRestV10TaxCodesIdPatchRequestTaxCode(self):
        """Test RestV10TaxCodesIdPatchRequestTaxCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
