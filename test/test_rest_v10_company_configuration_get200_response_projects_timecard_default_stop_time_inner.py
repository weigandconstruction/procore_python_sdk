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

from procore_sdk.models.rest_v10_company_configuration_get200_response_projects_timecard_default_stop_time_inner import RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner

class TestRestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner(unittest.TestCase):
    """RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner:
        """Test RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner`
        """
        model = RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner()
        if include_optional:
            return RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner(
                project_id = 1234,
                timecard_default_stop_time = '17:00'
            )
        else:
            return RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner(
        )
        """

    def testRestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner(self):
        """Test RestV10CompanyConfigurationGet200ResponseProjectsTimecardDefaultStopTimeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
