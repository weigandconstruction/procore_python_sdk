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

from procore_sdk.models.project_observation_template1 import ProjectObservationTemplate1

class TestProjectObservationTemplate1(unittest.TestCase):
    """ProjectObservationTemplate1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectObservationTemplate1:
        """Test ProjectObservationTemplate1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectObservationTemplate1`
        """
        model = ProjectObservationTemplate1()
        if include_optional:
            return ProjectObservationTemplate1(
                id = 1738,
                active = True,
                assignee = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                updated_at = '2016-08-23T15:23:57Z',
                company_observation_template_id = 1337,
                observation_title = 'Worker seen not wearing PPE',
                observation_type = procore_sdk.models.project_observation_type.Project Observation Type(
                    id = 2020, 
                    name = 'No Type', 
                    localized_name = 'No Type', 
                    category = 'Quality', 
                    category_key = 'quality', 
                    name_translations = '', 
                    active = True, 
                    company_active = True, 
                    parent_inactive = False, 
                    in_use = False, 
                    kind = 'project', ),
                trade = procore_sdk.models.trade.Trade(
                    id = 999, 
                    name = '09 - acoustical panels', 
                    active = True, 
                    updated_at = '2016-08-01T23:33:54Z', )
            )
        else:
            return ProjectObservationTemplate1(
        )
        """

    def testProjectObservationTemplate1(self):
        """Test ProjectObservationTemplate1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
