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

from procore_sdk.models.time_and_material_signature_create_body import TimeAndMaterialSignatureCreateBody

class TestTimeAndMaterialSignatureCreateBody(unittest.TestCase):
    """TimeAndMaterialSignatureCreateBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeAndMaterialSignatureCreateBody:
        """Test TimeAndMaterialSignatureCreateBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeAndMaterialSignatureCreateBody`
        """
        model = TimeAndMaterialSignatureCreateBody()
        if include_optional:
            return TimeAndMaterialSignatureCreateBody(
                signature = procore_sdk.models.time_and_material_signature_create_body_signature.TimeAndMaterialSignatureCreateBody_signature(
                    data = '', 
                    party_id = 56, 
                    signature_text = '', )
            )
        else:
            return TimeAndMaterialSignatureCreateBody(
                signature = procore_sdk.models.time_and_material_signature_create_body_signature.TimeAndMaterialSignatureCreateBody_signature(
                    data = '', 
                    party_id = 56, 
                    signature_text = '', ),
        )
        """

    def testTimeAndMaterialSignatureCreateBody(self):
        """Test TimeAndMaterialSignatureCreateBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
