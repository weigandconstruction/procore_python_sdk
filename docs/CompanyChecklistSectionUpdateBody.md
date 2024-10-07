# CompanyChecklistSectionUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | [**CompanyChecklistSection**](CompanyChecklistSection.md) |  | 

## Example

```python
from procore_sdk.models.company_checklist_section_update_body import CompanyChecklistSectionUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyChecklistSectionUpdateBody from a JSON string
company_checklist_section_update_body_instance = CompanyChecklistSectionUpdateBody.from_json(json)
# print the JSON string representation of the object
print(CompanyChecklistSectionUpdateBody.to_json())

# convert the object into a dict
company_checklist_section_update_body_dict = company_checklist_section_update_body_instance.to_dict()
# create an instance of CompanyChecklistSectionUpdateBody from a dict
company_checklist_section_update_body_from_dict = CompanyChecklistSectionUpdateBody.from_dict(company_checklist_section_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


