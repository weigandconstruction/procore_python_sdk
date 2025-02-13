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

from procore_sdk.models.sub_job_body import SubJobBody

class TestSubJobBody(unittest.TestCase):
    """SubJobBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubJobBody:
        """Test SubJobBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubJobBody`
        """
        model = SubJobBody()
        if include_optional:
            return SubJobBody(
                project_id = 4393334,
                sub_job = procore_sdk.models.sub_job_body_sub_job.Sub_Job_Body_sub_job(
                    name = 'Floor 2', 
                    code = '18', 
                    origin_id = '', 
                    origin_data = '{"data_field":{"is_important":true}}', )
            )
        else:
            return SubJobBody(
                project_id = 4393334,
                sub_job = procore_sdk.models.sub_job_body_sub_job.Sub_Job_Body_sub_job(
                    name = 'Floor 2', 
                    code = '18', 
                    origin_id = '', 
                    origin_data = '{"data_field":{"is_important":true}}', ),
        )
        """

    def testSubJobBody(self):
        """Test SubJobBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
