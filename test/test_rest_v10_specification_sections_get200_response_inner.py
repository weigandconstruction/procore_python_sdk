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

from procore_sdk.models.rest_v10_specification_sections_get200_response_inner import RestV10SpecificationSectionsGet200ResponseInner

class TestRestV10SpecificationSectionsGet200ResponseInner(unittest.TestCase):
    """RestV10SpecificationSectionsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10SpecificationSectionsGet200ResponseInner:
        """Test RestV10SpecificationSectionsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10SpecificationSectionsGet200ResponseInner`
        """
        model = RestV10SpecificationSectionsGet200ResponseInner()
        if include_optional:
            return RestV10SpecificationSectionsGet200ResponseInner(
                id = 161072,
                number = '08560',
                description = 'Vinyl Windows',
                label = '08560 Vinyl Windows',
                current_revision_id = 145092
            )
        else:
            return RestV10SpecificationSectionsGet200ResponseInner(
        )
        """

    def testRestV10SpecificationSectionsGet200ResponseInner(self):
        """Test RestV10SpecificationSectionsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
