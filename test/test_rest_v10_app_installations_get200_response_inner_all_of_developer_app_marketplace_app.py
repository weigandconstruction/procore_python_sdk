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

from procore_sdk.models.rest_v10_app_installations_get200_response_inner_all_of_developer_app_marketplace_app import RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp

class TestRestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp(unittest.TestCase):
    """RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp:
        """Test RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp`
        """
        model = RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp()
        if include_optional:
            return RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp(
                id = 'e3b8a1a0-5b0a-4b5a-9b0a-5b0a4b5a9b0a',
                about = 'Test Marketplace App',
                approval_state = 'approved',
                built_by = 'Test Developer',
                costs_money = False,
                created_at = '2020-01-01T00:00Z',
                description = 'Test Marketplace App',
                feature_bullets = [
                    'Test Marketplace App'
                    ],
                helpful_links = [
                    procore_sdk.models.rest_v10_app_installations_get_200_response_inner_all_of_developer_app_marketplace_app_helpful_links_inner.RestV10AppInstallationsGet_200_response_inner_allOf_developer_app_marketplace_app_helpful_links_inner(
                        url = 'https://www.example.com', 
                        label = 'Test Marketplace App', )
                    ],
                how_it_works = 'Test Marketplace App',
                live = True,
                pictures = [
                    procore_sdk.models.rest_v10_app_installations_get_200_response_inner_all_of_developer_app_marketplace_app_pictures_inner.RestV10AppInstallationsGet_200_response_inner_allOf_developer_app_marketplace_app_pictures_inner(
                        id = 'e3b8a1a0-5b0a-4b5a-9b0a-5b0a4b5a9b0a', 
                        description = 'Test Marketplace App Image', 
                        name = 'Test Marketplace App Image', 
                        original_file_name = 'e3b8a1a0-5b0a-4b5a-9b0a-5b0a4b5a9b0a.png', 
                        type = 'Picture', 
                        url = 'https://www.example.com/image.png', )
                    ],
                public_name = 'Test Marketplace App',
                requirements = [
                    'Test Marketplace App'
                    ],
                small_logo_url = 'https://www.example.com/logo.png',
                state = 'published',
                support_email = 'support@example.com',
                updated_at = '2020-01-01T00:00Z',
                version = 1,
                videos = [
                    procore_sdk.models.rest_v10_app_installations_get_200_response_inner_all_of_developer_app_marketplace_app_videos_inner.RestV10AppInstallationsGet_200_response_inner_allOf_developer_app_marketplace_app_videos_inner(
                        id = 'e3b8a1a0-5b0a-4b5a-9b0a-5b0a4b5a9b0a', 
                        description = 'Test Marketplace App Video', 
                        name = 'Test Marketplace App Video', 
                        original_filename = 'e3b8a1a0-5b0a-4b5a-9b0a-5b0a4b5a9b0a.mp4', 
                        type = 'Video', 
                        url = 'https://www.example.com/video.mp4', )
                    ],
                website_link = procore_sdk.models.rest_v10_app_installations_get_200_response_inner_all_of_developer_app_marketplace_app_website_link.RestV10AppInstallationsGet_200_response_inner_allOf_developer_app_marketplace_app_website_link(
                    url = 'https://www.example.com', 
                    label = 'Test Marketplace App', )
            )
        else:
            return RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp(
        )
        """

    def testRestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp(self):
        """Test RestV10AppInstallationsGet200ResponseInnerAllOfDeveloperAppMarketplaceApp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
