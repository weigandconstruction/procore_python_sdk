# CompanyChecklistSection

Company Checklist section object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**position** | **int** | The position of Section | [optional] 

## Example

```python
from procore_sdk.models.company_checklist_section import CompanyChecklistSection

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyChecklistSection from a JSON string
company_checklist_section_instance = CompanyChecklistSection.from_json(json)
# print the JSON string representation of the object
print(CompanyChecklistSection.to_json())

# convert the object into a dict
company_checklist_section_dict = company_checklist_section_instance.to_dict()
# create an instance of CompanyChecklistSection from a dict
company_checklist_section_from_dict = CompanyChecklistSection.from_dict(company_checklist_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


