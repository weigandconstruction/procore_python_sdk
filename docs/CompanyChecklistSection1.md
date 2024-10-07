# CompanyChecklistSection1

Company Checklist Section object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**position** | **int** | The position of Section | [optional] 

## Example

```python
from procore_sdk.models.company_checklist_section1 import CompanyChecklistSection1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyChecklistSection1 from a JSON string
company_checklist_section1_instance = CompanyChecklistSection1.from_json(json)
# print the JSON string representation of the object
print(CompanyChecklistSection1.to_json())

# convert the object into a dict
company_checklist_section1_dict = company_checklist_section1_instance.to_dict()
# create an instance of CompanyChecklistSection1 from a dict
company_checklist_section1_from_dict = CompanyChecklistSection1.from_dict(company_checklist_section1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


