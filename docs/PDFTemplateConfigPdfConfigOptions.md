# PDFTemplateConfigPdfConfigOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collapse_na_sections** | **bool** |  | [optional] 
**show_na_items** | **bool** |  | [optional] 
**show_status_change** | **bool** |  | [optional] 
**show_activity_details** | **bool** |  | [optional] 
**disclaimer_footer_text** | **bool** |  | [optional] 
**attendees_table_format** | **bool** |  | [optional] 
**attendees_phone_number_display** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.pdf_template_config_pdf_config_options import PDFTemplateConfigPdfConfigOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PDFTemplateConfigPdfConfigOptions from a JSON string
pdf_template_config_pdf_config_options_instance = PDFTemplateConfigPdfConfigOptions.from_json(json)
# print the JSON string representation of the object
print(PDFTemplateConfigPdfConfigOptions.to_json())

# convert the object into a dict
pdf_template_config_pdf_config_options_dict = pdf_template_config_pdf_config_options_instance.to_dict()
# create an instance of PDFTemplateConfigPdfConfigOptions from a dict
pdf_template_config_pdf_config_options_from_dict = PDFTemplateConfigPdfConfigOptions.from_dict(pdf_template_config_pdf_config_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


