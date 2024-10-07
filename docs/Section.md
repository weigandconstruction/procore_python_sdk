# Section

Section object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Section | 
**position** | **int** | The Position of the Section | 
**not_applicable** | **bool** | The Not Applicable status of the Section | [optional] [default to False]
**items_attributes** | [**List[SectionItemsAttributesInner]**](SectionItemsAttributesInner.md) | An array of the Section&#39;s Item attributes | [optional] 

## Example

```python
from procore_sdk.models.section import Section

# TODO update the JSON string below
json = "{}"
# create an instance of Section from a JSON string
section_instance = Section.from_json(json)
# print the JSON string representation of the object
print(Section.to_json())

# convert the object into a dict
section_dict = section_instance.to_dict()
# create an instance of Section from a dict
section_from_dict = Section.from_dict(section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


