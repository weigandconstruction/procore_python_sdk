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

from procore_sdk.models.observation_origin1 import ObservationOrigin1

class TestObservationOrigin1(unittest.TestCase):
    """ObservationOrigin1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationOrigin1:
        """Test ObservationOrigin1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationOrigin1`
        """
        model = ObservationOrigin1()
        if include_optional:
            return ObservationOrigin1(
                type = 'inspection',
                payload = procore_sdk.models.origin_payload.Origin Payload(
                    checklist_item_id = 42, 
                    checklist_list_id = 42, 
                    coordination_issue_id = 2312, 
                    coordination_issue_number = 21, 
                    incident_action_id = 53, 
                    incident_id = 53, 
                    bim_model_id = 63, 
                    bim_model_name = 'Combined Model', )
            )
        else:
            return ObservationOrigin1(
        )
        """

    def testObservationOrigin1(self):
        """Test ObservationOrigin1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
