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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request1 import RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1

class TestRestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1:
        """Test RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1(
                signature = procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_receivers_plan_receiver_id_signature_post_request_1_signature.RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePost_request_1_signature(
                    attachment_id = 42, )
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanReceiversPlanReceiverIdSignaturePostRequest1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
