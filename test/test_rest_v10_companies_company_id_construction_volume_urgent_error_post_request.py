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

from procore_sdk.models.rest_v10_companies_company_id_construction_volume_urgent_error_post_request import RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest

class TestRestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest(unittest.TestCase):
    """RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest:
        """Test RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest`
        """
        model = RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest()
        if include_optional:
            return RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest(
                message = ''
            )
        else:
            return RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest(
        )
        """

    def testRestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest(self):
        """Test RestV10CompaniesCompanyIdConstructionVolumeUrgentErrorPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
