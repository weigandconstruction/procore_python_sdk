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

from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post201_response import RestV10ProjectsProjectIdBudgetChangesPost201Response

class TestRestV10ProjectsProjectIdBudgetChangesPost201Response(unittest.TestCase):
    """RestV10ProjectsProjectIdBudgetChangesPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdBudgetChangesPost201Response:
        """Test RestV10ProjectsProjectIdBudgetChangesPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdBudgetChangesPost201Response`
        """
        model = RestV10ProjectsProjectIdBudgetChangesPost201Response()
        if include_optional:
            return RestV10ProjectsProjectIdBudgetChangesPost201Response(
                data = None
            )
        else:
            return RestV10ProjectsProjectIdBudgetChangesPost201Response(
        )
        """

    def testRestV10ProjectsProjectIdBudgetChangesPost201Response(self):
        """Test RestV10ProjectsProjectIdBudgetChangesPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
