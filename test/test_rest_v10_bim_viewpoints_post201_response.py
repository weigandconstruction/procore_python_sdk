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

from procore_sdk.models.rest_v10_bim_viewpoints_post201_response import RestV10BimViewpointsPost201Response

class TestRestV10BimViewpointsPost201Response(unittest.TestCase):
    """RestV10BimViewpointsPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10BimViewpointsPost201Response:
        """Test RestV10BimViewpointsPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10BimViewpointsPost201Response`
        """
        model = RestV10BimViewpointsPost201Response()
        if include_optional:
            return RestV10BimViewpointsPost201Response(
                id = 206,
                bim_file_id = 809,
                view_folder_id = 316,
                created_at = '2018-04-19T09:36:42Z',
                updated_at = '2018-04-20T09:36:42Z',
                snapshot = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_viewpoints_inner_all_of_snapshot.RestV10CoordinationIssuesGet_200_response_inner_allOf_viewpoints_inner_allOf_snapshot(
                    id = 56, 
                    name = 'filename.ext', 
                    content_type = 'image/png', 
                    url = 'https://storage.procore.com/v3/d/default/procore-files/1ZE258W9K804SAJJZX19JVAB3R?sig=e7a476ec0a46154d05e0d4a554fb2ea0904cb6604670f9247c54d7c56a84d0b6', ),
                name = 'Mechanical Conflict View',
                render_mode = 'shaded',
                visibility = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_viewpoints_inner_all_of_visibility.RestV10CoordinationIssuesGet_200_response_inner_allOf_viewpoints_inner_allOf_visibility(
                    default_visibility = True, 
                    exceptions = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_viewpoints_inner_all_of_visibility_exceptions.RestV10CoordinationIssuesGet_200_response_inner_allOf_viewpoints_inner_allOf_visibility_exceptions(
                        object_ids = [24861,46732], 
                        object_ranges = [[24862,24]], ), ),
                camera_data = '{"perspective_camera":{"camera_direction":{"x":-0.24,"y":-0.14,"z":-0.99},"camera_up_vector":{"x":-0.17,"y":-0.74,"z":0.14},"camera_view_point":{"x":-13.86,"y":64.83,"z":31.9},"field_of_view":0.78,"target_distance":9.18,"unit":"ft"}}',
                redlines_data = '{"lines":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"end_point":{"x":-0.29,"y":-0.15,"z":0.0},"thickness":3,"start_point":{"x":-0.29,"y":-0.53,"z":0.0}}],"texts":[{"origin":{"x":-0.29,"y":-0.15,"z":0.0},"text":"Issue","color":{"a":1.0,"b":0,"g":0,"r":1}}],"arrows":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"end_point":{"x":-0.16,"y":0.33,"z":0.0},"thickness":3,"start_point":{"x":0.58,"y":0.25,"z":0.0}}],"ellipses":[{"color":{"a":1.0,"b":0,"g":0,"r":1},"max_point":{"x":0.11,"y":-0.25,"z":0.0},"min_point":{"x":0.31,"y":0.68,"z":0.0},"thickness":3}]}',
                sections_data = '[{"location":{"x":0.0,"y":0.0,"z":28.82},"direction":{"x":0,"y":0,"z":-1},"unit":"ft"},{"location":{"x":10.0,"y":50.0,"z":68.82},"direction":{"x":2,"y":4,"z":-6}}]'
            )
        else:
            return RestV10BimViewpointsPost201Response(
        )
        """

    def testRestV10BimViewpointsPost201Response(self):
        """Test RestV10BimViewpointsPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
