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

from procore_sdk.models.rest_v10_cost_codes_copy_subset_from_standard_list_post207_response import RestV10CostCodesCopySubsetFromStandardListPost207Response

class TestRestV10CostCodesCopySubsetFromStandardListPost207Response(unittest.TestCase):
    """RestV10CostCodesCopySubsetFromStandardListPost207Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CostCodesCopySubsetFromStandardListPost207Response:
        """Test RestV10CostCodesCopySubsetFromStandardListPost207Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CostCodesCopySubsetFromStandardListPost207Response`
        """
        model = RestV10CostCodesCopySubsetFromStandardListPost207Response()
        if include_optional:
            return RestV10CostCodesCopySubsetFromStandardListPost207Response(
                successes = [
                    null
                    ],
                failures = [
                    null
                    ]
            )
        else:
            return RestV10CostCodesCopySubsetFromStandardListPost207Response(
        )
        """

    def testRestV10CostCodesCopySubsetFromStandardListPost207Response(self):
        """Test RestV10CostCodesCopySubsetFromStandardListPost207Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
