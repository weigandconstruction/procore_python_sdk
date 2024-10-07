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

from procore_sdk.models.pdf_template_config import PDFTemplateConfig

class TestPDFTemplateConfig(unittest.TestCase):
    """PDFTemplateConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PDFTemplateConfig:
        """Test PDFTemplateConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PDFTemplateConfig`
        """
        model = PDFTemplateConfig()
        if include_optional:
            return PDFTemplateConfig(
                description = 'pdf template config description',
                template_name = 'bid_single',
                default_project = True,
                pdf_config_options = procore_sdk.models.pdf_template_config_pdf_config_options.PDF_Template_config_pdf_config_options(
                    collapse_na_sections = True, 
                    show_na_items = True, 
                    show_status_change = False, 
                    show_activity_details = False, 
                    disclaimer_footer_text = False, 
                    attendees_table_format = True, 
                    attendees_phone_number_display = True, )
            )
        else:
            return PDFTemplateConfig(
        )
        """

    def testPDFTemplateConfig(self):
        """Test PDFTemplateConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
