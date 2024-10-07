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

from procore_sdk.models.observation_origin import ObservationOrigin

class TestObservationOrigin(unittest.TestCase):
    """ObservationOrigin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationOrigin:
        """Test ObservationOrigin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationOrigin`
        """
        model = ObservationOrigin()
        if include_optional:
            return ObservationOrigin(
                type = 'inspection',
                payload = procore_sdk.models.origin_payload.Origin Payload(
                    checklist_item_id = 42, 
                    checklist_list_id = 42, 
                    coordination_issue_id = 1231, 
                    coordination_issue_number = 42, 
                    incident_action_id = 53, 
                    incident_id = 53, 
                    bim_model_id = 63, 
                    bim_model_name = 'Combined Model', )
            )
        else:
            return ObservationOrigin(
        )
        """

    def testObservationOrigin(self):
        """Test ObservationOrigin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
