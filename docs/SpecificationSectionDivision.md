# SpecificationSectionDivision

Represents a construction division, which is used to group specification sections. Each SpecificationSectionDivision can contain many SpecificationSections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** | Address of a PDF file containing the PDFs for all of the SpecificationSections in this division, concatenated into one. | [optional] 

## Example

```python
from procore_sdk.models.specification_section_division import SpecificationSectionDivision

# TODO update the JSON string below
json = "{}"
# create an instance of SpecificationSectionDivision from a JSON string
specification_section_division_instance = SpecificationSectionDivision.from_json(json)
# print the JSON string representation of the object
print(SpecificationSectionDivision.to_json())

# convert the object into a dict
specification_section_division_dict = specification_section_division_instance.to_dict()
# create an instance of SpecificationSectionDivision from a dict
specification_section_division_from_dict = SpecificationSectionDivision.from_dict(specification_section_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


