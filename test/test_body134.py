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

from procore_sdk.models.body134 import Body134

class TestBody134(unittest.TestCase):
    """Body134 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body134:
        """Test Body134
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body134`
        """
        model = Body134()
        if include_optional:
            return Body134(
                project_id = 126,
                bim_model_revision_plans = [
                    procore_sdk.models.body_133_bim_model_revision_plan.Body_133_bim_model_revision_plan(
                        bim_model_revision_id = 16, 
                        bim_plan_id = 96, )
                    ]
            )
        else:
            return Body134(
                project_id = 126,
                bim_model_revision_plans = [
                    procore_sdk.models.body_133_bim_model_revision_plan.Body_133_bim_model_revision_plan(
                        bim_model_revision_id = 16, 
                        bim_plan_id = 96, )
                    ],
        )
        """

    def testBody134(self):
        """Test Body134"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
