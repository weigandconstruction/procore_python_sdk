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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_template_receivers_post_request_plan_template_receiver import RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver

class TestRestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver:
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver(
                plan_template_id = 1,
                party_id = '1'
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver(
                plan_template_id = 1,
                party_id = '1',
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanTemplateReceiversPostRequestPlanTemplateReceiver"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
