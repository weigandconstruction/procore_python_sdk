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

from procore_sdk.models.observation_category_configurable_field_sets import ObservationCategoryConfigurableFieldSets

class TestObservationCategoryConfigurableFieldSets(unittest.TestCase):
    """ObservationCategoryConfigurableFieldSets unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationCategoryConfigurableFieldSets:
        """Test ObservationCategoryConfigurableFieldSets
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationCategoryConfigurableFieldSets`
        """
        model = ObservationCategoryConfigurableFieldSets()
        if include_optional:
            return ObservationCategoryConfigurableFieldSets(
                id = 4,
                category = 'Commissioning',
                category_key = 'work_to_complete',
                configurable_field_set = procore_sdk.models.configurable_field_set.Configurable Field Set(
                    id = 999, 
                    name = 'Observation Fields', 
                    category = 'commissioning', 
                    class_name = 'Observations::Item', 
                    fields = { }, 
                    sections = [
                        procore_sdk.models.configurable_field_set_sections_inner.Configurable_Field_Set_sections_inner(
                            id = 1, 
                            name = 'Section 1', 
                            description = 'Project ABC', 
                            position = 999, 
                            from_v1_custom_fields = False, )
                        ], 
                    inspection_type_id = 1, 
                    generic_tool_id = 1, 
                    action_plan_type_id = 1, 
                    type = 'ConfigurabkeFieldSet::Observations::Item', )
            )
        else:
            return ObservationCategoryConfigurableFieldSets(
                id = 4,
                category = 'Commissioning',
                configurable_field_set = procore_sdk.models.configurable_field_set.Configurable Field Set(
                    id = 999, 
                    name = 'Observation Fields', 
                    category = 'commissioning', 
                    class_name = 'Observations::Item', 
                    fields = { }, 
                    sections = [
                        procore_sdk.models.configurable_field_set_sections_inner.Configurable_Field_Set_sections_inner(
                            id = 1, 
                            name = 'Section 1', 
                            description = 'Project ABC', 
                            position = 999, 
                            from_v1_custom_fields = False, )
                        ], 
                    inspection_type_id = 1, 
                    generic_tool_id = 1, 
                    action_plan_type_id = 1, 
                    type = 'ConfigurabkeFieldSet::Observations::Item', ),
        )
        """

    def testObservationCategoryConfigurableFieldSets(self):
        """Test ObservationCategoryConfigurableFieldSets"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
