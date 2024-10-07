# CompanyChecklistSectionCreateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | [**CompanyChecklistSection1**](CompanyChecklistSection1.md) |  | 

## Example

```python
from procore_sdk.models.company_checklist_section_create_body import CompanyChecklistSectionCreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyChecklistSectionCreateBody from a JSON string
company_checklist_section_create_body_instance = CompanyChecklistSectionCreateBody.from_json(json)
# print the JSON string representation of the object
print(CompanyChecklistSectionCreateBody.to_json())

# convert the object into a dict
company_checklist_section_create_body_dict = company_checklist_section_create_body_instance.to_dict()
# create an instance of CompanyChecklistSectionCreateBody from a dict
company_checklist_section_create_body_from_dict = CompanyChecklistSectionCreateBody.from_dict(company_checklist_section_create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


