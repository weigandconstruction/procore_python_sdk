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

from procore_sdk.models.rest_v10_projects_project_id_actual_production_quantities_post_request import RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest

class TestRestV10ProjectsProjectIdActualProductionQuantitiesPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest:
        """Test RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest`
        """
        model = RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest(
                actual_production_quantity = procore_sdk.models.actual_production_quantity.Actual Production Quantity(
                    quantity = 100, 
                    wbs_code_id = 1234, 
                    cost_code_id = 1, 
                    crew_id = 1, 
                    location_id = 1, 
                    timesheet_id = 1, 
                    sub_job_id = 1, 
                    date = 'Fri Feb 06 00:00:00 UTC 2015', )
            )
        else:
            return RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest(
                actual_production_quantity = procore_sdk.models.actual_production_quantity.Actual Production Quantity(
                    quantity = 100, 
                    wbs_code_id = 1234, 
                    cost_code_id = 1, 
                    crew_id = 1, 
                    location_id = 1, 
                    timesheet_id = 1, 
                    sub_job_id = 1, 
                    date = 'Fri Feb 06 00:00:00 UTC 2015', ),
        )
        """

    def testRestV10ProjectsProjectIdActualProductionQuantitiesPostRequest(self):
        """Test RestV10ProjectsProjectIdActualProductionQuantitiesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
