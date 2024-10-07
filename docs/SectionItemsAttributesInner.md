# SectionItemsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Item | 
**position** | **int** | The Position of the Item | 
**status** | **str** | The Status of the Item | [optional] 

## Example

```python
from procore_sdk.models.section_items_attributes_inner import SectionItemsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SectionItemsAttributesInner from a JSON string
section_items_attributes_inner_instance = SectionItemsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(SectionItemsAttributesInner.to_json())

# convert the object into a dict
section_items_attributes_inner_dict = section_items_attributes_inner_instance.to_dict()
# create an instance of SectionItemsAttributesInner from a dict
section_items_attributes_inner_from_dict = SectionItemsAttributesInner.from_dict(section_items_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


