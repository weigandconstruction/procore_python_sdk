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

from procore_sdk.models.body125_bim_plan_one_of_model_map_start import Body125BimPlanOneOfModelMapStart

class TestBody125BimPlanOneOfModelMapStart(unittest.TestCase):
    """Body125BimPlanOneOfModelMapStart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body125BimPlanOneOfModelMapStart:
        """Test Body125BimPlanOneOfModelMapStart
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body125BimPlanOneOfModelMapStart`
        """
        model = Body125BimPlanOneOfModelMapStart()
        if include_optional:
            return Body125BimPlanOneOfModelMapStart(
                x = 6.24,
                y = 12.48,
                z = 24.96
            )
        else:
            return Body125BimPlanOneOfModelMapStart(
        )
        """

    def testBody125BimPlanOneOfModelMapStart(self):
        """Test Body125BimPlanOneOfModelMapStart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
