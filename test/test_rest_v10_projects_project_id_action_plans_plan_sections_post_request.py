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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_post_request import RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest

class TestRestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest(
                plan_section = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_post_request_plan_section.RestV10ProjectsProjectIdActionPlansPlanSectionsPost_request_plan_section(
                    plan_id = 42, 
                    title = 'A new Action Plan Section', )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest(
                plan_section = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_sections_post_request_plan_section.RestV10ProjectsProjectIdActionPlansPlanSectionsPost_request_plan_section(
                    plan_id = 42, 
                    title = 'A new Action Plan Section', ),
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanSectionsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
