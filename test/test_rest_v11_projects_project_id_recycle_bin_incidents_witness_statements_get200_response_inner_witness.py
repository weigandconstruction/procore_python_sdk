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

from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_witness import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness

class TestRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness(unittest.TestCase):
    """RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness:
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness`
        """
        model = RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness()
        if include_optional:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness(
                id = 1,
                name = 'John Doe'
            )
        else:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness(
        )
        """

    def testRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness(self):
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerWitness"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
