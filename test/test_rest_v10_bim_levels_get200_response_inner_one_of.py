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

from procore_sdk.models.rest_v10_bim_levels_get200_response_inner_one_of import RestV10BimLevelsGet200ResponseInnerOneOf

class TestRestV10BimLevelsGet200ResponseInnerOneOf(unittest.TestCase):
    """RestV10BimLevelsGet200ResponseInnerOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BimLevelsGet200ResponseInnerOneOf:
        """Test RestV10BimLevelsGet200ResponseInnerOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BimLevelsGet200ResponseInnerOneOf`
        """
        model = RestV10BimLevelsGet200ResponseInnerOneOf()
        if include_optional:
            return RestV10BimLevelsGet200ResponseInnerOneOf(
                id = 144,
                elevation = 10.25,
                name = '1space>1 space',
                created_at = '2019-01-04T06:13:10Z',
                updated_at = '2019-01-06T11:26:08Z',
                bim_file = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_coordination_issue_file.RestV10CoordinationIssuesGet_200_response_inner_allOf_coordination_issue_file(
                    id = 101, 
                    name = '101_BLDG_FLR_2.NWF', 
                    uuid = 'a00147dd-a698-468a-b082-d277a564cf0c', ),
                location = procore_sdk.models.location.Location(
                    id = 15504, 
                    name = 'North Building>First Floor>Electrical Closet', 
                    node_name = 'Electrical Closet', 
                    parent_id = 788866, 
                    created_at = '2016-08-01T23:33:54Z', 
                    updated_at = '2016-08-01T23:33:54Z', 
                    code = 'L1', ),
                created_by = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_assignee.RestV10CoordinationIssuesGet_200_response_inner_allOf_assignee(
                    id = 1738090, 
                    name = 'John Doe', 
                    login = 'johndoe@example.com', 
                    company_name = 'Builders Inc.', 
                    locale = 'ko', )
            )
        else:
            return RestV10BimLevelsGet200ResponseInnerOneOf(
        )
        """

    def testRestV10BimLevelsGet200ResponseInnerOneOf(self):
        """Test RestV10BimLevelsGet200ResponseInnerOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
