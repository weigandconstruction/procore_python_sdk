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

from procore_sdk.models.rest_v10_companies_company_id_incidents_severity_levels_id_patch_request_severity_level import RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel

class TestRestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel(unittest.TestCase):
    """RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel:
        """Test RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel`
        """
        model = RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel()
        if include_optional:
            return RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel(
                name = 'Critical',
                email_trigger = False,
                push_notification_trigger = False,
                alert_recipient_ids = [
                    1
                    ]
            )
        else:
            return RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel(
        )
        """

    def testRestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel(self):
        """Test RestV10CompaniesCompanyIdIncidentsSeverityLevelsIdPatchRequestSeverityLevel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
