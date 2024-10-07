# CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | ID of the associated Company Inspection Template Item | 
**type** | **str** | Company Inspection Template Item Reference Type | 
**payload** | [**CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload**](CompanyInspectionTemplateItemReferenceCreateBodyTemplateReferencePayload.md) |  | 

## Example

```python
from procore_sdk.models.company_inspection_template_item_reference_create_body_template_reference import CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference from a JSON string
company_inspection_template_item_reference_create_body_template_reference_instance = CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference.from_json(json)
# print the JSON string representation of the object
print(CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference.to_json())

# convert the object into a dict
company_inspection_template_item_reference_create_body_template_reference_dict = company_inspection_template_item_reference_create_body_template_reference_instance.to_dict()
# create an instance of CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference from a dict
company_inspection_template_item_reference_create_body_template_reference_from_dict = CompanyInspectionTemplateItemReferenceCreateBodyTemplateReference.from_dict(company_inspection_template_item_reference_create_body_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


