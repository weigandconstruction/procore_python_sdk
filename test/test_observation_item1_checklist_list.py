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

from procore_sdk.models.observation_item1_checklist_list import ObservationItem1ChecklistList

class TestObservationItem1ChecklistList(unittest.TestCase):
    """ObservationItem1ChecklistList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationItem1ChecklistList:
        """Test ObservationItem1ChecklistList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationItem1ChecklistList`
        """
        model = ObservationItem1ChecklistList()
        if include_optional:
            return ObservationItem1ChecklistList(
                id = 11
            )
        else:
            return ObservationItem1ChecklistList(
        )
        """

    def testObservationItem1ChecklistList(self):
        """Test ObservationItem1ChecklistList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
