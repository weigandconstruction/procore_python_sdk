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

from procore_sdk.models.project_person1 import ProjectPerson1

class TestProjectPerson1(unittest.TestCase):
    """ProjectPerson1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectPerson1:
        """Test ProjectPerson1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectPerson1`
        """
        model = ProjectPerson1()
        if include_optional:
            return ProjectPerson1(
                contact = procore_sdk.models.normal_contact.Normal_contact(
                    is_active = True, 
                    email = 'paul@example.com', ),
                employee_id = '123456789',
                first_name = 'Leah',
                id = 381006,
                is_employee = False,
                last_name = 'Russell',
                user_id = 700215,
                user_uuid = 56,
                work_classification_id = 398438,
                origin_id = 398438
            )
        else:
            return ProjectPerson1(
        )
        """

    def testProjectPerson1(self):
        """Test ProjectPerson1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
