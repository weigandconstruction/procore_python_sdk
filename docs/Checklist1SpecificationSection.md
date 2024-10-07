# Checklist1SpecificationSection

Specification Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | Description | [optional] 
**section** | **str** | Number | [optional] 
**latest_revision_url** | **str** | Url to PDF view | [optional] 

## Example

```python
from procore_sdk.models.checklist1_specification_section import Checklist1SpecificationSection

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist1SpecificationSection from a JSON string
checklist1_specification_section_instance = Checklist1SpecificationSection.from_json(json)
# print the JSON string representation of the object
print(Checklist1SpecificationSection.to_json())

# convert the object into a dict
checklist1_specification_section_dict = checklist1_specification_section_instance.to_dict()
# create an instance of Checklist1SpecificationSection from a dict
checklist1_specification_section_from_dict = Checklist1SpecificationSection.from_dict(checklist1_specification_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


