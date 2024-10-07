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

from procore_sdk.models.rest_v11_requisitions_get200_response_inner_summary_text import RestV11RequisitionsGet200ResponseInnerSummaryText

class TestRestV11RequisitionsGet200ResponseInnerSummaryText(unittest.TestCase):
    """RestV11RequisitionsGet200ResponseInnerSummaryText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11RequisitionsGet200ResponseInnerSummaryText:
        """Test RestV11RequisitionsGet200ResponseInnerSummaryText
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11RequisitionsGet200ResponseInnerSummaryText`
        """
        model = RestV11RequisitionsGet200ResponseInnerSummaryText()
        if include_optional:
            return RestV11RequisitionsGet200ResponseInnerSummaryText(
                project_name = 'Project',
                project_number = '100',
                to_general_contractor = 'Company A',
                requisition_period_start = 'Fri Jan 01 00:00:00 UTC 2010',
                requisition_period_end = 'Fri Jan 01 00:00:00 UTC 2010',
                subcontractor_name = 'Company B',
                subcontractor_street = '101 XYZ Avenue',
                subcontractor_city = 'New York',
                subcontractor_state_code = 'NY',
                subcontractor_zip = '10101',
                subcontractor_country_code = 'US',
                application_number = '1',
                contract_for = 'Ceiling Tiles',
                contract_date = 'Fri Jan 01 00:00:00 UTC 2010'
            )
        else:
            return RestV11RequisitionsGet200ResponseInnerSummaryText(
        )
        """

    def testRestV11RequisitionsGet200ResponseInnerSummaryText(self):
        """Test RestV11RequisitionsGet200ResponseInnerSummaryText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
