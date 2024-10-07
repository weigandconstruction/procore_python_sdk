# PDFTemplateConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the PdfTemplateConfig | [optional] 
**template_name** | **str** | PdfTemplate name | [optional] 
**default_project** | **bool** | set the configs as default to every company&#39;s project | [optional] 
**pdf_config_options** | [**PDFTemplateConfigPdfConfigOptions**](PDFTemplateConfigPdfConfigOptions.md) |  | [optional] 

## Example

```python
from procore_sdk.models.pdf_template_config import PDFTemplateConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PDFTemplateConfig from a JSON string
pdf_template_config_instance = PDFTemplateConfig.from_json(json)
# print the JSON string representation of the object
print(PDFTemplateConfig.to_json())

# convert the object into a dict
pdf_template_config_dict = pdf_template_config_instance.to_dict()
# create an instance of PDFTemplateConfig from a dict
pdf_template_config_from_dict = PDFTemplateConfig.from_dict(pdf_template_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


